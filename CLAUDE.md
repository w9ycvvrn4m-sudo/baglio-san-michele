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

## Come lavorare con Pietro (valido per tutte le conversazioni)

- **Fare le domande con le caselle a spunta** (strumento a scelta multipla), non
  in forma di testo libero. Vale sempre, in ogni conversazione su questo progetto.
- Procedere senza chiedere conferma quando la strada è chiara; chiedere solo ciò
  che cambia davvero il risultato.
- Risposte sobrie e diritte. Nessun linguaggio da hotel, resort o marketing.

---

## Profilo di Pietro (per lettere ai partner e materiali simili)

Da usare quando serve presentarlo — lettere a partner privati, materiali per mecenati,
bio, ecc.

Pietro è uno **Strategic Cultural Architect** e **Heritage & Innovation Strategist**.
Formazione accademica in storia e filosofia medievale, unita a un background come
Country Manager in multinazionali tecnologiche e a collaborazioni strategiche con
fondazioni culturali americane; specializzato in sociologia degli spazi e progettazione
di comunità intenzionali. Ha curato realizzazione di eventi e mostre di alto profilo.

Preferisce operare **dietro le quinte**: sono gli interlocutori — in particolare i
partner privati — a ricevere il vantaggio d'immagine e il merito delle idee sviluppate.

Non si occupa di operazioni immobiliari tradizionali: disegna ecosistemi umani e
produttivi in cui il rigore gestionale si sposa con l'Umanesimo, restituendo al lavoro
artigiano e al territorio una dignità duratura. Questo approccio è diventato un
**master-format replicabile**, applicato in due laboratori d'eccellenza: il recupero
storico del Baglio San Michele in Sicilia e l'Ambasciata Permanente dei Mestieri d'Arte
Dar al-Hiraf a Marrakech.

---

## Dossier Dar al-Diyafa — punti fermi già acquisiti

Estensione del progetto Riad Al-Uns: foresteria d'élite + operazione immobiliare
sugli edifici adiacenti. Decisioni prese finora, da non rimettere in discussione
senza motivo:

- **Tipologia**: foresteria come *douiria* tradizionale — corpo staccato, due
  porte su derb diversi, un solo passaggio con soglia a gomito, comando
  dell'apertura dal lato del riad.
- **Regola progettuale**: la foresteria deve conservare tutto il suo valore con
  la porta murata. Dà al riad un veto reale e all'investitore una garanzia.
- **Denaro**: il riad non incassa dagli ospiti. Il veicolo versa una **quota
  fissa annuale**, mai una percentuale sui ricavi.
- **Quattro chiavi, mai una di più**, da scrivere nello statuto.
- **Mai** usare il sisma del 2023 come leva d'acquisto o come materiale
  narrativo ESG. Punto chiuso.
- Il mercato della medina di Marrakech **cresce** (+12% 2024-2026): non esiste
  alcuno sconto post-sisma. Ogni cifra ricevuta da terzi va verificata prima
  dell'uso — i documenti generati altrove contenevano prezzi gonfiati 2-3 volte.
- Documenti sempre **separati**: A = il riad (identità e limiti), B = il veicolo
  (tesi immobiliare), + la convenzione che lega i due.
- Da verificare di persona: esistenza e mandato di **Vincent Desmarie** (Barnes).

**I mestieri sono sei**, non di più: calligrafia, zellige, gesso e mocárabe,
tessitura e broccato, legno e intaglio, profumi ed essenze. Le prime cinque sono
i *métiers de la main* del sito (`al-uns/dar-al-hiraf/disciplines.html`). Musica
(al-âla, malhun, gnawa, tahtib) e discipline del corpo sono cosa distinta e non si
contano fra i mestieri. Sei maestri reggono **18-24 apprendisti**, non trenta.

**Cosa scala con il capitale e cosa no.** Sotto una certa soglia la tesi immobiliare
non esiste (serve il controllo di un isolato, non due case). Ma con più denaro
crescono l'anello di edifici, la qualità del restauro e il numero di mestieri —
**non** il numero dei residenti, **non** le quattro chiavi, **non** la velocità.
Il capitale va chiesto in tre tranche: acquisizione, restauro e **fondo di
dotazione** che copra in perpetuo il costo ordinario del riad. Quanto più alta è la
cifra, tanto prima va firmata la convenzione: un investitore grande chiede
governance, e dopo non si negozia più.

**La cartella `dossier/` è riservata.** È esclusa da Git (`.gitignore`) e dalla
pubblicazione (`.vercelignore`): i documenti restano sul computer e non finiscono
mai online. Non tracciarla, non forzarne il commit.

Documenti presenti:

| File | Contenuto |
|---|---|
| `schema-due-corpi.svg` | Pianta schematica riad + douiria, soglia, flussi, affacci |
| `convenzione-a-b.md` | Il testo che lega riad e veicolo — bozza italiana v1 |
| `scheda-fes-marrakech.md` | Confronto delle due sedi, solo dati verificati |
| `programma-funzionale.md` | Dimensionamento: ~1.750 m² coperti, sedime 900-1.150 m² |
| `sospeso-equitazione.md` | **Materiale sospeso — non menzionare l'equitazione** |
| `dar-al-diyafa-libretto-accoglienza.md` | Testo ricevuto da rifare: registro alberghiero |

Tutti in italiano. La traduzione francese si fa quando il contenuto è fermo.

---

## In sospeso

- **`al-uns/qui-cherchons-nous.html`** — 8 segnaposto `[À CHOISIR].jpeg` da
  sostituire: *Qui cherchons-nous*, *Formation du caractère*, *Stabilité et
  discipline*, *Fraternité*, *Transmission de la futuwwa*, e tre orientamenti
  (métier, formation spirituelle, discipline physique).
- **`radici-storiche.html`** (IT ed EN) — manca `baglio-regole-3.png`, un ritratto
  di Pietro Laureano. Serve una foto sua: le altre `baglio-regole-*` sono scene di
  vita del borgo, non ritratti.
