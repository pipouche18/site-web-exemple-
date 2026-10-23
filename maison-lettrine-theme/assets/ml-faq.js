/* Maison Lettrine – filtres de la FAQ par catégorie. */
if (!customElements.get('ml-faq')) {
  customElements.define(
    'ml-faq',
    class MlFaq extends HTMLElement {
      connectedCallback() {
        this.buttons = Array.from(this.querySelectorAll('[data-filter]'));
        this.buttons.forEach((button) => button.addEventListener('click', () => this.filter(button)));
      }

      filter(active) {
        const value = active.dataset.filter;
        this.buttons.forEach((button) => button.setAttribute('aria-pressed', button === active ? 'true' : 'false'));
        this.querySelectorAll('[data-category]').forEach((el) => {
          el.hidden = value !== 'all' && el.dataset.category !== value;
        });
      }
    }
  );
}
