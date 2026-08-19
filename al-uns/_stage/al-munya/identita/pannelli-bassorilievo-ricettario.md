# Pannelli in bassorilievo

## Ricettario dei prompt — oro e argento, dalla fotografia alla placca

*Nota di lavoro — agosto 2026. Da usare con uno strumento che accetta immagine di riferimento + testo.*

---

## 1. Il metodo, in tre passi

1. **Scegli la fotografia.** Una sola inquadratura, frontale o quasi, con un soggetto chiaro e uno sfondo che si possa buttare via. Le foto migliori sono quelle già simmetriche: un portale, una fontana, un arco, un banco di lavoro visto di fronte.
2. **Carica l'immagine e incolla il blocco di stile del §3**, senza cambiarlo di una parola.
3. **Aggiungi, sotto, la sola riga del soggetto** — presa dal §4 se il caso è previsto, altrimenti scritta secondo lo schema del §5.

Il blocco di stile non va mai riscritto né riassunto. È ciò che tiene insieme la serie: se cambia da un pannello all'altro, i pannelli non staranno più bene uno accanto all'altro, e sarà evidente.

---

## 2. Che cosa stiamo imitando

Il logo del riad non è un disegno: è **una placca di metallo sbalzato**. Va guardata come tale, perché è da lì che discendono tutte le regole che seguono.

- L'architettura, le piante e gli oggetti sono in **oro**, lucido sulle creste e opaco nelle superfici piane.
- Il cielo, il piano di fondo e i vuoti sono in **argento spazzolato**.
- Il rilievo è **basso**: tre o quattro piani di profondità, non di più. Non è un modellino, è una lastra.
- I vani veri — la porta, il sottarco, le finestre — sprofondano fino a leggere **quasi neri**. È quel contrasto che fa il disegno; senza, tutto si appiattisce in una poltiglia dorata.
- La luce viene **da sinistra in alto**, sempre, e le ombre cadono corte verso destra in basso.

Chi tiene queste cinque cose ottiene un pannello che sta accanto al logo. Chi ne perde una ottiene un'illustrazione dorata qualunque.

---

## 3. Il blocco di stile

Da incollare identico sopra ogni prompt, con l'immagine caricata.

```
Reinterpret the attached photograph as a shallow gilded bas-relief plaque.

MEDIUM: chased and repoussé metalwork, a single cast panel. Architecture,
objects and plants modelled in polished and matte GOLD; sky, ground plane and
empty background in brushed SILVER. No other colour anywhere in the image.

RELIEF: very shallow, with three or four clearly separated depth planes.
Deepest recesses — door openings, arch soffits, window voids — read almost
black. Crisp chiselled edges, faceted planes, no painterly brushwork, no
engraved hatching used as shading.

LIGHT: soft studio light from the upper left; warm specular highlights along
the top edges of the gold forms; short soft cast shadows falling to the lower
right.

COMPOSITION: keep the subject and the framing of the photograph. Square 1:1.
Subject centred, with an even margin on all four sides. Plain white background
outside the plaque. No frame, no border, no cartouche.

CLEAN-UP: remove all people, vehicles, cables, signage, modern fittings,
lighting fixtures and background clutter. Simplify foliage into stylised
sculptural masses. Simplify the sky into a plain brushed silver field.

Very high detail, sharp focus, no text, no lettering, no logo, no watermark.
```

### Il negative prompt

```
people, human figures, faces, hands, vehicles, text, letters, numerals,
signage, watermark, colour, coloured paint, patina, verdigris, rust, plastic,
photograph, painting, watercolour, engraved hatching, wood grain, marble,
lens flare, bokeh, motion blur, tilted horizon, cropped subject, decorative
frame, ornate border
```

---

## 4. Clausole di materia

Una riga sola, da aggiungere dopo il blocco di stile quando l'immagine contiene quella cosa. Se ne possono sommare due o tre; oltre, il modello comincia a perdere il soggetto.

**Acqua ferma**
> `WATER: still water rendered as horizontal parallel bands of polished silver, with the subject mirrored in it in shallow relief.`

**Acqua che scorre, fontana**
> `WATER: falling water rendered as thin vertical rods of polished silver with rounded ends; the basin surface as concentric chased rings.`

**Zellīj, mosaico, pavimento geometrico**
> `TILEWORK: the geometric pattern rendered as flat silver tesserae inlaid into the gold ground, every tessera a separate facet with a sharp edge, no gradient inside a tessera.`

**Gesso intagliato, muqarnas, stucco**
> `CARVED PLASTER: rendered as the deepest and finest relief in the panel, undercut, with sharp shadow lines; matte gold, no polish.`

**Legno intagliato, porta, moucharabieh**
> `WOODWORK: rendered as matte gold with deep straight-sided cuts; the lattice openings pierced right through to the dark ground behind.`

