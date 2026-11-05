# `<lang>_blog2.py` - four more blog posts (written natively per language)

Executed after `<lang>_seo.py`. It must ONLY add posts:

```python
T["blog"]["posts"].update({
    "ecommerce-cost": {...},
    "crm-construction": {...},
    "google-ads-small-business": {...},
    "redesign-without-seo-loss": {...},
})
```

Each post has exactly the same keys as the existing posts in `<lang>_seo.py`:
`slug, title (<=60), desc (120-155), h1, lead (1-2 sentences), date, iso, minutes, body (HTML), faq (3 pairs), services (keys)`.
Date: 5 November 2026 (localized like existing posts), iso "2026-11-05". Allowed body tags: p, h2, h3, ul, ol, li, strong, em, table, thead, tbody, tr, th, td, a.
Internal links: absolute paths of the SAME language (service pages, pricing, niche pages, other posts - take slugs from `<lang>.py`, `<lang>_seo.py`).
800-1100 words each (Estonian/Lithuanian may be ~15% fewer words), genuinely useful, specific, no fluff, no em/en dashes (use "-").

Fixed facts (do not invent other numbers about BoostLab):
- Prices: landing page €700, business website €1,700, online store €3,500, platform/CRM €4,500, ads campaign setup €599, ads+SMM €1,399/month, dedicated specialist €2,500/month.
- Timelines: landing 5-7 working days, business site 2-3 weeks, online store 3-5 weeks, CRM/platform from 4 weeks.
- BoostLab: studio in Tallinn, 200+ websites a year, 2 large international projects (RentMe, BalticLeads). Recommended local ads budget at least €500-1,000/month ad spend (management fee separate). Accounts are created in the client's name.
- Generic market facts are fine when common knowledge (Estonian bank links, Montonio, Stripe, Omniva/DPD/SmartPosti parcel lockers, VAT 24% in Estonia from 2025, Google Ads auction basics, Quality Score, conversion tracking, 301 redirects, Search Console). Do NOT invent statistics, studies, client names or results.

Topics:
1. ecommerce-cost - how much an online store costs in Estonia/Baltics: table by scope, what drives price (catalogue size, payments, shipping integrations, accounting export, languages), monthly running costs (hosting, payment fees, maintenance), custom vs Shopify/WooCommerce trade-offs honestly, how to get a fixed quote. services: ["web"], link the e-commerce niche page.
2. crm-construction - CRM for a construction / renovation company: leads from site, estimates/quotes, object (site) cards, subcontractors, photo reports, acts and invoices, material costs, mobile use on site; build vs off-the-shelf. services: ["crm"].
3. google-ads-small-business - Google Ads for a small business in Estonia: budget logic, search vs Performance Max, keywords and negative keywords, landing page quality, conversion tracking (calls, forms, email clicks), first 30 days plan, typical mistakes. services: ["ads", "web"].
4. redesign-without-seo-loss - redesign a website without losing Google rankings: URL inventory, 301 redirect map, keep ranking content, metadata, hreflang for multilingual, Search Console checks, speed, post-launch monitoring checklist (table). services: ["web"].
