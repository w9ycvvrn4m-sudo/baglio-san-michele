# Appunti di lavoro — borgoideale.com

File di riferimento per chi (o cosa) lavora su questo sito. Aggiornare quando cambiano
le convenzioni.

---

## Regole da non violare

**Mai usare immagini `baglio-*` nelle pagine di `al-uns/`.**
Appartengono all'altro sito. Se una pagina francese ha bisogno di un'immagine,
usare `riad-*` o le altre presenti in `assets/`.

Eccezione storica: 4 riferimenti `baglio-*` già presenti in
`al-uns/architecture/patio.html` e `al-uns/architecture/eau.html` sono stati
lasciati per scelta esplicita. Non aggiungerne altri.

---

## Struttura

Un solo repository ospita **due siti distinti**:

| Percorso | Sito | Lingua |
|---|---|---|
| radice (`index.html`, `il-progetto.html`…) | Baglio San Michele | italiano |
| `en/` | Baglio San Michele | inglese |
| `al-uns/` | Riad — Dar al-Hiraf | francese |
| `al-uns/en/` | Riad — Dar al-Hiraf | inglese |

Tutte le immagini stanno in **`assets/`**, senza sottocartelle.

---

## Percorsi delle immagini

Il numero di `../` dipende dalla profondità della pagina. Errore già capitato una
volta: le pagine di `al-uns/en/` erano state copiate da `al-uns/` senza aggiornare
i percorsi, e 78 immagini risultavano rotte online.

| Pagina | Percorso |
|---|---|
| `index.html` (radice) | `assets/foto.jpg` |
| `en/`, `al-uns/` | `../assets/foto.jpg` |
| `al-uns/en/`, `al-uns/architecture/` | `../../assets/foto.jpg` |
| `al-uns/en/architecture/` | `../../../assets/foto.jpg` |

**Nomi dei file:** niente spazi né accenti, usare trattini. Attenzione alle
maiuscole: su macOS non contano, sul server di Vercel sì.

---

## Pubblicare

1. Modificare i file in `Desktop/borgoideale.com`
2. Aprire **GitHub Desktop** → controllare la lista in `Changes`
3. Scrivere il `Summary` (obbligatorio) → `Commit to main`
4. `Push origin`

Vercel pubblica da solo in un paio di minuti su
[baglio-san-michele.vercel.app](https://baglio-san-michele.vercel.app).

**Prima di ogni push, controllare che non ci siano cancellazioni impreviste**
(icona `−` rossa). Non usare mai `rsync --delete` verso questa cartella: `assets/`
è condivisa fra i due siti e si rischia di cancellare immagini usate altrove.

---

## In sospeso

- **`al-uns/qui-cherchons-nous.html`** — 8 segnaposto `[À CHOISIR].jpeg` da
  sostituire: *Qui cherchons-nous*, *Formation du caractère*, *Stabilité et
  discipline*, *Fraternité*, *Transmission de la futuwwa*, e tre orientamenti
  (métier, formation spirituelle, discipline physique).
- **`radici-storiche.html`** (IT ed EN) — manca `baglio-regole-3.png`, un ritratto
  di Pietro Laureano. Serve una foto sua: le altre `baglio-regole-*` sono scene di
  vita del borgo, non ritratti.
