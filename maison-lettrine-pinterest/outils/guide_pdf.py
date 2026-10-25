"""Mini-guide « Les 7 erreurs à éviter » (PDF A4, 5 pages) aux couleurs de Maison Lettrine.

Usage : python3 guide_pdf.py <dossier_polices> <fichier_html>
Le PDF est ensuite rendu par render_pdf.js (Chromium headless).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib.util

spec = importlib.util.spec_from_file_location('pins', pathlib.Path(__file__).parent / 'pins.py')
# Réutilise polices et cachet du générateur d'épingles sans exécuter sa génération.
src = (pathlib.Path(__file__).parent / 'pins.py').read_text(encoding='utf-8')
head = src.split('BASE_CSS = """')[0]
ns = {'__file__': str(pathlib.Path(__file__).parent / 'pins.py')}
sys.argv = [sys.argv[0], sys.argv[1], '/tmp'] + sys.argv[2:]
exec(head, ns)
FONT_CSS, SEAL = ns['FONT_CSS'], ns['SEAL']
OUT = pathlib.Path(sys.argv[3])

ERRORS = [
    ('La cire colle au sceau', 'Le sceau en laiton chauffe d’un cachet à l’autre, ou la cire est encore trop liquide quand vous pressez.',
     'Posez le sceau quelques secondes sur un glaçon, essuyez-le, et attendez 5 secondes après avoir versé la cire. Refaites-le tous les 3 ou 4 cachets.'),
    ('La cire noircit', 'La flamme touche directement la cire : elle dépose de la suie.',
     'Chauffez la cuillère à distance, posée sur un petit four avec une bougie chauffe-plat. Jamais dans la flamme.'),
    ('Des bulles dans le cachet', 'La cire a surchauffé et bout.',
     'Retirez la cuillère dès que la cire est liquide (2 à 3 minutes). Une bulle ? Percez-la avec un cure-dent avant de presser.'),
    ('Une empreinte floue', 'Pas assez de cire, ou un sceau incliné au moment de presser.',
     'Comptez 3 perles minimum pour un sceau de 25 mm, et pressez bien droit, sans tourner, pendant 10 secondes.'),
    ('Un cachet ovale ou baveux', 'La cire est versée trop vite, ou de trop haut.',
     'Versez lentement, en cercle, à 1 cm du papier : un disque un peu plus large que le sceau.'),
    ('Le cachet casse à La Poste', 'Une cire dure se fend dans les machines de tri.',
     'Choisissez une cire souple, collez aussi le rabat, préférez une enveloppe épaisse et déposez vos enveloppes au guichet.'),
    ('Plus de cire à mi-chemin', 'La quantité a été sous-estimée.',
     'Comptez 3 perles par cachet, plus 10 % pour vos essais. Pour 100 faire-part : environ 330 perles, soit 3 boîtes.'),
]

CSS = FONT_CSS + """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
:root{--cream:#F5ECDD;--beige:#EFE3D3;--ink:#2A211E;--wax:#8E1F2B;--gold:#B88A3E;--muted:rgba(42,33,30,.74)}
body{font-family:Inter,sans-serif;color:var(--ink);font-variant-numeric:lining-nums;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;padding:22mm 20mm 18mm;background:var(--cream);position:relative;page-break-after:always;overflow:hidden}
.page:last-child{page-break-after:auto}
.kicker{font-size:9pt;font-weight:500;letter-spacing:.26em;text-transform:uppercase;color:var(--muted)}
.rule{width:22mm;height:.6mm;background:var(--gold);margin:7mm 0}
h1{font-family:Cormorant,serif;font-weight:600;font-size:40pt;line-height:1.04}
h1 em,h2 em{font-style:italic;font-weight:500;color:var(--wax)}
h2{font-family:Cormorant,serif;font-weight:600;font-size:26pt;line-height:1.1;margin-bottom:6mm}
p{font-size:11pt;line-height:1.6}
.lead{font-size:13pt;color:var(--muted);line-height:1.55}
.foot{position:absolute;left:20mm;right:20mm;bottom:12mm;display:flex;justify-content:space-between;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);border-top:.3mm solid rgba(42,33,30,.18);padding-top:4mm}
.err{display:grid;grid-template-columns:14mm 1fr;gap:0 5mm;padding:5mm 0;border-bottom:.3mm solid rgba(42,33,30,.14)}
.err:last-child{border-bottom:0}
.n{font-family:Cormorant,serif;font-weight:600;font-size:30pt;line-height:.9;color:var(--wax)}
.err h3{font-family:Cormorant,serif;font-weight:600;font-size:17pt;margin-bottom:1.5mm}
.cause{font-size:10pt;color:var(--muted);line-height:1.5}
.fix{margin-top:2.5mm;font-size:10.5pt;line-height:1.5;padding:3mm 4mm;background:#fff;border-left:.8mm solid var(--wax)}
.fix b{color:var(--wax);font-size:8pt;letter-spacing:.18em;text-transform:uppercase;display:block;margin-bottom:1mm}
.box{background:#fff;padding:7mm;border:.3mm solid rgba(42,33,30,.12);margin-top:6mm}
.steps{list-style:none;display:grid;gap:4mm;margin-top:4mm}
.steps li{display:grid;grid-template-columns:10mm 1fr;font-size:11pt;line-height:1.5}
.steps li span{font-family:Cormorant,serif;font-weight:600;font-size:20pt;color:var(--wax);line-height:1}
.cta{display:inline-block;margin-top:8mm;padding:4mm 8mm;background:var(--wax);color:#fff;font-size:10pt;font-weight:600;letter-spacing:.16em;text-transform:uppercase;text-decoration:none}
.small{font-size:9pt;color:var(--muted);line-height:1.5}
"""

