// Bandeau de démonstration
document.getElementById("demoClose")?.addEventListener("click", () => {
  document.getElementById("demoBanner").remove();
});

// Menu mobile
const burger = document.getElementById("burger");
const nav = document.getElementById("nav");
const toggleMenu = (open) => {
  burger.setAttribute("aria-expanded", String(open));
  burger.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
  nav.classList.toggle("is-open", open);
};
burger.addEventListener("click", () => toggleMenu(!nav.classList.contains("is-open")));
nav.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => toggleMenu(false)));
document.addEventListener("keydown", (e) => e.key === "Escape" && toggleMenu(false));

// Header au défilement
const header = document.getElementById("header");
const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 10);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

// Stock : filtres par catégorie et tri
const carsGrid = document.getElementById("cars");
const cars = [...carsGrid.querySelectorAll(".car")];
const emptyMsg = document.getElementById("carsEmpty");
const tabs = document.querySelectorAll(".tab");

const applyFilter = (filter) => {
  let visible = 0;
  cars.forEach((car) => {
    const show = filter === "all" || car.dataset.cat === filter;
    car.classList.toggle("is-hidden", !show);
    if (show) visible++;
  });
  emptyMsg.hidden = visible > 0;
};

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => {
      t.classList.toggle("is-active", t === tab);
      t.setAttribute("aria-pressed", String(t === tab));
    });
    applyFilter(tab.dataset.filter);
  });
});

document.getElementById("sort").addEventListener("change", (e) => {
  const [key, dir] = e.target.value.split("-");
  const sorted = key === "default"
    ? cars
    : [...cars].sort((a, b) => (Number(a.dataset[key]) - Number(b.dataset[key])) * (dir === "desc" ? -1 : 1));
  sorted.forEach((car) => carsGrid.appendChild(car));
});

// « Je suis intéressé » : pré-remplit le véhicule dans le formulaire de contact
const contactCar = document.getElementById("contactCar");
document.querySelectorAll(".car__link").forEach((link) => {
  link.addEventListener("click", () => {
    contactCar.value = link.dataset.car;
  });
});

// Formulaires (démonstration : pas d'envoi réel)
const handleForm = (form, successText) => {
  const msg = form.querySelector(".form__msg");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const fields = [...form.querySelectorAll("[required]")];
    fields.forEach((f) => f.classList.remove("is-invalid"));
    const invalid = fields.filter((f) => !f.value.trim() || !f.checkValidity());
    if (invalid.length) {
      invalid.forEach((f) => f.classList.add("is-invalid"));
      msg.textContent = "Merci de compléter correctement les champs indiqués.";
      msg.className = "form__msg is-error";
      invalid[0].focus();
      return;
    }
    msg.textContent = successText;
    msg.className = "form__msg is-ok";
    form.reset();
  });
};
handleForm(document.getElementById("estimateForm"), "Merci ! Vous recevrez notre offre sous 24 h.");
handleForm(document.getElementById("contactForm"), "Message envoyé. Nous revenons vers vous rapidement.");

// Apparition des éléments au défilement
const revealTargets = document.querySelectorAll(".section__head, .car, .rachat > *, .service, .review, .contact > *");
if ("IntersectionObserver" in window) {
  revealTargets.forEach((el) => el.classList.add("reveal"));
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  revealTargets.forEach((el) => io.observe(el));
}

document.getElementById("year").textContent = new Date().getFullYear();
