const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const root = document.documentElement;
document.getElementById('y').textContent = new Date().getFullYear();

// Apparition des blocs au défilement (cartes, chiffres, sections)
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add('is-in');
    if (e.target.matches('.stats > li')) countUp(e.target);
    io.unobserve(e.target);
  });
}, { threshold: 0.18 });
document.querySelectorAll('.card, .stats > li, .reveal, .row, .skill').forEach((el) => {
  const siblings = [...el.parentElement.children];
  el.style.setProperty('--delay', (siblings.indexOf(el) % 6) * 90 + 'ms');
  io.observe(el);
});

// Chiffres qui défilent jusqu'à leur valeur
function countUp(li) {
  li.querySelectorAll('[data-count]').forEach((n) => {
    const to = +n.dataset.count, from = +(n.dataset.from || 0);
    if (reduce) return;
    const t0 = performance.now(), dur = 1400;
    const tick = (t) => {
      const k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      n.textContent = Math.round(from + (to - from) * e);
      if (k < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  });
}

// Titres de section : effet « décodage » des lettres à l'apparition
const glyphs = '01ABCDEF#$%&/<>';
function scramble(el) {
  if (reduce) return;
  const node = [...el.childNodes].find((n) => n.nodeType === 3 && n.textContent.trim());
  if (!node) return;
  const final = node.textContent;
  let frame = 0;
  const total = final.length * 3;
  const id = setInterval(() => {
    node.textContent = final.split('').map((c, i) => (i < frame / 3 ? c : c === ' ' ? ' ' : glyphs[(Math.random() * glyphs.length) | 0])).join('');
    if (++frame > total) { node.textContent = final; clearInterval(id); }
  }, 28);
}
const hio = new IntersectionObserver((entries) => {
  entries.forEach((e) => { if (e.isIntersecting) { scramble(e.target); hio.unobserve(e.target); } });
}, { threshold: 0.6 });
document.querySelectorAll('.sec-head h2').forEach((h) => {
  h.setAttribute('aria-label', h.textContent.replace('/', '').trim());
  hio.observe(h);
});

// Cartes projets : inclinaison 3D qui suit la souris
if (!reduce && matchMedia('(hover: hover)').matches) {
  document.querySelectorAll('.card').forEach((card) => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
      card.style.setProperty('--rx', (-y * 8).toFixed(2) + 'deg');
      card.style.setProperty('--ry', (x * 10).toFixed(2) + 'deg');
      card.style.setProperty('--gx', (x + 0.5) * 100 + '%');
      card.style.setProperty('--gy', (y + 0.5) * 100 + '%');
    });
    card.addEventListener('pointerleave', () => { card.style.removeProperty('--rx'); card.style.removeProperty('--ry'); });
  });

  // Pièces du hero : parallaxe légère à la souris + halo qui suit le curseur
  const hero = document.querySelector('.hero');
  hero.addEventListener('pointermove', (e) => {
    const r = hero.getBoundingClientRect();
    hero.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100).toFixed(1) + '%');
    hero.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100).toFixed(1) + '%');
    hero.style.setProperty('--px', ((e.clientX - r.left) / r.width - 0.5).toFixed(3));
    hero.style.setProperty('--py', ((e.clientY - r.top) / r.height - 0.5).toFixed(3));
  });

  // Boutons « aimantés »
  document.querySelectorAll('.cta .btn, .btn-arrow').forEach((b) => {
    b.addEventListener('pointermove', (e) => {
      const r = b.getBoundingClientRect();
      b.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * 0.15}px, ${(e.clientY - r.top - r.height / 2) * 0.25}px)`;
    });
    b.addEventListener('pointerleave', () => { b.style.transform = ''; });
  });
}

// Section active dans la navigation
const nav = document.querySelector('.top nav');
const links = [...nav.querySelectorAll('a')];
const spy = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (!e.isIntersecting) return;
    links.forEach((a) => {
      const on = a.getAttribute('href') === '#' + e.target.id;
      a.classList.toggle('active', on);
      on ? a.setAttribute('aria-current', 'true') : a.removeAttribute('aria-current');
      // Sur mobile, la navigation défile pour garder la section active visible
      if (on && nav.scrollWidth > nav.clientWidth) nav.scrollTo({ left: a.offsetLeft - 24, behavior: reduce ? 'auto' : 'smooth' });
    });
  });
}, { rootMargin: '-45% 0px -50% 0px' });
document.querySelectorAll('main section[id]').forEach((s) => spy.observe(s));

// Barre de progression + en-tête compact au défilement
const bar = document.querySelector('.progress');
const topBar = document.querySelector('.top');
const toTop = document.querySelector('.to-top');
const onScroll = () => {
  const d = document.documentElement;
  const p = d.scrollTop / (d.scrollHeight - d.clientHeight || 1);
  bar.style.transform = `scaleX(${p})`;
  topBar.classList.toggle('scrolled', d.scrollTop > 40);
  toTop.style.setProperty('--p', p.toFixed(3));
  toTop.classList.toggle('show', d.scrollTop > innerHeight);
};
addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Copier l'email
document.querySelectorAll('.copy').forEach((b) => b.addEventListener('click', async () => {
  const etat = document.getElementById('copy-etat');
  try { await navigator.clipboard.writeText(b.dataset.copy); etat.textContent = 'Adresse email copiée.'; b.firstChild.textContent = 'COPIÉ ✓ '; }
  catch { etat.textContent = 'La copie a échoué, sélectionnez l\'adresse manuellement.'; b.firstChild.textContent = 'ÉCHEC '; }
  setTimeout(() => { b.firstChild.textContent = 'COPIER '; etat.textContent = ''; }, 2500);
}));

// Pause / lecture de toutes les animations en boucle (bandeau, pièces) — WCAG 2.2.2
const toggles = document.querySelectorAll('.anim-toggle');
const setPaused = (p) => {
  root.classList.toggle('anim-paused', p);
  toggles.forEach((t) => { t.setAttribute('aria-pressed', p); t.firstChild.textContent = p ? 'LECTURE ' : 'PAUSE '; });
};
if (reduce) setPaused(true);
toggles.forEach((t) => t.addEventListener('click', () => setPaused(!root.classList.contains('anim-paused'))));

// Version PDF via l'impression du navigateur
document.getElementById('print').addEventListener('click', () => window.print());
