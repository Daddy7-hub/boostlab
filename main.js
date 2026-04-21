// BoostLab – main.js
// Requires: i18n.js loaded first (provides T object)

(function() {
    'use strict';

    // === LANGUAGE SWITCHING ===
    var langCodes = { en:'en', et:'et', ru:'ru', lt:'lt', lv:'lv', es:'es', fr:'fr' };
    let currentLang = 'en';

    var growthTranslations = {
        en: {
            'gr.label': 'Growth & Lead Generation',
            'gr.title': 'Promotion Through Balticleads.ee',
            'gr.desc': 'We help client businesses get more qualified requests through Balticleads.ee and properly configured advertising campaigns. The goal is simple: connect your website, analytics and ad traffic into one measurable sales system.',
            'gr.p1': 'Campaign setup',
            'gr.p2': 'Lead generation funnels',
            'gr.p3': 'Tracking and analytics',
            'gr.p4': 'Landing page optimization',
            'gr.status': 'Lead platform',
            'gr.card': 'We use Balticleads.ee as part of a practical promotion workflow: prepare the offer, launch traffic, track conversions and improve the funnel based on real data.',
            'gr.link': 'Visit Balticleads.ee'
        },
        et: {
            'gr.label': 'Kasv ja müügivihjed',
            'gr.title': 'Edendamine Balticleads.ee kaudu',
            'gr.desc': 'Aitame klientide ettevõtetel saada Balticleads.ee ja õigesti seadistatud reklaamikampaaniate kaudu rohkem kvaliteetseid päringuid. Eesmärk on lihtne: ühendada veebileht, analüütika ja reklaamiliiklus üheks mõõdetavaks müügisüsteemiks.',
            'gr.p1': 'Kampaaniate seadistus',
            'gr.p2': 'Müügivihjete lehtrid',
            'gr.p3': 'Jälgimine ja analüütika',
            'gr.p4': 'Maandumislehe optimeerimine',
            'gr.status': 'Lead-platvorm',
            'gr.card': 'Kasutame Balticleads.ee platvormi praktilises edendustöös: valmistame pakkumise ette, käivitame liikluse, jälgime konversioone ja parandame lehtrit pärisandmete põhjal.',
            'gr.link': 'Ava Balticleads.ee'
        },
        ru: {
            'gr.label': 'Рост и лидогенерация',
            'gr.title': 'Продвижение через Balticleads.ee',
            'gr.desc': 'Мы помогаем бизнесу клиентов получать больше качественных заявок через Balticleads.ee и правильно настроенные рекламные кампании. Цель простая: связать сайт, аналитику и рекламный трафик в одну измеримую систему продаж.',
            'gr.p1': 'Настройка кампаний',
            'gr.p2': 'Воронки лидогенерации',
            'gr.p3': 'Трекинг и аналитика',
            'gr.p4': 'Оптимизация лендингов',
            'gr.status': 'Lead-платформа',
            'gr.card': 'Мы используем Balticleads.ee как часть практического процесса продвижения: готовим оффер, запускаем трафик, отслеживаем конверсии и улучшаем воронку по реальным данным.',
            'gr.link': 'Перейти на Balticleads.ee'
        },
        lt: {
            'gr.label': 'Augimas ir lead generavimas',
            'gr.title': 'Sklaida per Balticleads.ee',
            'gr.desc': 'Padedame klientų verslams gauti daugiau kokybiškų užklausų per Balticleads.ee ir tinkamai sukonfigūruotas reklamos kampanijas. Tikslas paprastas: sujungti svetainę, analitiką ir reklamos srautą į vieną matuojamą pardavimų sistemą.',
            'gr.p1': 'Kampanijų nustatymas',
            'gr.p2': 'Lead generavimo piltuvai',
            'gr.p3': 'Sekimas ir analitika',
            'gr.p4': 'Nukreipimo puslapių optimizavimas',
            'gr.status': 'Lead platforma',
            'gr.card': 'Balticleads.ee naudojame kaip praktinio sklaidos proceso dalį: paruošiame pasiūlymą, paleidžiame srautą, stebime konversijas ir geriname piltuvą pagal realius duomenis.',
            'gr.link': 'Atidaryti Balticleads.ee'
        },
        lv: {
            'gr.label': 'Izaugsme un potenciālie klienti',
            'gr.title': 'Virzīšana ar Balticleads.ee',
            'gr.desc': 'Palīdzam klientu uzņēmumiem iegūt vairāk kvalitatīvu pieprasījumu ar Balticleads.ee un pareizi iestatītām reklāmas kampaņām. Mērķis ir vienkāršs: savienot mājaslapu, analītiku un reklāmas trafiku vienā izmērāmā pārdošanas sistēmā.',
            'gr.p1': 'Kampaņu iestatīšana',
            'gr.p2': 'Lead ģenerēšanas piltuves',
            'gr.p3': 'Izsekošana un analītika',
            'gr.p4': 'Landing lapu optimizācija',
            'gr.status': 'Lead platforma',
            'gr.card': 'Balticleads.ee izmantojam kā praktiskas virzīšanas procesa daļu: sagatavojam piedāvājumu, palaižam trafiku, sekojam konversijām un uzlabojam piltuvi pēc reāliem datiem.',
            'gr.link': 'Atvērt Balticleads.ee'
        },
        es: {
            'gr.label': 'Crecimiento y leads',
            'gr.title': 'Promoción a través de Balticleads.ee',
            'gr.desc': 'Ayudamos a las empresas de nuestros clientes a recibir más solicitudes cualificadas mediante Balticleads.ee y campañas publicitarias bien configuradas. El objetivo es simple: conectar sitio web, analítica y tráfico publicitario en un sistema de ventas medible.',
            'gr.p1': 'Configuración de campañas',
            'gr.p2': 'Embudos de leads',
            'gr.p3': 'Seguimiento y analítica',
            'gr.p4': 'Optimización de landing pages',
            'gr.status': 'Plataforma de leads',
            'gr.card': 'Usamos Balticleads.ee como parte de un flujo práctico de promoción: preparar la oferta, lanzar tráfico, medir conversiones y mejorar el embudo con datos reales.',
            'gr.link': 'Visitar Balticleads.ee'
        },
        fr: {
            'gr.label': 'Croissance et leads',
            'gr.title': 'Promotion via Balticleads.ee',
            'gr.desc': 'Nous aidons les entreprises clientes à obtenir plus de demandes qualifiées via Balticleads.ee et des campagnes publicitaires bien configurées. L’objectif est simple : relier le site, l’analytique et le trafic publicitaire dans un système de vente mesurable.',
            'gr.p1': 'Configuration des campagnes',
            'gr.p2': 'Funnels de génération de leads',
            'gr.p3': 'Suivi et analytique',
            'gr.p4': 'Optimisation des landing pages',
            'gr.status': 'Plateforme de leads',
            'gr.card': 'Nous utilisons Balticleads.ee dans un processus de promotion concret : préparer l’offre, lancer le trafic, suivre les conversions et améliorer le funnel avec des données réelles.',
            'gr.link': 'Visiter Balticleads.ee'
        }
    };

    Object.keys(growthTranslations).forEach(function(lang) {
        if (T[lang]) Object.assign(T[lang], growthTranslations[lang]);
    });

    function setLang(lang) {
        if (!T[lang]) return;
        currentLang = lang;
        localStorage.setItem('bl_lang', lang);
        document.documentElement.lang = langCodes[lang] || 'en';

        // Update all [data-i] elements (text content)
        document.querySelectorAll('[data-i]').forEach(function(el) {
            var key = el.getAttribute('data-i');
            if (T[lang][key]) el.textContent = T[lang][key];
        });

        // Update all [data-ih] elements (innerHTML – for spans inside)
        document.querySelectorAll('[data-ih]').forEach(function(el) {
            var key = el.getAttribute('data-ih');
            if (T[lang][key]) el.innerHTML = T[lang][key];
        });

        // Update lang buttons (legacy) and dropdown label
        document.querySelectorAll('.lang-btn').forEach(function(btn) {
            btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
        });
        document.querySelectorAll('.lang-current').forEach(function(el) {
            el.textContent = lang.toUpperCase();
        });
        // Close dropdown after selection
        document.querySelectorAll('.lang-dropdown').forEach(function(dd) {
            dd.classList.remove('open');
        });

        // Update page title & meta description per page
        var page = document.body.getAttribute('data-page') || 'home';
        var pageTitles = {
            home: { en: 'BoostLab | Web Development, Apps & SEO-Ready Digital Projects', et: 'BoostLab | Veebiarendus, rakendused, digiturundus | Eesti', ru: 'BoostLab | Разработка сайтов, приложений, маркетинг | Эстония', lt: 'BoostLab | Svetainių kūrimas, programėlės, rinkodara | Estija', lv: 'BoostLab | Mājaslapu izstrāde, lietotnes, mārketings | Igaunija', es: 'BoostLab | Desarrollo web, apps, marketing digital | Estonia', fr: 'BoostLab | Développement web, apps, marketing digital | Estonie' },
            'web-development': { en: 'Website Development Estonia, Latvia, Lithuania | BoostLab', et: 'Veebiarendus Eestis, Lätis, Leedus | BoostLab', ru: 'Создание сайтов Эстония, Латвия, Литва | BoostLab', lt: 'Svetainių kūrimas Estija, Latvija, Lietuva | BoostLab', lv: 'Mājaslapu izstrāde Igaunija, Latvija, Lietuva | BoostLab', es: 'Desarrollo web Estonia, Letonia, Lituania | BoostLab', fr: 'Développement web Estonie, Lettonie, Lituanie | BoostLab' },
            'mobile-apps': { en: 'Mobile App Development iOS & Android | BoostLab Estonia', et: 'Mobiilirakenduste arendus iOS & Android | BoostLab', ru: 'Разработка мобильных приложений iOS и Android | BoostLab', lt: 'Mobiliųjų programėlių kūrimas iOS ir Android | BoostLab', lv: 'Mobilo lietotņu izstrāde iOS un Android | BoostLab', es: 'Desarrollo de apps móviles iOS y Android | BoostLab', fr: 'Développement d\'apps mobiles iOS et Android | BoostLab' },
            'smm-marketing': { en: 'SMM & Content Marketing Estonia, Latvia, Lithuania | BoostLab', et: 'SMM ja sisuturundus Eestis, Lätis, Leedus | BoostLab', ru: 'SMM и контент-маркетинг Эстония, Латвия, Литва | BoostLab', lt: 'SMM ir turinio rinkodara Estija, Latvija, Lietuva | BoostLab', lv: 'SMM un satura mārketings Igaunija, Latvija, Lietuva | BoostLab', es: 'SMM y marketing de contenidos Estonia | BoostLab', fr: 'SMM et marketing de contenu Estonie | BoostLab' },
            advertising: { en: 'Google Ads & PPC Advertising Estonia | BoostLab', et: 'Google Ads ja PPC reklaam Eestis | BoostLab', ru: 'Реклама Google Ads и PPC Эстония | BoostLab', lt: 'Google Ads ir PPC reklama Estija | BoostLab', lv: 'Google Ads un PPC reklāma Igaunija | BoostLab', es: 'Google Ads y publicidad PPC Estonia | BoostLab', fr: 'Google Ads et publicité PPC Estonie | BoostLab' },
            platforms: { en: 'Turnkey Platform Development | BoostLab Estonia', et: 'Võtmed kätte platvormide arendus | BoostLab', ru: 'Разработка платформ под ключ | BoostLab Эстония', lt: 'Platformų kūrimas „iki rakto" | BoostLab', lv: 'Platformu izstrāde „atslēgas rokā" | BoostLab', es: 'Desarrollo de plataformas llave en mano | BoostLab', fr: 'Développement de plateformes clé en main | BoostLab' },
            pricing: { en: 'Pricing – Web Development & Marketing | BoostLab', et: 'Hinnad – Veebiarendus ja turundus | BoostLab', ru: 'Цены – Разработка сайтов и маркетинг | BoostLab', lt: 'Kainos – Svetainių kūrimas ir rinkodara | BoostLab', lv: 'Cenas – Mājaslapu izstrāde un mārketings | BoostLab', es: 'Precios – Desarrollo web y marketing | BoostLab', fr: 'Tarifs – Développement web et marketing | BoostLab' },
            portfolio: { en: 'Portfolio – Digital Agency Projects | BoostLab Estonia', et: 'Portfoolio – Digiagentuur | BoostLab', ru: 'Портфолио – Проекты digital-агентства | BoostLab', lt: 'Portfelis – Skaitmeninės agentūros projektai | BoostLab', lv: 'Portfolio – Digitālās aģentūras projekti | BoostLab', es: 'Portafolio – Proyectos de agencia digital | BoostLab', fr: 'Portfolio – Projets d\'agence digitale | BoostLab' }
        };
        var pageDescs = {
            home: { en: 'BoostLab builds professional websites, web platforms, mobile apps and growth systems for businesses in Estonia, the Baltics and Europe. UX/UI, SEO, advertising, lead generation via Balticleads.ee and support.', et: 'BoostLab - taisteenuse digiagentuur Eestis. Veebilehed, mobiilirakendused, platvormid, Google Ads, SMM ja tehniline tugi.', ru: 'BoostLab - digital-агентство полного цикла в Эстонии. Сайты, приложения, платформы под ключ, Google Ads, SMM и техподдержка.', lt: 'BoostLab – viso ciklo skaitmeninė agentūra Estijoje. Svetainės, programėlės, platformos, Google Ads, SMM ir techninė pagalba.', lv: 'BoostLab – pilna cikla digitālā aģentūra Igaunijā. Mājaslapas, lietotnes, platformas, Google Ads, SMM un tehniskais atbalsts.', es: 'BoostLab – agencia digital de ciclo completo en Estonia. Sitios web, apps, plataformas, Google Ads, SMM y soporte técnico.', fr: 'BoostLab – agence digitale à cycle complet en Estonie. Sites web, apps, plateformes, Google Ads, SMM et support technique.' },
            'web-development': { en: 'Professional website development in Estonia, Latvia and Lithuania. Landing pages, corporate sites, e-commerce and web platforms. SEO-optimized, mobile-first.', et: 'Professionaalne veebiarendus Eestis, Lätis ja Leedus. Maandumislehed, ettevõtte veebilehed, e-poed ja veebiplatvormid.', ru: 'Профессиональное создание сайтов в Эстонии, Латвии и Литве. Лендинги, корпоративные сайты, интернет-магазины и веб-платформы.', lt: 'Profesionalus svetainių kūrimas Estijoje, Latvijoje ir Lietuvoje. Nukreipimo puslapiai, el. parduotuvės ir platformos.', lv: 'Profesionāla mājaslapu izstrāde Igaunijā, Latvijā un Lietuvā. Ielādes lapas, e-veikali un platformas.', es: 'Desarrollo web profesional en Estonia, Letonia y Lituania. Landing pages, tiendas online y plataformas.', fr: 'Développement web professionnel en Estonie, Lettonie et Lituanie. Landing pages, e-commerce et plateformes.' },
            'mobile-apps': { en: 'Mobile app development for iOS and Android in Estonia. Native and cross-platform apps from UX design to App Store publishing.', et: 'Mobiilirakenduste arendus iOS ja Android Eestis. Natiivsed ja platvormideülesed rakendused.', ru: 'Разработка мобильных приложений для iOS и Android в Эстонии. Нативные и кросс-платформенные приложения.', lt: 'Mobiliųjų programėlių kūrimas iOS ir Android Estijoje. Natyvios ir tarpplatforminės programėlės.', lv: 'Mobilo lietotņu izstrāde iOS un Android Igaunijā. Natīvās un starpplatformu lietotnes.', es: 'Desarrollo de apps móviles iOS y Android en Estonia. Apps nativas y multiplataforma.', fr: 'Développement d\'apps mobiles iOS et Android en Estonie. Apps natives et multiplateformes.' },
            'smm-marketing': { en: 'SMM and content marketing in Estonia, Latvia, Lithuania. Social media management, content strategy, Instagram, Facebook, TikTok.', et: 'SMM ja sisuturundus Eestis, Lätis, Leedus. Sotsiaalmeedia haldamine, sisustrateegia.', ru: 'SMM и контент-маркетинг в Эстонии, Латвии, Литве. Ведение соцсетей, контент-стратегия, Instagram, Facebook, TikTok.', lt: 'SMM ir turinio rinkodara Estijoje, Latvijoje, Lietuvoje. Socialinių tinklų valdymas ir turinio strategija.', lv: 'SMM un satura mārketings Igaunijā, Latvijā, Lietuvā. Sociālo tīklu vadība un satura stratēģija.', es: 'SMM y marketing de contenidos en Estonia, Letonia, Lituania. Gestión de redes sociales y estrategia de contenido.', fr: 'SMM et marketing de contenu en Estonie, Lettonie, Lituanie. Gestion des réseaux sociaux et stratégie de contenu.' },
            advertising: { en: 'Google Ads, Meta and TikTok advertising in Estonia. PPC campaign setup and management with measurable ROI.', et: 'Google Ads, Meta ja TikTok reklaam Eestis. PPC kampaaniate seadistamine ja haldamine.', ru: 'Реклама Google Ads, Meta и TikTok в Эстонии. Настройка и ведение PPC-кампаний с измеримым ROI.', lt: 'Google Ads, Meta ir TikTok reklama Estijoje. PPC kampanijų nustatymas ir valdymas.', lv: 'Google Ads, Meta un TikTok reklāma Igaunijā. PPC kampaņu iestatīšana un vadība.', es: 'Publicidad Google Ads, Meta y TikTok en Estonia. Configuración y gestión de campañas PPC.', fr: 'Publicité Google Ads, Meta et TikTok en Estonie. Configuration et gestion de campagnes PPC.' },
            platforms: { en: 'Turnkey platform development in Estonia. Marketplaces, car rental, real estate, ticketing systems. Launch in 4-6 months.', et: 'Võtmed kätte platvormide arendus Eestis. Turuplatside, autorendiplatvormide ja piletisüsteemide arendus.', ru: 'Разработка платформ под ключ в Эстонии. Маркетплейсы, аренда авто, недвижимость, билетные системы.', lt: 'Platformų kūrimas Estijoje. Prekyvietės, automobilių nuoma, nekilnojamasis turtas, bilietų sistemos.', lv: 'Platformu izstrāde Igaunijā. Tirgus platformas, auto noma, nekustamais īpašums, biļešu sistēmas.', es: 'Desarrollo de plataformas en Estonia. Marketplaces, alquiler de autos, inmobiliaria, ticketing.', fr: 'Développement de plateformes en Estonie. Marketplaces, location auto, immobilier, billetterie.' },
            pricing: { en: 'Transparent pricing for web development, apps and marketing. Landing pages from €700, business sites from €1,700.', et: 'Läbipaistev hinnakujundus veebiarendusele ja turundusele. Maandumislehed alates €700.', ru: 'Прозрачные цены на разработку сайтов, приложений и маркетинг. Лендинги от €700, бизнес-сайты от €1 700.', lt: 'Skaidrios kainos svetainių kūrimui ir rinkodarai. Nukreipimo puslapiai nuo €700.', lv: 'Caurspīdīgas cenas mājaslapu izstrādei un mārketingam. Ielādes lapas no €700.', es: 'Precios transparentes para desarrollo web y marketing. Landing pages desde €700.', fr: 'Tarifs transparents pour développement web et marketing. Landing pages à partir de €700.' },
            portfolio: { en: 'BoostLab portfolio – 150+ web development, mobile app and marketing projects in Estonia, Latvia, Lithuania.', et: 'BoostLab portfoolio – 150+ veebiarenduse ja turunduse projekti Eestis, Lätis, Leedus.', ru: 'Портфолио BoostLab – 150+ проектов веб-разработки и маркетинга в Эстонии, Латвии, Литве.', lt: 'BoostLab portfelis – 150+ svetainių kūrimo ir rinkodaros projektų Estijoje, Latvijoje, Lietuvoje.', lv: 'BoostLab portfolio – 150+ mājaslapu izstrādes un mārketinga projekti Igaunijā, Latvijā, Lietuvā.', es: 'Portafolio BoostLab – 150+ proyectos de desarrollo web y marketing en Estonia, Letonia, Lituania.', fr: 'Portfolio BoostLab – 150+ projets web et marketing en Estonie, Lettonie, Lituanie.' }
        };
        var t = pageTitles[page];
        document.title = t ? (t[lang] || t.en) : (pageTitles.home[lang] || pageTitles.home.en);
        var metaDesc = document.querySelector('meta[name="description"]');
        if (metaDesc) {
            var d = pageDescs[page];
            metaDesc.setAttribute('content', d ? (d[lang] || d.en) : (pageDescs.home[lang] || pageDescs.home.en));
        }

    }

    // Bind all lang buttons (inside dropdown or standalone)
    document.addEventListener('click', function(e) {
        var langBtn = e.target.closest('.lang-btn');
        if (langBtn) {
            var lang = langBtn.getAttribute('data-lang');
            if (lang) setLang(lang);
            return;
        }
        // Toggle dropdown
        var trigger = e.target.closest('.lang-trigger');
        if (trigger) {
            var dd = trigger.closest('.lang-dropdown');
            if (dd) dd.classList.toggle('open');
            return;
        }
        // Close dropdown on click outside
        document.querySelectorAll('.lang-dropdown.open').forEach(function(dd) {
            dd.classList.remove('open');
        });
    });

    // === TOP BANNER ===
    var topBanner = document.getElementById('topBanner');
    var bannerClose = document.getElementById('bannerClose');
    if (topBanner && bannerClose) {
        if (sessionStorage.getItem('bl_banner_closed')) {
            topBanner.remove();
            document.body.classList.remove('has-banner');
        } else {
            document.body.classList.add('has-banner');
            bannerClose.addEventListener('click', function() {
                topBanner.remove();
                document.body.classList.remove('has-banner');
                sessionStorage.setItem('bl_banner_closed', '1');
            });
        }
    }

    // Restore language from localStorage
    var savedLang = localStorage.getItem('bl_lang');
    if (savedLang && T[savedLang]) {
        setLang(savedLang);
    }

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
