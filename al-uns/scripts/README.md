# Site automations — Riad Al-Uns

## `sync_navbar_og.py`

Allinea la navbar FR/EN su tutte le pagine HTML e imposta `og:image` / `twitter:image` sull’immagine hero della pagina (prima foto in `<main>`, escluso il logo).

```bash
# sito in questo albero
python3 scripts/sync_navbar_og.py

# clone di produzione
AL_UNS_ROOT=/tmp/baglio-push/al-uns python3 scripts/sync_navbar_og.py
```

Idempotente: si può rilanciare dopo aver aggiunto voci al menu della pagina gold
(`comment-on-entre.html` per il FR, `en/index.html` per l’EN).

Saltate: `apres.html` (redirect), `dar-al-hiraf/productions.html` (redirect), `al-munya/`.

Pagine senza hero (FAQ, glossaire, …) non ricevono un og inventato.

## `sync_sitemap.py`

Riallinea `sitemap.xml` e `en/sitemap.xml` ai file reali. Da lanciare come **ultimo gesto prima di
pubblicare**: il `lastmod` e' vero solo nell'istante in cui lo si scrive.

```bash
python3 scripts/sync_sitemap.py              # scrive
python3 scripts/sync_sitemap.py --dry-run    # mostra soltanto

AL_UNS_ROOT=/tmp/baglio-push/al-uns python3 scripts/sync_sitemap.py
```

Fa tre cose e nient'altro:

- `<lastmod>` = data dell'ultimo commit che ha toccato la pagina; per le pagine con modifiche non
  ancora committate, la data di modifica del file, che in quel caso e' piu' recente.
- `<changefreq>` e `<priority>` = quelli della gemella francese, cosi' che le tre lingue dichiarino
  la stessa pagina allo stesso modo.
- Nessun URL aggiunto o tolto, nessun `hreflang` toccato. Le pagine `noindex` restano fuori,
  `/ar/glossaire.html` non viene inventato finche' la pagina non esiste.

Idempotente: rilanciato senza nuovi commit non cambia nulla. Se un `<loc>` non ha piu' un file su
disco lo segnala e lo lascia intatto, uscendo con stato 1.

Legge il git con `GIT_OPTIONAL_LOCKS=0`, cosi' non lascia un `.git/index.lock` di traverso.
