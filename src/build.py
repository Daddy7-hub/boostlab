"""Static site generator for boostlab.lt.

python src/build.py  ->  dist/  (published by GitHub Pages workflow)
Content lives in src/content/<lang>.py, page templates are functions below.
"""
import json
import re
import shutil
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
SITE = "https://boostlab.lt"
LANGS = ["en", "et", "ru", "lt"]
PHONE, PHONE_H, EMAIL = "+37256825854", "+372 568 25854", "info@boostlab.lt"
GA = ["G-5F8H438EKX", "AW-18015999232", "GT-TQDGLZ8J"]
PIXEL = "137665235020353"
V = __import__("hashlib").sha1(b"".join(p.read_bytes() for p in sorted((ROOT / "assets").glob("*/*.*")) if p.suffix in (".css", ".js"))).hexdigest()[:10]

CDN = {
    "lenis": "https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js",
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three_addons": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/",
}


def load(lang):
    """content/<lang>.py defines T; content/<lang>_pages.py (optional) extends it."""
    ns = {}
    for name in (f"{lang}.py", f"{lang}_pages.py", f"{lang}_extra.py", f"{lang}_seo.py"):
        f = SRC / "content" / name
        if f.exists():
            exec(compile(f.read_text(encoding="utf-8"), str(f), "exec"), ns)
    return ns["T"]


def url(T, key, absolute=False):
    """key: page key from T["slugs"], "niche:<id>" (industry page) or "post:<id>" (blog article)."""
    prefix = "/" if T["lang"] == "en" else f"/{T['lang']}/"
    if key.startswith("niche:"):
        rel = T["niches"][key[6:]]["slug"]
    elif key.startswith("post:"):
        rel = T["slugs"]["blog"] + T["blog"]["posts"][key[5:]]["slug"]
    else:
        rel = T["slugs"][key]
    u = prefix + rel
    return SITE + u if absolute else u


ARR = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" class="arr"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARR_UP = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 17L17 7M8 7h9v9"/></svg>'
LOGO = '<a class="logo" href="{home}" aria-label="BoostLab"><span class="mk" aria-hidden="true">B</span>BoostLab</a>'
SERVICE_KEYS = ["web", "crm", "platforms", "apps", "ads", "smm", "leadgen"]
# our own B2B product, linked from the header as a separate highlighted tab
BL_TAB = '<a class="bl-tab" href="https://balticleads.ee/" target="_blank" rel="noopener"><i></i>BalticLeads<span aria-hidden="true">↗</span></a>'


# ---------------------------------------------------------------- layout
def layout(T, ALL, key, body, meta, schema, stage=False):
    u = T["ui"]
    built = T.get("_built", set())
    has = lambda L: (L["lang"], key) in built
    alt = "".join(
        f'<link rel="alternate" hreflang="{L["lang"]}" href="{url(L, key, True)}">' for L in ALL.values() if has(L)
    ) + f'<link rel="alternate" hreflang="x-default" href="{url(ALL["en"], key, True)}">'
    langs = "".join(
        f'<a href="{url(L, key if has(L) else "home")}" hreflang="{L["lang"]}" lang="{L["lang"]}"'
        + (' aria-current="true"' if L["lang"] == T["lang"] else "")
        + f'>{L["label"]}</a>'
        for L in ALL.values()
    )
    menu = [("web", u["services"]), ("crm", T["nav"]["crm"]), ("portfolio", u["work"]), ("pricing", u["pricing"])]
    if "blog" in T:
        menu.append(("blog", T["blog"]["crumb"]))
    menu_html = "".join(
        f'<a href="{url(T, k)}"' + (' aria-current="page"' if k == key or (k == "blog" and key.startswith("post:")) else "") + f">{escape(lbl)}</a>" for k, lbl in menu
    )
    drawer = "".join(f'<a class="dl" href="{url(T, k)}">{escape(T["nav"][k])}</a>' for k in SERVICE_KEYS if k in T.get("pages", {}))
    drawer += f'<a class="dl" href="{url(T, "portfolio")}">{escape(u["work"])}</a><a class="dl" href="{url(T, "pricing")}">{escape(u["pricing"])}</a>'
    if "blog" in T:
        drawer += f'<a class="dl" href="{url(T, "blog")}">{escape(T["blog"]["crumb"])}</a>'
    drawer += BL_TAB
    og_img = f"{SITE}/assets/img/og-{T['lang']}.jpg"
    logo = LOGO.format(home=url(T, "home"))
    return f"""<!DOCTYPE html>
<html lang="{T['lang']}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(meta['title'])}</title>
<meta name="description" content="{escape(meta['desc'])}">
<link rel="canonical" href="{url(T, key, True)}">
{alt}
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BoostLab">
<meta property="og:locale" content="{T['locale']}">
<meta property="og:title" content="{escape(meta['title'])}">
<meta property="og:description" content="{escape(meta['desc'])}">
<meta property="og:url" content="{url(T, key, True)}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700&display=swap&subset=cyrillic,latin-ext" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v={V}">
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('consent','default',{{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500}});gtag('js',new Date());{''.join(f"gtag('config','{g}');" for g in GA)}window.BL_PIXEL='{PIXEL}';</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA[0]}"></script>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
<header class="hdr"><div class="wrap hdr-in">
{logo}
<nav class="menu" aria-label="Main">{menu_html}</nav>
<div class="hdr-r">{BL_TAB}<div class="langs">{langs}</div><a class="btn btn-solid" href="#contact">{escape(u['cta'])}</a>
<button class="burger" aria-label="{escape(u['menu'])}" aria-expanded="false"><i></i><i></i></button></div>
</div></header>
<div class="drawer">{drawer}<a class="btn btn-solid" href="#contact">{escape(u['cta'])}</a><div class="langs">{langs}</div></div>
<main>
{body}
{cta_block(T)}
</main>
{footer(T)}
<div class="ck" role="dialog" aria-live="polite"><p>{u['ck_text'].format(privacy=url(T, 'privacy'))}</p><div class="ck-b"><button class="no">{escape(u['ck_no'])}</button><button class="ok">{escape(u['ck_ok'])}</button></div></div>
<script src="/assets/js/site.js?v={V}" defer></script>
</body>
</html>
"""


