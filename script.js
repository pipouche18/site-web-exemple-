// Horaires d'ouverture (0 = dimanche). Chaque plage : [ouverture, fermeture] en heures décimales.
const HOURS = {
  0: [[7, 13.5]],
  1: [[6.5, 19.5]],
  2: [[6.5, 19.5]],
  3: [],
  4: [[6.5, 19.5]],
  5: [[6.5, 19.5]],
  6: [[7, 19.5]],
};

const formatHour = (h) => {
  const min = Math.round((h % 1) * 60);
  return `${Math.floor(h)}h${min ? String(min).padStart(2, "0") : ""}`;
};

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

// Ombre du header au défilement
const header = document.getElementById("header");
const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 10);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

// Statut « ouvert / fermé » et jour en cours dans le tableau
function updateStatus() {
  const now = new Date();
  const day = now.getDay();
  const time = now.getHours() + now.getMinutes() / 60;
  const status = document.getElementById("openStatus");

  document.querySelectorAll("#hours tr").forEach((row) => {
    row.classList.toggle("is-today", Number(row.dataset.day) === day);
  });

  const current = HOURS[day].find(([open, close]) => time >= open && time < close);
  if (current) {
    status.textContent = `Ouvert maintenant · jusqu'à ${formatHour(current[1])}`;
    status.classList.add("is-open");
    return;
  }

  status.classList.remove("is-open");
  const laterToday = HOURS[day].find(([open]) => time < open);
  if (laterToday) {
    status.textContent = `Fermé · ouvre aujourd'hui à ${formatHour(laterToday[0])}`;
    return;
  }
  const days = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
  for (let i = 1; i <= 7; i++) {
    const d = (day + i) % 7;
    if (HOURS[d].length) {
      const when = i === 1 ? "demain" : days[d];
      status.textContent = `Fermé · ouvre ${when} à ${formatHour(HOURS[d][0][0])}`;
      return;
    }
  }
}
updateStatus();
setInterval(updateStatus, 60 * 1000);

// Filtres produits
const tabs = document.querySelectorAll(".tab");
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => {
      t.classList.toggle("is-active", t === tab);
      t.setAttribute("aria-selected", String(t === tab));
    });
    const filter = tab.dataset.filter;
    document.querySelectorAll(".product").forEach((p) => {
      p.classList.toggle("is-hidden", filter !== "all" && p.dataset.cat !== filter);
    });
  });
});

// Formulaire de contact (démonstration : pas d'envoi réel)
const form = document.getElementById("contactForm");
const formMsg = document.getElementById("formMsg");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const missing = [...form.querySelectorAll("[required]")].filter((f) => !f.value.trim());
  if (missing.length) {
    formMsg.textContent = "Merci de remplir tous les champs.";
    formMsg.className = "form__msg is-error";
    missing[0].focus();
    return;
  }
  formMsg.textContent = "Merci ! Votre demande a bien été envoyée, nous vous rappelons rapidement.";
  formMsg.className = "form__msg is-ok";
  form.reset();
});

// Apparition des sections au défilement
const revealTargets = document.querySelectorAll(".feature, .about__grid > *, .section__head, .product, .review, .infos__grid > *, .contact__grid > *");
revealTargets.forEach((el) => el.classList.add("reveal"));
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealTargets.forEach((el) => io.observe(el));
} else {
  revealTargets.forEach((el) => el.classList.add("is-visible"));
}

document.getElementById("year").textContent = new Date().getFullYear();
