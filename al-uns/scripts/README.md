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
