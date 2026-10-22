// BoostLab site behaviour: preloader, smooth scroll, scroll-driven scenes, consent.
(function () {
  var d = document, root = d.documentElement;
  root.classList.remove('no-js');
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- preloader ----------
  var pre = d.querySelector('.pre'), bar = pre && pre.querySelector('.pre-bar i');
  var stage = d.querySelector('.stage');
  var ready = false;
  function finish() {
    if (ready) return; ready = true;
    if (bar) bar.style.width = '100%';
    setTimeout(function () { pre && pre.classList.add('done'); d.body.classList.add('loaded'); intro(); }, 350);
  }
  if (pre) {
    var w = 0, ti = setInterval(function () { w = Math.min(88, w + 7 + Math.random() * 9); bar.style.width = w + '%'; if (ready) clearInterval(ti); }, 160);
    if (stage) {
      addEventListener('scene:ready', finish);
      setTimeout(finish, 4500); // never block content
    } else addEventListener('load', finish);
    setTimeout(finish, 6000);
  } else setTimeout(intro, 0); // after the observers below are defined

  // ---------- smooth scroll ----------
  var lenis = null;
  if (!reduced && window.Lenis) {
    lenis = new Lenis({ duration: 1.15, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); } });
    (function raf(t) { lenis.raf(t); requestAnimationFrame(raf); })(0);
    d.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var id = a.getAttribute('href'); if (id.length < 2) return;
        var el = d.querySelector(id); if (!el) return;
        e.preventDefault(); closeNav(); lenis.scrollTo(el, { offset: -70 });
      });
    });
  }

  // ---------- header ----------
  var hdr = d.querySelector('.hdr'), lastY = 0;
  function onScroll() {
    var y = scrollY;
    hdr.classList.toggle('scrolled', y > 40);
    hdr.classList.toggle('hide', y > 300 && y > lastY && !root.classList.contains('nav-open'));
    lastY = y;
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var burger = d.querySelector('.burger');
  function closeNav() { root.classList.remove('nav-open'); burger && burger.setAttribute('aria-expanded', 'false'); lenis && lenis.start(); }
  burger && burger.addEventListener('click', function () {
    var open = root.classList.toggle('nav-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (lenis) open ? lenis.stop() : lenis.start();
  });
  d.querySelectorAll('.drawer a').forEach(function (a) { a.addEventListener('click', closeNav); });

  // ---------- split headings into masked words ----------
  d.querySelectorAll('[data-split]').forEach(function (el) {
    var walk = function (node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = d.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(d.createTextNode(' ')); return; }
            var w = d.createElement('span'); w.className = 'w';
            var i = d.createElement('span'); i.textContent = part; w.appendChild(i); frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
      });
    };
    walk(el); el.classList.add('split');
    var k = 0; el.querySelectorAll('.w>span').forEach(function (s) { s.style.transitionDelay = (k++ * 0.06) + 's'; });
  });
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px 12% 0px' });
  function intro() {
    d.querySelectorAll('[data-split],.fade').forEach(function (el) {
      if (el.closest('.sc-hero')) { el.classList.add('in'); return; }
      io.observe(el);
    });
  }

  // ---------- 3D stage: scroll progress + copy phases ----------
  if (stage) {
    var copies = stage.querySelectorAll('.sc'), dots = stage.querySelectorAll('.steps-bar span');
    // [in-start, in-end, out-start, out-end] per caption: hero, reveal, screen labels, numbers - no empty gaps
    var phases = [[-1, 0, 0.14, 0.21], [0.19, 0.26, 0.5, 0.56], [0.54, 0.6, 0.79, 0.84], [0.82, 0.88, 2, 3]];
    var upd = function () {
      var r = stage.getBoundingClientRect();
      var total = stage.offsetHeight - innerHeight;
      var p = Math.min(1, Math.max(0, -r.top / total));
      window.__stageP = p;
      copies.forEach(function (c, i) {
        var ph = phases[i]; if (!ph) return;
        var o = p < ph[0] ? 0 : p < ph[1] ? (p - ph[0]) / (ph[1] - ph[0]) : p < ph[2] ? 1 : p < ph[3] ? 1 - (p - ph[2]) / (ph[3] - ph[2]) : 0;
        if (i === 0 && p <= ph[1]) o = 1;
        c.style.opacity = o.toFixed(3);
        c.style.transform = 'translateY(' + ((1 - o) * (p > (ph[1] + ph[2]) / 2 ? -30 : 30)).toFixed(1) + 'px)';
        c.style.visibility = o < 0.01 ? 'hidden' : 'visible';
      });
      var idx = p < 0.2 ? 0 : p < 0.82 ? 1 : 2;
      dots.forEach(function (dt, i) { dt.classList.toggle('on', i === idx); });
    };
    addEventListener('scroll', upd, { passive: true }); addEventListener('resize', upd); upd();
    if (lenis) lenis.on('scroll', upd);
  }

  // ---------- parallax photo bands ----------
  var bands = d.querySelectorAll('[data-parallax]');
  if (bands.length && !reduced) {
    var par = function () {
      bands.forEach(function (b) {
        var r = b.parentNode.getBoundingClientRect();
        if (r.bottom < 0 || r.top > innerHeight) return;
        var k = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
        b.style.transform = 'translate3d(0,' + (k * -12).toFixed(2) + '%,0) scale(1.18)';
      });
    };
    addEventListener('scroll', par, { passive: true }); par();
  }

  // ---------- count-up numbers ----------
  var cio = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return; cio.unobserve(e.target);
      var el = e.target, to = parseFloat(el.dataset.count), suf = el.dataset.suf || '', pre = el.dataset.pre || '', t0 = performance.now();
      var dec = (el.dataset.count.split('.')[1] || '').length;
      (function step(now) {
        var k = Math.min(1, (now - t0) / 1600); k = 1 - Math.pow(1 - k, 4);
        el.textContent = pre + (to * k).toLocaleString(d.documentElement.lang, { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
        if (k < 1) requestAnimationFrame(step);
      })(t0);
    });
  }, { threshold: 0.6 });
  if (!reduced) d.querySelectorAll('[data-count]').forEach(function (el) { cio.observe(el); });

  // ---------- cursor ----------
  var cur = d.querySelector('.cur');
  if (cur && matchMedia('(hover:hover) and (pointer:fine)').matches) {
    var cx = 0, cy = 0, x = 0, y = 0;
    addEventListener('pointermove', function (e) { cx = e.clientX; cy = e.clientY; }, { passive: true });
    (function loop() { x += (cx - x) * 0.2; y += (cy - y) * 0.2; cur.style.transform = 'translate(' + x + 'px,' + y + 'px)'; requestAnimationFrame(loop); })();
    d.querySelectorAll('a,button,summary').forEach(function (el) {
      el.addEventListener('pointerenter', function () { cur.classList.add('big'); });
      el.addEventListener('pointerleave', function () { cur.classList.remove('big'); });
    });
  }

  // ---------- consent (Consent Mode v2; Meta pixel only after opt-in) ----------
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
  else if (!c && ck) setTimeout(function () { ck.classList.add('show'); }, 2200);
  if (ck) {
    ck.querySelector('.ok').addEventListener('click', function () { setC('yes'); grant(); ck.classList.remove('show'); });
    ck.querySelector('.no').addEventListener('click', function () { setC('no'); ck.classList.remove('show'); });
  }

  // track contact intent
  d.querySelectorAll('a[href^="mailto:"],a[href^="tel:"]').forEach(function (a) {
    a.addEventListener('click', function () { window.gtag && gtag('event', 'generate_lead', { method: a.href.split(':')[0] }); });
  });
})();
