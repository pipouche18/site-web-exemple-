/* Maison Lettrine – fiche produit :
   date de livraison estimée, aperçu du cachet (initiale choisie),
   initiales à graver (aperçu en direct, compteur, couleur de cire, validation). */
(() => {
  const onVariantChange = (callback) => {
    if (typeof subscribe === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
      subscribe(PUB_SUB_EVENTS.variantChange, ({ data }) => callback(data));
    }
  };

  /* Option choisie dans le sélecteur de variantes (boutons, pastilles ou liste). */
  const optionFromEvent = (target) => {
    const option = target.tagName === 'SELECT' ? target.selectedOptions[0] : target;
    if (!option || !option.dataset) return null;
    return { name: option.dataset.optionName, value: target.value };
  };

  /* Ajuste la taille du texte du cachet à sa longueur. */
  const setSealText = (seal, text) => {
    const el = seal.querySelector('[data-ml-seal-text]');
    el.textContent = text;
    el.dataset.length = String(text.length);
  };

  /* ---------- Livraison estimée (jours ouvrés) ---------- */
  const addDays = (start, days, business) => {
    const date = new Date(start);
    let added = 0;
    while (added < days) {
      date.setDate(date.getDate() + 1);
      const day = date.getDay();
      if (!business || (day !== 0 && day !== 6)) added += 1;
    }
    return date;
  };
  const dateFormat = new Intl.DateTimeFormat('fr-FR', { weekday: 'long', day: 'numeric', month: 'long' });

  document.querySelectorAll('[data-ml-delivery]').forEach((el) => {
    const min = parseInt(el.dataset.min, 10);
    const max = parseInt(el.dataset.max, 10);
    if (!min || !max) return;
    const business = el.dataset.business === 'true';
    const today = new Date();
    el.querySelector('[data-ml-delivery-text]').innerHTML = el.dataset.template
      .replace('[from]', dateFormat.format(addDays(today, min, business)))
      .replace('[to]', dateFormat.format(addDays(today, max, business)));
  });

  /* ---------- Aperçu de l'initiale choisie ---------- */
  document.querySelectorAll('[data-ml-seal-preview]').forEach((preview) => {
    const seal = preview.querySelector('[data-ml-seal]');
    const live = preview.querySelector('[data-ml-seal-live]');
    const index = parseInt(preview.dataset.optionIndex, 10);
    const update = (value) => {
      if (!value) return;
      setSealText(seal, value);
      live.textContent = value;
    };
    document.addEventListener('change', (event) => {
      const option = optionFromEvent(event.target);
      if (option && option.name === preview.dataset.optionName) {
        update(option.value);
        document.documentElement.dataset.mlOptionChosen = 'true';
      }
    });
    onVariantChange((data) => {
      if (data.sectionId === preview.dataset.section && data.variant) update(data.variant.options[index]);
    });
  });

  /* ---------- Initiales à graver ---------- */
  document.querySelectorAll('[data-ml-engraving]').forEach((root) => {
    const input = root.querySelector('[data-ml-engraving-input]');
    const seal = root.querySelector('[data-ml-seal]');
    const count = root.querySelector('[data-ml-count]');
    const colorIndex = parseInt(root.dataset.colorIndex, 10);
    const colors = {};
    try {
      JSON.parse(root.querySelector('[data-ml-wax-colors]').textContent).forEach((line) => {
        const [name, hex] = line.split('=').map((part) => part.trim());
        if (name && hex) colors[name.toLowerCase()] = hex;
      });
    } catch (error) {
      /* couleurs facultatives */
    }

    const render = () => {
      const value = input.value.trim();
      setSealText(seal, value || root.dataset.placeholder);
      seal.classList.toggle('is-placeholder', !value);
      count.textContent = input.value.length;
      if (value) input.setCustomValidity('');
    };
    const setColor = (name) => {
      const hex = name && colors[name.toLowerCase()];
      if (hex && hex.startsWith('#')) seal.style.setProperty('--wax', hex);
    };

    input.addEventListener('input', render);
    input.addEventListener('invalid', () => {
      if (!input.value.trim()) input.setCustomValidity(input.dataset.message);
    });
    render();

    if (colorIndex >= 0) {
      const checked = document.querySelector(`input[type="radio"][form="${input.getAttribute('form')}"]:checked`);
      if (checked) setColor(checked.value);
      document.addEventListener('change', (event) => {
        const option = optionFromEvent(event.target);
        if (option && option.name && option.name.toLowerCase().includes('couleur')) setColor(option.value);
      });
      onVariantChange((data) => data.variant && setColor(data.variant.options[colorIndex]));
    }

    /* Ajout au panier sans initiales : on ramène la cliente vers le champ. */
    document.addEventListener(
      'click',
      (event) => {
        const button = event.target.closest(`#${input.getAttribute('form')} [type="submit"]`);
        if (!button || input.value.trim()) return;
        event.preventDefault();
        input.setCustomValidity(input.dataset.message);
        input.scrollIntoView({ behavior: 'smooth', block: 'center' });
        input.focus({ preventScroll: true });
        input.reportValidity();
      },
      true
    );
  });
})();
