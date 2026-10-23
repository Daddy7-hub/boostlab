# SEO content (EN): B2B lead-generation page, industry pages, blog. Executed after en.py, en_pages.py, en_extra.py.
# Spec: SEO_SPEC.md. Keys (leadgen, niche ids, post ids) are shared by all languages.

T["ui"]["f_industries"] = "Industries"
T["nav"]["leadgen"] = "B2B lead generation"
T["slugs"]["leadgen"] = "b2b-lead-generation.html"
T["slugs"]["blog"] = "blog/"

# ---------------------------------------------------------------- lead generation
T["pages"]["leadgen"] = {
    "title": "B2B Lead Generation in the Baltics | BoostLab",
    "desc": "B2B lead generation in Estonia, Latvia, Lithuania and Finland: BalticLeads company data, cold email outreach, ads and CRM. Setup from €599.",
    "crumb": "B2B lead generation",
    "h1": "B2B leads direct from <span class=\"acc\">BalticLeads</span>, the leading B2B platform in the Baltics",
    "lead": "We work directly with BalticLeads, the B2B data and outreach platform built and run by our own team. We pick the companies you should be talking to, write the offer and run the outreach until replies turn into deals.",
    "stats": [("1.4M", "companies from official registers"), ("4", "countries: EE, LV, LT, FI"), ("744k", "companies with an email address")],
    "feat_title": "What we <span class=\"acc\">do</span>",
    "feats": [
        ("Target company lists", "We select companies in BalticLeads by country, industry, city and size. Only company and role addresses are used; free and personal webmail is hidden.", ""),
        ("Offer and copy", "One clear offer per segment, written in the language of the buyer: English, Estonian, Russian or Lithuanian, with follow-ups that add value.", ""),
        ("Landing page", "A focused page that matches the email and the ads, with a short form, booking or call button and conversion tracking.", "€700"),
        ("Email outreach", "Campaign setup, sending limits, moderation, global opt-out list and automatic unsubscribe handling, so your domain stays healthy.", "€599"),
        ("Google and Meta ads", "Search and retargeting campaigns that reach the same companies again, so your name is familiar before the second email lands.", "€599"),
        ("CRM and reporting", "Replies, meetings and deals tracked in a CRM, with a clear view of which segment and which message actually bring revenue.", ""),
    ],
    "partner": {
        "kicker": "Direct partnership",
        "title": "Built by our team, <span class=\"acc\">used every day</span>",
        "text": "BalticLeads is the B2B data platform our team built and operates, and we use it directly in every lead generation project. There is no reseller layer and no spreadsheets passed between agencies. We know how the data is collected from official business registers, how the filters and AI search work and how campaigns are moderated, so your lists are precise and your outreach stays compliant.",
        "points": [
            "1.4M companies from the business registers of Estonia, Latvia, Lithuania and Finland",
            "AI search: describe your ideal client and get a matching company list",
            "Company and role addresses only, with global opt-out and auto-unsubscribe",
        ],
        "cta": "Open BalticLeads",
    },
    "seo": [
        ("B2B lead generation in Estonia, Latvia, Lithuania and Finland",
         "Finding new B2B clients in the Baltics usually starts with a question: who exactly should we contact? BalticLeads answers it with data on 1.4 million companies taken from official business registers of Estonia, Latvia, Lithuania and Finland, about 744,000 of them with an email address. Because the platform is built and run by our team, we work with it directly: we filter by industry, city and company size, check the list against your ideal customer profile and remove companies that are not a fit. The result is a short, relevant list instead of a large one, and that is what drives replies."),
        ("Cold email outreach that respects the rules",
         "Cold B2B email to companies is allowed on an opt-out basis in Estonia, Latvia and Lithuania. We build every campaign around that model: generic role addresses such as info@ or sales@, a clear sender, an unsubscribe link in every message and objections honoured immediately. Free and personal webmail addresses are hidden in BalticLeads, and each campaign passes moderation before it is sent. Sending volumes are kept within safe daily limits per mailbox, with SPF and DKIM set up on your domain, so outreach builds your reputation instead of burning it."),
        ("From a company database in Estonia to signed deals",
         "A company database is only the first step. We write an offer for each segment, build a landing page that continues the conversation and support the emails with Google and Meta ads aimed at the same audience. Every reply, meeting and deal is tracked in a CRM, so after the first wave you know which industries and messages work and where to scale. Campaign setup starts at €599, and you can buy a ready database in BalticLeads yourself at any time if you prefer to run outreach in-house."),
    ],
    "faq": [
        ("Where does the company data come from?", "BalticLeads collects company data from the official business registers of Estonia, Latvia, Lithuania and Finland. Email addresses are company and role addresses; free and personal webmail addresses are hidden."),
        ("Is cold B2B email legal in the Baltics?", "Cold B2B email to companies is allowed on an opt-out basis in Estonia, Latvia and Lithuania (in Lithuania since 22 April 2026). Every message needs an unsubscribe link, and objections must be honoured immediately. Emails of named people are personal data under GDPR. This is general information, not legal advice."),
        ("How much does a lead generation campaign cost?", "Campaign setup starts at €599. A landing page starts at €700. The database itself is bought in BalticLeads and priced by the number of contacts. You get a fixed quote after a short call."),
        ("Can I use BalticLeads without your agency services?", "Yes. You can search, buy a ready database and launch email campaigns in BalticLeads yourself. We step in when you want the full setup: targeting, copy, landing page, ads and CRM."),
        ("How soon will I see results?", "Replies usually come within the first days of a wave. We review results after each wave and adjust segments and messages; meaningful conclusions need a few hundred contacted companies per segment."),
    ],
    "posts": ["b2b-leads-baltics", "landing-vs-website"],
}

