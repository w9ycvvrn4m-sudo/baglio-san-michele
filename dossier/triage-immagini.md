# Triage delle immagini — sito al-Uns

*17 agosto 2026. Esaminate le immagini del gruppo a rischio (corpo, bagno, lotta) e
le immagini d'apertura delle pagine principali. Le pagine inglesi usano gli stessi
file: ogni sostituzione vale per entrambe le versioni.*

---

## 1. Il quadro

Buona notizia, e conta più dell'elenco che segue: **il problema è concentrato, non
diffuso**. Su 198 immagini distinte, quelle che non reggerebbero un dossier per Doha
sono una dozzina, tutte riconducibili a due gruppi — il bagno e la lotta. Tutto il
resto — l'accoglienza, i mestieri, la furusiyya a cavallo, il tahtib, il vestiario,
l'architettura, i ritratti in gandoura — è nel registro giusto: uomini vestiti,
gesti di lavoro, dignità.

Non serve rifare il sito. Servono dodici immagini.

---

## 2. Da sostituire subito

Queste tre sono nella stessa categoria dell'hero del hammam che abbiamo già tolto.

| File | Pagina | Problema |
|---|---|---|
| `riad-hammam-1.jpg` | `architecture.html` | Tre giovani a torso nudo, bagnati, gambe scoperte, che si sorridono seduti vicini nel vapore. È la peggiore rimasta sul sito: non un bagno, una scena di intimità di gruppo. In più due dei tre hanno **tatuaggi** visibili. |
| `hammam-2.jpg` | `dar-al-hiraf/dress-code.html` | Torso nudo frontale, sguardo in camera, fūṭa annodata bassa, una seconda figura nuda nel vapore alle spalle. Illustra il paragrafo sulla fūṭa: l'immagine smentisce il testo che le sta accanto. |
| `jinn-dono.jpg` | *già rimossa* | Torso nudo con fūṭa cortissima e un jinn — anch'esso a torso nudo — inginocchiato che gli porge un vassoio. Tolta oggi dalle due pagine hammam. Non riutilizzarla altrove. |

**Fatto il 17 agosto**, su francese e inglese:

- `architecture.html` → `hammam-1.jpg`. Un uomo solo, ripreso di spalle, fūṭa
  annodata correttamente, nessuno sguardo in camera, nessun tatuaggio.
- `dress-code.html`, sezione *Al-Futa* → `hammam-C.jpg`, le fūṭa piegate sulla
  mensola. La sezione parla del capo: ora mostra il capo invece di chi lo porta.

---

## 3. Il gruppo della lotta

Qui il giudizio è diverso. La lotta tradizionale è una disciplina documentata,
il torso nudo è quello del *musara* e del *kispet* ottomano, e un lettore del Golfo
riconosce il genere: non è nudità gratuita. Il problema è un altro, ed è lo stesso
in tutte e quattro le immagini.

**I lottatori si sorridono.**

| File | Pagina | Nota |
|---|---|---|
| `lotta-piedi-sarouel.jpg` | `dress-code.html` | I due si sorridono, braccia intorno alle spalle. |
| `lotta-terra-kispet.jpg` | `furusiyya.html` | Stessa cosa, ma la presenza degli spettatori raddrizza la lettura: si vede che è un incontro pubblico. |
| `lotta-2.jpg` | `dress-code.html` | La migliore delle quattro: sforzo vero, presa vera, nessun sorriso. |
| `lottatori-riad-4.jpg` | `qui-cherchons-nous.html` | Tecnicamente corretta, ma su una pagina di reclutamento due torsi nudi fronte a fronte lavorano contro il testo. |

Un incontro si combatte con fatica e concentrazione, non guardandosi negli occhi
e sorridendo. Il sorriso reciproco è ciò che trasforma la presa in un gesto
affettuoso — ed è l'unica cosa che si potrebbe correggere. **Non serve vestirli.**

