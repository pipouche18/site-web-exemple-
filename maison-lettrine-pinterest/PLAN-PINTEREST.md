# Pinterest — plan de lancement Maison Lettrine

Objectif : un compte Pinterest crédible **avant** de lancer les publicités (50 €/semaine), qui attire les futures mariées 3 à 9 mois avant leur mariage, là où votre concurrent principal (cachetdecire.com, 100 % Google) est absent.

---

## 1. Créer et régler le compte (30 min)

1. **Compte professionnel** : pinterest.fr > S'inscrire > « Créer un compte professionnel » (ou convertir un compte personnel). Pays : France, langue : français.
2. **Nom affiché** : `Maison Lettrine · Cachet de cire`
   Le mot-clé dans le nom aide le référencement Pinterest.
3. **Nom d'utilisateur** : `maisonlettrine` (déjà réservé : pinterest.fr/maisonlettrine).
4. **Photo de profil** : le cachet seul (`maison-lettrine-cachet.png`).
5. **Bio** (160 caractères max) :
   > Coffrets cachet de cire à initiales : sceau, cire souple et méthode pas-à-pas pour réussir vos faire-part dès le premier cachet. ✉️
6. **Couverture du profil** : l'épingle `01-promesse.png`.
7. **Revendiquer le site** : Paramètres > Comptes revendiqués > Site web > `maisonlettrine.com`.
   Le plus simple : installer l'app officielle **Pinterest** dans Shopify, qui revendique le site, ajoute la balise et synchronise le catalogue.
8. **Rich Pins** : déjà prêtes dans le thème (balises Open Graph avec prix et disponibilité). Elles s'activent automatiquement une fois le site revendiqué. Sinon, valider une URL produit sur le validateur Rich Pins de Pinterest.

> ⚠️ Tant que la boutique est protégée par mot de passe, les liens des épingles mènent à la page « Ouverture prochaine ». Elle collecte les e-mails, ce qui reste utile. Mais publiez les épingles produit seulement une fois les produits actifs et la boutique ouverte.

---

## 2. Les 6 tableaux à créer

Créez-les **avant** l'import CSV. Les noms doivent être **exactement** ceux-ci, car le CSV y fait référence.

| # | Nom du tableau | Description (à coller) |
|---|---|---|
| 1 | **Faire-part de mariage à la cire** | Idées de faire-part de mariage scellés à la cire : cachets de cire, sceaux personnalisés aux initiales des mariés, enveloppes élégantes et papeterie de mariage chic ou champêtre. |
| 2 | **Cachet de cire : tutoriels et astuces** | Tutos et astuces pour réussir un cachet de cire : comment faire fondre la cire, verser, presser le sceau, éviter les bulles et les ratés, envoyer ses enveloppes par La Poste. Pour débutantes. |
| 3 | **Couleurs de cire et inspiration mariage** | Quelle couleur de cire à cacheter pour votre mariage ? Bordeaux, terracotta, sauge, or, blanc ivoire, bleu nuit : palettes et associations pour un mariage bohème, champêtre, chic ou d'hiver. |
| 4 | **Idées cadeau personnalisé** | Idées de cadeaux personnalisés et originaux : sceau de cire à l'initiale, coffret correspondance, cadeau pour une amie qui aime écrire, cadeau de Noël, d'anniversaire ou de fête des mères. |
| 5 | **Organisation du mariage** | Rétroplanning, checklists et conseils pour organiser son mariage sereinement : faire-part, papeterie, DIY, calendrier des préparatifs mois par mois. |
| 6 | **Papeterie et correspondance élégante** | Lettres manuscrites, enveloppes scellées, papier de qualité, calligraphie : l'art de la belle correspondance et des cartes qu'on garde. |

Plus tard, quand les produits seront actifs : un 7ᵉ tableau **« Coffrets Maison Lettrine »**, rempli automatiquement par le catalogue de l'app Pinterest.

**Important pour démarrer :** un tableau ne doit pas contenir que vos épingles. Ajoutez dans chaque tableau 10 à 15 épingles d'**autres créateurs** de qualité (faire-part, papeterie, mariage), en cherchant ces mots-clés. Pinterest comprend ainsi le sujet de vos tableaux et votre compte paraît vivant.

---

## 3. Les 10 premières épingles (prêtes)

Images au format Pinterest 1000 × 1500 px, dans [`epingles/`](epingles/). Titres, descriptions, liens avec suivi UTM et mots-clés sont dans [`import-pinterest.csv`](import-pinterest.csv).

| Épingle | Tableau | Lien |
|---|---|---|
| 01 Promesse « Réussis dès le premier cachet » | Faire-part de mariage à la cire | Collection coffrets |
| 02 Les 7 erreurs qui ratent un cachet | Tutoriels et astuces | Guide |
| 03 Un cachet en 4 gestes | Tutoriels et astuces | Guide |
| 04 Combien de cire pour 100 faire-part | Faire-part de mariage à la cire | Accueil (calculateur) |
| 05 Cachet de cire et La Poste | Tutoriels et astuces | Guide |
| 06 Quelle couleur de cire pour votre mariage | Couleurs de cire | Coffret Mariage |
| 07 L'astuce du glaçon | Tutoriels et astuces | Guide |
| 08 Rétroplanning faire-part | Organisation du mariage | Livraison et retours |
| 09 Idée cadeau à son initiale | Idées cadeau personnalisé | Coffret Initiale |
| 10 Cuillère ou pistolet | Tutoriels et astuces | FAQ |

