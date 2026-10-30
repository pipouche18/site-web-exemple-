"""Cachet Maison Lettrine, version 2 : trois pistes et fichiers d'impression.

Principes : filets fins (0,3 mm), beaucoup d'air, « L » en italique Cormorant Garamond,
textes en capitales Cormorant Garamond centrés exactement entre les deux filets
(même vide au-dessus et au-dessous), rien à moins de 3 mm de la coupe.

Unités du dessin : 1 = 0,1 mm. Autocollant : coupe 40 mm (rayon 200), fond perdu 2 mm (rayon 220).
Usage : python3 sceau.py <dossier_polices> <dossier_sortie_html>
"""
import base64, math, pathlib, sys

NM = pathlib.Path(sys.argv[1]) / '@fontsource'
OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()


def face(family, path, weight, style='normal'):
    return f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:{style};src:url(data:font/woff2;base64,{b64(NM / path)}) format('woff2')}}"


FONTS = ''.join([
    face('SC', 'cormorant-sc/files/cormorant-sc-latin-600-normal.woff2', 600),
    face('SC', 'cormorant-sc/files/cormorant-sc-latin-500-normal.woff2', 500),
    face('CG', 'cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2', 600, 'italic'),
    face('CG', 'cormorant-garamond/files/cormorant-garamond-latin-500-italic.woff2', 500, 'italic'),
    face('CG', 'cormorant-garamond/files/cormorant-garamond-latin-500-normal.woff2', 500),
    face('CG', 'cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2', 600),
    face('Inter', 'inter/files/inter-latin-500-normal.woff2', 500),
])

WAX = '#9A2834'     # bordeaux #8E1F2B éclairci (lamination mate)
WAX_SCREEN = '#8E1F2B'
CREAM = '#F5ECDD'
INK = '#2A211E'
CAP = 0.63          # hauteur des capitales Cormorant Garamond (mesurée)
L_ASC, L_CX = 0.63, 0.24   # « L » italique : hauteur et centre optique (en em)
C = 220             # centre du plan 440 × 440


def ring(r, w=3, color=CREAM):
    return f'<circle cx="{C}" cy="{C}" r="{r}" fill="none" stroke="{color}" stroke-width="{w}"/>'


def arc_text(top, bottom, r_in, r_out, size, spacing, color=CREAM, sep=True):
    """Texte en arc centré dans la bande [r_in, r_out] : même vide côté intérieur et extérieur."""
    mid = (r_in + r_out) / 2
    cap = CAP * size
    r_top = mid - cap / 2           # ligne de base du texte du haut (capitales vers l'extérieur)
    r_bot = mid + cap / 2           # ligne de base du texte du bas (capitales vers le centre)
    out = [f'<path id="t" d="M {C-r_top},{C} A {r_top},{r_top} 0 1,1 {C+r_top},{C}" fill="none"/>',
           f'<path id="b" d="M {C-r_bot},{C} A {r_bot},{r_bot} 0 0,0 {C+r_bot},{C}" fill="none"/>']
    style = f'font-family="CG" font-weight="600" font-size="{size}" letter-spacing="{spacing}" fill="{color}"'
    out.append(f'<text {style}><textPath href="#t" startOffset="50%" text-anchor="middle">{top}</textPath></text>')
    if bottom:
        out.append(f'<text {style}><textPath href="#b" startOffset="50%" text-anchor="middle">{bottom}</textPath></text>')
    if sep:  # petits losanges à 9 h et 3 h, au milieu de la bande
        s = 4.5
        for x in (C - mid, C + mid):
            out.append(f'<path d="M {x} {C-s} L {x+s} {C} L {x} {C+s} L {x-s} {C} Z" fill="{color}"/>')
    return '\n'.join(out)


def initial(size, color=CREAM, dy=0):
    x = C - L_CX * size
    y = C + L_ASC * size / 2 + dy
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="CG" font-style="italic" font-weight="600" font-size="{size}" fill="{color}">L</text>'


def beads(r, n=72, d=2.6, color=CREAM):
    return ''.join(f'<circle cx="{C + r*math.cos(2*math.pi*i/n):.2f}" cy="{C + r*math.sin(2*math.pi*i/n):.2f}" r="{d}" fill="{color}"/>' for i in range(n))


# --- Les trois pistes (contenu au-dessus du disque bordeaux) ---
def piste_a():  # « Écrin » : la recommandée
    return '\n'.join([ring(172), ring(122),
                      arc_text('MAISON LETTRINE', 'CACHETS DE CIRE', 123.5, 170.5, 26, 6.2),
                      initial(196)])


def piste_b():  # « Monogramme » : moderne, sans texte en arc
    return '\n'.join([ring(172),
                      initial(250, dy=-26),
                      f'<line x1="{C-30}" y1="{C+66}" x2="{C+30}" y2="{C+66}" stroke="{CREAM}" stroke-width="3"/>',
                      f'<text x="{C}" y="{C+104}" text-anchor="middle" font-family="CG" font-weight="600" font-size="19" letter-spacing="4" fill="{CREAM}">MAISON LETTRINE</text>'])


