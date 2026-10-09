# Checklist avant mise en ligne : Maison Nuits Douces

Cochez chaque ligne (`[ ]` → `[x]`). Ne publiez pas la boutique tant qu'une ligne **⚠️** n'est pas cochée.

## 1. Légal et honnêteté ⚠️
- [ ] ⚠️ Mentions légales complètes : nom, adresse, SIRET, mention « EI », TVA, hébergeur, e-mail
- [ ] ⚠️ CGV complètes : délai 10 à 18 jours ouvrés, rétractation 14 jours, formulaire de rétractation, garanties légales (encadré officiel), frais de retour
- [ ] ⚠️ Médiateur de la consommation choisi, et ses coordonnées présentes dans les mentions légales et les CGV
- [ ] ⚠️ Politique de confidentialité (transfert des adresses vers le fournisseur en Chine mentionné) et politique cookies publiées
- [ ] ⚠️ Bannière cookies Shopify active, avec « Refuser » aussi visible qu'« Accepter »
- [ ] ⚠️ Test en navigation privée : avant tout clic sur la bannière, aucun tag Pinterest ne se déclenche (extension « Pinterest Tag Helper » ou outils du navigateur > Réseau, filtre « pinterest »)
- [ ] ⚠️ Aucun prix barré, sauf ancien prix réellement pratiqué (le plus bas des 30 derniers jours)
- [ ] ⚠️ Aucun faux avis, faux compte à rebours ni faux stock (aucune appli de ce type installée)
- [ ] Le site ne dit nulle part « fabriqué en France »

## 2. Produits ⚠️
- [ ] ⚠️ `node outils/verifier-textes.mjs` : aucune mention de « lin » ou « linen » <!-- verifier-textes-ignore -->
- [ ] ⚠️ Plus aucun **[à confirmer]** ni **[À COMPLÉTER]** : recherchez-les aussi dans l'admin (Produits, Pages, éditeur)
- [ ] ⚠️ Chaque produit a son metafield **Composition** rempli, avec une composition confirmée par écrit par le fournisseur
- [ ] Grammage, dimensions de chaque pièce, contenu du colis et entretien remplis
- [ ] Couleurs, tailles et prix définitifs vérifiés ; tailles écrites comme dans la correspondance housse ↔ lit (`220×240 cm`)
- [ ] « Convient à : lit … » s'affiche correctement pour chaque taille
- [ ] Photos ajoutées (au moins 4 par produit, format vertical), avec un texte alternatif sur chacune, sans le mot « lin » <!-- verifier-textes-ignore -->
- [ ] Titres et méta-descriptions SEO relus (section « Référencement » en bas de chaque produit)
- [ ] Produits passés de « Brouillon » à « Actif » et disponibles sur le canal « Boutique en ligne »
- [ ] Poids des produits renseigné (utile au calcul des frais de livraison)

## 3. Pages, menus et collections
- [ ] Pages créées avec le bon modèle : Guide des tailles, Conseils d'entretien, À propos, FAQ, Livraison et retours, Contact, Politique cookies
- [ ] La barre d'annonce mène bien à la page Livraison et retours
- [ ] Menus principal, pied de page et « aide » configurés, sans lien cassé
- [ ] Collections Parures, Couvre-lits et les 3 styles créées, avec une image chacune
- [ ] Filtres Taille, Couleur et Style actifs (Search & Discovery)
- [ ] Produits complémentaires configurés (Search & Discovery > Recommandations) et produit suggéré dans le panier
- [ ] Page du guide des tailles choisie dans Paramètres du thème > Maison Nuits Douces
- [ ] Pages Entretien et Livraison choisies dans le bloc « Onglets produit »
- [ ] Adresse e-mail réelle partout ([VOTRE-EMAIL] remplacé), formulaire de contact testé (message bien reçu)

## 4. Commande test
- [ ] Commande test complète (Paramètres > Paiements > mode test, ou « passerelle de test »)
- [ ] La date de livraison estimée affichée sur la fiche est cohérente (10 à 18 jours ouvrés)
- [ ] Le panier latéral s'ouvre, la suggestion s'ajoute, les quantités se modifient
- [ ] E-mails de confirmation et d'expédition en français, avec le bon nom de boutique
- [ ] Frais de livraison corrects au paiement
- [ ] Remboursement test effectué

## 5. Mobile, vitesse et accessibilité
- [ ] Parcours complet sur un vrai téléphone : accueil → collection → filtre → produit → panier → paiement
- [ ] Test PageSpeed Insights (https://pagespeed.web.dev) sur l'accueil et une fiche produit, version **mobile**. Si le score est faible, réduisez la taille des photos importées (2500 px de large maximum) et désinstallez les applis inutiles
- [ ] Navigation au clavier (touche Tab) : menu, filtres, choix de taille, onglets (flèches gauche/droite), panier ; le focus reste toujours visible
- [ ] Toutes les images ont un texte alternatif (éditeur et fiches produits)

## 6. Pinterest et SEO
- [ ] Appli Pinterest installée, domaine revendiqué, catalogue synchronisé
- [ ] Une épingle test d'une fiche produit affiche bien le prix et la disponibilité (Rich Pin)
- [ ] Le bouton « Enregistrer » sur la photo produit ouvre Pinterest avec la bonne image
- [ ] Préférences de la boutique (Boutique en ligne > Préférences) : titre et méta-description de la page d'accueil en français, image de partage réseaux sociaux ajoutée
- [ ] Test des données structurées d'une fiche produit et de la FAQ : https://search.google.com/test/rich-results

## 7. Publication
- [ ] `shopify theme pull` fait juste avant tout nouveau `push` (pour ne pas écraser les réglages de l'éditeur)
- [ ] Thème publié (Boutique en ligne > Thèmes > Publier)
- [ ] Mot de passe de la boutique retiré (Boutique en ligne > Préférences > Accès restreint)
- [ ] Domaine personnalisé connecté (facultatif mais conseillé)
