/* Maison Nuits Douces – fiche produit : dates de livraison, taille de lit, onglets. */
(() => {
  /* ---------- Livraison estimée ---------- */
  const addDays = (start, days, business) => {
    const d = new Date(start);
    let added = 0;
    while (added < days) {
      d.setDate(d.getDate() + 1);
      const day = d.getDay();
      if (!business || (day !== 0 && day !== 6)) added += 1;
    }
    return d;
  };
  const fmt = new Intl.DateTimeFormat('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' });

  document.querySelectorAll('[data-nd-delivery]').forEach((el) => {
    const min = parseInt(el.dataset.min, 10);
    const max = parseInt(el.dataset.max, 10);
    if (!min || !max) return;
    const business = el.dataset.business === 'true';
    const today = new Date();
    const text = el.querySelector('[data-nd-delivery-text]');
    text.innerHTML =
      'Livraison estimée entre le <strong>' + fmt.format(addDays(today, min, business)) +
      '</strong> et le <strong>' + fmt.format(addDays(today, max, business)) + '</strong>';
  });

  /* ---------- Correspondance housse ↔ lit ---------- */
  const normalize = (s) =>
    String(s || '')
      .toLowerCase()
      .replace(/cm/g, '')
      .replace(/[x×*]/g, '×')
      .replace(/\s+/g, '');

  document.querySelectorAll('[data-nd-bed-size]').forEach((el) => {
    const map = {};
    try {
      JSON.parse(el.querySelector('[data-nd-bed-map]').textContent).forEach((raw) => {
        const line = raw.replace(/<br\s*\/?>/gi, '').trim();
        const [size, ...rest] = line.split('=');
        if (size && rest.length) map[normalize(size)] = rest.join('=').trim();
      });
    } catch (e) {
      return;
    }
    const output = el.querySelector('[data-nd-bed-value]');
    const index = parseInt(el.dataset.optionIndex, 10);
    const update = (value) => {
      const key = normalize(value);
      const found = key in map ? key : Object.keys(map).find((k) => key.includes(k));
      const match = found && map[found];
      el.hidden = !match;
      if (match) output.textContent = match;
    };
    update(el.dataset.current);

    if (typeof subscribe === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
      subscribe(PUB_SUB_EVENTS.variantChange, ({ data }) => {
        if (data.sectionId !== el.dataset.section || !data.variant) return;
        update(data.variant.options[index]);
      });
    }
  });

  /* ---------- Onglets accessibles ---------- */
  document.querySelectorAll('[data-nd-tabs]').forEach((root) => {
    const list = root.querySelector('[role="tablist"]');
    const tabs = Array.from(list.querySelectorAll('[role="tab"]'));
    const panels = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')));
    root.classList.add('nd-tabs--enhanced');
    list.hidden = false;

    const select = (i, focus) => {
      tabs.forEach((t, j) => {
        const on = i === j;
        t.setAttribute('aria-selected', on);
        t.tabIndex = on ? 0 : -1;
        panels[j].hidden = !on;
      });
      if (focus) tabs[i].focus();
    };
    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => select(i, false));
      tab.addEventListener('keydown', (e) => {
        const keys = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 };
        if (!(e.key in keys)) return;
        e.preventDefault();
        select((keys[e.key] + tabs.length) % tabs.length, true);
      });
    });
    select(0, false);
  });
})();

/* ---------------------------------------------------------------
   Galerie produit (ordinateur) : petit compteur « 2 / 5 » sur la grande
   photo. La molette garde partout son comportement normal (défilement).
   --------------------------------------------------------------- */
(function () {
  function thumbs(gallery) {
    return Array.prototype.slice
      .call(gallery.querySelectorAll('[id^="GalleryThumbnails"] .thumbnail-list__item'))
      .filter(function (li) { return li.offsetParent !== null; });
  }
  function currentIndex(list) {
    for (var i = 0; i < list.length; i++) {
      if (list[i].querySelector('button[aria-current]')) return i;
    }
    return 0;
  }
  function isThumbLayout(gallery) {
    return (gallery.dataset.desktopLayout || '').indexOf('thumbnail') !== -1;
  }

  function updateCount(gallery) {
    var viewer = gallery.querySelector('[id^="GalleryViewer"]');
    var list = thumbs(gallery);
    if (!viewer || list.length < 2) return;
    var pill = viewer.querySelector('.nd-gallery-count');
    if (!pill) {
      pill = document.createElement('span');
      pill.className = 'nd-gallery-count';
      pill.setAttribute('aria-hidden', 'true');
      viewer.appendChild(pill);
    }
    pill.textContent = currentIndex(list) + 1 + ' / ' + list.length;
  }

  function setup() {
    document.querySelectorAll('media-gallery').forEach(function (gallery) {
      if (gallery.ndCount || !isThumbLayout(gallery)) return;
      gallery.ndCount = true;
      updateCount(gallery);
      var t = gallery.querySelector('[id^="GalleryThumbnails"]');
      if (t) new MutationObserver(function () { updateCount(gallery); }).observe(t, { attributes: true, subtree: true, attributeFilter: ['aria-current'] });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', setup); else setup();
  // La galerie est re-rendue quand on change de variante : on se rebranche.
  new MutationObserver(setup).observe(document.body, { childList: true, subtree: true });

})();
