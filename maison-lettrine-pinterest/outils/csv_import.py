"""Fichier CSV d'import en masse Pinterest (Créer > Créer des épingles en masse).

Usage : python3 csv_import.py <commit_git>
Les images sont servies depuis le dépôt GitHub public (raw.githubusercontent.com).
"""
import csv, sys

COMMIT = sys.argv[1]
RAW = f'https://raw.githubusercontent.com/pipouche18/site-web-exemple-/{COMMIT}/maison-lettrine-pinterest/epingles/'
SITE = 'https://maisonlettrine.com'
UTM = '?utm_source=pinterest&utm_medium=organic&utm_campaign=lancement&utm_content='

B_MARIAGE = 'Faire-part de mariage à la cire'
B_TUTO = 'Cachet de cire : tutoriels et astuces'
B_COULEURS = 'Couleurs de cire et inspiration mariage'
B_CADEAU = 'Idées cadeau personnalisé'
B_ORGA = 'Organisation du mariage'

PINS = [
    ('01-promesse', B_MARIAGE, '/collections/coffrets-cachet-de-cire',
     'Faire-part scellés à la cire : réussis dès le premier cachet',
     'Sceller vos faire-part de mariage à la cire, même sans jamais avoir essayé : un coffret avec le sceau, la cire souple, le petit four et la méthode pas-à-pas. Faire-part élégants, papeterie de mariage, cachet de cire personnalisé.',
     'faire-part mariage, cachet de cire, sceau de cire personnalisé, papeterie mariage'),
    ('02-7-erreurs', B_TUTO, '/pages/guide-cachet-de-cire',
     'Les 7 erreurs qui ratent un cachet de cire (et comment les éviter)',
     'Cire qui colle, bulles, empreinte floue, cachet qui casse à La Poste : les 7 erreurs les plus fréquentes et leur solution. Guide gratuit pour réussir vos cachets de cire dès le premier essai.',
     'cachet de cire astuce, cachet de cire débutant, sceau de cire tuto, erreurs cachet de cire'),
    ('03-4-gestes', B_TUTO, '/pages/guide-cachet-de-cire',
     'Tuto cachet de cire : un cachet réussi en 4 gestes',
     'Chauffer, verser, presser, soulever : le tutoriel simple pour faire un cachet de cire net, avec les bons temps et les bonnes quantités. Idéal pour vos faire-part, cartes et lettres.',
     'tuto cachet de cire, comment faire un cachet de cire, cire à cacheter, DIY mariage'),
    ('04-calcul-cire', B_MARIAGE, '/',
     'Combien de cire pour 100 faire-part de mariage ?',
     'La règle simple : 3 perles de cire par cachet, plus 10 % pour vos essais. Pour 100 faire-part, comptez environ 330 perles, soit 3 boîtes. Calculez votre quantité selon votre nombre d’invités.',
     'faire-part mariage, quantité cire à cacheter, perles de cire, organisation mariage'),
    ('05-la-poste', B_TUTO, '/pages/guide-cachet-de-cire',
     'Cachet de cire et La Poste : 5 points pour limiter la casse',
     'Envoyer des enveloppes avec un cachet de cire : cire souple, rabat collé, enveloppe épaisse, dépôt au guichet et enveloppe test. Aucune méthode n’est garantie à 100 %, mais ces 5 points réduisent fortement le risque.',
     'cachet de cire la poste, envoyer faire-part cachet de cire, cire souple, enveloppe mariage'),
    ('06-nuancier', B_COULEURS, '/products/coffret-mariage-sceau-grave-a-vos-deux-initiales',
     'Quelle couleur de cire pour votre mariage ?',
     'Bordeaux, terracotta, sauge, or, blanc ivoire, bleu nuit : quelle couleur de cire choisir selon le thème de votre mariage, champêtre, bohème, chic ou hivernal. Inspiration faire-part et papeterie.',
     'couleur cire à cacheter, mariage bordeaux, mariage sauge, mariage terracotta, inspiration mariage'),
    ('07-glacon', B_TUTO, '/pages/guide-cachet-de-cire',
     'La cire colle au sceau ? L’astuce du glaçon',
     'Votre cachet de cire reste collé au sceau ? Le métal a chauffé. Posez le sceau quelques secondes sur un glaçon avant chaque pression : il se décolle net. Astuce simple pour débutantes.',
     'astuce cachet de cire, sceau colle, cachet de cire débutant, tuto sceau de cire'),
    ('08-retroplanning', B_ORGA, '/pages/livraison-et-retours',
     'Faire-part à la cire : le rétroplanning pour ne pas être en retard',
     'Choisir, commander, s’entraîner, envoyer : le calendrier pour sceller vos faire-part à la cire sereinement. Comptez au moins 4 semaines entre la commande du sceau et l’envoi de vos faire-part.',
     'rétroplanning mariage, organisation mariage, faire-part mariage quand envoyer, checklist mariage'),
    ('09-cadeau', B_CADEAU, '/products/coffret-initiale-cachet-de-cire-personnalise',
     'Idée cadeau : un sceau de cire à son initiale',
     'Un cadeau personnalisé et original : un sceau gravé à son initiale, la cire, le petit four et le guide pour écrire des lettres qu’on garde. Idée cadeau Noël, anniversaire, fête des mères.',
     'idée cadeau personnalisé, cadeau initiale, cadeau Noël femme, sceau de cire initiale'),
    ('10-cuillere-pistolet', B_TUTO, '/pages/faq',
     'Cuillère ou pistolet à colle pour le cachet de cire ?',
     'Débuter le cachet de cire : la cuillère pour un rendu authentique jusqu’à 150 cachets, le pistolet pour les grandes séries. Notre conseil : commencez à la cuillère, avec une cire souple.',
     'cachet de cire cuillère, pistolet cire à cacheter, débuter cachet de cire, matériel cachet de cire'),
]

with open(sys.argv[2] if len(sys.argv) > 2 else 'import-pinterest.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Title', 'Media URL', 'Pinterest board', 'Thumbnail', 'Description', 'Link', 'Publish date', 'Keywords'])
    for slug, board, path, title, desc, kw in PINS:
        assert len(title) <= 100 and len(desc) <= 500, slug
        w.writerow([title, RAW + slug + '.png', board, '', desc, SITE + path + UTM + slug, '', kw])
print(len(PINS), 'lignes')
