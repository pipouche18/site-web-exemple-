/* Maison Lettrine – ajout au panier en un clic (recharge suggérée, calculateur).
   Ouvre le panier latéral de Dawn ; sans panier latéral, envoi classique du formulaire. */
document.addEventListener('submit', async (event) => {
  const form = event.target.closest('[data-ml-add-form]');
  if (!form) return;
  const drawer = document.querySelector('cart-drawer');
  if (!drawer || typeof drawer.renderContents !== 'function') return;

  event.preventDefault();
  const button = form.querySelector('[type="submit"]');
  button.setAttribute('aria-busy', 'true');
  button.disabled = true;

  try {
    const body = new FormData(form);
    body.append('sections', drawer.getSectionsToRender().map((section) => section.id).join(','));
    body.append('sections_url', window.location.pathname);
    const response = await fetch(window.routes.cart_add_url, {
      method: 'POST',
      headers: { 'X-Requested-With': 'XMLHttpRequest', Accept: 'application/javascript' },
      body,
    });
    const state = await response.json();
    if (state.status) throw new Error(state.description);
    drawer.classList.remove('is-empty');
    drawer.renderContents(state);
    if (typeof publish === 'function' && typeof PUB_SUB_EVENTS !== 'undefined') {
      publish(PUB_SUB_EVENTS.cartUpdate, { source: 'ml-add-form', productVariantId: body.get('id'), cartData: state });
    }
  } catch (error) {
    form.submit();
  } finally {
    button.removeAttribute('aria-busy');
    button.disabled = false;
  }
});
