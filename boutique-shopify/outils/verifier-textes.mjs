// Vérifie le thème et les fichiers produits avant mise en ligne.
// Usage (depuis le dossier boutique-shopify) :  node outils/verifier-textes.mjs
//  1. Bloque toute mention interdite de la fibre « lin » / « linen » (nos produits sont en coton).
//  2. Liste les textes encore marqués « [à confirmer] » ou « [À COMPLÉTER] ».
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const racine = new URL('..', import.meta.url).pathname;
const dossiers = ['theme', 'produits', 'docs'];
const extensions = /\.(liquid|json|js|css|csv|md|txt)$/i;
// « linge » est autorisé : on ne cherche que le mot isolé.
const interdit = /\b(lin|linen|linens)\b/i;
const aCompleter = /\[(à confirmer|À COMPLÉTER|VOTRE-EMAIL)[^\]]*\]/gi;

const fichiers = [];
const parcourir = (d) => {
  for (const nom of readdirSync(d)) {
    const chemin = join(d, nom);
    if (statSync(chemin).isDirectory()) parcourir(chemin);
    else if (extensions.test(nom)) fichiers.push(chemin);
  }
};
dossiers.forEach((d) => parcourir(join(racine, d)));

let erreurs = 0;
const restes = {};
for (const f of fichiers) {
  // Les traductions d'origine de Dawn (locales) ne contiennent pas de texte produit.
  if (f.includes('/locales/') && !/fr\.default\.json$/.test(f)) continue;
  readFileSync(f, 'utf8').split('\n').forEach((ligne, i) => {
    if (interdit.test(ligne) && !ligne.includes('verifier-textes-ignore')) {
      erreurs++;
      console.log(`✗ Mot interdit dans ${relative(racine, f)}:${i + 1}\n    ${ligne.trim().slice(0, 160)}`);
    }
    const m = ligne.match(aCompleter);
    if (m) restes[relative(racine, f)] = (restes[relative(racine, f)] || 0) + m.length;
  });
}

console.log('\nTextes encore à compléter ou confirmer :');
const liste = Object.entries(restes);
if (!liste.length) console.log('  aucun 🎉');
liste.forEach(([f, n]) => console.log(`  - ${f} : ${n}`));

if (erreurs) {
  console.log(`\n✗ ${erreurs} mention(s) interdite(s) à corriger : nos produits sont en coton.`);
  process.exit(1);
}
console.log('\n✓ Aucune mention interdite de la fibre « lin » trouvée.');
