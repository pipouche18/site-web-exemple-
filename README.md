# Site d'exemple — Maison Dorée (boulangerie fictive)

Site vitrine de démonstration à mettre en lien dans les mails de prospection.
100 % statique (HTML/CSS/JS), aucune installation nécessaire.

## Mise en ligne gratuite avec GitHub Pages

1. Sur GitHub : **Settings → Pages**
2. *Source* : « Deploy from a branch », choisir la branche puis le dossier `/ (root)`, **Save**
3. Après 1 à 2 minutes, le site est en ligne à l'adresse
   `https://pipouche18.github.io/site-web-exemple-/`

## À personnaliser

- **Votre e-mail** dans le bandeau « Site de démonstration » en haut de `index.html`
  (remplacer `VOTRE-EMAIL@exemple.fr`).
- Nom, textes, prix, adresse, téléphone : directement dans `index.html`.
- Horaires : dans le tableau de `index.html` **et** dans l'objet `HOURS` en haut de `script.js`
  (utilisé pour l'indicateur « Ouvert maintenant »).
- Couleurs : variables en haut de `style.css` (`--gold`, `--cream`…).
- Photos : liens Unsplash, à remplacer par les vraies photos du commerce.

## Fonctionnalités

- Design responsive (mobile, tablette, ordinateur) avec menu mobile
- Indicateur « Ouvert / Fermé » en temps réel et jour actuel surligné
- Filtres de produits, avis clients, carte Google Maps, bouton d'appel direct
- Formulaire de contact (démo : n'envoie rien ; brancher Formspree ou similaire pour un vrai client)

---

# Site d'exemple — Rushcars (achat / revente de voitures)

Dossier `rushcars/` : site vitrine sobre, noir et épuré. En ligne à
`https://pipouche18.github.io/site-web-exemple-/rushcars/` une fois GitHub Pages activé.

- **Véhicules** : une carte `<article class="car">` par voiture dans `rushcars/index.html`
  (`data-cat` = citadine / berline / suv / sport, `data-price` et `data-km` servent au tri).
- **Couleurs** : variables en haut de `rushcars/style.css`.
- **Photos** : liens Unsplash à remplacer ; une silhouette de voiture s'affiche si une image ne charge pas.
- Formulaires « Estimation gratuite » et « Contact » en mode démo (brancher Formspree ou similaire).

---

# Logo — Maison Lettrine (cachets de cire)

Dossier `maison-lettrine/logo/` : un cachet de cire bordeaux en relief, avec la lettrine « L » au centre
et « Maison Lettrine » en couronne, accompagné du nom et du slogan « Cachets de cire ».
Les textes sont vectorisés : aucune police à installer.

| Fichier | Usage |
|---|---|
| `logo-principal` (.svg / .png) | Version principale, fond crème |
| `logo-principal-transparent` | Même chose sans fond (étiquettes, emballages) |
| `logo-horizontal` | En-tête de site, signature mail, bannières |
| `embleme` | Cachet seul : favicon, photo de profil réseaux sociaux |
| `logo-fond-sombre` | Sur fond foncé |
| `logo-monochrome` | Une seule couleur : tampon, gravure, impression N&B |

Couleurs : cire `#8E1F2B` (ombre `#5E1119`, reflet `#B8424D`), encre `#2B211D`, crème `#F5ECDD`, or `#B8893E`.
Pour modifier le slogan ou les couleurs : `pip install fonttools cairosvg`, éditer puis lancer
`python3 maison-lettrine/logo/generer_logo.py maison-lettrine/logo`.
