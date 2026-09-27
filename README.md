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
