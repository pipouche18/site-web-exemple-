"""Génère les déclinaisons du logo Maison Lettrine (cachet de cire).

Usage : python3 generer_logo.py <dossier_de_sortie>
Dépendances : pip install fonttools cairosvg
"""
import math, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import cairosvg

OUT = sys.argv[1]
FF = '/usr/share/fonts/truetype/freefont/'
FONTS = {
    'serif': TTFont(FF + 'FreeSerif.ttf'),
    'serifB': TTFont(FF + 'FreeSerifBold.ttf'),
    'ital': TTFont(FF + 'FreeSerifItalic.ttf'),
    'sans': TTFont('/usr/share/fonts/opentype/inter/Inter-Medium.otf'),
}

INK, CREAM, GOLD = '#2B211D', '#F5ECDD', '#B8893E'
WAX, WAX_DARK, WAX_LIGHT = '#8E1F2B', '#5E1119', '#B8424D'


def glyphs(font, s, size):
    f = FONTS[font]
    gs, cm = f.getGlyphSet(), f.getBestCmap()
    sc = size / f['head'].unitsPerEm
    return gs, [(gs[cm[ord(c)]], gs[cm[ord(c)]].width * sc) for c in s], sc


def text_path(font, s, x, y, size, track=0.0, anchor='middle'):
    """Chemin SVG d'une ligne de texte ; ligne de base en y ; track en em."""
    gs, gl, sc = glyphs(font, s, size)
    w = sum(a for _, a in gl) + track * size * (len(s) - 1)
    cx = x - (w / 2 if anchor == 'middle' else (w if anchor == 'end' else 0))
    pen = SVGPathPen(gs)
    for g, a in gl:
        g.draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
        cx += a + track * size
    return pen.getCommands(), w


def ring_text(font, s, cx, cy, r, size, track=0.0):
    """Texte disposé sur un cercle (lecture dans le sens horaire, centré en haut)."""
    gs, gl, sc = glyphs(font, s, size)
    total = sum(a for _, a in gl) + track * size * len(s)
    ang = -math.pi / 2 - (total / r) / 2
    pen = SVGPathPen(gs)
    for g, a in gl:
        mid = ang + (a / 2) / r
        ca, sa = math.cos(mid), math.sin(mid)
        # repère local : x tangent, y vers l'extérieur ; glyphe centré sur mid
        px, py = cx + r * ca, cy + r * sa
        tx, ty = -sa, ca            # tangent (sens horaire)
        ox, oy = ca, sa             # normale extérieure
        a_, b_ = tx * sc, ty * sc
        c_, d_ = ox * sc, oy * sc
        e_ = px - tx * a / 2
        f_ = py - ty * a / 2
        g.draw(TransformPen(pen, (a_, b_, c_, d_, e_, f_)))
        ang += (a + track * size) / r
    return pen.getCommands()


def blob(cx, cy, r, n=14, amp=0.035):
    """Contour irrégulier d'une goutte de cire écrasée (déterministe)."""
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        k = 1 + amp * (math.sin(3 * t + 0.7) + 0.6 * math.sin(5 * t + 2.1) + 0.4 * math.sin(8 * t))
        pts.append((cx + r * k * math.cos(t), cy + r * k * math.sin(t)))
    d = ''
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        if i == 0:
            d += f'M{p1[0]:.1f} {p1[1]:.1f}'
        d += f'C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}'
    return d + 'Z'


