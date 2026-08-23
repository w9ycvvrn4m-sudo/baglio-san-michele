#!/usr/bin/env python3
"""Align navbar across al-uns FR/EN pages and set og/twitter image = page hero.

Reusable. Run from anywhere:
  python3 scripts/sync_navbar_og.py
Default root: directory containing this file's parent (al-uns/),
or AL_UNS_ROOT env, or /tmp/baglio-push/al-uns.
"""
from __future__ import annotations

import os
import re
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

SKIP = {
    "dar-al-hiraf/productions.html",
    "apres.html",
}

NAV_RE = re.compile(r"<nav\b[^>]*>.*?</nav>", re.DOTALL | re.IGNORECASE)

TOP_INACT = "hover:text-[#c8872f] transition-colors"
TOP_ACT = "font-medium text-[#c8872f]"
PARENT_INACT = "hover:text-[#c8872f] transition-colors flex items-center gap-x-1"
PARENT_ACT = "font-medium text-[#c8872f] flex items-center gap-x-1"
ITEM_INACT = "block px-4 py-1.5 text-sm hover:bg-gray-50 hover:text-[#c8872f]"
ITEM_ACT = "block px-4 py-1.5 text-sm font-medium text-[#c8872f]"
MOB_INACT = "block py-1.5 pl-4 text-secondary hover:text-[#c8872f]"
MOB_ACT = "block py-1.5 pl-4 font-medium text-[#c8872f]"
MOB_HOME_INACT = "block py-3 text-secondary hover:text-[#c8872f]"
MOB_HOME_ACT = "block py-3 font-medium text-[#c8872f]"
SUM_INACT = "cursor-pointer list-none py-3 flex items-center justify-between text-secondary"
SUM_ACT = "cursor-pointer list-none py-3 flex items-center justify-between font-medium text-[#c8872f]"

MENU_JS = (
    "<script>document.addEventListener('DOMContentLoaded',function(){"
    "var b=document.getElementById('menu-btn'),m=document.getElementById('mobile-menu');"
    "if(b&&m){b.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();"
    "m.classList.toggle('hidden');m.classList.toggle('flex');});}});</script>"
)

VENIR_PAGES = {
    "comment-on-entre.html",
    "sejour.html",
    "faq.html",
    "glossaire.html",
    "qui-cherchons-nous.html",
    "maitres-et-personnel.html",
    "dar-al-hiraf/stages.html",
    "dar-al-hiraf/residence.html",
    "dar-al-hiraf/athar.html",
    "dar-al-hiraf/apres.html",
}
MAISON_PAGES = {
    "architecture.html",
    "jardin.html",
    "vie.html",
    "experiences.html",
    "rencontres.html",
    "projet/munya.html",
}
HIRAF_EXTRA = {
    "artisanat.html",
    "vestiario.html",
    "discipline-choreutique.html",
    "parfums.html",
    "furusiyya.html",
    "furusiyya/harnachement.html",
}


