# Maison Nuits Douces : thème Shopify

Thème Shopify « Online Store 2.0 » pour **Maison Nuits Douces**, une boutique de linge de lit en coton lavé et double gaze de coton. Il est construit sur **Dawn 16** (le thème gratuit officiel de Shopify). Tout se modifie depuis l'éditeur de thème, sans toucher au code.

## Contenu du dossier

```
boutique-shopify/
├── theme/        ← le thème (c'est CE dossier qu'on envoie sur Shopify)
├── produits/     ← les 5 produits d'exemple (fichier CSV à importer + textes à relire)
├── docs/         ← modèles de pages légales + checklist avant mise en ligne
└── outils/       ← un petit vérificateur de textes (mot « lin » interdit, textes à compléter)
```

---

## Étape 1 : installer les outils (une seule fois)

1. **Node.js** : téléchargez la version « LTS » sur https://nodejs.org et installez-la (suivant, suivant, terminer).
2. **Ouvrez un terminal** :
   - Mac : application **Terminal** (Cmd + Espace, tapez « Terminal »)
   - Windows : **PowerShell** (menu Démarrer, tapez « PowerShell »)
3. **Installez Shopify CLI** en copiant cette commande puis Entrée :
   ```
   npm install -g @shopify/cli@latest
   ```
   Sur Mac, si vous voyez une erreur « permission denied », relancez avec `sudo npm install -g @shopify/cli@latest` (votre mot de passe Mac vous sera demandé, il ne s'affiche pas quand vous tapez : c'est normal).
4. Vérifiez : `shopify version` doit afficher un numéro (par exemple 3.x).

## Étape 2 : récupérer le code

Sur la page GitHub du dépôt, choisissez la branche `claude/festive-galileo-idb0j2`, puis **Code > Download ZIP**. Décompressez le fichier (par exemple dans « Documents »).

Dans le terminal, placez-vous dans le dossier du thème (adaptez le chemin) :
```
cd Documents/site-web-exemple--claude-festive-galileo-idb0j2/boutique-shopify/theme
```
Astuce : tapez `cd ` (avec l'espace), puis faites glisser le dossier `theme` dans la fenêtre du terminal, et appuyez sur Entrée.

## Étape 3 : vérifier, prévisualiser, envoyer

Remplacez `votre-boutique.myshopify.com` par l'adresse de votre boutique (visible dans l'admin Shopify, Paramètres > Domaines).

| Je veux… | Commande |
|---|---|
| Vérifier le code (erreurs) | `shopify theme check` |
| Voir le thème en direct sur mon ordinateur | `shopify theme dev --store votre-boutique.myshopify.com` |
| Envoyer le thème sur ma boutique, **sans le publier** | `shopify theme push --unpublished --store votre-boutique.myshopify.com` |
| Récupérer les changements faits dans l'éditeur | `shopify theme pull --store votre-boutique.myshopify.com` |

- La première fois, Shopify ouvre votre navigateur pour vous connecter : acceptez.
- `theme dev` affiche une adresse du type `http://127.0.0.1:9292` : ouvrez-la pour voir le site. Faites **Ctrl + C** dans le terminal pour arrêter.
- `theme push --unpublished` crée un **nouveau thème non publié**, nommé comme vous le souhaitez. Ensuite, dans l'admin : **Boutique en ligne > Thèmes > … > Aperçu**, puis **Publier** quand tout est prêt.
- ⚠️ **Important** : les réglages faits dans l'éditeur Shopify (textes, couleurs, images) sont enregistrés sur Shopify, pas sur votre ordinateur. **Avant de refaire un `push`, faites toujours un `pull`**, sinon vous écraserez vos modifications.

**Sans terminal (méthode alternative)** : compressez le **contenu** du dossier `theme` en ZIP (les dossiers `assets`, `config`, `layout`… doivent être à la racine du ZIP), puis dans l'admin : **Boutique en ligne > Thèmes > Ajouter un thème > Importer un fichier ZIP**.

---