# ---------------------------------------------------------------- industry pages
T["niches"] = {
    "ecommerce": {
        "slug": "ecommerce-development.html", "nav": "E-commerce",
        "title": "Online Store Development in Estonia | BoostLab",
        "desc": "E-commerce website development in Estonia and the Baltics: catalogue, card and bank-link payments, shipping and order management. From €3,500.",
        "crumb": "E-commerce development",
        "h1": "Online store <span class=\"acc\">development</span>",
        "lead": "Online stores that load fast, rank in Google and make checkout easy, with payments, shipping and order management connected from day one.",
        "stats": [("€3,500", "online store from"), ("3-5", "weeks to launch"), ("4", "languages we write in")],
        "feat_title": "What your store <span class=\"acc\">gets</span>",
        "feats": [
            ("Catalogue and filters", "Products with variants, search, filters and category pages structured for SEO, easy to manage from the admin panel.", "€3,500"),
            ("Payments", "Card and bank-link payments in a short checkout, with receipts and order confirmations sent automatically.", ""),
            ("Shipping", "Courier and parcel locker delivery options, shipping rules by zone and weight, tracking links in customer emails.", ""),
            ("Orders and stock", "Order statuses, stock levels, returns and customer history in one place, with export to accounting.", ""),
            ("Multilingual store", "Estonian, English, Russian, Lithuanian or other versions with hreflang, so each market finds its own language in Google.", ""),
            ("Marketing ready", "Google Analytics 4, conversion tracking and product feeds for Google and Meta ads set up before launch.", ""),
        ],
        "seo": [
            ("E-commerce website development in Estonia",
             "BoostLab builds online stores for retailers and brands in Estonia, Latvia, Lithuania, Finland and across Europe. Every store gets its own design and is built mobile-first, because most shoppers browse on a phone. We plan the catalogue structure around the searches your customers make, write category texts that rank and keep page speed in the green. Checkout is kept short, with card and bank-link payments that local customers trust. A store starts at €3,500 and is usually live in 3-5 weeks, depending on the size of the catalogue and integrations."),
            ("Integrations that save hours every week",
             "An online store is only efficient when orders do not have to be retyped. We connect payments, delivery services, accounting export and email so that an order moves from checkout to shipping with as few manual steps as possible. If you already use a CRM or a warehouse system, the store can exchange data with it through an API. For larger catalogues we set up import from spreadsheets or supplier feeds, so prices and stock stay current without manual edits."),
            ("Built to sell after launch",
             "Launch day is the start of the work, not the end. Every store comes with analytics, conversion tracking and Search Console configured, so you can see which products and channels bring revenue. Product feeds make it easy to start Google Shopping and Meta catalogue ads; our ads setup starts at €599. We also offer support and improvements after launch: new payment methods, landing pages for campaigns, speed checks and SEO work on category pages. You decide how much help you need, month by month."),
        ],
        "faq": [
            ("How much does an online store cost?", "An online store with us starts at €3,500. The final price depends on the number of products and languages, custom features and integrations with accounting, warehouse or CRM systems. You get a fixed quote after a free call."),
            ("How long does it take to launch a store?", "Most stores go live in 3-5 weeks. Large catalogues, multiple languages or complex integrations can extend the timeline; the plan is agreed before development starts."),
            ("Can I manage products myself?", "Yes. You get an admin panel to add products, change prices, manage stock and handle orders without a developer."),
            ("Can you move my existing store without losing traffic?", "Yes. We map old URLs to new ones, set up redirects, keep the content that ranks and watch Search Console after the move."),
        ],
        "posts": ["website-cost", "seo-checklist"],
    },
    "clinics": {
        "slug": "crm-for-clinics-and-salons.html", "nav": "Clinics & salons",
        "title": "CRM and Online Booking for Clinics & Salons | BoostLab",
        "desc": "CRM and online booking for clinics, dental practices and beauty salons: staff calendars, reminders, client cards, payments and reports. From €4,500.",
        "crumb": "CRM for clinics and salons",
        "h1": "CRM and online booking for <span class=\"acc\">clinics and salons</span>",
        "lead": "Clients book online at any hour, reminders cut no-shows and your team sees schedules, client history and payments in one system built around how your practice works.",
        "stats": [("24/7", "online booking"), ("4-8", "weeks to launch"), ("€0", "per-seat licence fees")],
        "feat_title": "What your system <span class=\"acc\">can do</span>",
        "feats": [
            ("Online booking", "Clients choose a service, specialist and time on your website or app, and the slot is confirmed instantly.", "€4,500"),
            ("Staff and room calendars", "Schedules for specialists, rooms and equipment, with service durations, breaks and buffers between visits.", ""),
            ("Client cards", "Visit history, notes, consents and documents per client, with access limited by role and an audit log.", ""),
            ("Reminders", "Email and SMS confirmations and reminders before each visit, plus follow-ups for repeat treatments.", ""),
            ("Payments and deposits", "Prepayments or deposits for online bookings, invoices and receipts generated from the visit.", ""),
            ("Reports", "Revenue by service and specialist, schedule utilisation and returning clients, exportable to Excel and accounting.", ""),
        ],
        "seo": [
            ("CRM for clinics, dental practices and beauty salons",
             "Clinics and salons run on time slots. When bookings live in phone calls, messengers and a paper diary, slots are lost and specialists wait for clients who never come. We build a CRM with online booking around your services and your team: who does what, how long each treatment takes, which rooms and equipment it needs. Clients book through your website or app, the system confirms the visit and sends reminders, and administrators handle the exceptions instead of the routine. A system like this starts at €4,500."),
            ("Client data handled with care",
             "Client cards in a clinic often contain sensitive information, including health data, which GDPR treats as a special category. We design access by role, so a receptionist, a specialist and a manager each see only what they need, and actions are logged. Consents are stored with the client record, and data can be exported or deleted on request. You own the code and the data, and there are no per-seat licence fees as the team grows. Hosting is set up for you and billed at cost."),
            ("One system instead of five tools",
             "Many practices combine a booking widget, a spreadsheet, a messenger and a separate invoicing tool. A custom CRM brings these together: booking, client history, reminders, payments and reports in one place, connected to your website and, if you need it, a mobile app. Owners see revenue by service and specialist, and the team spends less time on the phone. We launch in 4-8 weeks, starting with the features that save the most time, and extend the system as the practice grows."),
        ],
        "faq": [
            ("How much does a CRM with online booking cost?", "A focused system for one practice starts at €4,500. Multi-location setups, client portals, mobile apps and many integrations are quoted after a short discovery call."),
            ("Can clients book from Instagram or Google?", "Yes. The booking page has its own link that you can add to your Instagram profile, Google Business profile, ads and messages."),
            ("Can we move our existing client base?", "Yes. We import clients, visit history and future bookings from spreadsheets or exports of your current system."),
            ("Does it work for a salon with several locations?", "Yes. Locations, staff, rooms and services can be managed separately, with shared reports for the owner."),
        ],
        "posts": ["custom-crm-vs-saas", "booking-system"],
    },
    "rental": {
        "slug": "car-rental-website.html", "nav": "Rental platforms",
        "title": "Car & Equipment Rental Website Development | BoostLab",
        "desc": "Rental website and booking platform for cars, equipment and property: availability calendar, deposits, contracts and payments. Turnkey from €21,790.",
        "crumb": "Rental platforms",
        "h1": "Rental website and <span class=\"acc\">booking platform</span>",
        "lead": "Car, equipment or property rental with online booking, deposits, contracts and payments. Built on the same foundation that runs RentMe, our own rental marketplace.",
        "stats": [("€21,790", "turnkey rental platform"), ("2-4", "months to launch"), ("iOS + Android", "apps optional")],
        "feat_title": "What the platform <span class=\"acc\">includes</span>",
        "feats": [
            ("Turnkey rental platform", "Listings, search, booking, payments, admin panel and host and renter dashboards, customised for your market.", "€21,790"),
            ("Availability calendar", "Real-time availability per car, item or property, with buffers between rentals and blocked dates for service.", ""),
            ("Deposits and payments", "Online prepayment or deposit at booking, the rest online or on pickup, with automatic receipts.", ""),
            ("Contracts and documents", "Rental agreements generated from the booking, ID and licence checks, handover photos and damage notes.", ""),
            ("Fleet and inventory", "Vehicles, equipment or units with prices by season and duration, maintenance status and utilisation reports.", ""),
            ("Reviews and mobile apps", "Verified reviews after each rental, and native iOS and Android apps connected to the same platform.", ""),
        ],
        "seo": [
            ("Car rental website development",
             "A rental business lives on its calendar. Customers want to see what is free, book in a few taps and pay a deposit online, and your team needs to know which car or item goes out when. We build rental websites and booking platforms for car, equipment and property rental: availability calendar, online booking, deposits, contracts, payments and an admin panel. The platform is responsive from the start, and native iOS and Android apps can be added on top through the same API, from €4,970 for Android and €5,970 for iOS."),
            ("A turnkey rental platform built on proven code",
             "Our turnkey rental platform starts at €21,790 and goes live in 2-4 months. It is built on the same foundation as RentMe (rentme.rent), the rental marketplace we develop and run for transport, property and things. That means accounts, roles, payments, notifications and the admin panel are already tested in production, and the project time goes into your business rules: pricing by season, deposits, insurance, delivery and the documents you need. You see a clickable prototype before development, and the scope and price are fixed in advance."),
            ("Single fleet or marketplace",
             "Some clients rent out their own fleet, others want a marketplace where many hosts list cars, tools or property and the platform takes a commission. Both models run on the same core: the difference is in host dashboards, payouts, moderation and reviews. We help you choose the model, plan the launch market and connect the platform to ads and a CRM, so the first bookings come in soon after go-live. If you start with your own fleet, the marketplace features can be switched on later without rebuilding the platform."),
        ],
        "faq": [
            ("How much does a rental platform cost?", "A turnkey rental platform starts at €21,790. The final price depends on the business model, integrations and design changes. Mobile apps are added from €4,970 for Android and €5,970 for iOS."),
            ("How long does it take to launch?", "Most rental platforms go live in 2-4 months, because the core is already tested in production and the work focuses on your business rules."),
            ("Can customers pay only a deposit online?", "Yes. You choose the model: full prepayment, a deposit or a percentage online, with the rest paid online later or on pickup."),
            ("Can the platform work as a marketplace for many hosts?", "Yes. Host dashboards, commissions, payouts, moderation and reviews are part of the marketplace setup."),
        ],
        "posts": ["booking-system", "website-cost"],
    },
    "restaurants": {
        "slug": "restaurant-website.html", "nav": "Restaurants & cafes",
        "title": "Restaurant & Cafe Website Development | BoostLab",
        "desc": "Restaurant and cafe websites with an easy-to-edit menu, table booking and online delivery orders, built for Google and mobile. From €1,700.",
        "crumb": "Restaurant websites",
        "h1": "Restaurant websites that <span class=\"acc\">fill tables</span>",
        "lead": "A fast, mobile-first website with a menu you can update yourself, table booking and online orders for delivery or takeaway, ready to be found on Google.",
        "stats": [("€1,700", "restaurant website from"), ("2-3", "weeks to launch"), ("4", "languages we write in")],
        "feat_title": "What your website <span class=\"acc\">does</span>",
        "feats": [
            ("Menu you control", "Dishes, prices, photos and allergens edited from the admin panel, with lunch and seasonal menus on a schedule.", "€1,700"),
            ("Table booking", "Guests pick a date, time and party size online and get a confirmation; your team sees all bookings in one list.", ""),
            ("Delivery and takeaway orders", "Online orders with card payment, pickup or delivery times and notifications to the kitchen.", ""),
            ("Multilingual menu", "Menu and pages in the languages of your guests and tourists, each version indexed in Google.", ""),
            ("Local SEO", "Structured data, opening hours, location and Google Business profile alignment, so you show up for searches nearby.", ""),
            ("Events and private dining", "Pages and request forms for events, group bookings and gift cards that bring in higher-value orders.", ""),
        ],
        "seo": [
            ("Restaurant website development",
             "For most guests, a restaurant website is the menu, the opening hours and the booking button, checked on a phone a few minutes before deciding. We build restaurant and cafe websites around exactly that: fast pages, a clear menu, a visible booking or order button and correct contact details. Your team can update dishes, prices and photos without a developer, and the site is ready for Google from launch. A restaurant website starts at €1,700 and is usually live in 2-3 weeks."),
            ("Table booking and online orders without middlemen",
             "Table booking on your own website keeps guest data and the relationship with you. Online ordering for delivery or takeaway can run on your site as well, with card payment and notifications to the kitchen, which reduces dependence on third-party platforms for repeat customers. We set it up around your service: booking slots, party sizes, pickup times and delivery zones. Orders and bookings appear in one admin view, so the floor team and the kitchen work from the same information, and you can see which days and dishes drive revenue."),
            ("Found by guests nearby",
             "Restaurants compete on local searches. We add structured data for your restaurant, menu and opening hours, align the website with your Google Business profile and write pages for the cuisine, location and occasions people search for. For tourists and international guests, the menu and key pages are available in several languages. After launch we can support you with Google and Meta ads from €599 setup, or with content and social media from €1,399 per month, so the website keeps bringing guests."),
        ],
        "faq": [
            ("How much does a restaurant website cost?", "A restaurant or cafe website starts at €1,700, including the menu, booking or order flow and SEO setup. Online ordering with payments and integrations is quoted after a short call."),
            ("Can we change the menu ourselves?", "Yes. Dishes, prices, photos, allergens and daily lunch menus are edited in the admin panel."),
            ("Can guests book tables online?", "Yes. Guests choose date, time and party size, and get a confirmation. Your team sees and manages all bookings in one place."),
            ("Do you also handle social media?", "Yes. Content and social media management starts at €1,399 per month, and ads setup at €599."),
        ],
        "posts": ["landing-vs-website", "seo-checklist"],
    },
}