def seal(x, y, s, mono=None, uid='a'):
    """Cachet de cire de taille s posé en (x, y)."""
    k = s / 400
    if mono:
        base = dark = light = mono['bg']
        fill = f'fill="{base}"'
        defs = ''
        line = mono['fg']
    else:
        base, dark, light, line = WAX, WAX_DARK, WAX_LIGHT, '#D27A83'
        defs = (f'<defs><radialGradient id="w{uid}" cx="38%" cy="32%" r="75%">'
                f'<stop offset="0" stop-color="{WAX_LIGHT}"/><stop offset=".55" stop-color="{WAX}"/>'
                f'<stop offset="1" stop-color="{WAX_DARK}"/></radialGradient></defs>')
        fill = f'fill="url(#w{uid})"'
    g = f'{defs}<g transform="translate({x},{y}) scale({k})">'
    # goutte de cire étalée
    g += f'<path d="{blob(200, 200, 176)}" {fill}/>'
    # empreinte du sceau : creux légèrement décalé pour l'effet de relief
    if not mono:
        g += f'<circle cx="203" cy="204" r="148" fill="{light}" opacity=".55"/>'
        g += f'<circle cx="197" cy="196" r="148" fill="{dark}"/>'
        g += f'<circle cx="200" cy="200" r="146" fill="{base}"/>'
    else:
        g += f'<circle cx="200" cy="200" r="146" fill="none" stroke="{line}" stroke-width="3"/>'
    g += f'<circle cx="200" cy="200" r="138" fill="none" stroke="{line}" stroke-width="1.5" opacity=".9"/>'
    g += f'<circle cx="200" cy="200" r="98" fill="none" stroke="{line}" stroke-width="1.5" opacity=".9"/>'
    # texte en couronne
    ring = ring_text('serif', 'MAISON LETTRINE', 200, 200, 110, 26, track=0.14)
    if not mono:
        g += f'<path d="{ring}" fill="{dark}" transform="translate(-1.2,-1.2)"/>'
    g += f'<path d="{ring}" fill="{line}"/>'
    # petits losanges de part et d'autre, bas de la couronne
    for ang in (115, 90, 65):
        rad = math.radians(ang)
        px, py = 200 + 118 * math.cos(rad), 200 + 118 * math.sin(rad)
        sz = 5 if ang == 90 else 3
        g += f'<rect x="{px-sz:.1f}" y="{py-sz:.1f}" width="{2*sz}" height="{2*sz}" transform="rotate(45 {px:.1f} {py:.1f})" fill="{line}"/>'
    # lettrine centrale « L », en relief (ombre + reflet + face)
    L, _ = text_path('serifB', 'L', 202, 258, 170)
    if not mono:
        g += f'<path d="{L}" fill="{dark}" transform="translate(-4,-4)"/>'
        g += f'<path d="{L}" fill="#D27A83" transform="translate(2.5,2.5)"/>'
        g += f'<path d="{L}" fill="{base}"/>'
    else:
        g += f'<path d="{L}" fill="{line}"/>'
    # filets décoratifs sous la lettre
    g += f'<path d="M158 278 H242" stroke="{line}" stroke-width="1.5"/>'
    g += f'<circle cx="200" cy="278" r="3" fill="{line}"/>'
    g += '</g>'
    return g


def svg(w, h, body, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<title>Maison Lettrine</title>{b}{body}</svg>\n')


def wordmark(cx, y, scale=1.0, ink=INK, accent=WAX, align='middle'):
    m, mw = text_path('ital', 'Maison', cx, y, 46 * scale, track=0.02, anchor=align)
    l, lw = text_path('serif', 'LETTRINE', cx, y + 66 * scale, 64 * scale, track=0.16, anchor=align)
    t, tw = text_path('sans', 'CACHETS DE CIRE', cx, y + 112 * scale, 15 * scale, track=0.32, anchor=align)
    out = (f'<path d="{m}" fill="{accent}"/><path d="{l}" fill="{ink}"/>'
           f'<path d="{t}" fill="{ink}" opacity=".75"/>')
    return out, max(mw, lw, tw)


def save(name, s, png_w=None):
    open(os.path.join(OUT, name + '.svg'), 'w').write(s)
    cairosvg.svg2png(bytestring=s.encode(), write_to=os.path.join(OUT, name + '.png'),
                     output_width=png_w)


W, H = 600, 620
wm, _ = wordmark(300, 440)
save('logo-principal', svg(W, H, seal(150, 40, 300) + wm, bg=CREAM), 1200)
save('logo-principal-transparent', svg(W, H, seal(150, 40, 300) + wm), 1200)

wm_h, wml = wordmark(0, 0, align='start')
save('logo-horizontal', svg(int(270 + wml + 40), 260, seal(25, 25, 210) +
                            f'<g transform="translate(270,72)">{wm_h}</g>', bg=CREAM), 1600)

save('embleme', svg(400, 400, seal(0, 0, 400)), 512)

wm_d, _ = wordmark(300, 440, ink=CREAM, accent=GOLD)
save('logo-fond-sombre', svg(W, H, seal(150, 40, 300) + wm_d, bg=INK), 1200)

wm_m, _ = wordmark(300, 440, ink=INK, accent=INK)
save('logo-monochrome', svg(W, H, seal(150, 40, 300, mono={'bg': INK, 'fg': '#FFFFFF'}) + wm_m,
                            bg='#FFFFFF'), 1200)
