import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import cairosvg

OUT = sys.argv[1]
FF = '/usr/share/fonts/truetype/freefont/'
FONTS = {
  'serif': TTFont(FF+'FreeSerif.ttf'),
  'serifB': TTFont(FF+'FreeSerifBold.ttf'),
  'ital': TTFont(FF+'FreeSerifItalic.ttf'),
  'sans': TTFont('/usr/share/fonts/opentype/inter/Inter-Medium.otf'),
}

def text_path(font, s, x, y, size, track=0.0, anchor='middle'):
    """Return (svg path d, width) for string s; baseline at y; track in em."""
    f = FONTS[font]; gs = f.getGlyphSet(); cm = f.getBestCmap()
    upm = f['head'].unitsPerEm; sc = size/upm
    adv = [gs[cm[ord(c)]].width*sc for c in s]
    w = sum(adv) + track*size*(len(s)-1)
    cx = x - (w/2 if anchor=='middle' else (w if anchor=='end' else 0))
    pen = SVGPathPen(gs)
    for c, a in zip(s, adv):
        g = gs[cm[ord(c)]]
        g.draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
        cx += a + track*size
    return pen.getCommands(), w

INK, CREAM, GOLD, FLAME, FLAME2 = '#2B211D', '#F5ECDD', '#C59A4A', '#E8A33D', '#F7D58A'

def emblem(x, y, s, ink=INK, wax=CREAM, gold=GOLD, mono=None):
    """Drop-cap tile of size s at (x,y): framed square, candle-L, flame, drip."""
    k = s/400
    if mono:
        ink, wax, gold = mono['bg'], mono['fg'], mono['fg']
        fl1 = fl2 = mono['fg']
    else:
        fl1, fl2 = FLAME, FLAME2
    # L glyph from FreeSerif Bold: stem x 106-268, top serif 20-369, height 676
    L, _ = text_path('serifB', 'L', 0, 0, 1000, anchor='start')
    g = f'<g transform="translate({x},{y}) scale({k})">'
    g += f'<rect width="400" height="400" rx="6" fill="{ink}"/>'
    g += f'<rect x="14" y="14" width="372" height="372" fill="none" stroke="{gold}" stroke-width="2.5"/>'
    g += f'<rect x="22" y="22" width="356" height="356" fill="none" stroke="{gold}" stroke-width="1"/>'
    for cx, cy in [(14,14),(386,14),(14,386),(386,386)]:
        g += f'<rect x="{cx-5}" y="{cy-5}" width="10" height="10" transform="rotate(45 {cx} {cy})" fill="{gold}"/>'
    # letter placement: scale 0.38, baseline at y=338, glyph left at x≈ 200-(649*.38)/2
    ls = 0.35; ox = 200 - 649*ls/2 + 4; base = 334
    g += f'<g transform="translate({ox},{base}) scale({ls})" fill="{wax}">'
    g += f'<path d="{L}"/>'
    # wax drips hanging from the top serif (overlap the stem to avoid seams)
    g += ('<path d="M260 -651 L334 -651 C334 -612 318 -592 314 -566 L312 -500 '
          'C312 -476 298 -464 287 -464 C276 -464 260 -476 260 -500 Z"/>')
    g += ('<path d="M114 -651 L52 -651 C52 -628 68 -614 74 -598 C78 -584 84 -574 96 -574 '
          'C108 -574 114 -586 114 -598 Z"/>')
    g += '</g>'
    # wick + flame above the stem (stem centre x = 187 glyph units)
    fx = ox + 187*ls; top = base - 676*ls
    g += f'<path d="M{fx} {top} L{fx} {top-12}" stroke="{wax}" stroke-width="3" stroke-linecap="round"/>'
    fy = top - 10
    F = 0.8
    g += (f'<path d="M{fx} {fy-78*F} C{fx+8*F} {fy-52*F} {fx+30*F} {fy-38*F} {fx+30*F} {fy-16*F} '
          f'C{fx+30*F} {fy+2*F} {fx+16*F} {fy+8*F} {fx} {fy+8*F} C{fx-16*F} {fy+8*F} {fx-30*F} {fy+2*F} {fx-30*F} {fy-16*F} '
          f'C{fx-30*F} {fy-38*F} {fx-6*F} {fy-50*F} {fx} {fy-78*F} Z" fill="{fl1}"/>')
    g += (f'<path d="M{fx} {fy-38*F} C{fx+4*F} {fy-26*F} {fx+14*F} {fy-20*F} {fx+14*F} {fy-9*F} '
          f'C{fx+14*F} {fy} {fx+7*F} {fy+4*F} {fx} {fy+4*F} C{fx-7*F} {fy+4*F} {fx-14*F} {fy} {fx-14*F} {fy-9*F} '
          f'C{fx-14*F} {fy-20*F} {fx-3*F} {fy-27*F} {fx} {fy-38*F} Z" fill="{fl2 if not mono else ink}"/>')
    # small gold rule & dot to the right, like a drop-cap ornament
    g += '</g>'
    return g

def svg(w, h, body, bg=None):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<title>Maison Lettrine</title>{b}{body}</svg>\n')

def wordmark(cx, y, scale=1.0, ink=INK, gold=GOLD, align='middle'):
    m, mw = text_path('ital', 'Maison', cx, y, 46*scale, track=0.02, anchor=align)
    l, lw = text_path('serif', 'LETTRINE', cx, y+66*scale, 64*scale, track=0.16, anchor=align)
    t, tw = text_path('sans', 'CRÉATIONS EN CIRE', cx, y+112*scale, 15*scale, track=0.32, anchor=align)
    out = f'<path d="{m}" fill="{gold}"/><path d="{l}" fill="{ink}"/><path d="{t}" fill="{ink}" opacity=".75"/>'
    return out, max(mw, lw, tw)

def save(name, s, png_w=None):
    p = os.path.join(OUT, name + '.svg'); open(p, 'w').write(s)
    cairosvg.svg2png(bytestring=s.encode(), write_to=os.path.join(OUT, name + '.png'),
                     output_width=png_w)

# 1. Logo principal (vertical)
W, H = 600, 600
wm, _ = wordmark(300, 430)
save('logo-principal', svg(W, H, emblem(160, 60, 280) + wm, bg=CREAM), 1200)
# transparent version
save('logo-principal-transparent', svg(W, H, emblem(160, 60, 280) + wm), 1200)

# 2. Logo horizontal
wm_l, wml = wordmark(0, 0, 1.0, align='start')
W2 = 200 + 40 + 470 + 40
body = emblem(30, 30, 200) + f'<g transform="translate(260,72)">{wm_l}</g>'
save('logo-horizontal', svg(int(260 + wml + 40), 260, body, bg=CREAM), 1600)

# 3. Emblème seul (favicon / réseaux sociaux)
save('embleme', svg(400, 400, emblem(0, 0, 400)), 512)

# 4. Version sur fond foncé
wm_d, _ = wordmark(300, 430, ink=CREAM)
save('logo-fond-sombre', svg(W, H, emblem(160, 60, 280, ink='#3A2D27') + wm_d, bg=INK), 1200)

# 5. Monochrome (tampon, étiquettes, gravure)
mono = {'bg': INK, 'fg': '#FFFFFF'}
wm_m, _ = wordmark(300, 430, ink=INK, gold=INK)
save('logo-monochrome', svg(W, H, emblem(160, 60, 280, mono=mono) + wm_m, bg='#FFFFFF'), 1200)
