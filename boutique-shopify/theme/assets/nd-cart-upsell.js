/* Ajout en un clic du produit suggéré dans le panier latéral. */
document.addEventListener('submit', async (event) => {
  const form = event.target.closest('[data-nd-upsell-form]');
  const drawer = document.querySelector('cart-drawer');
  if (!form || !drawer || typeof drawer.renderContents !== 'function') return;
  event.preventDefault();
  const button = form.querySelector('button');
  button.setAttribute('aria-busy', 'true');
  button.disabled = true;
  try {
    const body = new FormData(form);
    body.append('sections', drawer.getSectionsToRender().map((s) => s.id).join(','));
    body.append('sections_url', window.location.pathname);
    const response = await fetch(`${window.routes.cart_add_url}`, {
      method: 'POST',
      headers: { 'X-Requested-With': 'XMLHttpRequest', Accept: 'application/javascript' },
      body,
    });
    const state = await response.json();
    if (state.status) throw new Error(state.description);
    drawer.renderContents(state);
  } catch (e) {
    form.submit();
  }
});