**Tessuto, tappeto, drappo**
> `TEXTILE: rendered as deep parallel folds in matte gold, the weave suggested by fine regular chasing, never by colour.`

**Vegetazione**
> `FOLIAGE: leaves and fronds as flat layered gold blades with a chiselled midrib; no naturalistic texture; trees reduced to three or four stacked masses.`

**Fuoco, lampada, brace**
> `LIGHT SOURCE: the flame rendered as a small burst of polished silver with radiating chased rays; the glow as concentric shallow steps in the surrounding gold.`

**Cielo notturno**
> `NIGHT: invert the metals — the architecture in silver against an oxidised dark ground, with eight-pointed stars in polished silver.`

**Cavallo, animale**
> `ANIMAL: modelled in polished gold, in strict profile, stylised and heraldic rather than naturalistic; no eyes rendered in detail.`

---

## 5. Se il soggetto non è previsto

Scrivi una riga sola, in inglese, con questa struttura:

> `SUBJECT: [che cosa si vede], seen [da dove], with [i due o tre elementi da tenere]. Remove [ciò che va tolto].`

Esempio:

> `SUBJECT: a carved cedar door in a plastered wall, seen frontally and centred, with its iron studs, its horseshoe surround and the two steps below it. Remove the street, the wires and the shopfront to the right.`

Tre regole per scriverla bene:

- **Nomina che cosa tenere, non che cosa vuoi che sia bello.** «con i suoi chiodi di ferro» funziona; «magnifico e maestoso» non fa niente.
- **Di' sempre da dove si guarda.** Frontale, di tre quarti, dal basso. Il logo del riad è frontale e i pannelli dovrebbero esserlo quasi sempre: la frontalità è ciò che rende una scena araldica invece che turistica.
- **Elenca ciò che va tolto**, uno per uno. Il modello non indovina che il cavo elettrico ti dà fastidio.

---

## 6. Una questione da decidere prima di cominciare

**Le figure umane vanno escluse senza eccezioni** — sono già nel negative prompt. Non per prudenza grafica: un bassorilievo figurato di persone, in una casa maghrebina, è esattamente il genere di cosa su cui non conviene aprire una discussione, e non serve a niente che il progetto abbia bisogno. Il logo del riad, del resto, non ha figure: ha una porta.

**Gli animali sono un caso diverso e vale la pena pensarci una volta sola.** Il cavallo è nel cuore della *furūsiyya* e nel §4 della nota di concetto; il rilievo animale ha una tradizione lunga in ambito islamico occidentale — i leoni dell'Alhambra, la cerbiatta di Madīnat al-Zahrāʾ. È difendibile. Ma resta più discusso della sola architettura, e un pannello con un cavallo attirerà commenti che un pannello con una porta non attira mai.

La mia raccomandazione: **tenere la serie sull'architettura, gli oggetti, le piante e l'acqua**, e usare l'animale una volta sola, se serve davvero, e in forma dichiaratamente araldica — di profilo, stilizzato, come su una moneta. Non naturalistico.

Il mestiere si racconta benissimo senza mani: il banco, gli attrezzi posati, il pannello a metà, la forgia spenta. Un'officina vuota dice più lavoro di un'officina con dentro qualcuno che posa.

---

## 7. Controllo di qualità

Prima di tenere un pannello, sei domande. Se una risposta è no, si rigenera — non si corregge.

1. Il fondo è **argento spazzolato**, o è diventato un grigio piatto senza direzione?
2. I vuoti — porta, sottarco, finestre — sono **profondi e quasi neri**, o si sono riempiti di oro?
3. La luce viene **da sinistra in alto**, come in tutti gli altri pannelli della serie?
4. È rimasto **del colore** da qualche parte? Un verde, un azzurro, una patina. Non deve restarne.
5. Il rilievo è **basso**, o il modello ha prodotto un plastico tridimensionale?
6. Il modello ha aggiunto **una cornice** di sua iniziativa? Se sì, si scarta: il cartouche è dei tre marchi e di nient'altro.

---

## 8. Tenere insieme la serie

- **Generare tutti i pannelli nella stessa sessione**, uno dopo l'altro, senza cambiare il blocco di stile. Sessioni diverse danno metalli diversi, e la differenza si vede appena li metti in fila.
- Se lo strumento espone il **seed**, fissarlo e riusarlo per tutta la serie.
- Se lo strumento ha un cursore di **fedeltà all'immagine di riferimento**, tenerlo alto abbastanza da conservare l'architettura ma non tanto da conservare la fotografia: il pannello deve somigliare al luogo, non alla foto del luogo. In pratica si comincia a metà scala e si aggiusta.
- Quando la serie è finita, **guardarli tutti insieme a piccola dimensione**. Gli errori di luce e di profondità si vedono lì, non a schermo pieno.
- **Consegna**: quadrato, 2048 px, PNG, fondo bianco, senza scritte. Il testo si compone dopo, in impaginazione — mai dentro l'immagine.