# ---------------------------------------------------------------- blog
_DATE, _ISO = "23 October 2026", "2026-10-23"

T["blog"] = {
    "title": "Blog: Websites, CRM and B2B Growth | BoostLab",
    "desc": "Practical guides from a Tallinn studio: website costs, CRM choices, booking systems, SEO before launch and finding B2B clients in the Baltics.",
    "crumb": "Blog",
    "h1": "Notes from <span class=\"acc\">the studio</span>",
    "lead": "Practical guides on websites, CRM systems, platforms and B2B growth, written from projects we build and run every day.",
    "read": "min read",
    "posts": {
        "website-cost": {
            "slug": "how-much-does-a-website-cost-estonia.html",
            "title": "How Much Does a Website Cost in Estonia? | BoostLab",
            "desc": "Website prices in Estonia by type: landing page, business site, store, CRM, platform. What drives the cost, hidden costs and how to get a fixed quote.",
            "h1": "How much does a website cost in Estonia?",
            "lead": "A clear price breakdown by type of website, what moves the price up or down and the costs that are easy to forget.",
            "date": _DATE, "iso": _ISO, "minutes": 6,
            "body": """<p>"How much does a website cost?" is the first question almost every client asks, and the honest answer is: it depends on what the website has to do. A one-page site for an ad campaign and a booking platform with payments are both called websites, but they are different products. Below is how we price projects at BoostLab, what drives the price and which costs are easy to miss.</p>
<h2>Website prices by type</h2>
<p>These are our starting prices. Every project gets a fixed quote after a short call, so you know the final number before work begins.</p>
<table><thead><tr><th>Type</th><th>Price from</th><th>Timeline</th><th>Fits when</th></tr></thead><tbody>
<tr><td>Landing page</td><td>€700</td><td>5-7 working days</td><td>One offer, one goal, traffic from ads or outreach</td></tr>
<tr><td>Business website</td><td>€1,700</td><td>2-3 weeks</td><td>Several services, multiple languages, blog and SEO</td></tr>
<tr><td>Online store</td><td>€3,500</td><td>3-5 weeks</td><td>Catalogue, payments, shipping and orders</td></tr>
<tr><td>Web platform or CRM</td><td>€4,500</td><td>From 4 weeks</td><td>Accounts, bookings, payments, admin panel, integrations</td></tr>
<tr><td>Turnkey ticketing platform</td><td>€18,790</td><td>2-4 months</td><td>Ticket sales, QR check-in, organiser dashboard</td></tr>
<tr><td>Turnkey marketplace</td><td>€19,790</td><td>2-4 months</td><td>Many sellers, commissions, payouts, moderation</td></tr>
<tr><td>Turnkey rental platform</td><td>€21,790</td><td>2-4 months</td><td>Availability calendar, deposits, contracts, hosts</td></tr>
<tr><td>Mobile app on top</td><td>+€4,970 Android, +€5,970 iOS</td><td>6-12 weeks</td><td>Customers book, buy or manage from their phone</td></tr>
</tbody></table>
<p>Full details are on our <a href="/pricing.html">pricing page</a>. For each type you can read more on <a href="/web-development.html">web development</a>, <a href="/crm-development.html">CRM systems</a>, <a href="/platforms.html">platforms</a> and <a href="/mobile-apps.html">mobile apps</a>.</p>
<h2>What drives the cost</h2>
<p>Two websites with the same number of pages can differ in price several times over. The main factors are:</p>
<ul>
<li><strong>Number of unique templates.</strong> Ten service pages built on one template cost less than five pages that each need a different layout.</li>
<li><strong>Languages.</strong> Each language version needs copy, translation checks, hreflang tags and separate SEO work. In the Baltics, two to four languages is common.</li>
<li><strong>Custom design versus a theme.</strong> A custom design takes more time up front but matches your brand and converts better. A theme is cheaper but brings limits and unused code.</li>
<li><strong>Integrations.</strong> Payments, accounting export, CRM, booking calendars, delivery services and APIs each add work, especially when data has to flow both ways.</li>
<li><strong>Business logic.</strong> User accounts, roles, pricing rules, deposits or approval flows turn a website into an application, and that is where most of the budget goes.</li>
<li><strong>Content.</strong> Whether you provide texts and photos or we write the copy and source images changes the scope noticeably.</li>
<li><strong>Migration.</strong> Moving from an old site means mapping URLs, setting up redirects and protecting existing Google rankings.</li>
</ul>
<h2>Hidden costs to plan for</h2>
<p>The development price is not the whole budget. These items are often forgotten in a first estimate:</p>
<ul>
<li><strong>Domain, hosting and SSL.</strong> Small, but recurring every year. We set them up and bill hosting at cost, or deploy to your own server.</li>
<li><strong>Licences and subscriptions.</strong> Paid plugins, themes, booking widgets or SaaS tools often charge monthly or per user. Over three years, these can exceed the build cost.</li>
<li><strong>Payment fees.</strong> Card and bank-link providers charge per transaction. Compare providers before launch, not after.</li>
<li><strong>Copy, photos and translations.</strong> Professional texts and images make a visible difference to conversion and take time to produce.</li>
<li><strong>Maintenance.</strong> Updates, backups, security patches and small changes after launch. Budget for them from the start.</li>
<li><strong>Traffic.</strong> A website does not bring visitors by itself. SEO takes months, and ads need both a setup fee and an ad budget, which are separate costs.</li>
</ul>
<h2>What is included at BoostLab</h2>
<p>Some studios sell basic things as extras. In our projects these are standard: mobile-first design, SEO structure and schema markup, Google Analytics 4 and conversion tracking, GDPR cookie consent, multilingual structure with hreflang, SSL and backups, an admin panel to edit content and a warranty period with free bug fixes. When you compare quotes, check whether these are in the price or come later as change requests.</p>
<h2>How to get a fixed quote</h2>
<ol>
<li><strong>Describe the goal, not just the pages.</strong> "We need 30 booking requests a month" tells us more than "we need five pages".</li>
<li><strong>List must-have features and integrations.</strong> Payments, booking, CRM, accounting, languages. Mark what can wait for phase two.</li>
<li><strong>Share examples.</strong> Two or three websites you like, and what exactly you like about them.</li>
<li><strong>Get a scope document and prototype.</strong> We send a fixed quote after a free call and show a clickable prototype before development, so there are no surprises in the final invoice.</li>
</ol>
<p>If the budget is tight, start smaller rather than cheaper: a strong landing page for €700 that brings requests is a better first step than a large website built on shortcuts. You can extend it later without starting over.</p>""",
            "faq": [
                ("What is the cheapest way to get online?", "A landing page from €700. It works best for one clear offer and traffic from ads or outreach, and can grow into a full website later."),
                ("Why do quotes for the same website differ so much?", "Quotes differ in custom design versus themes, languages, integrations, content and what is included after launch. Compare scope, not just the total."),
                ("Are there monthly fees?", "Development is a one-time fee. Hosting is billed at cost, and support or marketing are optional monthly services."),
            ],
            "services": ["web", "crm", "platforms"],
        },
        "custom-crm-vs-saas": {
            "slug": "custom-crm-vs-hubspot-pipedrive.html",
            "title": "Custom CRM vs HubSpot or Pipedrive | BoostLab",
            "desc": "When an off-the-shelf CRM like HubSpot or Pipedrive is enough, when a custom CRM pays off and how to compare the real cost over three years.",
            "h1": "Custom CRM vs HubSpot or Pipedrive: which pays off?",
            "lead": "Off-the-shelf CRMs are a great start for many teams. Here is how to tell when they stop being the cheaper option.",
            "date": _DATE, "iso": _ISO, "minutes": 6,
            "body": """<p>We build custom CRM systems, so you might expect this article to say that everyone needs one. They do not. HubSpot, Pipedrive and similar tools are well made, quick to start and the right choice for many teams. The question is not which is better in general, but which costs less and works better for your business over the next few years.</p>
<h2>When an off-the-shelf CRM is enough</h2>
<p>A ready-made CRM is usually the right choice if most of these are true:</p>
<ul>
<li>Your sales process is a classic pipeline: lead, contact, offer, negotiation, deal.</li>
<li>The team is small and not expected to grow quickly.</li>
<li>You need to start this week, not in a month.</li>
<li>Your other tools (email, calendar, accounting) already have ready integrations with the CRM.</li>
<li>You do not manage bookings, resources or complex pricing inside the CRM.</li>
</ul>
<p>In that case, pick a well-known product, spend a day setting up stages and fields, and focus on selling. Building custom software here would be a cost without a return.</p>
<h2>When a custom CRM pays off</h2>
<p>A custom CRM starts to make sense when the software forces your team to work around it. Typical signs:</p>
<ul>
<li><strong>Your business runs on bookings or resources.</strong> Clinics, salons, rental companies, event venues and logistics companies need calendars for staff, rooms, cars or equipment. A sales pipeline does not model that well.</li>
<li><strong>The process is specific.</strong> Approval steps, custom pricing rules, deposits, contracts or service stages that do not fit standard fields end up in spreadsheets next to the CRM.</li>
<li><strong>Many users.</strong> Per-seat pricing grows with every new employee. For a large team, the licence bill becomes a significant fixed cost.</li>
<li><strong>Features locked behind higher tiers.</strong> Automation, custom objects, reporting or API limits often require a more expensive plan for every seat, even if only a few people need them.</li>
<li><strong>Customer-facing parts.</strong> Online booking, a client portal or a mobile app connected directly to the same data are easier to build around your own system.</li>
<li><strong>Data ownership.</strong> With a custom CRM, the code and the data are yours, hosted where you decide.</li>
</ul>
<h2>Comparing the cost over three years</h2>
<p>We do not quote vendor prices here, because plans and prices change often and depend on the tier. Instead, use this logic with the current prices from the vendor's website.</p>
<h3>Off-the-shelf CRM, 36 months</h3>
<ul>
<li>Per-seat monthly fee multiplied by the number of users, multiplied by 36.</li>
<li>Plus the higher tier, if you need automation, custom reports or API access.</li>
<li>Plus paid add-ons and marketplace apps (booking, document generation, SMS, telephony).</li>
<li>Plus setup and integration work, often by a consultant.</li>
<li>Plus the hidden cost of workarounds: time spent copying data between the CRM and spreadsheets.</li>
</ul>
<h3>Custom CRM, 36 months</h3>
<ul>
<li>One-time build: a focused CRM with us starts at €4,500 and launches in 4-8 weeks.</li>
<li>Plus hosting, billed at cost.</li>
<li>Plus support and improvements, either as needed or on a monthly plan.</li>
<li>No per-seat licence fees, so adding users does not change the cost.</li>
</ul>
<table><thead><tr><th>Factor</th><th>Off-the-shelf CRM</th><th>Custom CRM</th></tr></thead><tbody>
<tr><td>Start</td><td>Days</td><td>4-8 weeks</td></tr>
<tr><td>Upfront cost</td><td>Low</td><td>From €4,500</td></tr>
<tr><td>Cost as the team grows</td><td>Grows with every seat</td><td>Stays flat</td></tr>
<tr><td>Fit to your process</td><td>You adapt to the tool</td><td>The tool adapts to you</td></tr>
<tr><td>Bookings and resources</td><td>Via add-ons</td><td>Built in</td></tr>
<tr><td>Code and data ownership</td><td>Vendor platform</td><td>Yours</td></tr>
</tbody></table>
<p>Put your real numbers into both columns. For a team of three with a standard pipeline, the ready-made CRM usually wins. For a team of fifteen with bookings, deposits and a customer portal, the custom system often costs less within the first two to three years, and it does exactly what the business needs.</p>
<h2>A middle path</h2>
<p>You do not have to choose once and forever. Many companies start with an off-the-shelf CRM to learn what they actually need, then move to a custom system when the workarounds become expensive. Another option is to keep the SaaS CRM for sales and build a custom part for bookings or operations that connects through its API. When you migrate, contacts, deals and history are imported, so nothing is lost.</p>
<h2>How we build custom CRM systems</h2>
<p>We start with a short call and a map of how your team sells, books and invoices today. Then we design a clickable prototype that the team tests before development. The first version covers the features that save the most time, usually lead capture, pipeline, bookings, invoices and reminders, and the system grows from there. Read more on our <a href="/crm-development.html">CRM development</a> page, see industry examples for <a href="/crm-for-clinics-and-salons.html">clinics and salons</a>, or check <a href="/pricing.html">pricing</a>.</p>""",
            "faq": [
                ("Is a custom CRM always more expensive?", "Upfront, yes. Over three years it can cost less than per-seat subscriptions for larger teams or businesses that need bookings, portals or several paid add-ons."),
                ("Can you migrate our data from HubSpot or Pipedrive?", "Yes. Contacts, companies, deals, notes and history can be exported and imported into the new system."),
                ("How long does a custom CRM take?", "A focused CRM launches in 4-8 weeks. More features are added in later phases."),
            ],
            "services": ["crm", "platforms"],
        },
        "booking-system": {
            "slug": "booking-system-for-rental-business.html",
            "title": "Booking System for a Rental Business: Checklist",
            "desc": "Feature checklist for a rental booking system: availability calendar, deposits, contracts, payments, reminders, reviews and mobile apps.",
            "h1": "Booking system for a rental business: the feature checklist",
            "lead": "What a rental booking system needs before launch, and what can wait until the first customers are in.",
            "date": _DATE, "iso": _ISO, "minutes": 6,
            "body": """<p>Whether you rent out cars, vans, tools, event equipment or apartments, the booking system is the core of the business. It decides whether customers book in two minutes or call, whether items are double-booked and how much admin your team does every day. We build rental platforms and run our own, RentMe, so this checklist comes from practice. Use it to brief a developer or to evaluate a ready-made tool.</p>
<h2>1. Availability calendar</h2>
<ul>
<li>Real-time availability per item, not per category, so two customers cannot book the same car.</li>
<li>Buffers between rentals for cleaning, inspection or delivery.</li>
<li>Blocked dates for maintenance, with a reason visible to the team.</li>
<li>Minimum and maximum rental periods, and different rules for weekends or holidays.</li>
<li>Calendar sync if items are also listed on other channels.</li>
</ul>
<h2>2. Pricing rules</h2>
<ul>
<li>Prices by hour, day, week or month, with discounts for longer rentals.</li>
<li>Seasonal prices and special dates.</li>
<li>Extras: insurance, child seats, delivery, additional drivers, accessories.</li>
<li>Clear total before payment, including deposit and fees.</li>
</ul>
<h2>3. Deposits and payments</h2>
<ul>
<li>Online card and bank-link payments.</li>
<li>Flexible models: full prepayment, a deposit, or a percentage online with the rest on pickup. On RentMe, for example, renters pay 10% online and the rest in person.</li>
<li>Security deposits held and released according to your rules.</li>
<li>Automatic receipts and invoices for business customers.</li>
<li>Refund and cancellation policy applied by the system, not by hand.</li>
</ul>
<h2>4. Contracts and documents</h2>
<ul>
<li>Rental agreement generated from the booking, with customer and item details filled in.</li>
<li>ID and driving licence checks before handover.</li>
<li>Handover and return checklists with photos, mileage or condition notes.</li>
<li>Damage reports linked to the booking and the customer.</li>
</ul>
<h2>5. Reminders and communication</h2>
<ul>
<li>Booking confirmation by email and SMS with all key details.</li>
<li>Reminders before pickup and return, with location and opening hours.</li>
<li>Automatic messages when a booking changes or a payment fails.</li>
<li>Follow-up after return with a review request.</li>
</ul>
<h2>6. Reviews and trust</h2>
<ul>
<li>Reviews only from verified rentals.</li>
<li>Ratings for both sides if you run a marketplace with many hosts.</li>
<li>Verified host profiles and clear rules for listings.</li>
</ul>
<h2>7. Admin panel and reports</h2>
<ul>
<li>Daily view: what goes out, what comes back, what is overdue.</li>
<li>Item history: rentals, revenue, maintenance and damages.</li>
<li>Utilisation and revenue reports by item, category and period.</li>
<li>Roles for owners, managers and staff at different locations.</li>
</ul>
<h2>8. Mobile</h2>
<ul>
<li>A responsive booking flow is a must from day one: most customers search and book on a phone.</li>
<li>Native iOS and Android apps make sense when customers rent often, or when staff need an app for handovers. With us, apps are added to a platform from €4,970 for Android and €5,970 for iOS. More on <a href="/mobile-apps.html">mobile apps</a>.</li>
</ul>
<h2>9. Marketplace features, if you need them</h2>
<p>If many hosts will list their own cars, tools or property, add host dashboards, commissions, payouts, listing moderation and dispute handling. These are separate features with their own complexity, so decide early which model you are building.</p>
<h2>10. Integrations</h2>
<ul>
<li>Accounting export for invoices and payments, so bookkeeping does not retype data.</li>
<li>A CRM or customer list for business clients who rent regularly.</li>
<li>Analytics and conversion tracking, so you know which ads and pages bring bookings.</li>
<li>An API, so mobile apps, partner websites or a telematics system can connect later.</li>
</ul>
<p>Integrations are easy to postpone and expensive to retrofit, so at least plan the API from the beginning, even if the first version uses only a few connections.</p>
<h2>What to launch first</h2>
<p>For a single fleet, the minimum is the availability calendar, pricing, online payment or deposit, confirmations and an admin view of today's handovers. Contracts, damage reports and reviews can follow in the second phase if needed. For a marketplace, host onboarding and payouts belong in the first version, because without them there is nothing to book.</p>
<h2>Ready-made tool or your own platform?</h2>
<p>For a small fleet, a booking widget connected to your website may be enough. When your rules, payments and documents do not fit, or when you plan a marketplace, your own platform pays off. Our turnkey rental platform starts at €21,790 and goes live in 2-4 months, built on the same foundation as RentMe. A booking module inside a custom CRM is also possible, starting from €4,500. Read more on <a href="/car-rental-website.html">rental website development</a>, <a href="/platforms.html">platforms</a> and <a href="/crm-development.html">CRM systems</a>.</p>""",
            "faq": [
                ("What is the most important feature of a rental booking system?", "An accurate availability calendar per item. Everything else, from payments to reminders, depends on it."),
                ("Should customers pay the full amount online?", "Not necessarily. Many rental businesses take a deposit or a percentage online and the rest on pickup. The system should support the model you choose."),
                ("How much does a rental platform cost?", "Our turnkey rental platform starts at €21,790. A booking module inside a custom CRM starts at €4,500."),
            ],
            "services": ["platforms", "crm", "apps"],
        },
        "b2b-leads-baltics": {
            "slug": "how-to-find-b2b-clients-in-the-baltics.html",
            "title": "How to Find B2B Clients in the Baltics | BoostLab",
            "desc": "How to find B2B clients in Estonia, Latvia and Lithuania: business registers, building target lists, cold email rules and measuring results.",
            "h1": "How to find B2B clients in the Baltics",
            "lead": "A practical workflow for building target lists, reaching companies by email within the rules and measuring what brings deals.",
            "date": _DATE, "iso": _ISO, "minutes": 7,
            "body": """<p>The Baltic markets are small enough that a focused B2B company can reach a large share of its potential clients directly, and open enough that the data to do it is public. What separates campaigns that bring deals from campaigns that burn a domain is preparation: a clear target, a clean list, a legal approach and honest measurement.</p>
<h2>Start with the ideal client</h2>
<p>Before collecting any data, describe who buys from you. Industry, company size, location, whether they have a website, and the problem you solve for them. Look at your best existing clients: what do they have in common? A short description such as "construction companies in Tallinn and Tartu with 10-50 employees" is far more useful than "SMEs in Estonia".</p>
<h2>Where company data comes from</h2>
<p>All three Baltic countries and Finland keep official business registers with company names, registration codes, addresses, legal forms and activity codes. Estonia's e-Business Register is a well-known example, and Latvia and Lithuania publish company data as open data. Activity codes (NACE, called EMTAK in Estonia) let you filter by industry, and register data can be combined with company websites to find general contact addresses.</p>
<p>Collecting and cleaning this data yourself takes time: different formats per country, duplicate records, inactive companies and missing emails. That is the work BalticLeads does. It holds 1.4 million companies from the business registers of Estonia, Latvia, Lithuania and Finland, about 744,000 of them with an email address.</p>
<h2>Building the list</h2>
<ul>
<li><strong>Filter narrowly.</strong> Country, industry, city and size. A list of 500 relevant companies beats 20,000 random ones.</li>
<li><strong>Use company addresses.</strong> Prefer generic role addresses like info@ or sales@. Free and personal webmail addresses add legal risk and hurt deliverability.</li>
<li><strong>Split into segments.</strong> Each segment gets its own message. A dental clinic and a logistics company need different arguments.</li>
<li><strong>Remove existing clients and past opt-outs</strong> before every send.</li>
</ul>
<h2>The rules for cold outreach</h2>
<p>Cold B2B email to companies is allowed on an opt-out basis in Estonia, Latvia and Lithuania; in Lithuania this has applied since 22 April 2026. In practice that means:</p>
<ul>
<li><strong>Role addresses are company contact data.</strong> Addresses like info@ or sales@ belong to the company, not to a person.</li>
<li><strong>Named people are personal data.</strong> An address like jaan.tamm@company.ee is personal data under GDPR. If you contact named people, you need to inform them where you got their data and why, as required by Article 14 of GDPR.</li>
<li><strong>Every email needs an unsubscribe link.</strong> Make it one click, and make it work.</li>
<li><strong>Objections are honoured immediately.</strong> When a company asks to stop, it goes on a suppression list for all future campaigns.</li>
<li><strong>Identify yourself.</strong> A real sender name, company name and contact details in every message.</li>
</ul>
<p>This is a summary for orientation, not legal advice. For your specific case, check with a lawyer.</p>
<h2>Protecting deliverability</h2>
<p>Legal is one side; inbox placement is the other. Send from a properly configured domain with SPF and DKIM, warm up new mailboxes, keep daily volumes per mailbox low and stop sending to addresses that bounce. Many teams use a separate domain for outreach so that their main domain's reputation is never at risk.</p>
<h2>The BalticLeads workflow</h2>
<ol>
<li><strong>Describe your ideal client.</strong> In AI search you write in plain words who you are looking for, and the platform turns it into filters.</li>
<li><strong>Refine and check the count.</strong> Adjust industry, city and size until the list is focused.</li>
<li><strong>Buy the database.</strong> You pay for the contacts you actually need, and the list is saved to your account.</li>
<li><strong>Launch an email campaign.</strong> Each campaign is moderated before sending. Global opt-out and automatic unsubscribe handling are built in, and free or personal webmail addresses are hidden.</li>
<li><strong>Handle replies.</strong> Move interested companies into your CRM and follow up quickly.</li>
</ol>
<p>BalticLeads is built and run by our team, which is why we use it directly in client projects. If you prefer, we take on the whole process: targeting, copy, a landing page, outreach and Google and Meta ads. See <a href="/b2b-lead-generation.html">B2B lead generation</a>.</p>
<h2>Writing the email</h2>
<ul>
<li>Short: five to eight sentences.</li>
<li>About their problem, not your company history.</li>
<li>One clear next step: a reply, a short call or a link to a focused <a href="/web-development.html">landing page</a>.</li>
<li>One or two polite follow-ups that add something new, then stop.</li>
<li>In the language of the recipient: Estonian, Latvian, Lithuanian, Russian or English.</li>
</ul>
<h2>Measuring what works</h2>
<p>Do not judge a campaign by open rates; they are unreliable because of privacy features in email clients. Track instead:</p>
<ul>
<li><strong>Bounce rate</strong>, to keep the list and the domain healthy.</li>
<li><strong>Reply rate and positive replies</strong> per segment and per message.</li>
<li><strong>Meetings booked</strong> and <strong>deals closed</strong>, tracked in a CRM.</li>
<li><strong>Unsubscribes</strong>, as a signal that the targeting or the message is off.</li>
</ul>
<p>Test one change at a time: a new segment or a new message, not both. After a few waves you will know which industries and arguments bring revenue, and you can add <a href="/advertising.html">ads</a> aimed at the same companies to reinforce the emails.</p>""",
            "faq": [
                ("Is cold B2B email legal in Estonia, Latvia and Lithuania?", "Cold B2B email to companies is allowed on an opt-out basis in all three countries, in Lithuania since 22 April 2026. Include an unsubscribe link and honour objections immediately. This is not legal advice."),
                ("Can I email named employees?", "Their addresses are personal data under GDPR. You need to inform them about the source and purpose of processing (GDPR Article 14) and stop immediately if they object. Role addresses like info@ are simpler."),
                ("How many companies should the first campaign target?", "Start focused: a few hundred to a few thousand well-matched companies in one or two segments, so you can learn what works before scaling."),
            ],
            "services": ["leadgen", "ads", "crm"],
        },
        "seo-checklist": {
            "slug": "website-seo-checklist-before-launch.html",
            "title": "Website SEO Checklist Before Launch | BoostLab",
            "desc": "Technical and content SEO checklist before launching a website: structure, meta tags, schema, hreflang, speed, analytics and Google Search Console.",
            "h1": "Website SEO checklist before launch",
            "lead": "Everything to check before a new website goes live, so Google can find, understand and rank it from day one.",
            "date": _DATE, "iso": _ISO, "minutes": 6,
            "body": """<p>Most SEO problems on new websites are created before launch and are expensive to fix afterwards: wrong URLs, missing redirects, duplicate pages, language versions that compete with each other. This is the checklist we run on every project before it goes live. It works for a landing page, a business website and an online store.</p>
<h2>Structure and URLs</h2>
<ul>
<li><strong>One page per search intent.</strong> Each important service, product category or location has its own page targeting one main keyword.</li>
<li><strong>Clean, readable URLs</strong> in the language of the page, without IDs or parameters.</li>
<li><strong>A logical hierarchy</strong> that is no more than three clicks deep for important pages.</li>
<li><strong>Internal links</strong> between related pages, with descriptive anchor text.</li>
<li><strong>Redirects from the old site.</strong> Every old URL that had traffic or links gets a 301 redirect to its new equivalent.</li>
<li><strong>A useful 404 page</strong> that returns a real 404 status.</li>
</ul>
<h2>Titles, descriptions and headings</h2>
<ul>
<li>A unique title on every page, about 50-60 characters, with the main keyword near the start.</li>
<li>A unique meta description of 120-155 characters that gives a reason to click.</li>
<li>Exactly one H1 per page that matches the topic, and H2s that structure the content.</li>
<li>Descriptive alt text for meaningful images.</li>
</ul>
<h2>Indexing</h2>
<ul>
<li><strong>Canonical tags</strong> on every page, pointing to the preferred URL.</li>
<li><strong>XML sitemap</strong> with all indexable pages, and nothing that redirects or returns errors.</li>
<li><strong>robots.txt</strong> that allows crawling and points to the sitemap. Check that the staging "noindex" is removed.</li>
<li><strong>HTTPS everywhere</strong>, with one version of the domain (with or without www) redirecting to the other.</li>
</ul>
<h2>Multilingual websites and hreflang</h2>
<p>In the Baltics, websites often run in two to four languages. Without correct hreflang tags, Google may show the wrong version to users or treat versions as duplicates.</p>
<ul>
<li>Every language version links to all others with hreflang, including itself.</li>
<li>An x-default version for users whose language is not covered.</li>
<li>Localized URLs and translated titles, not just translated body text.</li>
<li>A language switcher that leads to the same page in the other language, not to the home page.</li>
</ul>
<h2>Structured data</h2>
<ul>
<li><strong>Organization or LocalBusiness</strong> with name, address, phone and logo.</li>
<li><strong>Service, Product or Offer</strong> markup where it applies, with prices.</li>
<li><strong>FAQPage</strong> for question sections and <strong>BreadcrumbList</strong> for navigation.</li>
<li><strong>Article</strong> or BlogPosting for blog posts, with dates.</li>
<li>Validate everything with Google's Rich Results Test before launch.</li>
</ul>
<h2>Speed and Core Web Vitals</h2>
<ul>
<li>Images in modern formats (WebP or AVIF), with width and height set to avoid layout shifts.</li>
<li>Lazy loading for images below the fold, priority loading for the main hero image.</li>
<li>Fonts preloaded or served with font-display swap, only the weights you use.</li>
<li>No unused scripts and plugins; third-party tags loaded only when needed.</li>
<li>Test on a mid-range phone on a mobile connection, not only on an office computer.</li>
</ul>
<h2>Content</h2>
<ul>
<li>Original copy written for the customer, answering the questions they ask before buying.</li>
<li>Prices or price ranges where possible; they are among the most searched details.</li>
<li>Contact details, address and opening hours consistent with your Google Business profile.</li>
<li>A short FAQ on key pages, written in the words customers use.</li>
</ul>
<h2>Mobile and accessibility</h2>
<ul>
<li>Google indexes the mobile version first, so check every page on a phone: menus, forms, tables and buttons.</li>
<li>Tap targets large enough, text readable without zooming, no horizontal scrolling.</li>
<li>Form fields with labels, sufficient colour contrast and keyboard navigation, following WCAG basics.</li>
<li>Pop-ups and cookie banners that do not cover the main content on small screens.</li>
</ul>
<h2>Analytics and Search Console</h2>
<ul>
<li><strong>Google Analytics 4</strong> installed with consent mode and a GDPR cookie banner.</li>
<li><strong>Conversions</strong> defined: form submissions, calls, bookings, purchases.</li>
<li><strong>Google Search Console</strong> verified for the domain, with the sitemap submitted.</li>
<li>For a relaunch: compare indexed pages and rankings before and after, and watch the coverage report for errors in the first weeks.</li>
</ul>
<h2>After launch</h2>
<p>SEO does not end at launch. Check Search Console weekly in the first month, fix crawl errors, and add content where you see impressions without clicks. Pages that rank on the second page often need only a better title, a few answered questions or more internal links to move up. New websites need time to build authority; good structure lets that work pay off faster.</p>
<p>In every BoostLab project, SEO structure, schema markup, hreflang, Core Web Vitals, GA4 and Search Console are part of the baseline, not extras. See <a href="/web-development.html">web development</a> and <a href="/pricing.html">pricing</a>.</p>""",
            "faq": [
                ("When should SEO start on a new website?", "Before design. The page structure and URLs should be planned around the searches your customers make; fixing them after launch is slower and riskier."),
                ("Do I need hreflang for a website in two languages?", "Yes. Hreflang tells Google which version to show to which users and prevents language versions from competing with each other."),
                ("How long until a new website ranks?", "It varies by competition. Technical SEO lets Google index the site quickly, but rankings for competitive keywords need content and links over months."),
            ],
            "services": ["web", "ads"],
        },
        "landing-vs-website": {
            "slug": "landing-page-vs-website.html",
            "title": "Landing Page vs Website: Which Do You Need? | BoostLab",
            "desc": "Landing page or full website? When each one fits, what they cost and how long they take to build, with a simple way to choose for your business.",
            "h1": "Landing page vs website: which do you need?",
            "lead": "A landing page sells one thing to one audience. A website represents the whole business. Here is how to choose, and when to have both.",
            "date": _DATE, "iso": _ISO, "minutes": 5,
            "body": """<p>"Do we need a landing page or a full website?" comes up in almost every first call. Both are useful, but they solve different problems. Choosing the wrong one usually means paying for pages nobody visits, or sending ad traffic to a page that does not convert.</p>
<h2>What a landing page is</h2>
<p>A landing page is a single page built around one offer and one action: leave a request, book a call, buy, register. There is no menu leading elsewhere and no content that distracts from the goal. Visitors usually arrive from a specific source, such as an ad, an email campaign or a QR code, and the page continues exactly that message.</p>
<h2>What a website is</h2>
<p>A website is the full presence of your business: several services, about, prices, cases, blog, contacts, often in several languages. It is built to be found in Google for many different searches and to answer the questions of people who are comparing you with competitors.</p>
<h2>Side by side</h2>
<table><thead><tr><th></th><th>Landing page</th><th>Business website</th></tr></thead><tbody>
<tr><td>Goal</td><td>One offer, one action</td><td>Present the whole business</td></tr>
<tr><td>Main traffic</td><td>Ads, email, social</td><td>Google search, referrals, direct</td></tr>
<tr><td>Pages</td><td>One</td><td>Several to dozens</td></tr>
<tr><td>SEO potential</td><td>Limited to one topic</td><td>Many keywords and locations</td></tr>
<tr><td>Price with BoostLab</td><td>From €700</td><td>From €1,700</td></tr>
<tr><td>Timeline</td><td>5-7 working days</td><td>2-3 weeks</td></tr>
</tbody></table>
<h2>When a landing page fits</h2>
<ul>
<li><strong>You are testing an idea.</strong> A new product or service can be validated with a landing page and a small ad budget before investing in a full website.</li>
<li><strong>You run ads or outreach for one offer.</strong> Sending paid traffic to a page that talks about exactly what the ad promised usually converts better than sending it to a home page.</li>
<li><strong>You need something live fast.</strong> An event, a seasonal offer or a launch with a fixed date.</li>
<li><strong>You have one core service.</strong> A specialist or a small business with one offer may not need more than one strong page at the start.</li>
</ul>
<h2>When you need a website</h2>
<ul>
<li><strong>You offer several services</strong> to different audiences, each with its own questions.</li>
<li><strong>Organic search matters.</strong> To rank for many keywords, locations and languages, you need a page for each.</li>
<li><strong>Trust is part of the sale.</strong> B2B buyers and larger clients check cases, team, prices and company details before they contact you.</li>
<li><strong>You serve several markets.</strong> Multilingual websites with hreflang let each market find its own version in Google.</li>
</ul>
<h2>The best answer is often both</h2>
<p>Many of our clients have a business website as the base and separate landing pages for campaigns. The website builds search visibility and trust over time; landing pages turn ad budgets and outreach into requests. Landing pages can live on the same domain, share the design and feed the same CRM, so leads from every source end up in one place. Over time you can see which campaigns and which pages bring the requests that turn into customers.</p>
<h2>Common mistakes</h2>
<ul>
<li><strong>Sending ads to the home page.</strong> Visitors who clicked on a specific offer have to search for it again, and many leave.</li>
<li><strong>A landing page with a full menu.</strong> Every extra link is a way out. Keep navigation minimal and the action visible on every screen.</li>
<li><strong>A website without clear actions.</strong> Each page should end with a next step: a form, a call button or a booking link.</li>
<li><strong>No tracking.</strong> Without conversion tracking you cannot tell whether the page or the traffic is the problem.</li>
</ul>
<h2>How to decide in five minutes</h2>
<ol>
<li>Where will most visitors come from in the next three months? Ads or email point to a landing page; search points to a website.</li>
<li>How many offers do you need to explain? One suggests a landing page; several suggest a website.</li>
<li>When must it be live? Under two weeks favours a landing page.</li>
<li>What is the budget? From €700 for a landing page, from €1,700 for a business website. You can start with the first and extend it later.</li>
</ol>
<h2>What every option includes with us</h2>
<p>Both landing pages and websites come with conversion-focused copy and design, mobile-first layout, SEO setup, Google Analytics 4 and conversion tracking, so you see from day one where requests come from. If you plan to run traffic to the page, our <a href="/advertising.html">ads setup</a> starts at €599. More details on <a href="/web-development.html">web development</a> and the <a href="/pricing.html">pricing page</a>.</p>""",
            "faq": [
                ("Can a landing page rank in Google?", "Yes, for one focused topic. For many services, locations or languages you need a website with a page for each."),
                ("Can a landing page be turned into a website later?", "Yes. We design landing pages so they can become the first page of a larger website without starting over."),
                ("How much does each cost?", "With BoostLab, a landing page starts at €700 and a business website at €1,700. You get a fixed quote after a free call."),
            ],
            "services": ["web", "ads"],
        },
    },
}
