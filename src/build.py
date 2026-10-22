"""Static site generator for boostlab.lt.

python src/build.py  ->  dist/  (published by GitHub Pages workflow)
Content lives in src/content/<lang>.py, page templates are functions below.
"""
import json
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
    for name in (f"{lang}.py", f"{lang}_pages.py", f"{lang}_extra.py"):
        f = SRC / "content" / name
        if f.exists():
            exec(compile(f.read_text(encoding="utf-8"), str(f), "exec"), ns)
    return ns["T"]


def url(T, key, absolute=False):
    prefix = "/" if T["lang"] == "en" else f"/{T['lang']}/"
    u = prefix + T["slugs"][key]
    return SITE + u if absolute else u


ARR = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" class="arr"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARR_UP = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 17L17 7M8 7h9v9"/></svg>'
SERVICE_KEYS = ["web", "crm", "platforms", "apps", "ads", "smm"]
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
    menu_html = "".join(
        f'<a href="{url(T, k)}"' + (' aria-current="page"' if k == key else "") + f">{escape(lbl)}</a>" for k, lbl in menu
    ) + BL_TAB
    drawer = "".join(f'<a class="dl" href="{url(T, k)}">{escape(T["nav"][k])}</a>' for k in SERVICE_KEYS)
    drawer += f'<a class="dl" href="{url(T, "portfolio")}">{escape(u["work"])}</a><a class="dl" href="{url(T, "pricing")}">{escape(u["pricing"])}</a>'
    drawer += BL_TAB.replace('class="bl-tab"', 'class="dl bl-tab"')
    og_img = f"{SITE}/assets/img/og-{T['lang']}.jpg"
    preload_three = (
        f'<link rel="modulepreload" href="{CDN["three"]}" crossorigin>' if stage else ""
    )
    scripts = (
        f'<script src="{CDN["lenis"]}" defer></script><script src="/assets/js/site.js?v={V}" defer></script>'
    )
    if stage:
        scripts += (
            '<script type="importmap">' + json.dumps({"imports": {"three": CDN["three"], "three/addons/": CDN["three_addons"]}}) + "</script>"
            f'<script type="module" src="/assets/js/scene.js?v={V}"></script>'
        )
    pre = (
        '<div class="pre" aria-hidden="true"><div class="pre-in"><div class="pre-logo">BOOST<span>LAB</span></div>'
        '<div class="pre-bar"><i></i></div></div></div>'
        if stage else ""
    )
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
<meta name="theme-color" content="#060608">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BoostLab">
<meta property="og:locale" content="{T['locale']}">
<meta property="og:title" content="{escape(meta['title'])}">
<meta property="og:description" content="{escape(meta['desc'])}">
<meta property="og:url" content="{url(T, key, True)}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
{preload_three}
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600&family=Unbounded:wght@300;400;500&display=swap&subset=cyrillic,latin-ext" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css?v={V}">
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('consent','default',{{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500}});gtag('js',new Date());{''.join(f"gtag('config','{g}');" for g in GA)}window.BL_PIXEL='{PIXEL}';</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA[0]}"></script>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
{pre}
<header class="hdr"><div class="wrap hdr-in">
<a class="logo" href="{url(T, 'home')}" aria-label="BoostLab">BOOST<span>LAB</span></a>
<nav class="menu" aria-label="Main">{menu_html}</nav>
<div class="hdr-r"><div class="langs">{langs}</div><a class="btn btn-solid" href="#contact">{escape(u['cta'])}</a>
<button class="burger" aria-label="{escape(u['menu'])}" aria-expanded="false"><i></i><i></i></button></div>
</div></header>
<div class="drawer">{drawer}<a class="btn btn-solid" href="#contact">{escape(u['cta'])}</a><div class="langs">{langs}</div></div>
<main>
{body}
{cta_block(T)}
</main>
{footer(T)}
<div class="ck" role="dialog" aria-live="polite"><p>{u['ck_text'].format(privacy=url(T, 'privacy'))}</p><div class="ck-b"><button class="no">{escape(u['ck_no'])}</button><button class="ok">{escape(u['ck_ok'])}</button></div></div>
<div class="cur" aria-hidden="true"></div>
{scripts}
</body>
</html>
"""


def cta_block(T):
    c = T["cta_block"]
    return f"""<section class="cta line-top" id="contact"><div class="wrap">
<h2 class="h-xl" data-split>{c['title']}</h2>
<p class="lead fade">{escape(c['lead'])}</p>
<div class="ctas fade"><a class="btn btn-solid" href="mailto:{EMAIL}?subject=BoostLab%20project">{escape(c['mail'])} {ARR}</a><a class="btn btn-line" href="tel:{PHONE}">{escape(c['call'])}</a></div>
<div class="contacts fade"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE}">{PHONE_H}</a></div>
</div></section>"""


def footer(T):
    u = T["ui"]
    svc = "".join(f'<a href="{url(T, k)}">{escape(T["nav"][k])}</a>' for k in SERVICE_KEYS)
    return f"""<footer class="ftr"><div class="wrap">
