// Menu mobile
const header = document.querySelector('.site-header');
const menuBtn = document.querySelector('.menu-btn');
if (menuBtn) {
  const close = () => { header.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false'); };
  menuBtn.addEventListener('click', () => {
    const open = header.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', String(open));
  });
  document.querySelectorAll('.nav-panel a[href^="#"]').forEach((a) => a.addEventListener('click', close));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && header.classList.contains('open')) { close(); menuBtn.focus(); }
  });
}

// Section courante dans la navigation
const links = [...document.querySelectorAll('.nav-links a')];
if (links.length && 'IntersectionObserver' in window) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      links.forEach((a) => {
        if (a.getAttribute('href') === '#' + e.target.id) a.setAttribute('aria-current', 'true');
        else a.removeAttribute('aria-current');
      });
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  links.forEach((a) => { const s = document.querySelector(a.getAttribute('href')); if (s) spy.observe(s); });
}

// Copie de l'adresse email, annoncée aux lecteurs d'écran
document.querySelectorAll('.copy').forEach((btn) => {
  const status = btn.parentElement.querySelector('[data-copy-status]');
  const label = btn.firstChild.textContent;
  btn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(btn.dataset.copy);
      status.textContent = btn.dataset.ok;
      btn.firstChild.textContent = '✓ ';
    } catch {
      status.textContent = btn.dataset.fail;
    }
    setTimeout(() => { btn.firstChild.textContent = label; status.textContent = ''; }, 2500);
  });
});
