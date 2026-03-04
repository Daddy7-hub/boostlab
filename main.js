// BoostLab — main.js
// Requires: i18n.js loaded first (provides T object)

(function() {
    'use strict';

    // === LANGUAGE SWITCHING ===
    let currentLang = 'en';

    function setLang(lang) {
        if (!T[lang]) return;
        currentLang = lang;
        document.documentElement.lang = lang === 'et' ? 'et' : lang === 'ru' ? 'ru' : 'en';

        // Update all [data-i] elements (text content)
        document.querySelectorAll('[data-i]').forEach(function(el) {
            var key = el.getAttribute('data-i');
            if (T[lang][key]) el.textContent = T[lang][key];
        });

        // Update all [data-ih] elements (innerHTML — for spans inside)
        document.querySelectorAll('[data-ih]').forEach(function(el) {
            var key = el.getAttribute('data-ih');
            if (T[lang][key]) el.innerHTML = T[lang][key];
        });

        // Update lang buttons
        document.querySelectorAll('.lang-btn').forEach(function(btn) {
            btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
        });

        // Update page title
        var titles = {
            en: 'BoostLab | Web Development, Apps, Digital Marketing | Estonia',
            et: 'BoostLab | Veebiarendus, rakendused, digiturundus | Eesti',
            ru: 'BoostLab | Разработка сайтов, приложений, маркетинг | Эстония'
        };
        document.title = titles[lang] || titles.en;

        // Update meta description
        var descs = {
            en: 'BoostLab - full-cycle digital agency in Estonia. Custom websites, mobile apps, turnkey platforms, Google Ads, SMM and technical support.',
            et: 'BoostLab - taisteenuse digiagentuur Eestis. Veebilehed, mobiilirakendused, platvormid, Google Ads, SMM ja tehniline tugi.',
            ru: 'BoostLab - digital-агентство полного цикла в Эстонии. Сайты, приложения, платформы под ключ, Google Ads, SMM и техподдержка.'
        };
        var metaDesc = document.querySelector('meta[name="description"]');
        if (metaDesc) metaDesc.setAttribute('content', descs[lang] || descs.en);

        // Recalculate calculator
        calcUpdate();
    }

    // Bind all lang buttons
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('lang-btn')) {
            var lang = e.target.getAttribute('data-lang');
            if (lang) setLang(lang);
        }
    });

    // === BURGER MENU ===
    var burger = document.getElementById('burger');
    var mobMenu = document.getElementById('mobMenu');
    if (burger && mobMenu) {
        burger.addEventListener('click', function() {
            mobMenu.classList.toggle('open');
        });
        mobMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                mobMenu.classList.remove('open');
            });
        });
    }

    // === SCROLL REVEAL ===
    var reveals = document.querySelectorAll('.reveal');

    if ('IntersectionObserver' in window) {
        var revealObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' });

        reveals.forEach(function(el) {
            revealObserver.observe(el);
        });
    } else {
        // Fallback: show everything immediately
        reveals.forEach(function(el) {
            el.classList.add('visible');
        });
    }

    // Safety net: if after 2 seconds elements are still hidden, force show
    setTimeout(function() {
        document.querySelectorAll('.reveal:not(.visible)').forEach(function(el) {
            el.classList.add('visible');
        });
    }, 2000);

    // === CALCULATOR ===
    function setupCalcOptions(containerId) {
        var container = document.getElementById(containerId);
        if (!container) return;
        container.querySelectorAll('.calc-opt').forEach(function(btn) {
            btn.addEventListener('click', function() {
                container.querySelectorAll('.calc-opt').forEach(function(b) { b.classList.remove('selected'); });
                btn.classList.add('selected');
                calcUpdate();
            });
        });
    }

    function setupCalcChecks(containerId) {
        var container = document.getElementById(containerId);
        if (!container) return;
        container.querySelectorAll('.calc-check').forEach(function(label) {
            label.addEventListener('click', function() {
                var input = label.querySelector('input');
                if (input) {
                    input.checked = !input.checked;
                    label.classList.toggle('checked', input.checked);
                }
                calcUpdate();
            });
        });
    }

    function calcUpdate() {
        var total = 0;

        // Get selected option values from each group
        ['calcType', 'calcDesign', 'calcMkt'].forEach(function(id) {
            var container = document.getElementById(id);
            if (!container) return;
            var selected = container.querySelector('.calc-opt.selected');
            if (selected) total += parseInt(selected.getAttribute('data-v')) || 0;
        });

        // Get checked checkboxes
        ['calcAddons', 'calcMobile'].forEach(function(id) {
            var container = document.getElementById(id);
            if (!container) return;
            container.querySelectorAll('input[type="checkbox"]:checked').forEach(function(input) {
                total += parseInt(input.getAttribute('data-v')) || 0;
            });
        });

        // Update display
        var display = document.getElementById('calcTotal');
        if (display) {
            display.textContent = '\u20AC' + total.toLocaleString('en-US');
        }
    }

    setupCalcOptions('calcType');
    setupCalcOptions('calcDesign');
    setupCalcOptions('calcMkt');
    setupCalcChecks('calcAddons');
    setupCalcChecks('calcMobile');
    calcUpdate();

    // === COOKIE BANNER ===
    var cookieBanner = document.getElementById('cookieBanner');
    var cookieAccept = document.getElementById('cookieAccept');
    var cookieDecline = document.getElementById('cookieDecline');

    if (cookieBanner && cookieAccept && cookieDecline) {
        cookieAccept.addEventListener('click', function() {
            cookieBanner.classList.add('hidden');
        });
        cookieDecline.addEventListener('click', function() {
            cookieBanner.classList.add('hidden');
        });
    }

    // === NAV SCROLL EFFECT ===
    var nav = document.querySelector('nav');
    if (nav) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                nav.style.boxShadow = '0 2px 20px rgba(0,0,0,0.06)';
            } else {
                nav.style.boxShadow = 'none';
            }
        });
    }

    // === SMOOTH SCROLL FOR ANCHOR LINKS ===
    document.querySelectorAll('a[href^="#"]').forEach(function(link) {
        link.addEventListener('click', function(e) {
            var target = document.querySelector(link.getAttribute('href'));
            if (target) {
                e.preventDefault();
                var offset = 80; // nav height
                var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
                window.scrollTo({ top: top, behavior: 'smooth' });
            }
        });
    });

})();