def cta_block(T):
    c = T["cta_block"]
    title = re.sub(r"<br\s*/?>", " ", c["title"])
    return f"""<section class="cta" id="contact"><div class="wrap split">
<div><h2>{title}</h2><p class="lead">{escape(c['lead'])}</p>
<div class="ctas"><a class="btn btn-solid" href="mailto:{EMAIL}?subject=BoostLab%20project">{escape(c['mail'])}</a><a class="btn btn-line" href="tel:{PHONE}">{escape(c['call'])}</a></div>
<div class="contacts"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE}">{PHONE_H}</a></div></div>
<figure>{pic("cta")}</figure>
</div></section>"""


def footer(T):
    u = T["ui"]
    svc = "".join(f'<a href="{url(T, k)}">{escape(T["nav"][k])}</a>' for k in SERVICE_KEYS if k in T.get("pages", {}))
    ind = "".join(f'<a href="{url(T, "niche:" + k)}">{escape(n["nav"])}</a>' for k, n in T.get("niches", {}).items())
    ind_col = f'<div class="ftr-col"><h4>{escape(u.get("f_industries", ""))}</h4>{ind}</div>' if ind else ""
    blog_a = f'<a href="{url(T, "blog")}">{escape(T["blog"]["crumb"])}</a>' if "blog" in T else ""
    return f"""<footer class="ftr"><div class="wrap">
<div class="ftr-top">
<div class="ftr-about">{LOGO.format(home=url(T, "home"))}<p>{escape(u['about'])}</p></div>
<div class="ftr-col"><h4>{escape(u['f_services'])}</h4>{svc}</div>{ind_col}
<div class="ftr-col"><h4>{escape(u['f_company'])}</h4><a href="{url(T, 'portfolio')}">{escape(u['work'])}</a><a href="{url(T, 'pricing')}">{escape(u['pricing'])}</a>{blog_a}<a href="#contact">{escape(u['contact'])}</a></div>
<div class="ftr-col"><h4>{escape(u['f_contact'])}</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE}">{PHONE_H}</a><a href="https://balticleads.ee/" rel="noopener">BalticLeads.ee</a></div>
</div>
<div class="ftr-bot"><span>&copy; {date.today().year} FANARI OÜ (BoostLab), Tallinn, Estonia. {escape(u['rights'])}</span>
<nav><a href="{url(T, 'privacy')}">{escape(u['privacy'])}</a><a href="{url(T, 'terms')}">{escape(u['terms'])}</a></nav></div>
</div></footer>"""


# ---------------------------------------------------------------- schema
def org_schema(T):
    return {
        "@type": ["Organization", "ProfessionalService"], "@id": f"{SITE}/#org", "name": "BoostLab",
        "legalName": "FANARI OÜ", "url": f"{SITE}/", "logo": f"{SITE}/apple-touch-icon.png", "image": f"{SITE}/assets/img/og-en.jpg",
        "email": EMAIL, "telephone": PHONE, "priceRange": "€€",
        "address": {"@type": "PostalAddress", "streetAddress": "Ehitajate tee 15-20", "postalCode": "12612", "addressLocality": "Tallinn", "addressCountry": "EE"},
        "areaServed": ["EE", "LT", "LV", "FI", "EU", "Worldwide"],
        "knowsLanguage": ["en", "et", "ru", "lt"],
        "sameAs": ["https://balticleads.ee/"],
    }


def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def graph(*nodes):
    return {"@context": "https://schema.org", "@graph": [n for n in nodes if n]}


def faq_html(T, faq):
    items = "".join(f'<details><summary>{escape(q)}</summary><div class="ans">{escape(a)}</div></details>' for q, a in faq)
    return f"""<section class="sec"><div class="wrap">
<div class="sec-head"><h2>{escape(T['ui']['faq'])}</h2></div>
<div class="faq">{items}</div></div></section>"""


