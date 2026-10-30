"""Génère les épingles Pinterest de Maison Lettrine (HTML -> PNG 1000×1500).

Usage : python3 pins.py <dossier_polices> <dossier_sortie_html>
Les PNG sont ensuite rendus par render.js (Chromium headless).
"""
import base64, pathlib, sys

FONTS = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
OUT.mkdir(parents=True, exist_ok=True)
HERE = pathlib.Path(__file__).parent


def b64(path):
    return base64.b64encode(pathlib.Path(path).read_bytes()).decode()


SEAL = 'data:image/png;base64,' + b64(HERE / 'cachet.png')
ICON = 'data:image/png;base64,' + b64(HERE / 'icone.png')  # en petit : l'icône « L » (cachet illisible sous 96 px)
CG = FONTS / '@fontsource/cormorant-garamond/files'
IN = FONTS / '@fontsource/inter/files'
FONT_CSS = ''.join(
    f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{w};src:url(data:font/woff2;base64,{b64(d / f)}) format('woff2');}}"
    for fam, d, f, w, st in [
        ('Cormorant', CG, 'cormorant-garamond-latin-500-normal.woff2', 500, 'normal'),
        ('Cormorant', CG, 'cormorant-garamond-latin-600-normal.woff2', 600, 'normal'),
        ('Cormorant', CG, 'cormorant-garamond-latin-500-italic.woff2', 500, 'italic'),
        ('Inter', IN, 'inter-latin-400-normal.woff2', 400, 'normal'),
        ('Inter', IN, 'inter-latin-500-normal.woff2', 500, 'normal'),
        ('Inter', IN, 'inter-latin-600-normal.woff2', 600, 'normal'),
    ]
)

BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--cream:#F5ECDD;--beige:#EFE3D3;--ink:#2A211E;--wax:#8E1F2B;--waxd:#6E1620;--gold:#B88A3E;--muted:rgba(42,33,30,.72)}
html,body{width:1000px;height:1500px}
body{font-family:Inter,sans-serif;font-variant-numeric:lining-nums;color:var(--ink);background:var(--cream);-webkit-font-smoothing:antialiased}
.pin{position:relative;width:1000px;height:1500px;padding:96px 90px 0;display:flex;flex-direction:column;overflow:hidden}
.kicker{font-size:24px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:var(--muted)}
.rule{width:80px;height:2px;background:var(--gold);margin:34px 0}
h1{font-family:Cormorant,serif;font-weight:600;font-size:104px;line-height:1.02;letter-spacing:-.005em}
h1 em{font-style:italic;font-weight:500;color:var(--wax)}
.lead{font-size:36px;line-height:1.45;color:var(--muted);margin-top:30px}
.foot{position:absolute;left:90px;right:90px;bottom:70px;display:flex;align-items:center;justify-content:space-between;padding-top:34px;border-top:1px solid rgba(42,33,30,.18)}
.brand{display:flex;align-items:center;gap:22px}
.brand img{width:84px;height:84px}
.dark .brand img,.wax .brand img{background:var(--cream);border-radius:50%;padding:6px}
.wm small{display:block;font-family:Cormorant,serif;font-style:italic;font-size:30px;color:var(--wax);line-height:1}
.wm b{display:block;font-family:Cormorant,serif;font-weight:600;font-size:40px;letter-spacing:.22em;line-height:1.1}
.url{font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.dark{background:var(--ink);color:var(--cream)} .dark .kicker,.dark .lead,.dark .url{color:rgba(245,236,221,.8)} .dark h1 em{color:#d9b46a} .dark .foot{border-color:rgba(245,236,221,.25)} .dark .wm small{color:#d9b46a}
.wax{background:var(--wax);color:#fff} .wax .kicker,.wax .lead,.wax .url{color:rgba(255,255,255,.85)} .wax h1 em{color:#f3d9a8} .wax .foot{border-color:rgba(255,255,255,.3)} .wax .wm small{color:#f3d9a8}
.beige{background:var(--beige)}
.list{list-style:none;margin-top:52px;display:grid;gap:34px}
.list.big li{font-size:40px}.list.big span.s{font-size:31px}.list.big{gap:44px}
.list li{display:flex;gap:26px;align-items:flex-start;font-size:33px;line-height:1.3}
.num{flex:none;width:58px;font-family:Cormorant,serif;font-weight:600;font-size:58px;line-height:.85;color:var(--wax)}
.list b{font-weight:600}
.list span.s{display:block;font-size:26px;color:var(--muted);margin-top:6px}
.seal{--s:300px;position:relative;display:grid;place-items:center;width:var(--s);height:var(--s);border-radius:48% 52% 46% 54%/53% 47% 53% 47%;
 background:radial-gradient(circle at 32% 26%,rgba(255,255,255,.28),transparent 38%),radial-gradient(circle at 70% 78%,rgba(0,0,0,.22),transparent 55%),var(--w,#8E1F2B);
 box-shadow:0 10px 30px rgba(42,33,30,.25),inset 0 -8px 16px rgba(0,0,0,.18)}
.seal i{display:grid;place-items:center;width:76%;height:76%;border-radius:50%;border:2px solid rgba(255,255,255,.3);box-shadow:inset 0 4px 10px rgba(0,0,0,.28);
 font-style:normal;font-family:Cormorant,serif;font-weight:600;font-size:calc(var(--s)*.42);color:rgba(0,0,0,.3);text-shadow:0 2px 0 rgba(255,255,255,.35),0 -1px 0 rgba(0,0,0,.25)}
.seal.two i{font-size:calc(var(--s)*.27)}
.center{text-align:center;align-items:center} .center .rule{margin-left:auto;margin-right:auto}
.cta{display:inline-block;margin-top:44px;padding:26px 44px;background:var(--wax);color:#fff;font-size:26px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}
.wax .cta,.dark .cta{background:var(--cream);color:var(--ink)}
"""

FOOT = f"""<div class="foot"><div class="brand"><img src="{ICON}" alt=""><div class="wm"><small>Maison</small><b>LETTRINE</b></div></div><div class="url">maisonlettrine.com</div></div>"""


def page(body, cls=''):
    return f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><style>{FONT_CSS}{BASE_CSS}</style></head><body><div class='pin {cls}'>{body}{FOOT}</div></body></html>"


def steps(items, big=True):
    return f'<ol class="list{" big" if big else ""}">' + ''.join(
        f'<li><span class="num">{i}</span><div><b>{t}</b><span class="s">{s}</span></div></li>' for i, (t, s) in enumerate(items, 1)
    ) + '</ol>'


PINS = {}

PINS['01-promesse'] = page(f"""
<div style="display:flex;justify-content:center;margin:10px 0 56px"><img src="{SEAL}" style="width:400px" alt=""></div>
<div class="center" style="display:flex;flex-direction:column">
<p class="kicker">Faire-part de mariage</p><div class="rule"></div>
<h1>Vos faire-part scellés à la cire. <em>Réussis dès le premier cachet.</em></h1>
<p class="lead">Le sceau, la cire souple et la méthode pas-à-pas, dans un seul coffret.</p></div>""", 'center')

PINS['02-7-erreurs'] = page("""
<p class="kicker">Cachet de cire · guide offert</p><div class="rule"></div>
<h1 style="font-size:92px">Les 7 erreurs qui <em>ratent</em> un cachet de cire</h1>
""" + steps([
    ('La cire colle au sceau', 'Sceau trop chaud : refroidissez-le sur un glaçon.'),
    ('La cire noircit', 'La flamme touche la cire : chauffez à distance.'),
    ('Des bulles', 'Surchauffe : retirez dès que c’est liquide.'),
    ('Empreinte floue', '3 perles minimum, pression bien droite.'),
    ('Cachet ovale ou baveux', 'Versez lentement, à 1 cm du papier.'),
    ('Il casse à La Poste', 'Cire souple + rabat collé.'),
    ('Plus de cire à mi-chemin', '3 perles par cachet + 10 % d’essais.'),
], big=False), 'beige')

PINS['03-4-gestes'] = page("""
<p class="kicker">Tutoriel cachet de cire</p><div class="rule"></div>
<h1>Un cachet réussi en <em>4 gestes</em></h1>
""" + steps([
    ('Chauffer', '3 perles dans la cuillère, sur le petit four. 2 à 3 minutes.'),
    ('Verser', 'En cercle, à 1 cm du papier, un peu plus large que le sceau.'),
    ('Presser', 'Attendez 5 s, puis sceau froid, bien droit, 10 s sans tourner.'),
    ('Soulever', 'D’un geste net. Refroidissez le sceau tous les 3 ou 4 cachets.'),
]) + """<p class="lead" style="margin-top:40px;font-size:28px">Le pas-à-pas complet, en photos : maisonlettrine.com</p>""")

PINS['04-calcul-cire'] = page("""
<p class="kicker">Faire-part de mariage</p><div class="rule"></div>
<h1>Combien de cire pour <em>100 faire-part&nbsp;?</em></h1>
<div style="margin-top:70px;display:grid;grid-template-columns:1fr 1fr;gap:30px">
 <div style="background:#fff;padding:60px 44px;border:1px solid rgba(42,33,30,.12)"><div style="font-family:Cormorant;font-weight:600;font-size:190px;line-height:.9;color:#8E1F2B">330</div><div style="font-size:30px;margin-top:14px">perles de cire</div></div>
 <div style="background:#fff;padding:60px 44px;border:1px solid rgba(42,33,30,.12)"><div style="font-family:Cormorant;font-weight:600;font-size:190px;line-height:.9;color:#8E1F2B">3</div><div style="font-size:30px;margin-top:14px">boîtes d’environ 150 perles</div></div>
</div>
<p class="lead" style="margin-top:56px">La règle : <b style="color:#2A211E">3 perles par cachet</b>, plus <b style="color:#2A211E">10 %</b> pour vos essais.</p>
<p class="lead" style="font-size:28px">Faites le calcul pour votre nombre d’invités sur maisonlettrine.com</p>""")

PINS['05-la-poste'] = page("""
<p class="kicker">Envoi postal</p><div class="rule"></div>
<h1 style="font-size:96px">Cachet de cire et La Poste : <em>la méthode</em> pour limiter la casse</h1>
""" + steps([
    ('Une cire souple', 'Elle plie au lieu de se fendre dans les machines de tri.'),
    ('Le rabat collé', 'Le cachet décore, il ne ferme pas seul.'),
    ('Une enveloppe épaisse', 'Le cachet est moins sollicité.'),
    ('Le dépôt au guichet', 'Plutôt que dans la boîte jaune.'),
    ('Une enveloppe test', 'Envoyez-vous-en une d’abord.'),
], big=False) + """<p class="lead" style="margin-top:34px;font-size:26px">Aucune méthode n’est garantie à 100 % : ces 5 points réduisent fortement le risque.</p>""", 'beige')

colors = [('Bordeaux', '#8E1F2B', 'Classique, chic'), ('Terracotta', '#B5583A', 'Bohème, champêtre'), ('Sauge', '#8A9A7B', 'Nature, eucalyptus'),
          ('Or', '#C9A54A', 'Soirée, élégant'), ('Blanc ivoire', '#EDE6D6', 'Romantique, épuré'), ('Bleu nuit', '#26324A', 'Hiver, intemporel')]
grid = ''.join(f'<div style="text-align:center"><div class="seal two" style="--s:190px;--w:{c};margin:0 auto"><i>C&amp;T</i></div><div style="font-family:Cormorant;font-weight:600;font-size:40px;margin-top:22px">{n}</div><div style="font-size:24px;color:rgba(42,33,30,.7);margin-top:4px">{s}</div></div>' for n, c, s in colors)
PINS['06-nuancier'] = page(f"""
<p class="kicker">Mariage · inspiration</p><div class="rule"></div>
<h1 style="font-size:94px">Quelle couleur de cire pour <em>votre mariage&nbsp;?</em></h1>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:46px 20px;margin-top:64px">{grid}</div>""")

PINS['07-glacon'] = page("""
<p class="kicker">Astuce cachet de cire</p><div class="rule"></div>
<h1>La cire colle au sceau&nbsp;? <em>L’astuce du glaçon.</em></h1>
<p class="lead" style="margin-top:44px">Le métal chauffe d’un cachet à l’autre et la cire accroche.</p>
<div style="margin-top:56px;padding:44px;background:rgba(255,255,255,.08);border-left:4px solid #d9b46a">
<p style="font-size:44px;line-height:1.45">Posez le sceau <b>quelques secondes sur un glaçon</b> avant de presser, puis essuyez-le. Il se décolle net.</p></div>
<p class="lead" style="margin-top:44px">Refaites-le tous les 3 ou 4 cachets.</p>""", 'dark')

PINS['08-retroplanning'] = page("""
<p class="kicker">Organisation du mariage</p><div class="rule"></div>
<h1 style="font-size:92px">Faire-part à la cire : <em>quand s’y prendre&nbsp;?</em></h1>
""" + steps([
    ('6 mois avant', 'Choisissez le style et la couleur de cire.'),
    ('5 mois avant', 'Commandez votre sceau gravé (validez l’aperçu de gravure).'),
    ('4 mois avant', 'Entraînez-vous : 2 ou 3 essais suffisent.'),
    ('3 mois avant', 'Scellez et envoyez vos faire-part.'),
]) + """<p class="lead" style="margin-top:34px;font-size:27px">Comptez au moins 4 semaines entre la commande et l’envoi de vos faire-part.</p>""", 'beige')

PINS['09-cadeau'] = page("""
<div style="display:flex;justify-content:center;margin:40px 0 70px"><div class="seal" style="--s:380px"><i>A</i></div></div>
<div class="center" style="display:flex;flex-direction:column">
<p class="kicker">Idée cadeau personnalisé</p><div class="rule"></div>
<h1>Un cadeau <em>à son initiale</em></h1>
<p class="lead">Un sceau gravé, la cire, le petit four et le guide : de quoi écrire des lettres qu’on garde.</p></div>""", 'center')

PINS['10-cuillere-pistolet'] = page("""
<p class="kicker">Débuter le cachet de cire</p><div class="rule"></div>
<h1>Cuillère ou pistolet à colle&nbsp;: <em>que choisir&nbsp;?</em></h1>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:60px">
 <div style="background:rgba(255,255,255,.12);padding:52px 40px"><div style="font-family:Cormorant;font-weight:600;font-size:62px">La cuillère</div>
 <p style="font-size:34px;line-height:1.45;margin-top:22px">Idéale pour débuter. Rendu plus authentique. Parfaite jusqu’à 150 cachets.</p></div>
 <div style="background:rgba(255,255,255,.12);padding:52px 40px"><div style="font-family:Cormorant;font-weight:600;font-size:62px">Le pistolet</div>
 <p style="font-size:34px;line-height:1.45;margin-top:22px">Plus rapide pour les grandes séries, au-delà de 150 cachets.</p></div>
</div>
<p class="lead" style="margin-top:56px">Le conseil : commencez à la cuillère, avec une cire souple.</p>""", 'wax')

for name, html in PINS.items():
    (OUT / f'{name}.html').write_text(html, encoding='utf-8')
print(len(PINS), 'épingles')
