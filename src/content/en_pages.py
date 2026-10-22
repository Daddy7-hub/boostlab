# Inner pages (EN). Executed after en.py, extends T.
T["ui"].update({
    "process": "How we work", "related": "Related services", "cases_here": "Built by us", "included": "Included",
    "updated": "Last updated", "notfound": "Page not found", "notfound_text": "The page you are looking for has moved or never existed.", "back": "Back to home",
    "month": "/ month", "once": "one-time", "plus_custom": "+ customisation",
})

T["process"] = [
    ("Brief", "A 30-minute call. We learn the business, the audience and the goal, then send a fixed quote."),
    ("Design", "Structure, copy and an interactive prototype. You approve before a line of code is written."),
    ("Build", "Clean code, CMS or admin panel, integrations, analytics and SEO set up from the start."),
    ("Launch & grow", "Go-live, tracking checks, ads and content. Support and improvements after launch."),
]

T["pages"] = {
    "web": {
        "title": "Website Development in Tallinn & the Baltics | BoostLab",
        "desc": "Website development: landing pages from €700, business sites from €1,700, e-commerce and web platforms. Fast, SEO-ready, multilingual.",
        "crumb": "Web development",
        "h1": "Website <span class=\"acc\">development</span>",
        "lead": "Landing pages, corporate websites and online stores that load in under two seconds, rank in Google and turn visitors into requests.",
        "stats": [("5-7", "days for a landing page"), ("200+", "websites a year"), ("4", "languages we write in")],
        "feat_title": "What we <span class=\"acc\">build</span>",
        "feats": [
            ("Landing pages", "One page, one goal. Sharp copy, fast loading, a form or booking that works, analytics and ads tracking from day one.", "€700"),
            ("Business websites", "Multi-page websites with custom design, CMS, blog, multilingual structure and a technical SEO base.", "€1,700"),
            ("Online stores", "E-commerce with catalogue, filters, bank-link and card payments, shipping integrations and order management.", "€3,500"),
            ("Web platforms", "Customer accounts, admin panel, bookings, payments and API integrations for complex business logic.", "€4,500"),
        ],
        "cases": ["balticleads", "after"],
        "seo": [
            ("Website development in Estonia, Lithuania and Latvia", "BoostLab is a web development studio based in Tallinn. We design and build websites for companies in Estonia, Lithuania, Latvia, Finland and across Europe, and deliver more than 200 websites a year for clients worldwide. Each project gets its own design - no off-the-shelf themes - and is built mobile-first with clean, fast code."),
            ("Websites that are ready for Google", "Search visibility is planned before design starts. We build a logical page structure around the keywords your customers use, add schema markup, set up hreflang for multilingual versions, optimise images and fonts and keep Core Web Vitals in the green. After launch you get Google Analytics 4, Search Console and conversion tracking already working."),
            ("Fixed price, clear timeline", "A landing page takes 5-7 working days, a business website 2-3 weeks, an online store 3-5 weeks. You receive a fixed quote after a short call and see progress through a prototype you can click before development."),
        ],
        "faq": [
            ("How much does a website cost?", "Landing pages start at €700, business websites at €1,700, online stores at €3,500 and web platforms at €4,500. The final price depends on the number of pages, languages and integrations. You get a fixed quote after a free call."),
            ("Which CMS do you use?", "It depends on the project. For content websites we use a lightweight CMS that your team can edit without a developer. For platforms we build a custom admin panel. You always own the code and the content."),
            ("Do you write the texts?", "Yes. We write conversion copy in English, Estonian, Russian and Lithuanian and can coordinate translations to other languages."),
            ("Can you redesign my website without losing Google rankings?", "Yes. We map old URLs to new ones, set up redirects, keep the content that ranks and monitor Search Console after launch."),
            ("Is hosting included?", "We set up hosting, SSL, backups and the domain for you. Hosting is billed at cost, or we deploy to your own server."),
        ],
    },
    "crm": {
        "title": "Custom CRM Development for Any Business | BoostLab",
        "desc": "Custom CRM built around your business: leads, deals, bookings, invoices and reports, integrated with your website, email and payments. From €4,500.",
        "crumb": "CRM systems",
        "h1": "CRM systems for <span class=\"acc\">any business</span>",
        "lead": "Off-the-shelf CRMs make your team adapt to the software. We build the CRM around how you already sell, book and invoice - and connect it to your website, ads and payments.",
        "stats": [("4-8", "weeks to launch"), ("100%", "your code and data"), ("€0", "per-seat licence fees")],
        "feat_title": "What your CRM <span class=\"acc\">can do</span>",
        "feats": [
            ("Lead capture", "Requests from the website, ads, calls and messengers land in one inbox with source tracking and automatic assignment.", ""),
            ("Pipeline & deals", "Stages that match your sales process, tasks, reminders and a clear view of what every manager is working on.", ""),
            ("Bookings & resources", "Calendars for staff, rooms, cars or equipment, online booking for customers and automatic confirmations.", ""),
            ("Invoices & payments", "Offers, invoices and receipts generated from the deal, card and bank-link payments, debt reminders.", ""),
            ("Email & SMS automation", "Follow-ups, reminders and campaigns triggered by status changes - with opt-out and GDPR consent built in.", ""),
            ("Reports & roles", "Revenue, conversion and team dashboards, permissions per role, export to Excel and accounting software.", ""),
        ],
        "cases": ["crm", "after", "balticleads"],
        "seo": [
            ("A CRM made for your business, not the other way round", "We build CRM systems for clinics and salons, rental and car-sharing companies, logistics, construction, event organisers, agencies, e-commerce and B2B sales teams. The system follows your process: the stages, fields, documents and reports you actually use. Your team learns it in an afternoon."),
            ("No licence fees per user", "You pay once for development and own the code and the data. There are no monthly fees per seat, so the CRM gets cheaper the more your team grows. We host it on a European server, or on your own infrastructure."),
            ("Integrations that remove manual work", "Website forms, Google and Meta lead ads, email, telephony, Baltic bank links, Stripe, Montonio, accounting software such as Merit and Directo, and any service with an API. Data flows in automatically and nobody copies it between tabs."),
        ],
        "faq": [
            ("How much does a custom CRM cost?", "A focused CRM for one team starts at €4,500. Systems with bookings, payments, client portals and many integrations are quoted after a short discovery call. You get a fixed price and a clickable prototype first."),
            ("Why not just use HubSpot, Pipedrive or Bitrix?", "They are great for standard sales. When your process has bookings, resources, special documents or many integrations, a custom CRM costs less over time and fits the work instead of forcing workarounds."),
            ("Can you migrate data from our current system or Excel?", "Yes. We import clients, deals and history from Excel, Google Sheets or your current CRM and check the data with you before going live."),
            ("Is the CRM GDPR compliant?", "Yes. Data is stored in the EU, access is role-based and logged, and consent and right-to-erasure tools are part of the system."),
            ("Do you provide support after launch?", "Yes - monitoring, backups, updates and new features under a monthly support plan or on request."),
        ],
    },
    "platforms": {
        "title": "Booking, Rental & Marketplace Platform Development | BoostLab",
        "desc": "Turnkey rental, ticketing, marketplace, real estate and job platforms with payments, admin panel and mobile apps. Launch in 2-4 months.",
        "crumb": "Platforms",
        "h1": "Platforms & <span class=\"acc\">marketplaces</span>",
        "lead": "We launch booking, rental, ticketing and marketplace platforms on a proven foundation - so you go live in months, not years, with payments and an admin panel from day one.",
        "stats": [("2-4", "months to launch"), ("€18,790", "turnkey from"), ("iOS + Android", "apps optional")],
        "feat_title": "Platform <span class=\"acc\">foundations</span>",
        "feats": [
            ("Rental & car-sharing", "Listings, availability calendar, deposits, contracts, host and renter dashboards and reviews. The foundation behind RentMe.", "€21,790"),
            ("Ticketing & events", "Ticket sales, seating and VIP tables, QR check-in, promo and referral codes, organiser dashboard. The foundation behind AFTER.", "€18,790"),
            ("Marketplace", "Multi-vendor catalogue, seller dashboards, commissions, payouts, search and filters, moderation.", "€19,790"),
            ("Real estate portal", "Listings with map search, agent profiles, lead routing and mortgage calculator.", "€27,900"),
            ("Job portal", "Job posting, company profiles, applicant tracking, CV builder and matching.", "€19,690"),
            ("Travel booking", "Search, packages, booking management, reviews and loyalty programme.", "€36,590"),
        ],
        "cases": ["rentme", "after"],
        "seo": [
            ("Turnkey platforms, built on what already works", "Each platform starts from a production-tested core: user accounts, roles, payments, notifications, admin panel and analytics. We customise the design, business rules and integrations for your market. This cuts the launch time to 2-4 months and removes most of the risk of building from scratch."),
            ("Payments and compliance for the Baltic market", "Estonian, Latvian and Lithuanian bank links, card payments through Stripe or Montonio, deposits and refunds, VAT invoices, GDPR consent and terms of service are part of the foundation."),
            ("Mobile apps on top", "Every platform exposes an API, so native iOS and Android apps can be added at any time: from €4,970 for Google Play and €5,970 for the App Store."),
        ],
        "faq": [
            ("How fast can a platform launch?", "Usually 2-4 months from signed brief to production, depending on customisation and integrations."),
            ("Do I own the platform?", "Yes. After payment you receive the source code and full ownership of your instance and data."),
            ("Can you build a platform that is not on the list?", "Yes. The list shows foundations we have ready; custom platforms are built from the same core components."),
            ("How do payments and commissions work?", "We integrate Stripe Connect, Montonio or bank links, so the platform takes its commission automatically and pays out to sellers or hosts."),
        ],
    },
    "apps": {
        "title": "Mobile App Development iOS & Android | BoostLab Tallinn",
        "desc": "iOS and Android app development: booking, loyalty and business apps connected to your website, CRM and payments. Design to App Store.",
        "crumb": "Mobile apps",
        "h1": "Mobile apps for <span class=\"acc\">iOS & Android</span>",
        "lead": "Apps your customers keep on the home screen: bookings, orders, loyalty and accounts - connected to the same backend as your website and CRM.",
        "stats": [("2", "platforms, one codebase"), ("6-12", "weeks to the stores"), ("100%", "store publishing handled")],
        "feat_title": "What we <span class=\"acc\">deliver</span>",
        "feats": [
            ("UX & interface design", "User flows and a clickable prototype tested before development.", ""),
            ("Cross-platform apps", "React Native apps for iOS and Android from one codebase - faster to build and cheaper to maintain.", "€4,970"),
            ("Native features", "Push notifications, payments, maps and geolocation, camera, QR scanning, offline mode.", ""),
            ("Store publishing", "App Store and Google Play accounts, listings, screenshots, review process and updates.", ""),
        ],
        "cases": ["rentme"],
        "seo": [
            ("Apps that are part of your business system", "An app is most valuable when it shares data with the website, CRM and payments. We build the backend once and use it everywhere: a booking made in the app appears in the CRM, a loyalty point earned in the shop shows in the app."),
            ("From idea to the App Store", "We handle research, design, development, testing on real devices and the store review process. After launch we monitor crashes and ratings and ship updates."),
        ],
        "faq": [
            ("How much does an app cost?", "Adding an app to an existing platform starts at €4,970 for Android and €5,970 for iOS. Standalone apps are quoted after a short call."),
            ("Native or cross-platform?", "For most business apps we use React Native: one codebase, both stores, near-native performance. For heavy graphics or special hardware we build native."),
            ("Do you publish the app for me?", "Yes. We prepare the listings and screenshots and take the app through App Store and Google Play review."),
        ],
    },
    "ads": {
        "title": "Google Ads, Meta & TikTok Advertising | BoostLab Tallinn",
        "desc": "PPC advertising that pays back: Google Ads, Meta (Facebook, Instagram) and TikTok campaigns with proper conversion tracking and landing pages. Setup from €599.",
        "crumb": "Advertising",
        "h1": "Advertising that <span class=\"acc\">pays back</span>",
        "lead": "Campaigns are only as good as the tracking and the landing page behind them. We build all three - so every euro of budget is measured against real leads and sales.",
        "stats": [("€599", "campaign setup"), ("3", "ad platforms"), ("Weekly", "optimisation")],
        "feat_title": "Channels & <span class=\"acc\">services</span>",
        "feats": [
            ("Google Ads", "Search, Performance Max, YouTube and remarketing - structured around the keywords that bring buyers.", "€599"),
            ("Meta Ads", "Facebook and Instagram campaigns with lead forms, catalogue ads and creative testing.", "€599"),
            ("TikTok Ads", "Short-form video campaigns for reach and conversions, with creatives made for the platform.", "€599"),
            ("Tracking & analytics", "GA4, Google Tag Manager, Meta Conversions API and offline conversions from your CRM.", ""),
        ],
        "cases": ["balticleads"],
        "seo": [
            ("PPC management in Estonia and the Baltics", "We plan and run campaigns in English, Estonian, Russian and Lithuanian for local and international audiences. Budgets, bids and creatives are adjusted weekly on the basis of cost per lead and cost per sale, not clicks."),
            ("B2B lead generation", "For B2B we combine search ads with targeted outreach using BalticLeads.ee - our own database of 1.4M companies in Estonia, Latvia, Lithuania and Finland."),
        ],
        "faq": [
            ("What budget do I need?", "We recommend at least €500-1,000 per month in ad spend for local campaigns so the algorithms have enough data. Management fees are separate from ad spend."),
            ("How soon will I see results?", "Search campaigns bring traffic from day one; a stable cost per lead usually comes after 3-6 weeks of optimisation."),
            ("Do I keep access to the ad accounts?", "Always. Accounts are created in your name and you see every number."),
        ],
    },
    "smm": {
        "title": "SMM & Content Marketing in Estonia | BoostLab",
        "desc": "Social media management: Instagram, Facebook, TikTok and LinkedIn. Strategy, reels, stories, community and monthly reports. From €1,399/month.",
        "crumb": "SMM & content",
        "h1": "SMM & <span class=\"acc\">content</span>",
        "lead": "Consistent, on-brand content that keeps your company visible and gives your ads something worth clicking.",
        "stats": [("12-20+", "posts a month"), ("Reels", "and stories included"), ("Monthly", "reports")],
        "feat_title": "What's <span class=\"acc\">included</span>",
        "feats": [
            ("Content strategy", "Audience, tone of voice, content pillars and a monthly plan tied to your sales goals.", ""),
            ("Production", "Photo, reels, stories, carousels and copy in the languages of your customers.", "€1,399"),
            ("Community management", "Replies to comments and messages, moderation and lead hand-off to your team.", ""),
            ("Analytics", "Monthly report on reach, engagement, followers and leads with recommendations.", ""),
        ],
        "cases": [],
        "seo": [
            ("Social media management for Baltic companies", "We run social media for brands in hospitality, events, retail, beauty and B2B services. Content is planned a month ahead, approved by you and published on time, so your channels stay active without taking your team's time."),
        ],
        "faq": [
            ("Which platforms do you manage?", "Instagram, Facebook, TikTok, LinkedIn and Telegram. We recommend the channels where your customers actually are."),
            ("Do you also run ads?", "Yes - the Ads + SMM package combines content with Google and Meta ad management."),
        ],
    },
}