# ---------------------------------------------------------------- mock UIs for cases
def mock(kind):
    chart = '<div class="chart"><svg viewBox="0 0 300 100" preserveAspectRatio="none"><defs><linearGradient id="g{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D88A4C" stop-opacity=".35"/><stop offset="1" stop-color="#D88A4C" stop-opacity="0"/></linearGradient></defs><path d="M0 85 C40 80 60 60 90 62 S150 40 180 44 230 18 300 12 V100 H0Z" fill="url(#g{k})"/><path d="M0 85 C40 80 60 60 90 62 S150 40 180 44 230 18 300 12" fill="none" stroke="#D88A4C" stroke-width="2"/></svg></div>'.replace("{k}", kind)
    if kind == "tickets":
        kpis = [("Tickets sold", "2,418", "+27%"), ("Checked in", "1,962", "81%"), ("VIP tables", "38/40", "sold out")]
        rows = [("Halloween · Standard", "€10", "Paid"), ("VIP table #4", "€240", "Paid"), ("Early bird", "€8", "Checked in"), ("Referral · Mari K.", "€10", "Paid")]
    elif kind == "rent":
        kpis = [("Active listings", "1,204", "+12%"), ("Bookings", "312", "this week"), ("Occupancy", "87%", "+6%")]
        rows = [("Tesla Model 3 · 3 days", "€177", "Confirmed"), ("Camera kit · 1 day", "€35", "Deposit held"), ("Volvo XC60 · 7 days", "€448", "Confirmed"), ("Cargo van · 2 days", "€98", "Pending")]
    else:
        kpis = [("Open deals", "€182k", "+18%"), ("New leads", "1,284", "+32%"), ("Win rate", "31%", "+4%")]
        rows = [("Nordic Dental OÜ", "Proposal", "Synced"), ("Kalev Logistics", "Qualified", "Synced"), ("Pirita Rent", "Won", "Invoice sent"), ("Baltic Build AS", "New", "Call today")]
    k = "".join(f'<div class="kpi">{a}<b>{b}</b><s>{c}</s></div>' for a, b, c in kpis)
    r = "".join(f'<div><span>{a}</span><span>{b}</span><span><i class="pill{" g" if i % 2 == 0 else ""}">{c}</i></span></div>' for i, (a, b, c) in enumerate(rows))
    return f'<div class="mock" aria-hidden="true"><div class="sb"><i class="a"></i><i></i><i></i><i></i><i></i><i></i></div><div class="mn"><div class="row">{k}</div>{chart}<div class="tbl">{r}</div></div></div>'


def img_size(name):
    from PIL import Image
    with Image.open(ROOT / "assets" / "img" / name) as im:
        return im.size


# which projects are shown where - examples live only on home and portfolio
HOME_CASES = ["rentme", "balticleads"]
PORTFOLIO_CASES = ["rentme", "balticleads", "after"]


def pick_cases(T, ids):
    by_id = {c["id"]: c for c in T["cases"]}
    return [by_id[i] for i in ids]


def case_cards(T, cases):
    """Vertical case rows: screenshot in a browser frame + what we built."""
    out = []
    pts = T.get("case_points", {})
    for i, c in enumerate(cases):
        if c.get("img"):
            w, h = img_size(c["img"])
            media = f'<img src="/assets/img/{c["img"]}" alt="{escape(c["name"])} - {escape(c["tags"][0])}" loading="lazy" decoding="async" width="{w}" height="{h}">'
        else:
            media = mock(c["mock"])
        link = (f'<a class="btn btn-line" href="{c["url"]}" target="_blank" rel="noopener">{escape(T["ui"]["visit"])}</a>'
                if c.get("url") else "")
        tags = "".join(f'<span class="tag">{escape(t)}</span>' for t in c["tags"])
        host = c["url"].replace("https://", "").rstrip("/") if c.get("url") else c["id"] + ".app"
        li = "".join(f"<li>{escape(x)}</li>" for x in pts.get(c["id"], []))
        out.append(f"""<article class="case-row"><div class="case-media"><div class="win"><div class="win-bar"><i></i><i></i><i></i><span>{escape(host)}</span></div><div class="win-body">{media}</div></div></div>
<div class="case-info"><h3 class="h-m">{escape(c['name'])}</h3><div class="case-tags">{tags}</div><p>{escape(c['text'])}</p>{f'<ul class="points">{li}</ul>' if li else ''}{link}</div></article>""")
    return f'<div class="cases-list">{"".join(out)}</div>'


