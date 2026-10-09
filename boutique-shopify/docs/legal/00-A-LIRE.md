# Pages légales : mode d'emploi

⚠️ **Ce sont des modèles, pas des conseils juridiques.** Ils couvrent les points habituels pour une micro-entreprise qui vend en ligne en France, mais ils doivent être **relus et adaptés** à votre situation (idéalement par un juriste, ou au minimum comparés aux fiches officielles de service-public.fr, economie.gouv.fr et cnil.fr).

## Ce que vous devez compléter

Tout ce qui est entre crochets et en majuscules : **[À COMPLÉTER : …]**. Pour vérifier qu'il ne reste rien, lancez `node outils/verifier-textes.mjs` (voir le README).

## Où coller chaque texte dans Shopify

| Fichier | Où le coller |
|---|---|
| `mentions-legales.md` | Paramètres > Politiques > **Mentions légales** |
| `cgv.md` | Paramètres > Politiques > **Conditions d'utilisation / Conditions générales de vente** |
| `politique-confidentialite.md` | Paramètres > Politiques > **Politique de confidentialité** |
| `politique-cookies.md` | Boutique en ligne > Pages > nouvelle page « Politique cookies » (modèle par défaut) |
| (déjà dans le thème) | Les politiques **Expédition** et **Remboursement** : copiez le texte de la page « Livraison et retours » |

Shopify affiche automatiquement ces politiques dans le pied de page et au moment du paiement.

## Informations à réunir avant de commencer

- Nom, prénom, adresse de domiciliation de la micro-entreprise
- Numéro SIREN / SIRET
- Régime de TVA (franchise en base : « TVA non applicable, art. 293 B du CGI »)
- Adresse e-mail de contact (et téléphone si vous en avez un professionnel)
- **Médiateur de la consommation** : l'adhésion est **obligatoire** pour vendre à des particuliers (liste des médiateurs agréés sur economie.gouv.fr / CECMC). Comptez quelques dizaines d'euros par an.
- Adresse de retour des colis
- Frais de livraison et de retour
