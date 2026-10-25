# E-mail de bienvenue : « Le mini-guide des 7 erreurs »

Déclencheur : une personne s'inscrit avec le formulaire du site, en bas de l'accueil.
Le formulaire lui ajoute automatiquement les tags `newsletter` et `guide-7-erreurs`.

**Lien du guide PDF** (déjà dans Shopify > Contenu > Fichiers) :
`https://cdn.shopify.com/s/files/1/1024/3997/7344/files/mini-guide-7-erreurs-maison-lettrine.pdf?v=1792971737`

---

## Mise en place dans Shopify (10 minutes)

1. Installez l'app **Shopify Email** si ce n'est pas fait (gratuite jusqu'à 10 000 e-mails par mois).
2. Allez dans **Marketing > Automatisations > Créer une automatisation**, puis choisissez le modèle **« Accueillir les nouveaux abonnés »** (« Welcome new subscribers »).
3. Ajoutez une **condition** juste après le déclencheur : *Le client a le tag* `guide-7-erreurs`.
   Sans cette condition, les inscrites de la page « Ouverture prochaine » (tag `ouverture`) recevraient aussi ce guide.
4. Cliquez sur l'étape **E-mail**, puis remplacez le contenu par celui ci-dessous.
5. **Expéditeur** : nom `Maison Lettrine`, adresse de réponse : votre e-mail de contact.
6. Envoyez-vous un **e-mail test**, vérifiez que le bouton ouvre bien le PDF, puis **activez** l'automatisation.

> Shopify ajoute automatiquement en bas de l'e-mail le lien de désinscription et l'adresse de la boutique, deux mentions obligatoires. L'adresse affichée est celle de Paramètres > Infos sur la boutique : vérifiez-la.

---

## E-mail 1 — envoyé tout de suite

**Objet (à choisir) :**
- ✅ `Votre mini-guide : les 7 erreurs à éviter`
- `Vos premiers cachets de cire, sans les ratés`
- `C'est ici : votre guide du cachet de cire`

**Texte d'aperçu** (la ligne grise sous l'objet) :
`Cire qui colle, bulles, cachet qui casse à La Poste : tout se corrige.`

**Contenu, bloc par bloc dans l'éditeur Shopify Email :**

**[Image]** Logo Maison Lettrine (`maison-lettrine-logo.png`), centré, environ 220 px de large.

**[Titre]**
> Votre mini-guide est prêt

**[Texte]**
> Bonjour,
>
> Merci de votre inscription. Voici, comme promis, le mini-guide des 7 erreurs qui font rater un cachet de cire, et la solution à chacune.
>
> Il se lit en 5 minutes. Le mieux : le parcourir **avant** votre premier essai.

**[Bouton]** `Télécharger le guide (PDF)` → lien du guide ci-dessus.

**[Texte]**
> **Le conseil le plus utile, si vous ne deviez en retenir qu'un :**
> la cire qui colle au sceau vient presque toujours d'un sceau trop chaud. Posez-le quelques secondes sur un glaçon avant de presser, essuyez-le, et il se décollera net.
>
> Une question sur vos faire-part, une couleur de cire, une quantité ? **Répondez simplement à cet e-mail** : une vraie personne vous lit et vous répond sous 48 h.
>
> À très vite,
> Ejilane, Maison Lettrine

**[Bouton secondaire, optionnel]** `Voir le guide complet en ligne` → `https://maisonlettrine.com/pages/guide-cachet-de-cire`

> Remplacez « Ejilane » par la signature de votre choix : un prénom rend l'e-mail plus chaleureux.

---

## E-mail 2 — 3 jours après (optionnel, recommandé)

Dans la même automatisation : **+ Ajouter une étape > Attendre 3 jours**, puis **E-mail**.

**Objet :** `Combien de cire pour vos faire-part ?`
**Aperçu :** `Le calcul en 10 secondes, pour ne pas en manquer à mi-chemin.`

> Bonjour,
>
> C'est l'erreur n°7 du guide, et la plus frustrante : tomber à court de cire au milieu des enveloppes.
>
> La règle est simple : **3 perles par cachet, plus 10 % pour vos essais.**
> - 50 faire-part : environ 165 perles
> - 100 faire-part : environ 330 perles
> - 150 faire-part : environ 500 perles
>
> Une boîte contient environ 150 perles. Pour votre nombre exact d'invités, notre calculateur fait le compte pour vous, et vous indique le coffret adapté.

**[Bouton]** `Calculer ma quantité de cire` → `https://maisonlettrine.com/?utm_source=email&utm_medium=automation&utm_campaign=bienvenue-2`

> Un dernier conseil, pour un mariage : comptez **au moins 4 semaines** entre la commande de votre coffret et l'envoi de vos faire-part, le temps de recevoir le colis et de vous entraîner sans stress.
>
> Ejilane, Maison Lettrine

---

## E-mail 3 — 7 jours après (optionnel)

**Attendre 4 jours** de plus, puis **E-mail**. Ajoutez la condition *« Le client n'a passé aucune commande »*, pour ne pas l'envoyer à celles qui ont déjà acheté.

**Objet :** `Tout ce qu'il faut, dans un seul coffret`
**Aperçu :** `Le sceau, la cire souple, le petit four et la méthode.`

> Bonjour,
>
> Si vous avez lu le guide, vous savez qu'un cachet réussi tient à peu de choses : un sceau froid, une cire chauffée à distance, la bonne quantité.
>
> C'est pour ça qu'on a conçu nos coffrets : tout est dedans, rien à commander en plus, rien à calculer.
>
> **Coffret Initiale** — le sceau à votre initiale, la cire en 10 couleurs, le petit four, la cuillère et la carte guide. Pour vos lettres, ou pour offrir.
>
> **Coffret Mariage** — vos deux initiales gravées sur mesure, avec un aperçu de la gravure envoyé par e-mail avant fabrication, et la cire dans la couleur de votre mariage.
>
> La livraison est offerte dès 50 €.

**[Bouton]** `Découvrir les coffrets` → `https://maisonlettrine.com/collections/coffrets-cachet-de-cire?utm_source=email&utm_medium=automation&utm_campaign=bienvenue-3`

> Et si vous hésitez, répondez à cet e-mail : je vous aide à choisir.
>
> Ejilane, Maison Lettrine

---

### Vérifications avant d'activer
- [ ] Les e-mails 2 et 3 mentionnent des produits. Activez-les **seulement quand les produits sont en ligne** ; l'e-mail 1 (le guide) peut partir dès maintenant.
- [ ] Le mot « cire souple » (e-mail 3) suppose que votre agent l'a confirmée. Sinon, retirez-le.
- [ ] Le délai « 4 semaines » est à ajuster selon le délai réel de votre agent.
- [ ] Aucun faux compte à rebours, aucune fausse promo : ces e-mails n'en contiennent pas, gardez-les ainsi.