# ---------------------------------------------------------------- pages
def page_home(T, ALL):
    h = T["home"]
    facts = "".join(f'<div><b>{escape(n)}{escape(suf)}</b><span>{escape(p)}</span></div>' for _, n, suf, p in h["nums"])
    rows = []
    for k, t, d in h["svc"]:
        P = T.get("pages", {}).get(k, {})
        prices = [price_int(f) for _, _, f in P.get("feats", []) if f]
        price = f'<span class="price"><small>{escape(T["ui"]["from"])}</small>€{min(prices):,}</span>' if prices else '<span></span>'
        rows.append(f'<li><a href="{url(T, k)}"><span class="ph">{pic(k, "", t)}</span><span><h3>{escape(t)}</h3><p>{escape(d)}</p></span>{price}</a></li>')
    steps = "".join(f"<li><span><b>{escape(t)}</b><p>{escape(d)}</p></span></li>" for t, d in T["process"])
    incl = "".join(f"<li>{escape(x)}</li>" for x in h["incl"])
    ptable = "".join(
        f'<div class="row"><b>{escape(n)}</b><span>{escape(", ".join(f))}</span><em><small class="muted" style="font-size:15px;font-weight:400">{escape(T["ui"]["from"])}</small> {p}</em></div>'
        for n, p, f in h["tiers"])
    h1 = re.sub(r"<br\s*/?>", " ", h["h1"])
    body = f"""
<section class="hero"><div class="wrap">
<div class="hero-grid">
<div class="hero-text"><h1>{h1}</h1><p class="lead">{escape(h['lead'])}</p>
<div class="ctas"><a class="btn btn-solid" href="#contact">{escape(h['cta1'])}</a><a class="btn btn-line" href="#work">{escape(h['cta2'])}</a></div>
<p class="hero-note">{escape(h['price_from'])} <b>€700</b></p></div>
<figure class="hero-img">{pic("hero", "", "").replace('loading="lazy"', 'fetchpriority="high"')}</figure>
</div>
<div class="facts">{facts}</div>
</div></section>

<section class="sec sec-fog" id="services"><div class="wrap">
<div class="sec-head"><h2>{h['svc_title']}</h2><p class="lead">{escape(h['svc_lead'])}</p></div>
<ul class="svc-list">{"".join(rows)}</ul>
</div></section>

<section class="sec" id="work"><div class="wrap">
<div class="sec-head"><h2>{h['cases_title']}</h2><p class="lead">{escape(h['cases_lead'])}</p></div>
{case_cards(T, pick_cases(T, HOME_CASES))}
</div></section>

<section class="sec sec-fog"><div class="wrap split">
<figure>{pic("process")}</figure>
<div><h2>{escape(T['ui']['process'])}</h2><ol class="steps-list">{steps}</ol></div>
</div></section>

<section class="sec"><div class="wrap incl2">
<div><h2>{h['incl_title']}</h2><p class="lead">{escape(h['incl_lead'])}</p></div>
<ul class="checks">{incl}</ul>
</div></section>

<section class="sec sec-fog"><div class="wrap">
<div class="sec-head"><h2>{escape(T['pricing']['crumb'] if 'pricing' in T else h['price_kicker'])}</h2><p class="lead">{escape(h['price_note'])}</p></div>
<div class="ptable">{ptable}</div>
<div class="ptable-foot"><span></span><a class="btn btn-line" href="{url(T, 'pricing')}">{escape(h['price_all'])}</a></div>
</div></section>

{faq_html(T, h['faq'])}
"""
    schema = graph(org_schema(T), {
        "@type": "WebSite", "@id": f"{SITE}/#web", "url": f"{SITE}/", "name": "BoostLab", "inLanguage": T["lang"], "publisher": {"@id": f"{SITE}/#org"}},
        {"@type": "OfferCatalog", "name": "BoostLab services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "provider": {"@id": f"{SITE}/#org"}},
             "priceSpecification": {"@type": "PriceSpecification", "minPrice": int(p.replace("€", "").replace(",", "")), "priceCurrency": "EUR"}}
            for n, p, _ in h["tiers"]]},
        faq_schema(h["faq"]))
    return layout(T, ALL, "home", body, {"title": h["title"], "desc": h["desc"]}, schema)


def crumbs_html(T, label):
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{url(T, "home")}">{escape(T["ui"]["home"])}</a><span>/</span><span>{escape(label)}</span></nav>'


def crumbs_schema(T, key, label):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": T["ui"]["home"], "item": url(T, "home", True)},
        {"@type": "ListItem", "position": 2, "name": label, "item": url(T, key, True)}]}


# stock photos (CC0, no people/logos) per page key; missing files are simply skipped
PAGE_IMG = {"hero": "lt-hero.webp", "web": "lt-web.webp", "crm": "lt-crm.webp", "platforms": "lt-platforms.webp",
            "apps": "lt-apps.webp", "ads": "lt-ads.webp", "smm": "lt-smm.webp", "leadgen": "lt-leadgen.webp",
            "portfolio": "lt-portfolio.webp", "pricing": "lt-pricing.webp", "process": "lt-process.webp", "cta": "lt-contact.webp",
            "ecommerce": "lt-ecommerce.webp", "clinics": "lt-clinics.webp", "rental": "lt-rental.webp", "restaurants": "lt-restaurants.webp",
            "post:website-cost": "lt-post1.webp", "post:custom-crm-vs-saas": "lt-post2.webp", "post:booking-system": "lt-post3.webp",
            "post:b2b-leads-baltics": "lt-post4.webp", "post:seo-checklist": "lt-post5.webp", "post:landing-vs-website": "lt-post6.webp"}


def img_src(key):
    name = PAGE_IMG.get(key)
    return f"/assets/img/{name}" if name and (ROOT / "assets" / "img" / name).exists() else ""