<div class="ftr-top">
<div class="ftr-about"><a class="logo" href="{url(T, 'home')}">BOOST<span>LAB</span></a><p>{escape(u['about'])}</p></div>
<div class="ftr-col"><h4>{escape(u['f_services'])}</h4>{svc}</div>
<div class="ftr-col"><h4>{escape(u['f_company'])}</h4><a href="{url(T, 'portfolio')}">{escape(u['work'])}</a><a href="{url(T, 'pricing')}">{escape(u['pricing'])}</a><a href="#contact">{escape(u['contact'])}</a></div>
<div class="ftr-col"><h4>{escape(u['f_contact'])}</h4><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE}">{PHONE_H}</a><a href="https://balticleads.ee/" rel="noopener">BalticLeads.ee</a></div>
</div>
<div class="mega" aria-hidden="true">BOOSTLAB</div>
<div class="ftr-bot"><span>&copy; {date.today().year} FANARI OÜ · BoostLab · Tallinn, Estonia. {escape(u['rights'])}</span>
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
<div class="sec-head"><div><span class="eyebrow">FAQ</span><h2 class="h-l" data-split style="margin-top:22px">{escape(T['ui']['faq'])}</h2></div></div>
<div class="faq fade">{items}</div></div></section>"""


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
        link = (f'<a class="btn btn-line" href="{c["url"]}" target="_blank" rel="noopener">{escape(T["ui"]["visit"])} {ARR_UP}</a>'
                if c.get("url") else "")
        tags = "".join(f'<span class="tag">{escape(t)}</span>' for t in c["tags"])
        host = c["url"].replace("https://", "").rstrip("/") if c.get("url") else c["id"] + ".app"
        li = "".join(f"<li>{escape(x)}</li>" for x in pts.get(c["id"], []))
        out.append(f"""<article class="case-row fade"><div class="case-media"><div class="win"><div class="win-bar"><i></i><i></i><i></i><span>{escape(host)}</span></div><div class="win-body">{media}</div></div></div>
<div class="case-info"><span class="case-n">0{i + 1} / 0{len(cases)}</span><h3 class="h-m">{escape(c['name'])}</h3><div class="case-tags">{tags}</div><p>{escape(c['text'])}</p>{f'<ul class="points">{li}</ul>' if li else ''}{link}</div></article>""")
    return f'<div class="cases-list">{"".join(out)}</div>'


# ---------------------------------------------------------------- pages
def page_home(T, ALL):
    h = T["home"]
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{escape(b)}</span></div>' for a, b in h["s3_stats"])
    steps = "".join(f'<span><i></i>0{i + 1} {escape(x)}</span>' for i, x in enumerate(h["steps"]))
    hot = "".join(f'<div class="hot hot-{i}"><b>{escape(t)}</b><span>{escape(d)}</span></div>' for i, (t, d) in enumerate(h["hot"]))
    nums = "".join(
        f'<div class="num fade"><small>{escape(s)}</small><b data-count="{n}" data-suf="{escape(suf)}">{n}{escape(suf)}</b><p>{escape(p)}</p></div>'
        for s, n, suf, p in h["nums"])
    svc = "".join(
        f'<a href="{url(T, k)}"><span class="n">0{i + 1}</span><h3 class="h-m">{escape(t)}</h3><p>{escape(d)}</p><span class="go">{ARR_UP}</span></a>'
        for i, (k, t, d) in enumerate(h["svc"]))
    incl = "".join(f"<li>{escape(x)}</li>" for x in h["incl"])
    tiers = "".join(
        f'<div class="tier"><span class="muted">{escape(n)}</span><b><small class="muted" style="font-size:14px">{escape(T["ui"]["from"])}</small> {p}</b><ul>{"".join(f"<li>{escape(x)}</li>" for x in f)}</ul></div>'
        for n, p, f in h["tiers"])
    body = f"""
