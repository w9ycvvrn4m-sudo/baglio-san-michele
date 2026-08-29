# Appunti di lavoro — borgoideale.com

File di riferimento per chi (o cosa) lavora su questo sito. Aggiornare quando cambiano
le convenzioni.

---

## Regole da non violare

**La prosa del sito è francese colto, non pubblicità.** Le pagine devono meritare di
essere lette per intero e citate da un architetto o da un conservatore. Il che
significa, in concreto:

- **Periodi ampi e subordinati.** Una media di venti parole a frase è troppo poco:
  la prosa francese saggistica sta fra le venticinque e le trentacinque. La chiarezza
  si ottiene con la sintassi, non spezzando.
- **Non più di tre o quattro trattini lunghi per pagina.** Quattordici sono un tic.
- **Bandita la formula «X n'est pas Y : c'est Z».** È il costrutto che più di ogni
  altro fa suonare artificiale un testo, e nelle pagine se ne era accumulato uno o due
  per pagina.
- **Niente frase a effetto in chiusura di paragrafo**, niente aforisma finale, niente
  domande retoriche, niente paragrafi di una riga sola messi lì per far colpo.
- **Niente calchi dal francese quando si parla in italiano**: *métier de la main* sul
  sito va benissimo, «mestiere di mano» in italiano no — si dice **mestiere manuale**.
  Stessa regola per «lavori d'acqua», «lavori di legno» e simili invenzioni.
- **Lessico tecnico esatto** — architettonico, artigianale, giuridico — al posto di
  perifrasi suggestive. È la precisione a rendere un testo citabile.

Vale per il francese e per l'inglese del sito, e per i documenti del dossier.

**Mai usare immagini `baglio-*` nelle pagine di `al-uns/`.**
Appartengono all'altro sito. Se una pagina francese ha bisogno di un'immagine,
usare `riad-*` o le altre presenti in `assets/`.

Eccezione storica: 4 riferimenti `baglio-*` già presenti in
`al-uns/architecture/patio.html` e `al-uns/architecture/eau.html` sono stati
lasciati per scelta esplicita. Non aggiungerne altri.

**Mai diacritici nei titoli.** Il font dei titoli è **Julius Sans One**, che non
ha i caratteri della traslitterazione scientifica: dove manca il glifo, il
browser sostituisce un altro font e la riga si sfascia.

Vale per ogni elemento con `class="heading"` — `h1`, `h2`, `h3`, `h4` — su tutti
e due i siti.

Il discrimine non è il blocco Unicode preso alla lettera. Il font copre il latino
di base e il **Latin-1** (fino a `U+00FF`) — accenti francesi, italiani e spagnoli
normali (`é è à â î ô û ë ï ü ç á`) — e copre anche la punteggiatura tipografica
che i titoli del sito già usano in un centinaio di casi: trattino lungo `—`,
freccia `→`, apostrofo `’`, legatura `œ`. Nessuno di questi è un problema.

Quello che il font non ha è la **traslitterazione scientifica**: vietati i macron
`ā ī ū ē ō`, i punti sottoscritti `ḥ ḍ ṣ ṭ ẓ`, la `ʿ` e la `ʾ`. Vietato anche
l'arabo, se non dentro un elemento annidato col font Amiri.

Scrivere il titolo in forma piana e mettere la forma vocalizzata altrove:

| | |
|---|---|
| Titolo | `Bawwab`, `Riyada`, `Faqih résident`, `Istidhan` |
| Corsivo nel testo | `<em>bawwāb</em>` — diacritici ammessi |
| Riga `class="translit"` | `bawwāb` — diacritici ammessi, font diverso |
| Indice alfabetico del glossario | `Bawwāb` — diacritici ammessi |

È la convenzione che il glossario seguiva già: titolo piano, traslitterazione
nella riga sotto. Per lo stesso motivo niente arabo dentro un titolo, a meno che
non stia in un elemento annidato col font Amiri.

Controllo rapido prima di pubblicare:

```
grep -roE '<h[1-4][^>]*class="[^"]*heading[^"]*"[^>]*>[^<]*' --include=*.html . \
  | grep -P '[āīūēōḥḍṣṭẓġḫšžʿʾ\x{0600}-\x{06FF}]'
```

Non deve restituire nulla. Attenzione a non allargare il set con `à á é è`:
sono legittimi, e includerli riempie il risultato di falsi positivi.

Le violazioni note sono state sistemate il 22 agosto 2026: la sezione
«Discipline du corps — Fur**ū**siyya» dei due glossari, e le tre voci
`Al-ʿudda`, `Al-ʿinan` e `Al-ʿaql as-salim fi l-jism as-salim`, che portavano la
ʿayn nel titolo. In tutti i casi la forma vocalizzata è rimasta nella riga
`translit` sotto. Il `grep` qui sopra non restituisce più nulla su nessuna delle
due lingue: se un giorno restituisce qualcosa, è roba nuova.

---

## Struttura

Sul desktop il clone locale è **`baglio-git`**. Un solo repository ospita
**tre siti distinti**:

