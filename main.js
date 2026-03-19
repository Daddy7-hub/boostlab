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

        // Update page title & meta description per page
        var page = document.body.getAttribute('data-page') || 'home';
        var pageTitles = {
            home: { en: 'BoostLab | Web Development, Apps, Digital Marketing | Estonia', et: 'BoostLab | Veebiarendus, rakendused, digiturundus | Eesti', ru: 'BoostLab | Разработка сайтов, приложений, маркетинг | Эстония' },
            'web-development': { en: 'Website Development Estonia, Latvia, Lithuania | BoostLab', et: 'Veebiarendus Eestis, Lätis, Leedus | BoostLab', ru: 'Создание сайтов Эстония, Латвия, Литва | BoostLab' },
            'mobile-apps': { en: 'Mobile App Development iOS & Android | BoostLab Estonia', et: 'Mobiilirakenduste arendus iOS & Android | BoostLab', ru: 'Разработка мобильных приложений iOS и Android | BoostLab' },
            'smm-marketing': { en: 'SMM & Content Marketing Estonia, Latvia, Lithuania | BoostLab', et: 'SMM ja sisuturundus Eestis, Lätis, Leedus | BoostLab', ru: 'SMM и контент-маркетинг Эстония, Латвия, Литва | BoostLab' },
            advertising: { en: 'Google Ads & PPC Advertising Estonia | BoostLab', et: 'Google Ads ja PPC reklaam Eestis | BoostLab', ru: 'Реклама Google Ads и PPC Эстония | BoostLab' },
            platforms: { en: 'Turnkey Platform Development | BoostLab Estonia', et: 'Võtmed kätte platvormide arendus | BoostLab', ru: 'Разработка платформ под ключ | BoostLab Эстония' },
            pricing: { en: 'Pricing — Web Development & Marketing | BoostLab', et: 'Hinnad — Veebiarendus ja turundus | BoostLab', ru: 'Цены — Разработка сайтов и маркетинг | BoostLab' },
            portfolio: { en: 'Portfolio — Digital Agency Projects | BoostLab Estonia', et: 'Portfoolio — Digiagentuur | BoostLab', ru: 'Портфолио — Проекты digital-агентства | BoostLab' }
        };
        var pageDescs = {
            home: { en: 'BoostLab - full-cycle digital agency in Estonia. Custom websites, mobile apps, turnkey platforms, Google Ads, SMM and technical support.', et: 'BoostLab - taisteenuse digiagentuur Eestis. Veebilehed, mobiilirakendused, platvormid, Google Ads, SMM ja tehniline tugi.', ru: 'BoostLab - digital-агентство полного цикла в Эстонии. Сайты, приложения, платформы под ключ, Google Ads, SMM и техподдержка.' },
            'web-development': { en: 'Professional website development in Estonia, Latvia and Lithuania. Landing pages, corporate sites, e-commerce and web platforms. SEO-optimized, mobile-first.', et: 'Professionaalne veebiarendus Eestis, Lätis ja Leedus. Maandumislehed, ettevõtte veebilehed, e-poed ja veebiplatvormid.', ru: 'Профессиональное создание сайтов в Эстонии, Латвии и Литве. Лендинги, корпоративные сайты, интернет-магазины и веб-платформы.' },
            'mobile-apps': { en: 'Mobile app development for iOS and Android in Estonia. Native and cross-platform apps from UX design to App Store publishing.', et: 'Mobiilirakenduste arendus iOS ja Android Eestis. Natiivsed ja platvormideülesed rakendused.', ru: 'Разработка мобильных приложений для iOS и Android в Эстонии. Нативные и кросс-платформенные приложения.' },
            'smm-marketing': { en: 'SMM and content marketing in Estonia, Latvia, Lithuania. Social media management, content strategy, Instagram, Facebook, TikTok.', et: 'SMM ja sisuturundus Eestis, Lätis, Leedus. Sotsiaalmeedia haldamine, sisustrateegia.', ru: 'SMM и контент-маркетинг в Эстонии, Латвии, Литве. Ведение соцсетей, контент-стратегия, Instagram, Facebook, TikTok.' },
            advertising: { en: 'Google Ads, Meta and TikTok advertising in Estonia. PPC campaign setup and management with measurable ROI.', et: 'Google Ads, Meta ja TikTok reklaam Eestis. PPC kampaaniate seadistamine ja haldamine.', ru: 'Реклама Google Ads, Meta и TikTok в Эстонии. Настройка и ведение PPC-кампаний с измеримым ROI.' },
            platforms: { en: 'Turnkey platform development in Estonia. Marketplaces, car rental, real estate, ticketing systems. Launch in 4-6 months.', et: 'Võtmed kätte platvormide arendus Eestis. Turuplatside, autorendiplatvormide ja piletisüsteemide arendus.', ru: 'Разработка платформ под ключ в Эстонии. Маркетплейсы, аренда авто, недвижимость, билетные системы.' },
            pricing: { en: 'Transparent pricing for web development, apps and marketing. Landing pages from €700, business sites from €1,700.', et: 'Läbipaistev hinnakujundus veebiarendusele ja turundusele. Maandumislehed alates €700.', ru: 'Прозрачные цены на разработку сайтов, приложений и маркетинг. Лендинги от €700, бизнес-сайты от €1 700.' },
            portfolio: { en: 'BoostLab portfolio — 150+ web development, mobile app and marketing projects in Estonia, Latvia, Lithuania.', et: 'BoostLab portfoolio — 150+ veebiarenduse ja turunduse projekti Eestis, Lätis, Leedus.', ru: 'Портфолио BoostLab — 150+ проектов веб-разработки и маркетинга в Эстонии, Латвии, Литве.' }
        };
        var t = pageTitles[page];
        document.title = t ? (t[lang] || t.en) : (pageTitles.home[lang] || pageTitles.home.en);
        var metaDesc = document.querySelector('meta[name="description"]');
        if (metaDesc) {
            var d = pageDescs[page];
            metaDesc.setAttribute('content', d ? (d[lang] || d.en) : (pageDescs.home[lang] || pageDescs.home.en));
        }

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



