# Audit Baglio San Michele — 17 agosto 2026

> **Stato al termine della sessione — tutto chiuso tranne i minori.**
> Corretti: le 14 unità (§1), le date della Fase 1 (§2), le navbar (§3), le traduzioni (§4),
> `brand.html` in noindex (§5), hreflang / canonical / sitemap / robots.txt (§6).
> In più, fuori elenco: l'Open Graph con immagine propria per ogni pagina, un `</main>`
> chiuso a metà di `figure-professionali.html`, e l'introduzione della **Fase 0**.
> **Restano aperti** solo i punti minori di §7 e la domanda su §8.
>
> **Come sono state chiuse le 14 unità.** Decisione: 14 = appartamenti per le famiglie
> **più** cellette per i single. La ripartizione fra Bronze / Silver / Gold è stata tolta da
> `index` e `il-progetto` (IT ed EN) perché richiede la perizia; restano le tipologie con le
> metrature. Tolti anche i due «8-9 residenti / 5-6 ospitalità» di `il-concept` e
> `investimento-etico`, sostituiti da «una parte minoritaria». `autonomia-energetica` e
> `radici-storiche` dicevano «14 appartamenti»: ora «14 unità abitative».
>
> **Fase 0 — progettazione operativa (settembre 2026 – marzo/aprile 2027).** Aggiunta prima
> della Fase 1 in `il-progetto` (sezione propria), `il-concept` (schema delle fasi), `faq` e
> `archivum-artium` (riga nell'elenco), `autonomia-alimentare` e `autonomia-energetica`
> (paragrafo introduttivo), IT ed EN. Comprende rilievi e perizie di geometri e architetti,
> analisi agronomiche, progettazione in permacultura, razionalizzazione energetica e idrica,
> pratiche autorizzative.
>
> **Calendario rifatto.** Con la Fase 0 che chiude nella primavera 2027, la vecchia Fase 1
> «2026-2028» avrebbe fatto partire il cantiere prima che il progetto esistesse. Slittate
> entrambe: **Fase 1 = 2027-2029**, **Fase 2 = post-2029**. 18 occorrenze corrette in 10
> pagine, `governance` compresa.


Perimetro: 25 pagine italiane in radice + 25 pagine in `en/`. Escluse `assets/` e `al-uns/`.

Stato generale: nessun link interno rotto, nessuna immagine rotta oltre a quella già nota,
nessun diacritico nei titoli, nessuna immagine `riad-*` sconfinata nel Baglio, `charset` e
`viewport` presenti su tutte le pagine, un solo `h1` per pagina, nessuna `img` senza `alt`,
nessun `id` duplicato, nessun refuso ortografico ricorrente. I problemi stanno altrove.

---

## 1. Contenuto — le 14 unità della Fase 1 sono raccontate in tre modi diversi

È l'incongruenza più visibile perché tocca il numero che un investitore legge per primo.

| Pagina | Cosa dice |
|---|---|
| `index.html`, `il-progetto.html` | 14 unità = **Bronze 3 + Silver 8 + Gold 3**, e le cellette «All'interno delle 14 unità … sono previste **anche**» |
| `faq.html`, `il-concept.html` (timeline), `chi-cerchiamo.html` | 14 unità = **appartamenti famiglie + cellette single** |
| `il-concept.html` (apertura) | 14 appartamenti = **8-9 residenti permanenti + 5-6 ospitalità selettiva** |

Le tre versioni non possono essere vere insieme: se 3+8+3 esaurisce già il 14, le cellette
sono fuori conto; e 8-9 + 5-6 fa 13-15, non 14. Inoltre `il-concept.html` si contraddice
al proprio interno (apertura vs. timeline in fondo alla pagina).

Da decidere una volta e propagare: **14 = quante case, cellette dentro o fuori, quante per
l'ospitalità**. Poi riscrivere le 6 pagine IT e le 6 EN corrispondenti.

Conteggi che invece tornano: Fase 2 = 5+10+6 = 21, e 14+21 = 35, coerente con le «35 unità»
di `autonomia-alimentare.html`. I 23 ettari compaiono una sola volta (`il-progetto.html`) e
nessuna pagina li contraddice.

## 2. Contenuto — date della Fase 1 discordanti

- `archivum-artium`, `autonomia-alimentare`, `autonomia-energetica`, `faq`: **Fase 1 (2026-2028)**
- `governance.html`: **Fase 1 (2026-inizio 2027)**

Nella stessa frase `governance.html` dà al Reggente un mandato di «massimo 24-36 mesi», che
sfora la Fase 1 così come la definisce quella riga. Va allineata a 2026-2028.

## 3. Navigazione — 6 pagine hanno una navbar vecchia

Queste pagine non elencano le voci aggiunte dopo:

| Pagina | Voci mancanti | Switch EN |
|---|---|---|
| `soggiornare.html` | Radici storiche, Vita comunitaria, Animali domestici | → `en/index.html` |
| `archivum-artium.html` | Radici storiche, Vita comunitaria, Animali domestici | → `en/index.html` |
| `figure-professionali.html` | Radici storiche, Vita comunitaria, Animali domestici | → `en/index.html` |
| `sicilian-slow-living.html` | Radici storiche, Vita comunitaria, Animali domestici | → `en/index.html` |
| `un-modello-diverso.html` | Radici storiche, Vita comunitaria, Animali domestici | → `en/index.html` |
| `animali-domestici.html` | Radici storiche, Vita comunitaria | → `en/index.html` |

Doppio effetto: `radici-storiche.html`, `vita-comunitaria.html` e `animali-domestici.html`
perdono link interni (contano per il posizionamento), e chi premeva EN da una di queste
sei pagine finiva sulla home inglese invece che sulla pagina corrispondente. Le 25 pagine
`en/` sono a posto: navbar identica su tutte e switch IT sempre alla pagina gemella.

## 4. Traduzioni — due pagine inglesi sono incomplete

`en/come-entrare.html` ha 3 sezioni su 7. Mancano:

- «Due destinazioni, uno stesso percorso»
- «Perché esiste un processo di selezione»
- «Cosa cerchiamo in chi vuole entrare»
- «Nota per chi desidera investire senza risiedere»

`en/tokenizzazione.html` ha 3 sezioni su 5. Mancano:

- «I crediti e il futuro del Borgo»
- «Chi decide le regole»

Sono le due pagine che un lettore straniero interessato a investire cerca per prime. Le
altre 23 traduzioni sono complete (rapporto testo EN/IT fra 0,82 e 1,04, numero di `h2`
identico).

## 5. `brand.html` — documento interno pubblicato online

La style guide è raggiungibile a `https://www.borgoideale.com/brand.html` — verificato, la
pagina risponde. Porta scritto «DOCUMENTO INTERNO» ma è indicizzabile: non ha `noindex`,
non ha `canonical`, non ha `description` né Open Graph, non è nella sitemap e non è linkata
da nessuna pagina (ha una navbar propria di 3 voci).

Tre strade: aggiungerla a `.vercelignore` (resta sul computer, come `dossier/`), oppure
metterle `<meta name="robots" content="noindex, nofollow">`, oppure trattarla come pagina
vera e completarla. La prima è la più coerente con la natura del file.

## 6. SEO — buchi sparsi nei metadati

**`hreflang` assente su 13 pagine.** IT: `animali-domestici`, `archivum-artium`, `brand`,
`chi-cerchiamo`, `come-entrare`, `figure-professionali`, `sicilian-slow-living`,
`soggiornare`, `un-modello-diverso`, `vita-comunitaria`, `vivere-qui`. EN: `en/donazioni`,
`en/vita-comunitaria`. Le altre 37 hanno il blocco `it` / `en` / `x-default` corretto.

**`en/donazioni.html`** è l'unica pagina del sito senza `canonical` e senza `meta robots`,
pur avendo og:url corretto. È la pagina delle donazioni: vale la pena sistemarla.

**Metadati social a chiazze.** `og:locale` su 10 pagine, `og:site_name` su 6,
Twitter Card su 27 su 50, `twitter:site`/`twitter:creator` solo su `en/index.html`.
Non è un errore, ma l'anteprima di un link cambia aspetto a seconda della pagina condivisa.

**`sitemap.xml`**: 50 URL, corretti e completi (tranne `brand.html`, giustamente fuori).
Tutti con `lastmod` 2026-07-28, mentre i file sono stati toccati il 15 agosto. Da
aggiornare quando si pubblica.

**`robots.txt`**: `Disallow: /dossier/` nomina in chiaro una cartella riservata che non
viene comunque pubblicata (è in `.vercelignore`). Meglio togliere la riga: dichiararla
serve solo a segnalarne l'esistenza.

## 7. Minori

- `san-michele.html` — 247 caratteri di testo, una citazione latina e una frase. È in
  navbar e in sitemap come le altre. Se la sobrietà è voluta va bene; se no è la pagina
  più povera del sito.
- **Apostrofi misti** — 59 apostrofi diritti (`'`) su 11 pagine IT, il resto del sito usa
  quello tipografico (`’`). Più visibile in `vita-comunitaria` (16), `vivere-qui` (14) e
  `chi-cerchiamo` (10).
- **Titoli identici IT/EN** su `faq.html` e `sicilian-slow-living.html`. Innocuo, l'hreflang
  copre il caso.
- **Due chiavi web3forms diverse**: `contatti` usa `e0ef2929…`, `figure-professionali` usa
  `991621e0…`. Probabilmente due caselle distinte, ma vale la pena averne conferma: se una
  delle due non è più attiva, le candidature si perdono senza errore visibile.
- **Nessun indirizzo email in chiaro** su tutto il sito del Baglio: si può scrivere solo dal
  form. Se è una scelta, va bene; se no, `contatti.html` è il posto.
- `assets/baglio-regole-3.png` manca ancora (ritratto di Pietro Laureano), rompe un'immagine
  in `radici-storiche.html` e `en/radici-storiche.html`. Già a elenco in `CLAUDE.md`.
- Tailwind da CDN su tutte le 51 pagine. Già a elenco in `CLAUDE.md`.

## 8. Fuori perimetro, ma da sapere

I 7 form del Riad puntano a `formsubmit.co/info@borgoideale.com`, mentre il Baglio usa
web3forms. Alla migrazione su `al-uns.com` va cambiato anche quello, altrimenti le
richieste del Riad continuano ad arrivare su una casella del Baglio.