def piste_c():  # « Médaille » : bordure perlée façon pièce de monnaie
    return '\n'.join([beads(166), ring(128),
                      arc_text('MAISON LETTRINE', None, 129.5, 158, 25, 6.5, sep=False),
                      f'<path d="M {C} {C+141} l 6 6 l -6 6 l -6 -6 z" fill="{CREAM}"/>',
                      initial(200)])


def disc(inner, bleed=True, color=WAX):
    r = 220 if bleed else 200
    return f'<circle cx="{C}" cy="{C}" r="{r}" fill="{color}"/>' + inner


def svg(inner, w='44mm', h='44mm', vb='0 0 440 440', extra=''):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{vb}">{inner}{extra}</svg>'


CUT = f'<circle cx="{C}" cy="{C}" r="200" fill="none" stroke="#00A0E9" stroke-width="2" stroke-dasharray="8 6"/>'


def page(body, w, h, bg='transparent'):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}"
            f"@page{{size:{w} {h};margin:0}}html,body{{margin:0;width:{w};height:{h};background:{bg};"
            f"-webkit-print-color-adjust:exact;print-color-adjust:exact}}svg{{display:block}}</style></head><body>{body}</body></html>")


def write(name, html):
    (OUT / f'{name}.html').write_text(html, encoding='utf-8')


# 1. Fichiers d'impression de l'autocollant (piste A)
write('autocollant-impression__44mm', page(svg(disc(piste_a())), '44mm', '44mm'))
write('autocollant-avec-trait-de-coupe__44mm', page(svg(disc(piste_a()), extra=CUT), '44mm', '44mm'))

# 2. Cachet maître (logo seul, sans fond perdu, fond transparent), bordeaux écran
write('cachet-maison-lettrine__40mm', page(svg(disc(piste_a().replace(WAX, WAX_SCREEN), bleed=False, color=WAX_SCREEN),
                                               w='40mm', h='40mm', vb='20 20 400 400'), '40mm', '40mm'))

# 3. Planche de comparaison des trois pistes (en grand + à taille réelle)
def card(title, sub, inner):
    big = svg(disc(inner, bleed=False), w='300', h='300', vb='20 20 400 400')
    real = svg(disc(inner, bleed=False), w='151', h='151', vb='20 20 400 400')  # ~4 cm à l'écran
    return (f"<div class='c'><div class='big'>{big}</div><h2>{title}</h2><p>{sub}</p>"
            f"<div class='real'>{real}<span>taille réelle (4 cm)</span></div></div>")

board = f"""<div class='board'><h1>Cachet Maison Lettrine — trois pistes</h1><div class='row'>
{card('A · Écrin <em>(recommandée)</em>', 'Le sceau complet, nom et métier, texte centré entre deux filets fins, « L » italique.', piste_a())}
{card('B · Monogramme', 'Plus moderne : la lettre seule, le nom en petites capitales dessous.', piste_b())}
{card('C · Médaille', 'Bordure perlée façon pièce ancienne, plus patrimoniale.', piste_c())}
</div></div>"""
write('planche-pistes__1500x900', page(board, '1500px', '900px', CREAM).replace('</style>', """
.board{font-family:CG;color:#2A211E;padding:56px 60px}.board h1{font-family:SC;font-weight:600;font-size:34px;letter-spacing:.18em;margin:0 0 40px;text-align:center}
.row{display:grid;grid-template-columns:repeat(3,1fr);gap:40px}.c{text-align:center}.big{display:flex;justify-content:center}
.c h2{font-family:SC;font-weight:600;font-size:28px;letter-spacing:.1em;margin:22px 0 6px}.c h2 em{font-family:CG;font-style:italic;font-weight:500;letter-spacing:0;color:#8E1F2B;text-transform:none}
.c p{font-family:Inter;font-size:15px;line-height:1.5;color:rgba(42,33,30,.75);margin:0 20px 18px}.real{display:flex;flex-direction:column;align-items:center;gap:8px}
.real span{font-family:Inter;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:rgba(42,33,30,.6)}</style>"""))

# 4. Planche logo complet (cachet + nom), versions claire et foncée
def lockup(bg, ink, accent, wax):
    seal = svg(disc(piste_a().replace(WAX, wax), bleed=False, color=wax), w='280', h='280', vb='20 20 400 400')
    return (f"<div class='lk' style='background:{bg};color:{ink}'>{seal}"
            f"<div class='m' style='color:{accent}'>Maison</div><div class='w'>LETTRINE</div><div class='t'>Cachets de cire</div></div>")

logo = f"<div class='g'>{lockup(CREAM, INK, WAX_SCREEN, WAX_SCREEN)}{lockup(INK, CREAM, '#C9A86A', WAX_SCREEN)}</div>"
write('planche-logo__1600x900', page(logo, '1600px', '900px', CREAM).replace('</style>', """
.g{display:grid;grid-template-columns:1fr 1fr;height:900px}.lk{display:flex;flex-direction:column;align-items:center;justify-content:center}
.m{font-family:CG;font-style:italic;font-weight:500;font-size:64px;line-height:1;margin-top:46px}
.w{font-family:CG;font-weight:500;font-size:84px;letter-spacing:.3em;margin-right:-.3em;line-height:1.1}
.t{font-family:Inter;font-weight:500;font-size:17px;letter-spacing:.42em;text-transform:uppercase;margin-top:26px;opacity:.8}</style>"""))
print('ok')