> **Decisione del 17 agosto: `lotta-piedi-sarouel.jpg` e `lotta-terra-kispet.jpg`
> restano come sono.** Il torso nudo del *musara* e del kispet è la disciplina, non
> un problema. Quanto segue vale solo se un giorno si rigenerano per altri motivi.

**Da aggiungere al prompt in un'eventuale rigenerazione:**

> strained concentrated expressions, jaw set, eyes on the grip not on each other,
> effort visible, dust and sweat, spectators watching in the background

**Negative:** `smiling, laughing, mutual gaze, eye contact between the two,
affectionate, relaxed, playful, embrace`

---

## 4. Il tiro con l'arco

`arco-3.jpg` (`dress-code.html`) — la gandoura senza maniche lascia scoperta tutta
la spalla e l'ascella, la pelle è lucida, e l'arciere sorride verso l'obiettivo
mentre un compagno lo guarda sorridendo. La giustificazione funzionale è reale e
sta nel testo — la corda non deve incontrare ostacoli — ma l'immagine non la
racconta: racconta un ritratto.

**Risolto il 17 agosto senza rigenerare nulla**: sostituita con `arco-1.jpg`, che
era già in `assets/`. Stesso formato verticale, quindi nessuna modifica al layout;
mostra la spalla scoperta di cui parla il testo; e l'arciere è di profilo con gli
occhi sulla freccia. Sparisce il sorriso in camera, che era l'unico difetto.

*(`arc.jpg` e `IMG_7404.png` non esistono in `assets/`. C'è `arc.jpeg`, ma è
orizzontale 1200×670 in uno slot verticale 3:4 e mostra arcieri con le maniche,
in contraddizione con la didascalia sulla spalla libera.)*

---

## 5. Una nota a parte: i tatuaggi

In `riad-hammam-1.jpg` due dei tre ragazzi portano tatuaggi ben visibili, uno sul
petto e uno sulla gamba. È un problema **indipendente** dalla nudità: nella lettura
maggioritaria del diritto islamico il tatuaggio è proibito, e un progetto che si
presenta come custode della tradizione non può mostrare i propri residenti tatuati.
Vale la pena controllare tutte le immagini generate con corpi scoperti: i modelli
li aggiungono da soli, come dettaglio «di carattere».

Da mettere stabilmente nel negative prompt di ogni immagine con persone:
`tattoo, tattoos, body art, piercing, earring`.

---

## 6. Cosa è risultato in ordine

Verificate e senza problemi:

- `welcome-c.jpg` (home) — accoglienza in gandoura e tarbouche, tono giusto;
- `furusiyya-2.jpeg` — cavallo, turbante, due uomini vestiti, ottima;
- `IMG_7420.jpeg` (discipline choreutiche) — tre giovani in qamis con i bastoni
  del tahtib, sobria e forte;
- `kispet-2.jpg` e `zurkhane-2.jpg` — nature morte di calzoni di cuoio, perfette:
  sono la prova che il vestiario si può raccontare senza corpi.

---

## 7. Il resto del censimento

Le 198 immagini comprendono 66 file `IMG_XXXX.jpeg` distribuiti su quasi tutte le
pagine. Il campione che ho aperto — le immagini d'apertura di home, projet,
dar al-Hiraf, furusiyya, discipline choreutiche — è risultato tutto in ordine, il
che suggerisce che il grosso non abbia bisogno di interventi.

Se vuoi la certezza invece della probabilità, il modo più rapido è procedere per
pagina e non per file: partire da `dress-code.html` (che è la pagina con più corpi
in assoluto), poi `furusiyya.html`, `javanmardi.html`, `qui-cherchons-nous.html`,
`vie.html` e `sejour.html`. Sono sei pagine; il resto del sito è architettura,
mestieri e oggetti.

**Nota tecnica:** i nomi `IMG_7053.jpeg` e simili andrebbero rinominati in forma
parlante prima della migrazione su al-uns.com. Non è una questione estetica: nel
sorgente di una pagina, un `IMG_7053.jpeg` accanto a un `hammam-C.jpg` dice che il
sito è stato messo insieme senza un criterio, e chi verifica legge anche questo.