## Étape 4 : configurer la boutique (dans l'admin Shopify)

À faire **dans cet ordre**, car les produits ont besoin des metafields, et les collections ont besoin des produits.

### 4.1 Langue et marché
- **Paramètres > Langues** : français comme langue par défaut.
- **Paramètres > Marchés** : France, en euros.

### 4.2 Créer les metafields (environ 5 minutes)
**Paramètres > Données personnalisées > Produits > Ajouter une définition**. Pour chaque ligne, saisissez le nom. Shopify propose alors « custom.xxx » : **vérifiez que l'espace de noms et la clé sont exactement ceux du tableau**.

| Nom | Espace de noms et clé | Type | Remarque |
|---|---|---|---|
| Composition | `custom.composition` | Texte sur une seule ligne | Affichée en haut de chaque fiche. **Obligatoire** |
| Grammage | `custom.grammage` | Texte sur une seule ligne | ex. « 180 g/m² » |
| Dimensions | `custom.dimensions` | Texte sur plusieurs lignes | Une pièce par ligne : `Housse de couette : 220×240 cm` |
| Contenu du colis | `custom.contenu_colis` | Texte sur plusieurs lignes | Un élément par ligne |
| Entretien | `custom.entretien` | Texte sur plusieurs lignes | Un conseil par ligne |
| Style | `custom.style` | Texte sur une seule ligne | Cochez « Limiter à des valeurs prédéfinies » : Japonais, Nordique, Romantique. Activez **le filtrage** |
| Délai min. | `custom.delai_min` | Nombre entier | Facultatif : remplace les 10 jours par défaut |
| Délai max. | `custom.delai_max` | Nombre entier | Facultatif : remplace les 18 jours par défaut |

### 4.3 Importer les 5 produits
**Produits > Importer** et choisissez `produits/produits-shopify.csv`.
- Les produits arrivent en **brouillon** : rien n'est visible des clients tant que vous ne les passez pas en « Actif ».
- Relisez-les et complétez chaque **[à confirmer]** (composition exacte, grammage, dimensions) avec les infos du fournisseur.
- Ajoutez les photos (voir `produits/fiches-produits.md` pour la liste des photos et des textes alternatifs proposés).
- Le stock n'est pas suivi (dropshipping). Aucun message de stock n'apparaît donc, et c'est voulu.

**Ajouter un produit à la main plus tard** : Produits > Ajouter un produit → titre, description, prix, options « Couleur » et « Taille » (écrivez la taille comme `220×240 cm`). Puis, **en bas de la page produit, section « Metafields »**, remplissez Composition, Grammage, Dimensions, Contenu du colis, Entretien et Style. Type de produit : `Parure de lit`.

### 4.4 Collections
**Produits > Collections > Créer une collection**, de type **automatisée** :

| Titre | Condition |
|---|---|
| Parures | Type de produit est égal à `Parure de lit` |
| Couvre-lits | Type de produit est égal à `Couvre-lit` |
| Style japonais | Balise du produit est égale à `Style japonais` |
| Style nordique | Balise du produit est égale à `Style nordique` |
| Style romantique | Balise du produit est égale à `Style romantique` |

Ajoutez une belle image d'ambiance à chaque collection de style : elle apparaît dans la section « Trouver mon style » de l'accueil.

### 4.5 Filtres (taille, couleur, style)
Installez l'appli gratuite **Search & Discovery** (de Shopify), puis **Filtres > Ajouter un filtre** : Disponibilité, Prix, **Couleur** (option), **Taille** (option), **Style** (metafield produit). Les filtres apparaissent automatiquement sur les pages de collection.

### 4.6 Pages
**Boutique en ligne > Pages > Ajouter une page**. Mettez seulement le titre, laissez le contenu vide, et choisissez le **modèle** à droite :

| Titre de la page | Modèle |
|---|---|
| Guide des tailles | `guide-des-tailles` |
| Conseils d'entretien | `entretien` |
| À propos | `a-propos` |
| FAQ | `faq` |
| Livraison et retours | `livraison-retours` |
| Contact | `contact` |
| Politique cookies | par défaut : collez le texte de `docs/legal/politique-cookies.md` |

