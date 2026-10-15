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

## Thème Shopify « Maison Nuits Douces »

Le dossier [`boutique-shopify/`](boutique-shopify/README.md) contient un thème Shopify complet (basé sur Dawn) pour une boutique de linge de lit en coton. Ce n'est pas un site statique : voir son propre README pour l'installer.
