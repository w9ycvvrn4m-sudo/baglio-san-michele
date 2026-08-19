# Al-Munya — note per la messa online

## File

```
index.html                    pagina pubblica (FR)
en/index.html                 pagina pubblica (EN)
espace-a7f3c9e2.html          area riservata (FR)   ← nome non indovinabile
en/espace-a7f3c9e2.html       area riservata (EN)
assets/                       marchi ridotti e favicon
robots.txt                    esclusione totale dai motori
.htaccess                     protezione con password (Apache), da attivare
```

## L'area riservata

Il nome del file contiene un token casuale: `espace-a7f3c9e2.html`. Finché non
c'è la password, è questo a proteggerla, insieme a tre cose:

- `noindex, nofollow, noarchive` in ogni pagina;
- **nessun link dalla pagina pubblica** — ci si arriva solo conoscendo l'indirizzo;
- **il percorso non compare in `robots.txt`**, perché elencarlo lo rivelerebbe:
  `robots.txt` è pubblico e sarebbe la prima cosa che un curioso apre.

Il token va comunicato ai soci una volta sola e non va scritto in nessuna
email che possa essere inoltrata. Se un giorno trapela, si cambia il token e si
rigenera il sito: è un parametro solo, in cima al generatore.

### La password

Tre strade, a seconda di dove ospiterai il sito.

| Hosting | Come |
|---|---|
| **Apache** (la maggior parte degli hosting classici) | il file `.htaccess` è già pronto: genera il `.htpasswd` **fuori** dalla cartella pubblica e correggi il percorso |
| **Netlify** | protezione password integrata, a livello di sito o di cartella |
| **Cloudflare Access** | la più solida: accesso per indirizzo email, con codice inviato al momento, e nessuna password condivisa da cambiare quando un socio esce |

Per un centinaio di soci consiglierei **Cloudflare Access**: una password unica
condivisa fra novantanove uomini non è una password, ed è impossibile revocarla
a uno solo. Con l'accesso per email, radiare un socio è togliere una riga.

## I marchi ridotti

Non sono riduzioni dell'emblema: sono disegnati a parte, come il documento sui
marchi (§6) prescrive.

- **Al-Munya** — l'arco a ferro di cavallo del *menzeh* e la linea dell'acqua.
  Il riflesso, che nell'emblema grande è la cosa più bella, a 16 px sparisce:
  è stato tolto.
- **An-Nudamāʾ** — il *khātam*, la stella a otto punte, in oro su notte.
  Regge a qualunque dimensione.

Formati: `.svg` (browser moderni), `.ico` a 16 e 32 px, `.png` a 180 px per
iOS, `.png` a 512 px per ogni altro uso.

## L'emblema grande

Le pagine cercano `assets/emblema-al-munya.svg` e `assets/emblema-an-nudama.svg`.
**Copiali dalla cartella `identita/`**. Finché non ci sono, l'immagine si
nasconde da sola e la pagina resta pulita — nessun riquadro rotto.

## Da fare prima di pubblicare

- [ ] copiare i due emblemi in `assets/`
- [ ] decidere il dominio: `al-munya` o `an-nudama` (§13 della nota di concetto)
- [ ] aggiungere `canonical` e `hreflang` nel `<head>`, oggi assenti di proposito
- [ ] attivare la protezione dell'area riservata
- [ ] sottoporre al faqīh: il ḥadīth *al-majālis bi-l-amāna* e la formula *cento meno uno*