def rel_of(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def page_key(rel: str) -> str:
    return rel[3:] if rel.startswith("en/") else rel


def section_for(key: str) -> str:
    if key == "index.html":
        return "home"
    if key == "projet/munya.html":
        return "maison"
    if key == "projet.html" or key.startswith("projet/"):
        return "projet"
    if key in MAISON_PAGES or key.startswith("architecture/"):
        return "maison"
    if key in VENIR_PAGES:
        return "venir"
    if key == "soutenir.html":
        return "soutenir"
    if key in ("contact.html", "merci.html"):
        return "contact"
    if key.startswith("dar-al-hiraf") or key in HIRAF_EXTRA or key.startswith("furusiyya"):
        return "hiraf"
    return "home"


def extract_nav(html: str) -> str:
    m = NAV_RE.search(html)
    if not m:
        raise SystemExit("no nav found in gold page")
    return m.group(0)


def normalize_nav(nav: str) -> str:
    nav = nav.replace(PARENT_ACT, PARENT_INACT)
    nav = nav.replace(ITEM_ACT, ITEM_INACT)
    nav = nav.replace(MOB_ACT, MOB_INACT)
    nav = nav.replace(MOB_HOME_ACT, MOB_HOME_INACT)
    nav = nav.replace(SUM_ACT, SUM_INACT)
    nav = re.sub(
        r'(<a href="[^"]+" class=")font-medium text-\[#c8872f\](">(?:Riad Al-Uns|Soutenir|Contact|Support)</a>)',
        r"\1" + TOP_INACT + r"\2",
        nav,
    )
    nav = re.sub(
        r'<details class="group border-t border-gray-50" open>',
        '<details class="group border-t border-gray-50">',
        nav,
    )
    return nav


def insert_after(nav: str, needle: str, insert: str) -> str:
    if insert.strip() in nav:
        return nav
    if needle not in nav:
        raise SystemExit("needle not found: " + needle[:120])
    return nav.replace(needle, needle + insert, 1)


def prepare_fr_gold(nav: str) -> str:
    nav = normalize_nav(nav)
    nav = insert_after(
        nav,
        '<a href="/architecture.html" class="' + ITEM_INACT + '">Espaces</a>\n',
        '<a href="/architecture/organisation.html" class="' + ITEM_INACT + '">Organisation des espaces</a>\n',
    )
    nav = insert_after(
        nav,
        '<a href="/architecture.html" class="' + MOB_INACT + '">Espaces</a>\n',
        '<a href="/architecture/organisation.html" class="' + MOB_INACT + '">Organisation des espaces</a>\n',
    )
    return nav


def prepare_en_gold(nav: str) -> str:
    nav = normalize_nav(nav)
    if "Adjoining house" not in nav:
        nav = insert_after(
            nav,
            '<a href="/en/architecture/eau.html" class="' + ITEM_INACT + '">Water</a>\n',
            '<div class="px-4 pt-2 pb-1 text-[10px] tracking-[1.5px] uppercase text-[#c8872f]/70">Adjoining house</div>\n',
        )
        nav = insert_after(
            nav,
            '<a href="/en/architecture/eau.html" class="' + MOB_INACT + '">Water</a>\n',
            '<div class="pl-4 pt-2 pb-1 text-[10px] tracking-[1.5px] uppercase text-[#c8872f]/70">Adjoining house</div>\n',
        )
    nav = insert_after(
        nav,
        '<a href="/en/architecture.html" class="' + ITEM_INACT + '">Spaces</a>\n',
        '<a href="/en/architecture/organisation.html" class="' + ITEM_INACT + '">Organisation of the spaces</a>\n',
    )
    nav = insert_after(
        nav,
        '<a href="/en/architecture.html" class="' + MOB_INACT + '">Spaces</a>\n',
        '<a href="/en/architecture/organisation.html" class="' + MOB_INACT + '">Organisation of the spaces</a>\n',
    )
    if "How one enters" not in nav:
        nav = insert_after(
            nav,
            '<a href="/en/sejour.html" class="' + ITEM_INACT + '">Staying</a>\n',
            '<a href="/en/comment-on-entre.html" class="' + ITEM_INACT + '">How one enters</a>\n',
        )
        nav = insert_after(
            nav,
            '<a href="/en/dar-al-hiraf/athar.html" class="' + ITEM_INACT + '">Al-Athar — The work left behind</a>\n',
            '<a href="/en/dar-al-hiraf/apres.html" class="' + ITEM_INACT + '">After the residency</a>\n',
        )
        nav = insert_after(
            nav,
            '<a href="/en/sejour.html" class="' + MOB_INACT + '">Staying</a>\n',
            '<a href="/en/comment-on-entre.html" class="' + MOB_INACT + '">How one enters</a>\n',
        )
        nav = insert_after(
            nav,
            '<a href="/en/dar-al-hiraf/athar.html" class="' + MOB_INACT + '">Al-Athar — The work left behind</a>\n',
            '<a href="/en/dar-al-hiraf/apres.html" class="' + MOB_INACT + '">After the residency</a>\n',
        )
    nav = nav.replace(
        '<a href="/en/sejour.html" class="' + PARENT_INACT + '">Joining',
        '<a href="/en/comment-on-entre.html" class="' + PARENT_INACT + '">Joining',
    )
    return nav


def activate_href_items(nav: str, href: str) -> str:
    nav = nav.replace(
        '<a href="' + href + '" class="' + ITEM_INACT + '">',
        '<a href="' + href + '" class="' + ITEM_ACT + '">',
    )
    nav = nav.replace(
        '<a href="' + href + '" class="' + MOB_INACT + '">',
        '<a href="' + href + '" class="' + MOB_ACT + '">',
    )
    return nav


def activate_section(nav: str, section: str, is_en: bool) -> str:
    prefix = "/en" if is_en else ""
    parent_href = {
        "projet": prefix + "/projet.html",
        "maison": prefix + "/architecture.html",
        "hiraf": prefix + "/dar-al-hiraf.html",
        "venir": prefix + "/comment-on-entre.html",
    }
    details_label = {
        "projet": "The project" if is_en else "Le projet",
        "maison": "The house" if is_en else "La maison",
        "hiraf": "Dar al-Hiraf",
        "venir": "Joining" if is_en else "Venir",
    }
    if section == "home":
        home = prefix + "/index.html"
        nav = nav.replace(
            '<a href="' + home + '" class="' + TOP_INACT + '">Riad Al-Uns</a>',
            '<a href="' + home + '" class="' + TOP_ACT + '">Riad Al-Uns</a>',
        )
        nav = nav.replace(
            '<a href="' + home + '" class="' + MOB_HOME_INACT + '">Riad Al-Uns</a>',
            '<a href="' + home + '" class="' + MOB_HOME_ACT + '">Riad Al-Uns</a>',
        )
        return nav
    if section == "soutenir":
        h = prefix + "/soutenir.html"
        label = "Support" if is_en else "Soutenir"
        nav = nav.replace(
            '<a href="' + h + '" class="' + TOP_INACT + '">' + label + "</a>",
            '<a href="' + h + '" class="' + TOP_ACT + '">' + label + "</a>",
        )
        nav = nav.replace(
            '<a href="' + h + '" class="block py-2.5 text-secondary hover:text-[#c8872f]">' + label + "</a>",
            '<a href="' + h + '" class="block py-2.5 font-medium text-[#c8872f]">' + label + "</a>",
        )
        return nav
    if section == "contact":
        h = prefix + "/contact.html"
        nav = nav.replace(
            '<a href="' + h + '" class="' + TOP_INACT + '">Contact</a>',
            '<a href="' + h + '" class="' + TOP_ACT + '">Contact</a>',
        )
        nav = nav.replace(
            '<a href="' + h + '" class="block py-2.5 text-secondary hover:text-[#c8872f]">Contact</a>',
            '<a href="' + h + '" class="block py-2.5 font-medium text-[#c8872f]">Contact</a>',
        )
        return nav
    ph = parent_href[section]
    nav = nav.replace(
        '<a href="' + ph + '" class="' + PARENT_INACT + '">',
        '<a href="' + ph + '" class="' + PARENT_ACT + '">',
        1,
    )
    label = details_label[section]
    nav = re.sub(
        r'(<details class="group border-t border-gray-50">\s*<summary class="'
        + re.escape(SUM_INACT)
        + r'">\s*<span>'
        + re.escape(label)
        + r"</span>)",
        '<details class="group border-t border-gray-50" open>\n<summary class="'
        + SUM_ACT
        + '">\n<span>'
        + label
        + "</span>",
        nav,
        count=1,
    )
    return nav


def set_lang_switcher(nav: str, key: str, is_en: bool) -> str:
    if is_en:
        fr_href = "/" + key
        nav = re.sub(
            r'<a href="/[^"]*" class="hover:text-\[#c8872f\] transition-colors text-xs tracking-wider">FR</a>',
            '<a href="' + fr_href + '" class="hover:text-[#c8872f] transition-colors text-xs tracking-wider">FR</a>',
            nav,
            count=1,
        )
        nav = re.sub(
            r'<a href="/[^"]*" class="text-secondary hover:text-\[#c8872f\]">FR</a>',
            '<a href="' + fr_href + '" class="text-secondary hover:text-[#c8872f]">FR</a>',
            nav,
            count=1,
        )
    else:
        en_href = "/en/" + key
        nav = re.sub(
            r'<a href="/en/[^"]*" class="hover:text-\[#c8872f\] transition-colors text-xs tracking-wider">EN</a>',
            '<a href="' + en_href + '" class="hover:text-[#c8872f] transition-colors text-xs tracking-wider">EN</a>',
            nav,
            count=1,
        )
        nav = re.sub(
            r'<a href="/en/[^"]*" class="text-secondary hover:text-\[#c8872f\]">EN</a>',
            '<a href="' + en_href + '" class="text-secondary hover:text-[#c8872f]">EN</a>',
            nav,
            count=1,
        )
    return nav


def build_nav(gold: str, rel: str) -> str:
    is_en = rel.startswith("en/")
    key = page_key(rel)
    href = "/" + rel if is_en else "/" + key
    nav = gold
    nav = activate_section(nav, section_for(key), is_en)
    nav = activate_href_items(nav, href)
    nav = set_lang_switcher(nav, key, is_en)
    return nav


def normalize_src(src: str) -> str:
    m = re.search(r"assets/.+", src)
    if m:
        return "/" + m.group(0).lstrip("/")
    return src


def extract_hero(html: str):
    """Hero = first non-logo image in <main> (the image under the title)."""
    m = re.search(r"<main\b[^>]*>([\s\S]*?)</main>", html, re.IGNORECASE)
    body = m.group(1) if m else html
    for im in re.finditer(r"<img[^>]+>", body):
        tag = im.group(0)
        sm = re.search(r'src="([^"]+)"', tag)
        if not sm:
            continue
        src = normalize_src(sm.group(1))
        low = src.lower()
        if "logo" in low or "favicon" in low or "apple-touch" in low:
            continue
        am = re.search(r'alt="([^"]*)"', tag)
        return src, (am.group(1) if am else "")
    return None, ""


def og_url(src: str) -> str:
    if src.startswith("http"):
        return src.replace("https://al-uns.com/", "https://www.al-uns.com/")
    return "https://www.al-uns.com" + src


def upsert_og(html: str, image_url: str, alt: str) -> str:
    alt_esc = alt.replace(chr(34), "'")
    if 'property="og:image"' in html:
        html = re.sub(
            r'<meta property="og:image" content="[^"]*"\s*/?>',
            '<meta property="og:image" content="' + image_url + '">',
            html,
        )
        html = re.sub(
            r'<meta name="twitter:image" content="[^"]*"\s*/?>',
            '<meta name="twitter:image" content="' + image_url + '">',
            html,
        )
        if 'property="og:image:alt"' in html:
            html = re.sub(
                r'<meta property="og:image:alt" content="[^"]*"\s*/?>',
                '<meta property="og:image:alt" content="' + alt_esc + '">',
                html,
            )
        else:
            html = html.replace(
                '<meta property="og:image" content="' + image_url + '">',
                '<meta property="og:image" content="' + image_url + '">\n<meta property="og:image:alt" content="'
                + alt_esc
                + '">',
                1,
            )
        if 'name="twitter:image:alt"' in html:
            html = re.sub(
                r'<meta name="twitter:image:alt" content="[^"]*"\s*/?>',
                '<meta name="twitter:image:alt" content="' + alt_esc + '">',
                html,
            )
        if 'property="og:image:width"' not in html:
            html = html.replace(
                '<meta property="og:image" content="' + image_url + '">',
                '<meta property="og:image" content="'
                + image_url
                + '">\n<meta property="og:image:width" content="1376">\n<meta property="og:image:height" content="768">',
                1,
            )
        return html
    title_m = re.search(r"<title>([^<]+)</title>", html)
    title = title_m.group(1) if title_m else "Riad Al-Uns"
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', html)
    desc = desc_m.group(1) if desc_m else "Riad Al-Uns"
    canon_m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    canon = canon_m.group(1) if canon_m else "https://www.al-uns.com/"
    block = (
        '<meta property="og:type" content="website">\n'
        '<meta property="og:site_name" content="Riad Al-Uns">\n'
        '<meta property="og:title" content="' + title + '">\n'
        '<meta property="og:description" content="' + desc + '">\n'
        '<meta property="og:url" content="' + canon + '">\n'
        '<meta property="og:image" content="' + image_url + '">\n'
        '<meta property="og:image:width" content="1376">\n'
        '<meta property="og:image:height" content="768">\n'
        '<meta property="og:image:alt" content="' + alt_esc + '">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:title" content="' + title + '">\n'
        '<meta name="twitter:description" content="' + desc + '">\n'
        '<meta name="twitter:image" content="' + image_url + '">\n'
        '<meta name="twitter:image:alt" content="' + alt_esc + '">\n'
    )
    html = re.sub(r"</head>", block + "</head>", html, count=1, flags=re.IGNORECASE)
    return html


def ensure_menu_js(html: str) -> str:
    if "getElementById('menu-btn')" in html or 'getElementById("menu-btn")' in html:
        return html
    if "</body>" in html:
        return html.replace("</body>", MENU_JS + "\n</body>", 1)
    return html + MENU_JS


def process(path: Path, gold: str) -> dict:
    rel = rel_of(path)
    html = path.read_text(encoding="utf-8")
    if not NAV_RE.search(html):
        return {"rel": rel, "status": "no-nav"}
    nav = build_nav(gold, rel)
    html2, n = NAV_RE.subn(nav, html, count=1)
    if n != 1:
        return {"rel": rel, "status": "nav-sub-" + str(n)}
    html2 = ensure_menu_js(html2)
    hero, alt = extract_hero(html2)
    og_note = "no-hero"
    if hero:
        title_m = re.search(r"<title>([^<]+)</title>", html2)
        if not alt:
            alt = title_m.group(1) if title_m else "Riad Al-Uns"
        html2 = upsert_og(html2, og_url(hero), alt)
        og_note = hero
    path.write_text(html2, encoding="utf-8")
    return {"rel": rel, "status": "ok", "hero": og_note}


def main() -> None:
    print("ROOT", ROOT)
    fr_gold = prepare_fr_gold(extract_nav((ROOT / "comment-on-entre.html").read_text(encoding="utf-8")))
    en_gold = prepare_en_gold(extract_nav((ROOT / "en/index.html").read_text(encoding="utf-8")))
    for label in ("Comment on entre", "Après la résidence", "Organisation des espaces"):
        if label not in fr_gold:
            raise SystemExit("FR gold missing " + label)
    for label in ("How one enters", "After the residency", "Organisation of the spaces", "Adjoining house"):
        if label not in en_gold:
            raise SystemExit("EN gold missing " + label)

    results = []
    for p in sorted(ROOT.rglob("*.html")):
        rel = rel_of(p)
        if rel.startswith("al-munya/") or "/al-munya/" in rel:
            continue
        if rel.startswith("scripts/"):
            continue
        if rel in SKIP:
            continue
        gold = en_gold if rel.startswith("en/") else fr_gold
        try:
            results.append(process(p, gold))
        except Exception as e:
            results.append({"rel": rel, "status": "ERR " + str(e)})

    ok = [r for r in results if r["status"] == "ok"]
    bad = [r for r in results if r["status"] != "ok"]
    no_hero = [r for r in ok if r.get("hero") == "no-hero"]
    print("updated", len(ok), " errors", len(bad), " no-hero", len(no_hero))
    for r in bad:
        print("BAD", r)
    print("--- no hero ---")
    for r in no_hero:
        print(r["rel"])


if __name__ == "__main__":
    main()