T["portfolio"] = {
    "title": "Portfolio & Case Studies | BoostLab Web Studio",
    "desc": "BoostLab case studies: BalticLeads B2B platform, AFTER event ticketing, RentMe rental marketplace and custom CRM. 200+ websites a year.",
    "crumb": "Work",
    "h1": "Selected <span class=\"acc\">work</span>",
    "lead": "Platforms we built and run, CRM systems for companies in different industries, and more than 200 websites delivered every year for clients worldwide.",
    "stats": [("200+", "websites a year"), ("2", "international projects in development"), ("1.4M", "companies in BalticLeads")],
    "more_title": "And every <span class=\"acc\">year</span>",
    "more": "Beyond these platforms we ship more than 200 websites a year - landing pages, corporate sites and online stores for clients in Europe, the US and Asia. Many are under NDA; ask us for examples from your industry.",
}

T["pricing"] = {
    "title": "Prices: Website, CRM & App Development | BoostLab",
    "desc": "Landing page from €700, business website from €1,700, platform or CRM from €4,500. Ads from €599, SMM from €1,399/month. Fixed quotes.",
    "crumb": "Pricing",
    "h1": "Clear <span class=\"acc\">prices</span>",
    "lead": "Starting prices for every service. After a short call you get a fixed quote - no hidden fees, no lock-in.",
    "web_title": "Websites & <span class=\"acc\">systems</span>",
    "web": [
        ("Landing page", "€700", "", ["Responsive one-page site", "Conversion copy & design", "Contact form or booking", "SEO setup + GA4", "SSL and hosting setup"]),
        ("Business website", "€1,700", "", ["Multi-page custom design", "CMS to edit content", "Multilingual structure", "Advanced SEO & schema", "1 month of support"]),
        ("Platform / CRM", "€4,500", "", ["Accounts and roles", "Admin panel", "Payments & bookings", "API integrations", "Priority support"]),
    ],
    "mkt_title": "Ads & <span class=\"acc\">SMM</span>",
    "mkt": [
        ("Campaign setup", "€599", "once", ["Google Ads or Meta", "Audience & keyword research", "Up to 5 ad creatives", "Conversion tracking", "Performance report"]),
        ("Ads + SMM", "€1,399", "month", ["Google & Meta management", "12 posts a month", "Stories & reels", "Community management", "Monthly report, A/B tests"]),
        ("Dedicated specialist", "€2,500", "month", ["Personal account manager", "Full ad management", "20+ posts a month", "Content strategy", "Weekly reports"]),
    ],
    "plat_title": "Turnkey <span class=\"acc\">platforms</span>",
    "addons_title": "Mobile apps",
    "addons": [("Android app (Google Play)", "+€4,970"), ("iOS app (App Store)", "+€5,970")],
    "note": "Prices are starting prices. Add-ons: booking calendar, online payments, extra languages, custom integrations.",
    "faq": [
        ("Why are prices shown as 'from'?", "Every business is different. The starting price covers the typical scope; the fixed quote depends on pages, languages, features and integrations."),
        ("Do you work with a prepayment?", "Usually 50% before start and 50% at launch. Larger projects are split into milestones."),
        ("Are there monthly fees?", "Only hosting at cost and optional support plans. There are no licence fees for code we build for you."),
    ],
}