<section class="stage" aria-label="BoostLab">
<div class="stage-pin">
<div class="stage-fallback"></div>
<canvas id="scene" aria-hidden="true"></canvas>
<div class="stage-shade"></div>
<div class="steps-bar" aria-hidden="true">{steps}</div>
<div class="sc sc-hero">
<span class="eyebrow fade">01 / {escape(h["steps"][0])} · {escape(h["eyebrow"])}</span>
<h1 class="h-xl" data-split style="margin-top:22px">{h['h1']}</h1>
<p class="lead fade">{escape(h['lead'])}</p>
<div class="ctas fade"><a class="btn btn-solid" href="#contact">{escape(h['cta1'])} {ARR}</a><a class="btn btn-line" href="#work">{escape(h['cta2'])}</a></div>
</div>
<div class="sc sc-2"><span class="eyebrow">{escape(h['reveal_kicker'])}</span><p class="h-l" style="margin:20px 0 18px">{h['reveal_title']}</p><p class="lead">{escape(h['reveal_text'])}</p></div>
<div class="sc sc-hot">{hot}</div>
<div class="sc sc-3"><div><span class="eyebrow" style="margin-bottom:22px">{escape(h['final_kicker'])}</span><div class="stats">{stats}</div></div><a class="btn btn-solid" href="#contact">{escape(h['s3_cta'])} {ARR}</a></div>
<div class="scroll-cue" aria-hidden="true"><i></i>{escape(T['ui']['scroll'])}</div>
</div>
</section>

<section class="sec"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">{escape(h['nums_kicker'])}</span><h2 class="h-l" data-split style="margin-top:22px">{h['nums_title']}</h2></div></div>
<div class="nums">{nums}</div>
</div></section>

{band_html()}

<section class="sec line-top" id="services"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">{escape(h['svc_kicker'])}</span><h2 class="h-l" data-split style="margin-top:22px">{h['svc_title']}</h2></div><p class="lead fade">{escape(h['svc_lead'])}</p></div>
<div class="svc">{svc}</div>
</div></section>

<section class="cases sec line-top" id="work">
<div class="wrap"><div class="sec-head"><div><span class="eyebrow">{escape(h['cases_kicker'])}</span><h2 class="h-l" data-split style="margin-top:22px">{h['cases_title']}</h2></div>
<p class="lead fade"><a class="btn btn-line" href="{url(T, 'portfolio')}">{escape(T['ui']['work'])} {ARR}</a></p></div></div>
<div class="wrap"><p class="lead fade" style="margin:-10px 0 34px;max-width:760px">{escape(h['cases_lead'])}</p>{case_cards(T, pick_cases(T, HOME_CASES))}</div>
</section>

<section class="sec line-top"><div class="wrap incl">
<div><span class="eyebrow">{escape(h['incl_kicker'])}</span><h2 class="h-l" data-split style="margin:22px 0 24px">{h['incl_title']}</h2><p class="lead fade">{escape(h['incl_lead'])}</p></div>
<ul class="fade">{incl}</ul>
</div></section>

<section class="sec"><div class="wrap">
<span class="eyebrow">{escape(h['price_kicker'])}</span>
<div class="price" style="margin-top:30px">
<div><p class="muted" style="margin-bottom:14px">{escape(h['price_from'])}</p><p class="big"><small>€</small><span data-count="700">700</span></p></div>
<div class="price-r"><p class="lead">{escape(h['price_note'])}</p><a class="btn btn-solid" href="#contact">{escape(h['price_cta'])} {ARR}</a><a class="btn btn-line" href="{url(T, 'pricing')}">{escape(h['price_all'])} {ARR}</a></div>
</div>
<div class="tiers fade">{tiers}</div>
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
    return layout(T, ALL, "home", body, {"title": h["title"], "desc": h["desc"]}, schema, stage=True)


def crumbs_html(T, label):
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{url(T, "home")}">{escape(T["ui"]["home"])}</a><span>/</span><span>{escape(label)}</span></nav>'


def crumbs_schema(T, key, label):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": T["ui"]["home"], "item": url(T, "home", True)},
        {"@type": "ListItem", "position": 2, "name": label, "item": url(T, key, True)}]}


# stock photos (CC0, no people/logos) per page key; missing files are simply skipped
PAGE_IMG = {"web": "stock-web.webp", "crm": "stock-crm.webp", "platforms": "stock-platforms.webp", "apps": "stock-apps.webp",
            "ads": "stock-ads.webp", "smm": "stock-smm.webp", "portfolio": "stock-portfolio.webp", "pricing": "stock-pricing.webp",
            "band": "stock-home.webp"}


def photo(key, cls, eager=False):
    name = PAGE_IMG.get(key)
    if not name or not (ROOT / "assets" / "img" / name).exists():
        return ""
    w, h = img_size(name)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<div class="{cls}" aria-hidden="true"><img src="/assets/img/{name}" alt="" width="{w}" height="{h}" {load} decoding="async"></div>'


def band_html():
    img = photo("band", "band-img")
    return f'<section class="band">{img.replace("<img ", "<img data-parallax ")}</section>' if img else ""


