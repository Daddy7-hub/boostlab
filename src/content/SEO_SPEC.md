# `<lang>_seo.py` - content spec (lead-gen page, industry pages, blog)

Executed after `<lang>.py`, `<lang>_pages.py`, `<lang>_extra.py`; it extends the existing dict `T`.
Keys (`leadgen`, niche ids, post ids) MUST be identical in every language - they link translations via hreflang.
Prices are fixed facts - copy them exactly: landing €700, business site €1,700, online store €3,500,
platform/CRM €4,500, ads setup €599, ads+SMM €1,399/month, rental platform €21,790, ticketing €18,790,
marketplace €19,790, Android app +€4,970, iOS app +€5,970. Plain hyphen "-" only, never em/en dashes.

```python
T["ui"]["f_industries"] = "..."            # footer column title, e.g. "Industries"
T["nav"]["leadgen"] = "..."                # menu label, e.g. "B2B lead generation"
T["slugs"]["leadgen"] = "<localized-slug>.html"
T["slugs"]["blog"] = "blog/"               # same in all languages

T["pages"]["leadgen"] = {                  # same shape as other service pages + "partner" + "posts"
    "title": "...<=60 chars", "desc": "...120-155 chars", "crumb": "...",
    "h1": 'Text with <span class="acc">accent</span>', "lead": "...",
    "stats": [("1.4M", "..."), ("4", "..."), ("...", "...")],        # 3 items
    "feat_title": 'What we <span class="acc">do</span>',
    "feats": [("title", "text", "€599" or "")],                       # 4-6 items
    "partner": {"kicker": "...", "title": 'HTML with <span class="acc">..</span>', "text": "...",
                "points": ["...", "...", "..."], "cta": "Open BalticLeads"},
    "seo": [("h2", "paragraph"), ...],                                # 3 blocks, 80-140 words each
    "faq": [("question", "answer"), ...],                             # 4-5
    "posts": ["b2b-leads-baltics"],                                   # related blog post ids
}

T["niches"] = {   # ids fixed: "ecommerce", "clinics", "rental", "restaurants" (this order)
    "ecommerce": {"slug": "<localized>.html", "nav": "short footer label",
                  ...same keys as a service page (title, desc, crumb, h1, lead, stats, feat_title, feats, seo, faq)...,
                  "posts": ["website-cost", ...]},
    ...
}

T["blog"] = {
    "title": "<=60", "desc": "120-155", "crumb": "Blog", "h1": 'HTML', "lead": "...", "read": "min read",
    "posts": {   # ids fixed, this order
        "website-cost": {"slug": "<localized>.html", "title": "<=60", "desc": "120-155", "h1": "...", "lead": "1-2 sentences",
                         "date": "23 October 2026 (localized)", "iso": "2026-10-23", "minutes": 6,
                         "body": "<p>..</p><h2>..</h2><p>..</p><ul><li>..</li></ul><table>..</table> ...",
                         "faq": [("q", "a"), ...],            # 3
                         "services": ["web", "crm"]},         # related service keys from: web crm platforms apps ads smm leadgen
        "custom-crm-vs-saas": {...}, "booking-system": {...}, "b2b-leads-baltics": {...},
        "seo-checklist": {...}, "landing-vs-website": {...},
    },
}
```

Body HTML: only `p, h2, h3, ul, ol, li, strong, em, table, thead, tbody, tr, th, td, a`.
Internal links in bodies use absolute site paths of the SAME language (e.g. `/ru/ceny.html`, `/crm-development.html`).
700-1100 words per article, genuinely useful, specific numbers, no fluff, no invented statistics or clients.