def pic(key, cls="", alt=""):
    """Plain lazy <img> for a PAGE_IMG key (empty string when the file is missing)."""
    name = PAGE_IMG.get(key)
    if not name or not (ROOT / "assets" / "img" / name).exists():
        return ""
    w, h = img_size(name)
    return f'<img class="{cls}" src="/assets/img/{name}" alt="{escape(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async">'


def photo(key, cls, eager=False):
    name = PAGE_IMG.get(key)
    if not name or not (ROOT / "assets" / "img" / name).exists():
        return ""
    w, h = img_size(name)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<div class="{cls}" aria-hidden="true"><img src="/assets/img/{name}" alt="" width="{w}" height="{h}" {load} decoding="async"></div>'


def marquee_html(T):
    words = [T["nav"][k] for k in SERVICE_KEYS if k in T.get("nav", {})]
    row = "".join(f'<span>{escape(w)}</span><i aria-hidden="true">✦</i>' for w in words)
    return f'<section class="marquee" aria-hidden="true"><div class="mq-track" data-marquee>{row}{row}</div></section>'


def band_html():
    img = photo("band", "band-img")
    return f'<section class="band">{img.replace("<img ", "<img data-parallax ")}</section>' if img else ""


def phero(T, P, ctas=True, key=""):
    stats = "".join(f'<div class="stat"><b>{escape(a)}</b><span>{escape(b)}</span></div>' for a, b in P.get("stats", []))
    btns = (f'<div class="ctas"><a class="btn btn-solid" href="#contact">{escape(T["home"]["cta1"])}</a>'
            f'<a class="btn btn-line" href="{url(T, "pricing")}">{escape(T["ui"]["pricing"])}</a></div>') if ctas else ""
    st = f'<div class="pstats">{stats}</div>' if stats else ""
    img = photo(key, "phero-img", eager=True)
    h1 = re.sub(r"<br\s*/?>", " ", P["h1"])
    return f"""<section class="phero{'' if img else ' no-img'}"><div class="wrap">
<div class="phero-txt">{crumbs_html(T, P['crumb'])}
<h1>{h1}</h1>
<p class="lead">{escape(P['lead'])}</p>
{btns}{st}</div>
{img}
</div></section>"""


def process_html(T):
    steps = "".join(f'<div class="step"><h3>{escape(t)}</h3><p>{escape(d)}</p></div>' for t, d in T["process"])
    return f"""<section class="sec sec-fog"><div class="wrap">
<div class="sec-head"><h2>{escape(T['ui']['process'])}</h2></div>
<div class="steps">{steps}</div></div></section>"""


def related_html(T, key):
    links = "".join(f'<a href="{url(T, k)}">{escape(T["nav"][k])}</a>' for k in SERVICE_KEYS if k != key and k in T.get("pages", {}))
    return f'<section class="sec"><div class="wrap"><h2 class="h-m">{escape(T["ui"]["related"])}</h2><div class="rel">{links}</div></div></section>'


def seo_html(blocks):
    inner = "".join(f"<h2>{escape(h)}</h2><p>{escape(p)}</p>" for h, p in blocks)
    return f'<section class="sec"><div class="wrap"><div class="prose">{inner}</div></div></section>'


def price_int(p):
    return int(p.replace("€", "").replace("+", "").replace(",", ""))


def partner_html(P):
    """BalticLeads partnership block (lead-gen page only)."""
    b = P.get("partner")
    if not b:
        return ""
    pts = "".join(f"<li>{escape(x)}</li>" for x in b["points"])
    return f"""<section class="sec line-top"><div class="wrap partner">
<div class="partner-media"><div class="win"><div class="win-bar"><i></i><i></i><i></i><span>balticleads.ee</span></div><div class="win-body"><img src="/assets/img/case-balticleads.webp" alt="BalticLeads" loading="lazy" width="{img_size('case-balticleads.webp')[0]}" height="{img_size('case-balticleads.webp')[1]}"></div></div></div>
<div class="case-info"><h2>{b['title']}</h2><p>{escape(b['text'])}</p><ul class="points">{pts}</ul>
<a class="btn btn-solid" href="https://balticleads.ee/" target="_blank" rel="noopener">{escape(b['cta'])}</a></div></div></section>"""


def page_service(key):
    def render(T, ALL):
        if key.startswith("niche:"):
            P = T["niches"][key[6:]]
        else:
            P = T["pages"][key]
        feats = "".join(
            f'<div class="card"><span class="n">0{i + 1}</span><h3 class="h-s">{escape(t)}</h3><p>{escape(d)}</p>'
            + (f'<span class="from"><small class="muted">{escape(T["ui"]["from"])}</small> {f}</span>' if f else "") + "</div>"
            for i, (t, d, f) in enumerate(P["feats"]))
        body = f"""{phero(T, P, key=P.get("img", key.split(":")[-1]))}
<section class="sec"><div class="wrap">
<div class="sec-head"><h2>{P['feat_title']}</h2></div>
<div class="cards">{feats}</div></div></section>
{partner_html(P)}
{process_html(T)}
{seo_html(P['seo'])}
{faq_html(T, P['faq'])}
{posts_related(T, P.get("posts", []))}
{related_html(T, key)}"""
        prices = [price_int(f) for _, _, f in P["feats"] if f]
        service = {"@type": "Service", "name": P["crumb"], "serviceType": P["crumb"], "description": P["desc"],
                   "provider": {"@id": f"{SITE}/#org"}, "areaServed": ["EE", "LT", "LV", "FI", "EU"], "url": url(T, key, True)}
        if prices:
            service["offers"] = {"@type": "AggregateOffer", "lowPrice": min(prices), "priceCurrency": "EUR"}
        schema = graph(org_schema(T), service, crumbs_schema(T, key, P["crumb"]), faq_schema(P["faq"]))
        return layout(T, ALL, key, body, P, schema)
    return render