def phero(T, P, ctas=True, key=""):
    stats = "".join(f'<div class="stat"><b>{escape(a)}</b><span>{escape(b)}</span></div>' for a, b in P.get("stats", []))
    btns = (f'<div class="ctas fade"><a class="btn btn-solid" href="#contact">{escape(T["home"]["cta1"])} {ARR}</a>'
            f'<a class="btn btn-line" href="{url(T, "pricing")}">{escape(T["ui"]["pricing"])}</a></div>') if ctas else ""
    st = f'<div class="pstats fade">{stats}</div>' if stats else ""
    return f"""<section class="phero">{photo(key, "phero-img", eager=True)}<div class="wrap">
{crumbs_html(T, P['crumb'])}
<h1 class="h-xl" data-split>{P['h1']}</h1>
<p class="lead fade">{escape(P['lead'])}</p>
{btns}{st}
</div></section>"""


def process_html(T):
    steps = "".join(f'<div class="step fade"><span class="n">0{i + 1}</span><h3 class="h-s">{escape(t)}</h3><p>{escape(d)}</p></div>'
                    for i, (t, d) in enumerate(T["process"]))
    return f"""<section class="sec line-top"><div class="wrap">
<div class="sec-head"><div><span class="eyebrow">{escape(T['ui']['process'])}</span></div></div>
<div class="steps">{steps}</div></div></section>"""


def related_html(T, key):
    links = "".join(f'<a href="{url(T, k)}"><span>{escape(T["nav"][k])}</span>{ARR_UP}</a>' for k in SERVICE_KEYS if k != key)
    return f'<section class="sec line-top"><div class="wrap"><span class="eyebrow">{escape(T["ui"]["related"])}</span><div class="rel fade">{links}</div></div></section>'


def seo_html(blocks):
    inner = "".join(f"<h2>{escape(h)}</h2><p>{escape(p)}</p>" for h, p in blocks)
    return f'<section class="sec line-top"><div class="wrap"><div class="prose fade">{inner}</div></div></section>'


def price_int(p):
    return int(p.replace("€", "").replace("+", "").replace(",", ""))


def page_service(key):
    def render(T, ALL):
        P = T["pages"][key]
        feats = "".join(
            f'<div class="card fade"><span class="n">0{i + 1}</span><h3 class="h-s">{escape(t)}</h3><p>{escape(d)}</p>'
            + (f'<span class="from"><small class="muted">{escape(T["ui"]["from"])}</small> {f}</span>' if f else "") + "</div>"
            for i, (t, d, f) in enumerate(P["feats"]))
        body = f"""{phero(T, P, key=key)}
<section class="sec line-top"><div class="wrap">
<div class="sec-head"><div><h2 class="h-l" data-split>{P['feat_title']}</h2></div></div>
<div class="cards">{feats}</div></div></section>
{process_html(T)}
{seo_html(P['seo'])}
{faq_html(T, P['faq'])}
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


PAGES = {"home": page_home, **{k: page_service(k) for k in SERVICE_KEYS},
         "portfolio": page_portfolio, "pricing": page_pricing, "privacy": page_legal("privacy"), "terms": page_legal("terms")}

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
        for key in PAGES:
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
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    W, H = 1200, 630
    base = Image.new("RGB", (W, H), "#060608")
    glow = Image.new("RGB", (W, H), "#060608")
    ImageDraw.Draw(glow).ellipse([640, 110, 1260, 730], fill="#6a3c1a")
    im = Image.blend(base, glow.filter(ImageFilter.GaussianBlur(130)), 0.9)
    d = ImageDraw.Draw(im)
    ttf = str(SRC / "fonts" / "Unbounded.ttf")

    def F(size, wght=400):
        f = ImageFont.truetype(ttf, size)
        try:
            f.set_variation_by_axes([wght])
        except Exception:
            pass
        return f
    d.text((70, 70), "BOOST", font=F(30), fill="#ECE8E1")
    d.text((70 + d.textlength("BOOST", font=F(30)), 70), "LAB", font=F(30), fill="#D88A4C")
    y = 220
    for i, ln in enumerate(T["og"]):
        d.text((70, y), ln, font=F(62), fill="#D88A4C" if i == len(T["og"]) - 1 else "#ECE8E1")
        y += 82
    d.text((70, 540), T["og_foot"], font=F(20, 300), fill="#8E8A84")
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
    built = set()
    for T in ALL.values():
        for key in PAGES:
            ok = key == "home" or (key in SERVICE_KEYS and key in T.get("pages", {})) or \
                 (key == "portfolio" and "portfolio" in T) or (key == "pricing" and "pricing" in T) or \
                 (key in ("privacy", "terms") and key in T.get("legal", {}))
            if ok:
                built.add((T["lang"], key))
    for T in ALL.values():
        T["_built"] = built
        for key, fn in PAGES.items():
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
