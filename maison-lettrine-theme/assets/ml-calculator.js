/* Maison Lettrine – calculateur de cire (accueil). Aucune dépendance. */
if (!customElements.get('ml-calculator')) {
  customElements.define(
    'ml-calculator',
    class MlCalculator extends HTMLElement {
      connectedCallback() {
        this.strings = JSON.parse(this.querySelector('[data-calc-strings]').textContent);
        this.chips = Array.from(this.querySelectorAll('.ml-chip'));
        this.input = this.querySelector('[data-calc-input]');

        this.chips.forEach((chip) =>
          chip.addEventListener('click', () => {
            this.input.value = '';
            this.select(chip);
            this.update(parseInt(chip.dataset.value, 10));
          })
        );
        this.input.addEventListener('input', () => {
          const value = parseInt(this.input.value, 10);
          this.select(null);
          if (value > 0) this.update(Math.min(value, 2000));
        });

        const start = this.chips.find((chip) => chip.getAttribute('aria-pressed') === 'true') || this.chips[0];
        if (start) this.update(parseInt(start.dataset.value, 10));
      }

      select(active) {
        this.chips.forEach((chip) => chip.setAttribute('aria-pressed', chip === active ? 'true' : 'false'));
      }

      format(template, values) {
        return Object.keys(values).reduce((text, key) => text.split(`[${key}]`).join(values[key]), template);
      }

      update(envelopes) {
        const d = this.dataset;
        const beads = Math.ceil(envelopes * Number(d.perSeal) * (1 + Number(d.margin) / 100));
        const boxes = Math.ceil(beads / Number(d.perBox));
        const large = envelopes > Number(d.threshold);
        const included = Number(large ? d.largeBeads : d.smallBeads);
        const refills = Math.max(0, Math.ceil((beads - included) / Number(d.refillBeads)));

        this.querySelector('[data-calc-beads]').textContent = beads;
        this.querySelector('[data-calc-boxes]').textContent = boxes;
        this.querySelector('[data-calc-summary]').textContent = this.format(this.strings.summary, {
          envelopes,
          beads,
          boxes,
        });

        const link = this.querySelector(`[data-calc-product="${large ? 'large' : 'small'}"]`);
        this.querySelectorAll('[data-calc-product]').forEach((el) => (el.hidden = el !== link));
        const title = link ? link.dataset.title : '';
        let advice = this.format(large ? this.strings.adviceLarge : this.strings.adviceSmall, { title });
        if (refills > 0) {
          const refillText = this.format(refills === 1 ? this.strings.refillOne : this.strings.refillMany, {
            count: refills,
          });
          advice += ' ' + this.format(this.strings.adviceRefills, { refills: refillText });
        }
        this.querySelector('[data-calc-advice]').textContent = advice;

        const form = this.querySelector('[data-calc-refill]');
        if (form) {
          form.hidden = refills === 0;
          form.querySelector('[data-calc-qty]').value = refills || 1;
          form.querySelector('[data-calc-refill-label]').textContent =
            refills === 1 ? this.strings.addOne : this.format(this.strings.addMany, { count: refills });
        }
      }
    }
  );
}
