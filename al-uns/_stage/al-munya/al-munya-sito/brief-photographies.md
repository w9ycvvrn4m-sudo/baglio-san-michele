# Al-Munya — brief photographique

*Document de travail. Une seule image par page, en bandeau, au-dessus du titre.*

## Principe

Le sujet est **allusif**. Jamais la maison, jamais une chambre, jamais un lit, jamais une table dressée, jamais une piscine, jamais un visage. Une maison qui interdit la photographie à ses membres ne peut pas se photographier elle-même pour se vendre : l'image doit donc montrer **une matière ou une lumière**, pas un lieu identifiable.

Si l'image pouvait figurer dans la brochure d'un hôtel, elle est mauvaise.

## Contraintes techniques communes

- Format bandeau, très large : 2400 × 900 px minimum, recadrable en 3:1.
- Lumière naturelle uniquement. Aucune lumière ajoutée, aucun réflecteur.
- Heure rasante — juste après le *fajr*, ou l'heure qui précède le *maghrib*.
- Gamme chromatique de la maison : crème, ocre, or éteint, brun. Aucune couleur saturée.
- Le tirage doit rester lisible sous un voile blanc à 90 % d'opacité (l'image passe derrière un dégradé).
- Aucune retouche autre que densité et contraste. Aucun filtre.

## Page 1 — la maison (`index.html`)

**Sujet retenu : un mur.** Enduit de chaux ancien, en lumière rasante, à hauteur d'homme. Rien d'autre dans le cadre : ni porte, ni fenêtre, ni objet, ni ombre humaine. La matière seule, ses reprises, ses accidents, la trace des mains qui l'ont posée.

*Variantes acceptables :*
- L'eau immobile d'une vasque, sombre, avant le lever du jour.
- L'ombre portée d'une mashrabiya sur un sol nu — géométrie et lumière, personne.

*Interdits explicites :* le patio en entier, une arcade reconnaissable, un plan large qui permettrait d'identifier l'adresse.

## Page 2 — le cercle (`espace-membres.html`)

**Sujet retenu : le coffret fermé.** Le coffret de dépôt des téléphones, en bois, posé sur une surface nue, fermé. Cadrage serré, fond neutre. C'est l'objet le plus éloquent de la maison et il ne dit rien à qui n'a pas lu la page.

*Variantes acceptables :*
- Une pile de vêtements pliés en lin écru non teint — la tenue, sans aucun signe.
- Une paire de babouches de cuir non teint, posées côte à côte, vides.

*Interdits explicites :* un homme portant la tenue, des mains, un intérieur reconnaissable.

## Mise en place

Le bandeau est déjà construit dans les quatre pages, avec une géométrie dessinée (étoile à huit branches) qui tient lieu d'image en attendant. Pour installer une photographie, remplacer dans le bloc `<section>` d'ouverture le `<svg>…</svg>` par :

```html
<img src="assets/hero-maison.jpg" alt="" class="absolute inset-0 w-full h-full object-cover">
<div class="absolute inset-0" style="background:linear-gradient(to bottom,rgba(255,255,255,.15),rgba(255,255,255,.92))"></div>
```

Le dégradé blanc doit être conservé : il fait que l'image ne soit jamais tout à fait donnée.
