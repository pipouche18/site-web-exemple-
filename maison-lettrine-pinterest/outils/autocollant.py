"""Autocollant rond 4 cm « cachet » Maison Lettrine, fichiers d'impression.

Produit un HTML (SVG vectoriel, textes en Cormorant Garamond intégrée) rendu ensuite
en PDF par render_sticker.js : format 44 × 44 mm = 40 mm + 2 mm de fond perdu par côté.
Le bordeaux est légèrement éclairci pour compenser l'assombrissement de la lamination mate.

Usage : python3 autocollant.py <dossier_polices> <dossier_sortie_html>
"""
import base64, pathlib, sys

FONTS = pathlib.Path(sys.argv[1]) / '@fontsource/cormorant-garamond/files'
OUT = pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
b64 = lambda p: base64.b64encode(p.read_bytes()).decode()
FONT = ''.join(
    f"@font-face{{font-family:'Cormorant';font-weight:{w};font-style:{s};src:url(data:font/woff2;base64,{b64(FONTS / f)}) format('woff2')}}"
    for f, w, s in [('cormorant-garamond-latin-600-normal.woff2', 600, 'normal'), ('cormorant-garamond-latin-500-normal.woff2', 500, 'normal')]
)

WAX = '#9A2834'      # bordeaux de marque #8E1F2B, éclairci d'environ 8 % (lamination mate)
CREAM = '#F5ECDD'


def svg(cut_line=False):
    # Unités : 1 = 0,1 mm. Plan de 440 × 440 (44 mm), cercle de coupe de rayon 200 (40 mm).
    # Tous les éléments restent à 3 mm au moins de la coupe (rayon ≤ 170) ; traits ≥ 0,25 mm.
    c = 220
    cut = f'<circle cx="{c}" cy="{c}" r="200" fill="none" stroke="#00A0E9" stroke-width="2" stroke-dasharray="8 6"/>' if cut_line else ''
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="44mm" height="44mm" viewBox="0 0 440 440">
  <defs>
    <path id="arc" d="M {c-136},{c} A 136,136 0 1,1 {c+136},{c}"/>
  </defs>
  <!-- Fond bordeaux jusqu'au fond perdu (2 mm au-delà de la coupe) -->
  <circle cx="{c}" cy="{c}" r="220" fill="{WAX}"/>
  <!-- Double filet extérieur -->
  <circle cx="{c}" cy="{c}" r="170" fill="none" stroke="{CREAM}" stroke-width="3" opacity=".9"/>
  <circle cx="{c}" cy="{c}" r="162" fill="none" stroke="{CREAM}" stroke-width="2.5" opacity=".75"/>
  <!-- Filet intérieur -->
  <circle cx="{c}" cy="{c}" r="108" fill="none" stroke="{CREAM}" stroke-width="2.5" opacity=".8"/>
  <!-- MAISON LETTRINE en arc -->
  <text font-family="Cormorant" font-weight="600" font-size="31" letter-spacing="6.5" fill="{CREAM}">
    <textPath href="#arc" startOffset="50%" text-anchor="middle">MAISON LETTRINE</textPath>
  </text>
  <!-- Lettrine centrale -->
  <text x="{c}" y="{c+44}" text-anchor="middle" font-family="Cormorant" font-weight="600" font-size="138" fill="{CREAM}">L</text>
  <!-- Filet et point sous la lettre -->
  <line x1="{c-48}" y1="{c+66}" x2="{c+48}" y2="{c+66}" stroke="{CREAM}" stroke-width="2.5"/>
  <circle cx="{c}" cy="{c+66}" r="3.2" fill="{CREAM}"/>
  <!-- Trois losanges en bas, entre les filets -->
  <path d="M {c} {c+118} l 8 8 l -8 8 l -8 -8 z" fill="{CREAM}"/>
  <path d="M {c-38} {c+113} l 5 5 l -5 5 l -5 -5 z" fill="{CREAM}" opacity=".85"/>
  <path d="M {c+38} {c+113} l 5 5 l -5 5 l -5 -5 z" fill="{CREAM}" opacity=".85"/>
  {cut}
</svg>"""


def page(body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT}
@page{{size:44mm 44mm;margin:0}} html,body{{margin:0;width:44mm;height:44mm;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
svg{{display:block}}</style></head><body>{body}</body></html>"""


(OUT / 'autocollant-impression.html').write_text(page(svg(False)), encoding='utf-8')
(OUT / 'autocollant-avec-trait-de-coupe.html').write_text(page(svg(True)), encoding='utf-8')
print('ok')