Le contenu de ces pages est **déjà rédigé dans le thème**. Pour le modifier, ouvrez la page dans l'éditeur de thème (voir étape 5).

### 4.7 Menus
**Boutique en ligne > Navigation** :
- **Menu principal** (`main-menu`) : Parures · Couvre-lits · Par style (sous-menu : Japonais, Nordique, Romantique) · Guide des tailles · À propos
- **Pied de page** (`footer`) : Toutes les parures · Couvre-lits · Nos styles
- Créez un menu **« Aide »** dont l'identifiant est `aide` : Livraison et retours · FAQ · Guide des tailles · Conseils d'entretien · Contact · Politique cookies

### 4.8 Politiques légales
Suivez `docs/legal/00-A-LIRE.md`.

### 4.9 Bannière cookies (CNIL)
**Paramètres > Confidentialité client > Bannière de cookies** :
- Activez la bannière (au minimum pour l'Union européenne, idéalement partout).
- Vérifiez que **« Refuser » et « Accepter » sont deux boutons de même taille et au même niveau** : c'est l'exigence de la CNIL.
- Textes en français, avec un lien vers votre page « Politique cookies ».

Le thème ajoute un lien **« Gérer mes cookies »** dans le pied de page, qui rouvre cette bannière. Le thème lui-même ne charge **aucun traceur publicitaire**.

### 4.10 Pinterest
- Installez l'appli officielle **Pinterest** (App Store Shopify) et connectez votre compte Pinterest Business.
- Elle installe le **tag Pinterest et le suivi des conversions**, qui ne se déclenchent qu'après acceptation des cookies. **Ne collez aucun code Pinterest dans le thème.**
- Elle synchronise aussi votre catalogue. Les **Rich Pins** (titre, prix, disponibilité) fonctionnent grâce aux balises déjà présentes sur les fiches produit.
- Le bouton « Enregistrer » sur les photos produit est un simple lien, sans script : il ne ralentit pas le site et ne trace personne.

### 4.11 Avis clients (plus tard)
La section « Avis clients » affiche un message honnête tant qu'il n'y a pas d'avis. Quand vous installez **Judge.me** (ou une autre appli d'avis) : éditeur de thème > section « Avis clients » > **Ajouter un bloc** > widget de l'appli. **Jamais de faux avis.**

---

## Étape 5 : modifier textes, couleurs et images (éditeur de thème)

**Boutique en ligne > Thèmes > Personnaliser.**

- **Changer de page** : menu déroulant en haut au centre (Page d'accueil, Produits, Collections, Pages > FAQ…).
- **Modifier un texte ou une image** : cliquez sur la section dans la colonne de gauche, modifiez, puis **Enregistrer** (en haut à droite).
- **Ajouter, déplacer ou masquer une section** : « Ajouter une section », glisser-déposer avec les 6 points, ou l'icône œil.
- **Couleurs** : icône engrenage **Paramètres du thème > Couleurs**. Il y a 5 « schémas » :
  - Schéma 1 : écru, couleur principale du site
  - Schéma 2 : sable (bandeaux, réassurance, pied de page)
  - Schéma 3 : blanc
  - Schéma 4 : sauge
  - Schéma 5 : argile, avec texte blanc

  Changer une couleur dans un schéma la change partout où ce schéma est utilisé.
- **Polices** : Paramètres du thème > Typographie (titres : Cormorant, texte : Jost). Si l'une n'est pas disponible, cliquez sur « Modifier » et choisissez-en une proche, par exemple **Lora** pour les titres ou **DM Sans** pour le texte.
- **Délai de livraison, correspondance housse ↔ lit, bouton Pinterest** : Paramètres du thème > **Maison Nuits Douces**. Choisissez aussi la **page du guide des tailles** dans cet onglet.
- **Fiche produit** : modèle « Produits par défaut ».
  - Dans le bloc **Onglets produit**, choisissez les pages « Conseils d'entretien » et « Livraison et retours ».
  - Le bloc **Produits complémentaires** se remplit dans l'appli Search & Discovery (onglet Recommandations) : associez drap housse et plaid à chaque parure.
- **Suggestion dans le panier** : Paramètres du thème > **Panier** > Produit suggéré.
- **Barre en haut du site** : section « Barre d'annonces » (en haut de chaque page dans l'éditeur).