| Percorso | Sito | Dominio | Lingua |
|---|---|---|---|
| radice (`index.html`, `il-progetto.html`…) | Baglio San Michele | borgoideale.com | italiano |
| `en/` | Baglio San Michele | borgoideale.com/en | inglese |
| `al-uns/` | Riad — Dar al-Hiraf | al-uns.com | francese |
| `al-uns/en/` | Riad — Dar al-Hiraf | al-uns.com/en | inglese |
| `al-uns/al-munya/` | Al-Munya | al-munya.com | francese |
| `al-uns/al-munya/en/` | Al-Munya | al-munya.com/en | inglese |

Le immagini del **Baglio** stanno in **`/assets`** (radice di `baglio-git`),
senza sottocartelle. È la directory condivisa da cui le pagine del Baglio
prendono foto, loghi e card Open Graph (`og-index.jpg`, `og-*.jpg`, ecc.).

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

1. Modificare i file in `Desktop/baglio-git` (immagini del Baglio: `Desktop/baglio-git/assets`)
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
- **Prompt per immagini (Firefly e simili): sempre la clausola sui personaggi.**
  Ogni volta che Pietro chiede un prompt in cui compare una persona, il prompt deve
  contenere l'istruzione esplicita che il personaggio ha l'aspetto, le fattezze, la
  corporatura e l'età di quello dell'immagine di riferimento che Pietro allega su
  Firefly. Non va chiesto: si mette sempre. Formula già usata e approvata:

  > The groom must be the same young Moroccan man as in the uploaded reference image:
  > same face and facial features, same skin tone, same hair and beard, same build and
  > height, same apparent age. Do not invent a different person and do not idealise or
  > slim the face — keep the likeness of the reference.

  Va messa subito dopo la descrizione del soggetto, non in fondo: Firefly pesa di più
  le prime righe. Quando i personaggi sono più d'uno, la clausola li nomina tutti.
  Nel resto del prompt non si descrivono tratti del viso che potrebbero contraddire
  il riferimento: l'identità la porta l'immagine, non il testo.

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

- **Migrazione su `al-uns.com`** (dominio da registrare entro fine agosto 2026).
  Il riad esce da `borgoideale.com` e diventa un sito autonomo. Da fare nello
  stesso giro: spostare anche gli **asset** (oggi le immagini sono servite dal
  dominio del Baglio, e il legame resta visibile nel sorgente), riscrivere tutti
  i `canonical`, gli `og:url` e la sitemap, e **non** mettere redirect 301 — il
  sito è di agosto 2026, non c'è autorità di dominio da preservare e un 301
  manterrebbe in piedi proprio la traccia che si vuole togliere. Verificare che
  nessuna pagina del riad linki il Baglio e viceversa.
- **Immagini da cancellare alla migrazione** — non più usate da nessuna pagina ma
  ancora pubblicate: `hammam-2.jpg`, `riad-hammam-1.jpg`, `jinn-dono.jpg`,
  `IMG_8232.jpeg`, `IMG_8235.jpg`, `arco-3.jpg`, `04_geste_c.jpg`,
  `06_huiles_b.jpg`, `05_huiles_a_copia.jpg`, `01_tayeb_a.jpg`,
  `02_tayeb_b_copia.jpg`, `jrdrD.jpg`, `iR4G8.jpg`. Attenzione: `assets/` è
  condivisa con il Baglio — cancellare solo dopo aver separato le due cartelle.
- **`al-uns/architecture/hammam.html`** — mancano due nature morte: *savon beldi*
  e *ghassoul*. Le tre voci del rituale sono per ora solo testo. Prompt pronti in
  `dossier/` (file dei prompt immagini). Non riusare `IMG_8232`/`IMG_8235`: sono
  due torsi nudi, non nature morte.
- **`al-uns/qui-cherchons-nous.html`** — 8 segnaposto `[À CHOISIR].jpeg` da
  sostituire: *Qui cherchons-nous*, *Formation du caractère*, *Stabilité et
  discipline*, *Fraternité*, *Transmission de la futuwwa*, e tre orientamenti
  (métier, formation spirituelle, discipline physique).
- **`radici-storiche.html`** (IT ed EN) — manca `baglio-regole-3.png`, un ritratto
  di Pietro Laureano. Serve una foto sua: le altre `baglio-regole-*` sono scene di
  vita del borgo, non ritratti.
- **`al-uns/soutenir.html`** — pagina per i mecenati, creata ma **non ancora
  collegata**: manca dalla navbar (37 pagine FR), manca dalla sitemap, manca la
  versione inglese, e il form di `contact.html` non ha ancora il motivo
  «mécénat». Dentro la pagina resta un segnaposto `https://donate.stripe.com/REMPLACER`:
  serve un link Stripe **distinto da quello del Baglio**, altrimenti i due
  progetti finiscono nello stesso rendiconto. Da decidere anche se e come
  compare il nome di Pietro (sezione «chi porta il progetto», non scritta).
- **Tailwind da CDN** su 124 pagine su 126. Scelta consapevole finché il sito
  cambia spesso: il CSS si compila nel browser a ogni visita, quindi il sito
  dipende da `cdn.tailwindcss.com` e senza quello resta senza grafica. Da
  convertire in un CSS statico in `assets/` **prima di mandare il sito ai
  mecenati**. Dopo la conversione ogni giro di modifiche richiede di
  rigenerare il file — non si fa da GitHub Desktop.