**Import en masse :** Pinterest > Créer > **Créer des épingles en masse** > importer `import-pinterest.csv`.
- La colonne « Publish date » est vide : soit les épingles partent tout de suite, soit vous les programmez une par une dans l'outil (voir le calendrier ci-dessous).
- Vous pouvez aussi les créer à la main : glissez l'image, puis copiez le titre, la description et le lien depuis le CSV.

**Texte alternatif** (champ « alt » des épingles) : reprenez le titre.

### Règles d'honnêteté respectées dans ces visuels
- Aucune photo produit inventée, aucun « fait main » ni « fabriqué en France ».
- Aucun faux avis, aucune fausse promo.
- La Poste : « réduit fortement le risque », jamais « garanti ».
- Le délai : « comptez au moins 4 semaines avant l'envoi de vos faire-part ».

---

## 4. Calendrier des 4 premières semaines

Pinterest récompense la **régularité** plutôt que le volume : 1 épingle par jour vaut mieux que 10 d'un coup.

| Semaine | Lundi | Mercredi | Vendredi | Dimanche |
|---|---|---|---|---|
| 1 | 01 Promesse | 02 7 erreurs | 06 Couleurs | 03 4 gestes |
| 2 | 04 Calcul cire | 07 Glaçon | 09 Cadeau (Noël) | 05 La Poste |
| 3 | 08 Rétroplanning | 10 Cuillère/pistolet | Re-épingler 01 dans « Papeterie » | Re-épingler 06 dans « Faire-part » |
| 4 | Nouvelles épingles avec **vos photos** (voir §5) | | | |

Chaque jour, en plus : **5 à 10 minutes** à ré-épingler des contenus d'autres créateurs dans vos tableaux.

**Saisonnalité :**
- **Novembre et décembre** : poussez l'épingle 09 (cadeau) et créez-en 2 ou 3 autres sur Noël.
- **De janvier à mars** : pic des recherches mariage sur Pinterest, poussez les épingles faire-part.

---

## 5. Ce qu'il faudra ajouter avec vos photos (dès réception de l'échantillon)

Ce sont les épingles qui convertiront le mieux. Prévoyez les **photos verticales** suivantes :
1. Le coffret ouvert, vu du dessus, avec tout son contenu.
2. Gros plan sur un cachet réussi sur une enveloppe de faire-part.
3. Une pile de faire-part scellés, dans les 6 couleurs.
4. Les mains en train de presser le sceau.
5. **Vidéo de 10 à 15 s** : de la cuillère au cachet soulevé (les vidéos ont la meilleure portée sur Pinterest).
6. Le Coffret Mariage avec un sceau gravé « C & T ».

Je pourrai alors générer une seconde série d'épingles avec ces photos, aux mêmes couleurs.

---

## 6. Publicités Pinterest (après ouverture de la boutique)

À lancer quand : produits actifs, boutique ouverte, balise Pinterest installée via l'app, au moins 15 épingles publiées.

- **Budget** : 50 €/semaine, soit environ 7 €/jour.
- **Campagne 1 – Considération (trafic)**, 70 % du budget : promouvoir les 2 ou 3 épingles qui ont le mieux marché en organique (souvent les tutos : 02, 03, 06).
  - Ciblage : femmes de 25 à 44 ans, France.
  - Centres d'intérêt : mariage, préparatifs du mariage, papeterie, DIY.
  - Mots-clés : « faire-part mariage », « cachet de cire », « sceau de cire », « papeterie mariage », « faire-part original ».
- **Campagne 2 – Conversions (catalogue)**, 30 % du budget, une fois que la balise a enregistré quelques ajouts au panier.
- **Mesure** : regardez le coût par clic et le taux d'ajout au panier après 2 semaines, pas avant. Arrêtez les épingles en dessous de 0,5 % de clics.

---

## 7. Mots-clés à réutiliser

**Mariage :** faire-part mariage · faire-part original · faire-part chic · faire-part champêtre · papeterie mariage · enveloppe mariage · DIY mariage · organisation mariage · rétroplanning mariage

**Cachet de cire :** cachet de cire · sceau de cire · cachet de cire personnalisé · sceau initiales · cire à cacheter · tuto cachet de cire · cachet de cire débutant · comment faire un cachet de cire

**Cadeau :** idée cadeau personnalisé · cadeau initiale · cadeau original femme · cadeau Noël · coffret cadeau

**Couleurs :** mariage bordeaux · mariage terracotta · mariage sauge · mariage or et blanc · mariage bleu nuit

---

## Fichiers

- `epingles/` : les 10 épingles PNG (1000 × 1500).
- `import-pinterest.csv` : import en masse (titres, descriptions, liens UTM, mots-clés).
- `outils/` : scripts pour régénérer les épingles (`pins.py` + `render.js`) et le CSV (`csv_import.py`).
