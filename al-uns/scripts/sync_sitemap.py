#!/usr/bin/env python3
"""Riallinea sitemap.xml e en/sitemap.xml ai file reali del sito.

Fa tre cose, e solo quelle:
  1. <lastmod>    = data dell'ultimo commit che ha toccato la pagina;
                    per le pagine con modifiche non ancora committate, la data
                    di modifica del file, che in quel caso e' piu' recente.
  2. <changefreq> e <priority> = quelli della gemella francese, cosi' che le
                    tre lingue dichiarino la stessa pagina allo stesso modo.
  3. Nient'altro. Nessun URL aggiunto, nessuno tolto, nessun hreflang toccato.
     Le pagine noindex restano fuori, /ar/glossaire.html non viene inventato.

Da lanciare come ultimo gesto prima di pubblicare: il lastmod e' vero solo
nell'istante in cui lo si scrive.

  python3 scripts/sync_sitemap.py              # scrive
  python3 scripts/sync_sitemap.py --dry-run    # mostra soltanto

  AL_UNS_ROOT=/tmp/baglio-push/al-uns python3 scripts/sync_sitemap.py

Idempotente: rilanciato senza nuovi commit non cambia nulla.
"""
from __future__ import annotations

import collections
import datetime
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATES = [
    Path(os.environ["AL_UNS_ROOT"]) if os.environ.get("AL_UNS_ROOT") else None,
    HERE.parent if (HERE.parent / "comment-on-entre.html").exists() else None,
    Path("/tmp/baglio-push/al-uns"),
    Path("/workspace/artifacts/al-uns"),
]
ROOT = next(p for p in CANDIDATES if p and (p / "comment-on-entre.html").exists())

BASE = "https://www.al-uns.com/"
SITEMAPS = ["sitemap.xml", "en/sitemap.xml"]

# GIT_OPTIONAL_LOCKS=0: git non prende il lock dell'index per le sole letture.
# Senza, una lettura puo' lasciare un .git/index.lock che blocca i commit.
GIT_ENV = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}


def git(*args: str, cwd: Path) -> str:
    r = subprocess.run(["git", *args], cwd=cwd, env=GIT_ENV,
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def utc(iso: str) -> str:
    d = datetime.datetime.fromisoformat(iso)
    return d.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def mtime(path: Path) -> str:
    d = datetime.datetime.fromtimestamp(path.stat().st_mtime, datetime.timezone.utc)
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")


def split_lang(loc: str) -> tuple[str, str]:
    """https://www.al-uns.com/ar/faq.html -> ('ar', 'faq.html')"""
    p = loc[len(BASE):]
    for lang in ("en", "ar"):
        if p.startswith(lang + "/"):
            return lang, p[len(lang) + 1:]
    return "fr", p


def build_dates() -> tuple[dict[str, str], set[str]]:
    """percorso-relativo-al-sito -> ultimo commit; piu' l'insieme dei file sporchi."""
    try:
        top = Path(git("rev-parse", "--show-toplevel", cwd=ROOT).strip())
    except Exception as e:
        print(f"! git non disponibile ({e}); si usera' la data di modifica dei file.",
              file=sys.stderr)
        return {}, set()
    prefix = ROOT.resolve().relative_to(top).as_posix()
    prefix = f"{prefix}/" if prefix != "." else ""

    # I pathspec di git sono relativi alla cartella corrente: si interroga dalla
    # radice del repo, non da quella del sito, altrimenti non combacia nulla.
    last: dict[str, str] = {}
    stamp = None
    for line in git("log", "--name-only", "--format=@%cI", "--",
                    prefix or ".", cwd=top).splitlines():
        if line.startswith("@"):
            stamp = line[1:]
        elif line.strip() and stamp:
            rel = line.strip()
            if rel.startswith(prefix):
                last.setdefault(rel[len(prefix):], stamp)

    dirty = set()
    for line in git("status", "--porcelain", "--", prefix or ".", cwd=top).splitlines():
        rel = line[3:].strip().strip('"')
        if rel.startswith(prefix):
            dirty.add(rel[len(prefix):])
    return last, dirty


def main() -> int:
    write = "--dry-run" not in sys.argv
    last, dirty = build_dates()

    # tabella di riferimento: changefreq/priority del francese
    ref: dict[str, tuple[str, str]] = {}
    for blk in re.findall(r"<url>.*?</url>", (ROOT / "sitemap.xml").read_text("utf-8"), re.S):
        loc = re.search(r"<loc>(.*?)</loc>", blk).group(1)
        lang, path = split_lang(loc)
        if lang == "fr":
            ref[path] = (re.search(r"<changefreq>(.*?)</changefreq>", blk).group(1),
                         re.search(r"<priority>(.*?)</priority>", blk).group(1))

    touched_lastmod: list[tuple[str, str, str]] = []
    touched_meta: list[tuple[str, str, str]] = []
    orphans: list[str] = []

    for name in SITEMAPS:
        src = ROOT / name
        text = src.read_text("utf-8")

        def replace(m: re.Match) -> str:
            blk = m.group(0)
            loc = re.search(r"<loc>(.*?)</loc>", blk).group(1)
            lang, path = split_lang(loc)
            rel = path if lang == "fr" else f"{lang}/{path}"
            page = ROOT / rel

            old_lm = re.search(r"<lastmod>(.*?)</lastmod>", blk).group(1)
            old_cf = re.search(r"<changefreq>(.*?)</changefreq>", blk).group(1)
            old_pr = re.search(r"<priority>(.*?)</priority>", blk).group(1)

            if not page.exists():
                orphans.append(loc)
                return blk
            lm = mtime(page) if (rel in dirty or rel not in last) else utc(last[rel])
            cf, pr = ref.get(path, (old_cf, old_pr))

            if lm != old_lm:
                touched_lastmod.append((loc, old_lm, lm))
            if (cf, pr) != (old_cf, old_pr):
                touched_meta.append((loc, f"{old_cf}/{old_pr}", f"{cf}/{pr}"))

            blk = re.sub(r"<lastmod>.*?</lastmod>", f"<lastmod>{lm}</lastmod>", blk)
            blk = re.sub(r"<changefreq>.*?</changefreq>", f"<changefreq>{cf}</changefreq>", blk)
            blk = re.sub(r"<priority>.*?</priority>", f"<priority>{pr}</priority>", blk)
            return blk

        out = re.sub(r"<url>.*?</url>", replace, text, flags=re.S)
        if write and out != text:
            src.write_text(out, "utf-8")

    verb = "aggiornati" if write else "da aggiornare"
    print(f"lastmod {verb}: {len(touched_lastmod)}")
    for day, n in sorted(collections.Counter(t[2][:10] for t in touched_lastmod).items()):
        print(f"  {day}: {n} URL")
    print(f"changefreq/priority riallineati al francese: {len(touched_meta)}")
    for loc, before, after in touched_meta:
        print(f"  {loc}  {before} -> {after}")
    if orphans:
        print(f"! {len(orphans)} loc senza file su disco, lasciati intatti:")
        for loc in orphans:
            print(f"  {loc}")
    if not write:
        print("(--dry-run: nessun file scritto)")
    return 1 if orphans else 0


if __name__ == "__main__":
    raise SystemExit(main())