def page_portfolio(T, ALL):
    P = T["portfolio"]
    body = f"""{phero(T, P, ctas=False, key="portfolio")}
<section class="sec line-top"><div class="wrap">{case_cards(T, pick_cases(T, PORTFOLIO_CASES))}</div></section>
<section class="sec line-top"><div class="wrap incl"><div><h2 class="h-l" data-split>{P['more_title']}</h2></div><p class="lead fade">{escape(P['more'])}</p></div></section>"""
    items = [{"@type": "CreativeWork", "name": c["name"], "description": c["text"], **({"url": c["url"]} if c.get("url") else {})} for c in pick_cases(T, PORTFOLIO_CASES)]
    schema = graph(org_schema(T), {"@type": "CollectionPage", "name": P["title"], "url": url(T, "portfolio", True),
                                   "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": it} for i, it in enumerate(items)]}},
                   crumbs_schema(T, "portfolio", P["crumb"]))
    return layout(T, ALL, "portfolio", body, P, schema)


def tier_cards(T, rows):
    out = []
    for n, p, per, feats in rows:
        per_s = {"once": T["ui"]["once"], "month": T["ui"]["month"]}.get(per, "")
        li = "".join(f"<li>{escape(x)}</li>" for x in feats)
        per_html = f' <small class="muted" style="font-size:14px">{escape(per_s)}</small>' if per_s else ""
        out.append(f'<div class="tier"><span class="muted">{escape(n)}</span><b><small class="muted" style="font-size:14px">{escape(T["ui"]["from"])}</small> {p}{per_html}</b><ul>{li}</ul></div>')
    return "".join(out)


def page_pricing(T, ALL):
    P = T["pricing"]
    plat = T["pages"]["platforms"]["feats"]
    plat_html = "".join(f'<div class="prow"><span>{escape(n)}</span><b>{escape(T["ui"]["from"])} {f}</b></div>' for n, _, f in plat)
    addons = "".join(f'<div class="prow"><span>{escape(n)}</span><b>{p}</b></div>' for n, p in P["addons"])
    body = f"""{phero(T, P, ctas=False, key="pricing")}
<section class="sec line-top"><div class="wrap"><h2 class="h-l" data-split>{P['web_title']}</h2><div class="tiers fade">{tier_cards(T, P['web'])}</div></div></section>
<section class="sec line-top"><div class="wrap"><h2 class="h-l" data-split>{P['mkt_title']}</h2><div class="tiers fade">{tier_cards(T, P['mkt'])}</div></div></section>
<section class="sec line-top"><div class="wrap incl"><div><h2 class="h-l" data-split>{P['plat_title']}</h2><p class="lead fade" style="margin-top:24px">{escape(P['note'])}</p></div>
<div class="fade"><div class="plist">{plat_html}</div><h3 class="h-s" style="margin:40px 0 10px">{escape(P['addons_title'])}</h3><div class="plist">{addons}</div></div></div></section>
{faq_html(T, P['faq'])}"""
    offers = []
    for n, p, per, _ in P["web"] + P["mkt"]:
        spec = {"@type": "UnitPriceSpecification", "minPrice": price_int(p), "priceCurrency": "EUR"}
        if per == "month":
            spec["unitText"] = "MONTH"
        offers.append({"@type": "Offer", "name": n, "priceCurrency": "EUR", "price": price_int(p), "priceSpecification": spec})
    schema = graph(org_schema(T), {"@type": "OfferCatalog", "name": P["title"], "url": url(T, "pricing", True), "itemListElement": offers},
                   crumbs_schema(T, "pricing", P["crumb"]), faq_schema(P["faq"]))
    return layout(T, ALL, "pricing", body, P, schema)


def page_legal(key):
    def render(T, ALL):
        P = T["legal"][key]
        body = f"""<section class="phero"><div class="wrap">{crumbs_html(T, P['crumb'])}<h1 class="h-l" data-split>{escape(P['h1'])}</h1>
<p class="muted" style="margin-top:20px">{escape(T['ui']['updated'])}: {escape(P['updated'])}</p></div></section>
<section class="sec line-top" style="padding-top:60px"><div class="wrap"><div class="prose">{P['body']}</div></div></section>"""
        return layout(T, ALL, key, body, P, graph(org_schema(T), crumbs_schema(T, key, P["crumb"])))
    return render