// === MODALS ===

    window.closeModal = function() {
        var modal = document.getElementById('projectModal');
        modal.classList.remove('open');
        document.body.style.overflow = '';
    };

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeModal();
    });
// === SMM PACKAGE DETAILS ===
    var smmDetails = [
        {
            title: 'Ad Campaign Setup - €599',
            list: [
                'Target audience & competitor analysis',
                'Campaign structure & strategy',
                'Keyword research (Google Ads)',
                'Ad creatives (up to 5)',
                'Targeting setup (geo, demographics, interests)',
                'Conversion & goal tracking',
                'Google Ads / Meta Ads integration',
                'A/B testing of ads',
                'Retargeting setup',
                'Performance report (first 2 weeks)'
            ]
        },
        {
            title: 'Ads + SMM Management - €1,399+/mo',
            list: [
                'Google Ads campaign management',
                'Meta Ads (Facebook + Instagram)',
                '12 social media posts / month',
                'Stories & Reels (up to 8/mo)',
                'Creative design for posts & ads',
                'Community management',
                'Monthly campaign optimization',
                'A/B testing',
                'Monthly analytics report',
                'Conversion improvement recommendations'
            ]
        },
        {
            title: 'Dedicated SMM Specialist - €2,500+/mo',
            list: [
                'Personal account manager',
                'Full Google Ads & Meta Ads management',
                '20+ posts / month',
                'Stories & Reels (up to 16/mo)',
                'Content strategy & content plan',
                'Professional copywriting',
                'All creative design',
                'Influencer & blogger outreach',
                'Reputation management',
                'TikTok content & ads',
                'Email marketing setup',
                'Weekly reports & calls',
                'SEO monitoring & optimization',
                'Priority support'
            ]
        }
    ];

    document.querySelectorAll('.smm-card').forEach(function(card, i) {
        card.style.cursor = 'pointer';
        card.addEventListener('click', function() {
            if (i >= smmDetails.length) return;
            var d = smmDetails[i];
            var modal = document.getElementById('projectModal');
            document.getElementById('pmMockup').innerHTML = '';
            document.getElementById('pmTags').innerHTML = '';
            document.getElementById('pmTitle').textContent = d.title;
            document.getElementById('pmDesc').textContent = '';
            document.getElementById('pmDetails').innerHTML = '<ul>' + d.list.map(function(item) { return '<li>' + item + '</li>'; }).join('') + '</ul>';
            modal.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    });

// === PRICING CARD DETAILS ===
    var pricingDetails = [
        {
            title: 'Starter - €700+',
            list: [
                'Responsive landing page',
                'Contact form with email notifications',
                'Mobile-first design',
                'Basic SEO setup (meta tags, sitemap)',
                'SSL certificate (HTTPS)',
                'Google Analytics integration',
                'Social media links',
                'GDPR cookie banner',
                '1 round of revisions',
                'Delivery: 5-7 business days'
            ]
        },
        {
            title: 'Business - €1,700+',
            list: [
                'Multi-page website (up to 8 pages)',
                'Custom UX/UI design in Figma',
                'Content management system (CMS)',
                'Advanced SEO (schema, hreflang, keywords)',
                'Google Analytics + Search Console',
                'Blog / news section',
                'Multi-language support',
                'Contact form + Google Maps',
                'Social media integration',
                'Speed optimization',
                '2 rounds of revisions',
                '1 month free support',
                'Delivery: 2-3 weeks'
            ]
        },
        {
            title: 'Advanced - €4,500+',
            list: [
                'Admin panel + user-facing side',
                'Payment integration (Stripe, PayPal)',
                'User accounts, roles & permissions',
                'Booking / shopping cart system',
                'API integrations (CRM, ERP, email)',
                'Advanced search & filtering',
                'Dashboard with analytics',
                'Email notifications system',
                'Multi-language support',
                'Full SEO package',
                'Load testing & optimization',
                'Priority support (SLA)',
                '3 rounds of revisions',
                'Delivery: 4-8 weeks'
            ]
        }
    ];

    document.querySelectorAll('.price-card').forEach(function(card, i) {
        card.style.cursor = 'pointer';
        card.addEventListener('click', function(e) {
            if (e.target.classList.contains('price-btn')) return;
            if (i >= pricingDetails.length) return;
            var d = pricingDetails[i];
            var modal = document.getElementById('projectModal');
            document.getElementById('pmMockup').innerHTML = '';
            document.getElementById('pmTags').innerHTML = '';
            document.getElementById('pmTitle').textContent = d.title;
            document.getElementById('pmDesc').textContent = '';
            document.getElementById('pmDetails').innerHTML = '<ul>' + d.list.map(function(item) { return '<li>' + item + '</li>'; }).join('') + '</ul>';
            modal.classList.add('open');
            document.body.style.overflow = 'hidden';
        });
    });

    // === FAQ ACCORDION ===
    document.querySelectorAll('.faq-q').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var item = btn.closest('.faq-item');
            var wasOpen = item.classList.contains('open');
            // Close all
            document.querySelectorAll('.faq-item.open').forEach(function(el) { el.classList.remove('open'); });
            // Toggle current
            if (!wasOpen) item.classList.add('open');
        });
    });
})();