T["legal"] = {
    "privacy": {
        "title": "Privacy & Cookie Policy | BoostLab", "desc": "How FANARI OÜ (BoostLab) processes personal data and uses cookies on boostlab.lt, in line with the GDPR.",
        "crumb": "Privacy", "h1": "Privacy & cookies", "updated": "October 2026",
        "body": """<p>FANARI OÜ (BoostLab, "we") respects the privacy of visitors to boostlab.lt. This policy explains what personal data we process, why, and what rights you have under the General Data Protection Regulation (GDPR) and Estonian law.</p>
<h2>1. Controller</h2><p>FANARI OÜ (BoostLab), Ehitajate tee 15-20, 12612 Tallinn, Estonia. Email: <a href="mailto:info@boostlab.lt">info@boostlab.lt</a>, phone +372 568 25854.</p>
<h2>2. Data we process</h2><ul><li>Contact data you send us by email or phone: name, email, phone, company and the content of your message.</li><li>Technical data collected only with your consent: pages visited, device and browser type, approximate location and anonymised IP address.</li></ul>
<h2>3. Purposes and legal basis</h2><ul><li>Answering enquiries and preparing quotes - legitimate interest and steps before a contract (Art. 6(1)(b) and (f) GDPR).</li><li>Website analytics and advertising measurement - your consent (Art. 6(1)(a) GDPR).</li><li>Legal and accounting obligations - Art. 6(1)(c) GDPR.</li></ul>
<h2>4. Cookies</h2><p>Analytics and advertising cookies are not set until you click "Accept" in the cookie banner. Until then Google tags run in consent mode without storing cookies, and the Meta Pixel is not loaded at all. You can change your choice at any time by clearing this site's data in your browser.</p>
<h2>5. Processors and recipients</h2><ul><li>Google Ireland Ltd - Google Analytics 4 and Google Ads measurement (with consent).</li><li>Meta Platforms Ireland Ltd - Meta Pixel (with consent).</li><li>Google Fonts, jsDelivr and Cloudflare cdnjs - delivery of fonts and scripts.</li><li>GitHub Inc. - website hosting.</li></ul><p>Where data is transferred outside the EEA, the transfer relies on the EU-US Data Privacy Framework or standard contractual clauses.</p>
<h2>6. Retention</h2><p>Enquiries are kept for up to 24 months after the last contact; contracts and invoices for 7 years as required by Estonian accounting law. Analytics data is kept for 14 months.</p>
<h2>7. Your rights</h2><p>You may request access, rectification, erasure, restriction or portability, object to processing and withdraw consent at any time. Write to <a href="mailto:info@boostlab.lt">info@boostlab.lt</a>; we answer within 30 days.</p>
<h2>8. Complaints</h2><p>You can lodge a complaint with the Estonian Data Protection Inspectorate (Andmekaitse Inspektsioon), <a href="https://www.aki.ee" rel="noopener">www.aki.ee</a>.</p>""",
    },
    "terms": {
        "title": "Terms of Service | BoostLab", "desc": "Terms of use of boostlab.lt and general terms for BoostLab services provided by FANARI OÜ.",
        "crumb": "Terms", "h1": "Terms of service", "updated": "October 2026",
        "body": """<p>These terms govern the use of boostlab.lt, operated by FANARI OÜ (BoostLab), Tallinn, Estonia. Project work is governed by an individual agreement or accepted proposal, which takes priority over these terms.</p>
<h2>1. Services</h2><p>BoostLab provides website, CRM, platform and mobile app development, advertising, SMM and technical support. Scope, timeline and price are agreed individually in writing.</p>
<h2>2. Prices and quotes</h2><p>Prices on this website are starting prices for reference. The final price is set in a written quote, valid for 30 days unless stated otherwise.</p>
<h2>3. Payment</h2><p>Payment schedules are set in the project agreement. As a rule, work starts after an advance payment.</p>
<h2>4. Intellectual property</h2><p>After full payment the client owns the deliverables as specified in the agreement. BoostLab may show completed work in its portfolio unless agreed otherwise in writing.</p>
<h2>5. Timelines</h2><p>Timelines in proposals are estimates. Delays in feedback, content delivery or scope changes may extend them; we inform you of any significant change.</p>
<h2>6. Warranty and support</h2><p>A warranty period (typically 1-3 months) is set in the agreement. During it, defects in the delivered work are fixed free of charge.</p>
<h2>7. Liability</h2><p>BoostLab is not liable for indirect or consequential damage. Total liability is limited to the amount paid for the specific project.</p>
<h2>8. Third-party services</h2><p>Projects may use third-party services such as payment providers, hosting and APIs. BoostLab is not responsible for their availability or terms.</p>
<h2>9. Termination</h2><p>Either party may terminate a project agreement in writing. Work completed up to the termination date is payable.</p>
<h2>10. Governing law</h2><p>These terms are governed by the laws of the Republic of Estonia. Disputes are resolved in Harju County Court, Tallinn.</p>""",
    },
}