def post_card(T, k):
    p = T["blog"]["posts"][k]
    cover = pic("post:" + k, "", p["h1"])
    cover = f'<div class="post-cover">{cover}</div>' if cover else ""
    return (f'<a class="post" href="{url(T, "post:" + k)}">{cover}<span class="case-n">{escape(p["date"])} · {p["minutes"]} {escape(T["blog"]["read"])}</span>'
            f'<h3 class="h-s">{escape(p["h1"])}</h3><p>{escape(p["lead"])}</p><span class="go">{ARR_UP}</span></a>')


def posts_related(T, keys):
    keys = [k for k in keys if k in T.get("blog", {}).get("posts", {})]
    if not keys:
        return ""
    return f'<section class="sec sec-fog"><div class="wrap"><div class="sec-head"><h2 class="h-m">{escape(T["blog"]["crumb"])}</h2></div><div class="posts">{"".join(post_card(T, k) for k in keys)}</div></div></section>'


def page_blog(T, ALL):
    B = T["blog"]
    body = f"""<section class="phero no-img"><div class="wrap"><div class="phero-txt">{crumbs_html(T, B['crumb'])}<h1>{B['h1']}</h1><p class="lead">{escape(B['lead'])}</p></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="posts">{"".join(post_card(T, k) for k in B["posts"])}</div></div></section>"""
    items = [{"@type": "ListItem", "position": i + 1, "url": url(T, "post:" + k, True), "name": p["h1"]} for i, (k, p) in enumerate(B["posts"].items())]
    schema = graph(org_schema(T), {"@type": "Blog", "name": B["title"], "url": url(T, "blog", True), "inLanguage": T["lang"],
                                   "publisher": {"@id": f"{SITE}/#org"}}, {"@type": "ItemList", "itemListElement": items}, crumbs_schema(T, "blog", B["crumb"]))
    return layout(T, ALL, "blog", body, B, schema)


def page_post(k):
    def render(T, ALL):
        B, p = T["blog"], T["blog"]["posts"][k]
        key = "post:" + k
        crumbs = (f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{url(T, "home")}">{escape(T["ui"]["home"])}</a><span>/</span>'
                  f'<a href="{url(T, "blog")}">{escape(B["crumb"])}</a></nav>')
        rel = "".join(f'<a href="{url(T, s)}"><span>{escape(T["nav"][s])}</span>{ARR_UP}</a>' for s in p.get("services", []) if s in T.get("pages", {}))
        others = [o for o in B["posts"] if o != k][:3]
        body = f"""<section class="phero">{photo("post:" + k, "phero-img", eager=True)}<div class="wrap">{crumbs}<h1 class="h-l" data-split>{escape(p['h1'])}</h1>
<p class="lead fade">{escape(p['lead'])}</p><p class="case-n" style="margin-top:22px">{escape(p['date'])} · {p['minutes']} {escape(B['read'])}</p></div></section>
<section class="sec line-top" style="padding-top:60px"><div class="wrap"><article class="prose article">{p['body']}</article></div></section>
{faq_html(T, p['faq']) if p.get('faq') else ''}
{f'<section class="sec line-top"><div class="wrap"><span class="eyebrow">{escape(T["ui"]["related"])}</span><div class="rel fade">{rel}</div></div></section>' if rel else ''}
{posts_related(T, others)}"""
        art = {"@type": "BlogPosting", "headline": p["h1"], "description": p["desc"], "datePublished": p["iso"], "dateModified": p["iso"],
               "inLanguage": T["lang"], "mainEntityOfPage": url(T, key, True), "image": f"{SITE}/assets/img/og-{T['lang']}.jpg",
               "author": {"@id": f"{SITE}/#org"}, "publisher": {"@id": f"{SITE}/#org"}}
        bc = {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": T["ui"]["home"], "item": url(T, "home", True)},
            {"@type": "ListItem", "position": 2, "name": B["crumb"], "item": url(T, "blog", True)},
            {"@type": "ListItem", "position": 3, "name": p["h1"], "item": url(T, key, True)}]}
        schema = graph(org_schema(T), art, bc, faq_schema(p["faq"]) if p.get("faq") else None)
        return layout(T, ALL, key, body, p, schema)
    return render


PAGES = {"home": page_home, **{k: page_service(k) for k in SERVICE_KEYS},
         "portfolio": page_portfolio, "pricing": page_pricing, "privacy": page_legal("privacy"), "terms": page_legal("terms"),
         "blog": page_blog}


def all_pages(ALL):
    """Static pages plus per-language dynamic ones (industries, blog posts); keys are shared across languages."""
    pages = dict(PAGES)
    for T in ALL.values():
        for k in T.get("niches", {}):
            pages["niche:" + k] = page_service("niche:" + k)
        for k in T.get("blog", {}).get("posts", {}):
            pages["post:" + k] = page_post(k)
    return pages


def has_page(T, key):
    if key == "home":
        return True
    if key in SERVICE_KEYS:
        return key in T.get("pages", {})
    if key.startswith("niche:"):
        return key[6:] in T.get("niches", {})
    if key.startswith("post:"):
        return key[5:] in T.get("blog", {}).get("posts", {})
    if key in ("privacy", "terms"):
        return key in T.get("legal", {})
    return key in T

# old URLs from the previous site that are not reused 1:1
REDIRECTS = {"et.html": "/et/", "ru.html": "/ru/"}