### Règles à respecter (droit français)
- **Prix barré** : remplissez « Prix avant réduction » seulement avec un prix **réellement pratiqué** (le plus bas des 30 derniers jours avant la promotion). Sinon, laissez vide.
- Pas de faux compte à rebours, pas de faux stock limité, pas de faux avis : le thème n'en contient pas, n'en ajoutez pas.
- **Composition** : n'écrivez jamais « lin » ou « linen ». Vos produits sont en coton.

---

## Le vérificateur de textes

Depuis le dossier `boutique-shopify` (et non `theme`) :
```
node outils/verifier-textes.mjs
```
Il signale toute mention interdite de « lin » ou « linen », et liste les fichiers où il reste des **[à confirmer]** ou **[À COMPLÉTER]**. Il ne vérifie que les fichiers de ce dossier : pensez aussi à relire vos produits dans l'admin.

---

## Ce que vous devez compléter vous-même

| Quoi | Où |
|---|---|
| Logo (ou laisser le nom en texte) et favicon | Éditeur > En-tête / Paramètres du thème > Logo |
| **Photos** : accueil (grande image d'ambiance), collections, produits | Éditeur + fiches produits (liste dans `produits/fiches-produits.md`) |
| Infos fournisseur marquées **[à confirmer]** : composition, grammage, dimensions, contenu du colis, couleurs, tailles, poids, fermeture | Fiches produits (metafields) |
| Prix définitifs par taille | Fiches produits |
| **Adresse e-mail** de contact ([VOTRE-EMAIL]) | Pages Contact, Livraison et retours + Paramètres > Coordonnées de la boutique |
| Frais de livraison, zone, seuil de livraison offerte | Paramètres > Expédition + FAQ + page Livraison |
| Adresse de retour et qui paie le retour | Page Livraison et retours, FAQ, CGV |
| Moyens de paiement | Paramètres > Paiements + FAQ + réassurance de l'accueil |
| Histoire personnelle de la marque | Page À propos (éditeur) |
| **Mentions légales, CGV, confidentialité, cookies** (identité, SIRET, médiateur…) | `docs/legal/` → Paramètres > Politiques |
| Bannière cookies | Paramètres > Confidentialité client |
| Réseaux sociaux (Pinterest, Instagram) | Paramètres du thème > Réseaux sociaux |
| Produits complémentaires (drap housse, plaid) | Créer les produits + Search & Discovery + suggestion du panier |

Ensuite, suivez la **checklist** : `docs/checklist-mise-en-ligne.md`.

---

## Ce qui a été ajouté à Dawn (pour information)

- `sections/` : `nd-reviews` (avis), `nd-reassurance`, `nd-article` (pages de texte), `nd-faq` (FAQ + données structurées), `nd-size-guide` (tableau des tailles)
- `snippets/` : `nd-composition`, `nd-bed-size`, `nd-delivery-estimate`, `nd-product-tabs`, `nd-pinterest-save`, `nd-cart-upsell`, `nd-lines`
- `assets/` : `nd-theme.css`, `nd-product.js` (dates de livraison, taille de lit, onglets), `nd-cart-upsell.js`
- Modifiés : `main-product` (nouveaux blocs), `meta-tags` (Open Graph / Rich Pins), `cart-drawer` (suggestion), `footer` (lien cookies), `theme.liquid`
- Langue : français par défaut (`locales/fr.default.json`)

Licence : Dawn est fourni par Shopify sous une licence qui autorise son utilisation pour des thèmes Shopify (voir `theme/LICENSE.md`).
