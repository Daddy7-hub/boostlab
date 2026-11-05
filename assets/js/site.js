// BoostLab: mobile menu, header border, hero entrance, consent mode, lead tracking.
(function () {
  var d = document, root = d.documentElement;
  root.classList.remove('no-js');
  root.classList.add('js');
  requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('ready'); }); });

  var hdr = d.querySelector('.hdr');
  var onScroll = function () { hdr && hdr.classList.toggle('scrolled', scrollY > 8); };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var burger = d.querySelector('.burger');
  var closeNav = function () { root.classList.remove('nav-open'); burger && burger.setAttribute('aria-expanded', 'false'); };
  burger && burger.addEventListener('click', function () {
    var open = root.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  d.querySelectorAll('.drawer a').forEach(function (a) { a.addEventListener('click', closeNav); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') closeNav(); });

  // consent (Consent Mode v2; Meta pixel only after opt-in)
  var ck = d.querySelector('.ck'), KEY = 'bl_consent';
  function getC() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setC(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function grant() {
    if (window.gtag) gtag('consent', 'update', { ad_storage: 'granted', analytics_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted' });
    if (window.BL_PIXEL && !window.fbq) {
      !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(window, d, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', window.BL_PIXEL); fbq('track', 'PageView');
    }
  }
  var c = getC();
  if (c === 'yes') grant();
  else if (!c && ck) setTimeout(function () { ck.classList.add('show'); }, 1500);
  if (ck) {
    ck.querySelector('.ok').addEventListener('click', function () { setC('yes'); grant(); ck.classList.remove('show'); });
    ck.querySelector('.no').addEventListener('click', function () { setC('no'); ck.classList.remove('show'); });
  }

  d.querySelectorAll('a[href^="mailto:"],a[href^="tel:"]').forEach(function (a) {
    a.addEventListener('click', function () {
      if (!window.gtag) return;
      var m = a.href.split(':')[0] === 'tel' ? 'phone' : 'email';
      gtag('event', 'generate_lead', { method: m });
      var lbl = (window.BL_ADS || {})[m];
      if (lbl) gtag('event', 'conversion', { send_to: lbl });
    });
  });
})();