def page_404(T, ALL):
    body = f"""<section class="phero" style="min-height:70vh"><div class="wrap"><p class="eyebrow">404</p>
<h1 class="h-xl" style="margin-top:22px">{escape(T['ui']['notfound'])}</h1><p class="lead" style="margin-top:24px">{escape(T['ui']['notfound_text'])}</p>
<div class="ctas" style="margin-top:36px"><a class="btn btn-solid" href="/">{escape(T['ui']['back'])} {ARR}</a></div></div></section>"""
    html = layout(T, ALL, "home", body, {"title": "404 | BoostLab", "desc": T["ui"]["notfound_text"]}, graph(org_schema(T)))
    html = html.replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')
    return html.replace(f'<link rel="canonical" href="{SITE}/">', "")


def redirect_html(to):
    return (f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>BoostLab</title><link rel="canonical" href="{SITE}{to}">'
            f'<meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={to}"></head>'
            f'<body><a href="{to}">{SITE}{to}</a><script>location.replace("{to}")</script></body></html>')


def sitemap(ALL, built):
    today = date.today().isoformat()
    rows = []
    for T in ALL.values():
        for key in all_pages(ALL):
            if (T["lang"], key) not in built:
                continue
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{L["lang"]}" href="{url(L, key, True)}"/>'
                           for L in ALL.values() if (L["lang"], key) in built)
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url(ALL["en"], key, True)}"/>'
            pr = "1.0" if key == "home" else "0.3" if key in ("privacy", "terms") else "0.8"
            rows.append(f"<url><loc>{url(T, key, True)}</loc>{alts}<lastmod>{today}</lastmod><priority>{pr}</priority></url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")


def og_image(T):
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    ttf = str(SRC / "fonts" / "Onest.ttf")

    def F(size, wght=600):
        f = ImageFont.truetype(ttf, size)
        try:
            f.set_variation_by_axes([wght])
        except Exception:
            pass
        return f
    # photo panel on the right, text on the left - same split as the site hero
    ph = Image.open(ROOT / "assets" / "img" / "lt-hero.webp").convert("RGB")
    k = max(520 / ph.width, 550 / ph.height)
    ph = ph.resize((round(ph.width * k), round(ph.height * k)))
    left, top = (ph.width - 520) // 2, (ph.height - 550) // 2
    ph = ph.crop((left, top, left + 520, top + 550))
    mask = Image.new("L", ph.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, ph.width, ph.height], 18, fill=255)
    im.paste(ph, (640, 40), mask)
    d.rounded_rectangle([70, 64, 114, 108], 10, fill="#13212E")
    d.text((80, 66), "B", font=F(32, 700), fill="#FFFFFF")
    d.ellipse([101, 95, 109, 103], fill="#D88A4C")
    d.text((128, 70), "BoostLab", font=F(30, 700), fill="#13212E")
    # headline = the home page H1, wrapped to the text column
    words, lines, cur = re.sub(r"<[^>]+>", " ", T["home"]["h1"]).split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=F(48)) > 520 and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    y = 180
    for ln in lines[:4]:
        d.text((70, y), ln, font=F(48, 600), fill="#13212E")
        y += 62
    d.text((70, 520), T["og_foot"], font=F(21, 500), fill="#0F766E")
    return im


def build():
    ALL = {lang: load(lang) for lang in LANGS if (SRC / "content" / f"{lang}.py").exists()}
    # media and links of cases are language independent - EN is the source of truth
    en_cases = {c["id"]: c for c in ALL["en"]["cases"]}
    for T in ALL.values():
        for c in T["cases"]:
            for k in ("img", "url", "mock"):
                c[k] = en_cases[c["id"]].get(k, "")
    # empty dist/ in place (the dev server keeps the directory itself open on Windows)
    DIST.mkdir(exist_ok=True)
    for p in DIST.iterdir():
        shutil.rmtree(p) if p.is_dir() else p.unlink()
    shutil.copytree(ROOT / "assets", DIST / "assets")
    for f in (ROOT / "static").glob("*"):
        shutil.copy(f, DIST / f.name)
    # which (lang, page) pairs exist - languages may be added page by page
    pages = all_pages(ALL)
    built = {(T["lang"], key) for T in ALL.values() for key in pages if has_page(T, key)}
    for T in ALL.values():
        T["_built"] = built
        for key, fn in pages.items():
            if (T["lang"], key) not in built:
                continue
            rel = url(T, key).lstrip("/")
            out = DIST / (rel + "index.html" if rel == "" or rel.endswith("/") else rel)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fn(T, ALL), encoding="utf-8")
        if "og" in T:
            og_image(T).save(DIST / "assets" / "img" / f"og-{T['lang']}.jpg", quality=86)
    (DIST / "404.html").write_text(page_404(ALL["en"], ALL), encoding="utf-8")
    for old, new in REDIRECTS.items():
        if new.strip("/") in ALL:
            (DIST / old).write_text(redirect_html(new), encoding="utf-8")
    (DIST / "sitemap.xml").write_text(sitemap(ALL, built), encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print(f"built {len(built)} pages for {list(ALL)} -> {DIST}")


if __name__ == "__main__":
    build()