FOOT = lambda n: f'<div class="foot"><span>Maison Lettrine · Le mini-guide des 7 erreurs</span><span>{n} / 5</span></div>'


def err_block(start, items):
    return ''.join(
        f'<div class="err"><div class="n">{i}</div><div><h3>{t}</h3><p class="cause">{c}</p><div class="fix"><b>La solution</b>{s}</div></div></div>'
        for i, (t, c, s) in enumerate(items, start)
    )


html = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Le mini-guide des 7 erreurs à éviter – Maison Lettrine</title><style>{CSS}</style></head><body>

<section class="page" style="display:flex;flex-direction:column;align-items:center;text-align:center;justify-content:center">
  <img src="{SEAL}" style="width:70mm" alt="">
  <p class="kicker" style="margin-top:14mm">Guide offert</p><div class="rule" style="margin-left:auto;margin-right:auto"></div>
  <h1>Le mini-guide des <em>7 erreurs</em> à éviter</h1>
  <p class="lead" style="margin-top:8mm;max-width:130mm">Tout ce qu’on aurait aimé savoir avant nos premiers cachets de cire. Lisez-le avant de commencer : vos faire-part vous remercieront.</p>
  <p class="small" style="position:absolute;bottom:16mm">maisonlettrine.com</p>
</section>

<section class="page">
  <p class="kicker">Avant de commencer</p><div class="rule"></div>
  <h2>Un cachet réussi, c’est <em>une question de température</em></h2>
  <p>Presque tous les ratés viennent de là : une cire trop chaude, un sceau trop chaud, ou une flamme trop proche. Bonne nouvelle : tout se corrige avec trois habitudes simples.</p>
  <div class="box">
    <p class="kicker" style="margin-bottom:2mm">Votre matériel</p>
    <ol class="steps">
      <li><span>1</span><div><b>Un sceau</b> à votre initiale (tête en laiton).</div></li>
      <li><span>2</span><div><b>De la cire</b> en perles : 3 perles par cachet de 25 mm.</div></li>
      <li><span>3</span><div><b>Une cuillère</b> et <b>un petit four</b> avec une bougie chauffe-plat.</div></li>
      <li><span>4</span><div><b>Un glaçon</b> ou un sceau passé au congélateur.</div></li>
      <li><span>5</span><div><b>Une feuille de brouillon</b> pour 2 ou 3 essais.</div></li>
    </ol>
  </div>
  <div class="box">
    <p class="kicker" style="margin-bottom:2mm">Un cachet en 4 gestes</p>
    <ol class="steps">
      <li><span>1</span><div><b>Chauffer</b> : 3 perles dans la cuillère, sur le four, 2 à 3 minutes.</div></li>
      <li><span>2</span><div><b>Verser</b> : en cercle, à 1 cm du papier.</div></li>
      <li><span>3</span><div><b>Presser</b> : attendez 5 s, puis sceau froid, bien droit, 10 s.</div></li>
      <li><span>4</span><div><b>Soulever</b> : d’un geste net et vertical.</div></li>
    </ol>
  </div>
  {FOOT(2)}
</section>

<section class="page">
  <p class="kicker">Les erreurs 1 à 4</p><div class="rule"></div>
  <h2>Ce qui rate, et <em>comment l’éviter</em></h2>
  {err_block(1, ERRORS[:4])}
  {FOOT(3)}
</section>

<section class="page">
  <p class="kicker">Les erreurs 5 à 7</p><div class="rule"></div>
  {err_block(5, ERRORS[4:])}
  <div class="box" style="margin-top:8mm">
    <p class="kicker" style="margin-bottom:2mm">Combien de cire&nbsp;?</p>
    <p><b>3 perles par cachet + 10 % d’essais.</b> 50 faire-part ≈ 165 perles · 100 faire-part ≈ 330 perles · 150 faire-part ≈ 500 perles. Une boîte contient environ 150 perles.</p>
  </div>
  {FOOT(4)}
</section>

<section class="page">
  <p class="kicker">Envoi postal</p><div class="rule"></div>
  <h2>Vos enveloppes à La Poste : <em>la méthode</em></h2>
  <ol class="steps">
    <li><span>1</span><div><b>Une cire souple</b> : elle plie au lieu de se fendre dans les machines de tri.</div></li>
    <li><span>2</span><div><b>Le rabat collé</b> : le cachet décore, il ne ferme pas l’enveloppe seul.</div></li>
    <li><span>3</span><div><b>Une enveloppe épaisse</b> ou rigide.</div></li>
    <li><span>4</span><div><b>Le dépôt au guichet</b> plutôt que dans la boîte jaune (vérifiez le tarif en vigueur).</div></li>
    <li><span>5</span><div><b>Une enveloppe test</b> envoyée à vous-même avant le grand envoi.</div></li>
  </ol>
  <p class="small" style="margin-top:5mm">Aucune méthode n’est garantie à 100 % : ces 5 points réduisent fortement le risque.</p>
  <div class="box" style="margin-top:10mm;text-align:center">
    <img src="{SEAL}" style="width:26mm" alt="">
    <h2 style="font-size:22pt;margin:4mm 0 3mm">Tout est réuni dans <em>nos coffrets</em></h2>
    <p>Le sceau à votre initiale, la cire, le petit four, la cuillère et la méthode pas-à-pas.<br>Une question ? Répondez simplement à notre e-mail : une vraie personne vous répond.</p>
    <a class="cta" href="https://maisonlettrine.com/collections/coffrets-cachet-de-cire?utm_source=guide&amp;utm_medium=pdf">Découvrir les coffrets</a>
  </div>
  {FOOT(5)}
</section>
</body></html>"""
OUT.write_text(html, encoding='utf-8')
print('ok')