---

## 9. Il menzeh — prompt di visualizzazione architettonica

Caso a parte: qui non si parte da una fotografia da trasformare, ma si costruisce **una lastra pulita** — un prospetto frontale del padiglione, da lavorare poi in Photoshop e solo alla fine da portare in oro e argento.

Il modello di riferimento sono i due *templetes* sporgenti del **Patio de los Leones** dell'Alhambra: è la forma canonica del padiglione da giardino nasride, ed è esattamente ciò che la nota di concetto chiama *menzeh*.

### 9.1 — Prompt

```
A single free-standing Nasrid garden pavilion (menzeh), rendered as a straight
architectural elevation.

BUILDING: a square open pavilion in the manner of the two projecting templetes
of the Court of the Lions, Alhambra, Granada. Front façade of three arches — a
wider central arch flanked by two narrower ones. The arches are lambrequin
muqarnas arches with finely pierced carved stucco (yesería) spandrels above
them, filled with sebka lattice and a narrow epigraphic band. They spring from
slender cylindrical white marble columns with ringed necking and cubic muqarnas
capitals: the outer supports in clusters of two or three columns, the inner
ones single. Below the arcade, a low white marble plinth of two steps running
the full width of the building.

ROOF: a low four-sided pyramidal roof of small curved glazed ceramic tiles in
green and brown, with deep overhanging eaves carried on a carved cedar cornice
of closely spaced corbels; a slender ceramic finial at the apex. Between the
arcade and the eaves, a band of carved stucco panelling.

VIEW: strict frontal elevation. Camera exactly on the central axis at mid
height, long telephoto lens, no perspective convergence, no vanishing point,
verticals perfectly vertical, perfectly symmetrical left to right.

LIGHT: soft even overcast daylight, no direct sun, no strong cast shadows, so
that every carved detail stays legible.

BACKGROUND: the pavilion isolated on a plain flat neutral background — no sky,
no landscape, no ground beyond the plinth. Generous even margin on all four
sides; the whole building inside the frame, finial and plinth included.

Square 1:1, very high resolution, sharp throughout, architectural photography,
no people, no text.
```

**Negative prompt**

```
people, tourists, ropes, stanchions, signage, text, watermark, sky, clouds,
trees, garden, furniture, light fittings, cables, wide-angle distortion,
fisheye, low camera angle, dutch angle, motion blur, bokeh, HDR halo,
oversaturated orange, warm sunset light, night, dome, minaret
```

### 9.2 — Che cosa aspettarsi, e che cosa fare in Photoshop

- **La prospettiva non sarà mai davvero ortogonale.** I modelli non sanno fare un prospetto. Si raddrizza con *Perspective Warp* o una *Free Transform* sui quattro angoli, prendendo come riferimento la linea di gronda e il filo del plinto.
- **La simmetria sarà imperfetta**, ed è qui che si guadagna di più: si sceglie **la metà migliore**, la si specchia sull'asse e si ricompone la facciata. Un prospetto costruito così è pulito in un modo che nessuna generazione diretta raggiunge.
- **I muqarnas e la sebka verranno impastati.** È il limite duro. Conviene generare tre o quattro varianti e comporre: il tetto di una, l'arcata di un'altra, il fregio di una terza. Oppure accettare un'arcata semplificata e ricostruire il traforo a parte, come *pattern* ripetuto.
- **Generare alla risoluzione massima disponibile.** Lo stucco è il primo dettaglio che muore.
- **Ritaglio**: il fondo neutro piatto serve proprio a questo, per staccare il soggetto con una selezione pulita e conservare il canale alfa.
- **Solo alla fine** si applica il blocco di stile del §3 sul prospetto ripulito. Se lo si applica prima, si porta in oro anche l'errore.

### 9.3 — Una nota che vale la pena fare adesso

Il *templete* dell'Alhambra è il riferimento giusto **per l'emblema**: è la forma canonica del padiglione da giardino andaluso, e la nota di concetto rivendica esplicitamente le radici andaluse.

Ma se il pannello dovrà un giorno rappresentare **il padiglione reale della Munya**, il riferimento onesto è marocchino, non granadino: i *menzeh* dell'Agdal e della Menara a Marrakech, i padiglioni saadiani, il vocabolario marīnide di Fès. Sono più sobri — meno stucco, più legno di cedro e tegola verde — e sono ciò che si potrà davvero costruire.

Conviene decidere fin d'ora quale dei due si sta disegnando, perché sono due edifici diversi e la differenza si vedrà.

---

*Documento di lavoro. Complemento a `marchi-al-munya-an-nudama.md`.*
