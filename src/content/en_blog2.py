# Blog, batch 2 (EN): four more posts. Executed after en_seo.py. Spec: BLOG2_SPEC.md.
# Only adds posts; keys are shared by all languages.

_DATE2, _ISO2 = "5 November 2026", "2026-11-05"

T["blog"]["posts"].update({
    "ecommerce-cost": {
        "slug": "how-much-does-an-online-store-cost-estonia.html",
        "title": "How Much Does an Online Store Cost in Estonia? | BoostLab",
        "desc": "Online store prices in Estonia and the Baltics: costs by scope, what drives the price, monthly running costs and custom build vs Shopify or WooCommerce.",
        "h1": "How much does an online store cost in Estonia?",
        "lead": "A practical breakdown of what an online store costs to build and to run in Estonia and the Baltics, and how to get a fixed quote instead of a guess.",
        "date": _DATE2, "iso": _ISO2, "minutes": 7,
        "body": """<p>An online store is not one product with one price. A shop with 30 products, one language and card payments is a very different job from a store with 5,000 products, variants, three languages, parcel lockers in three countries and daily export to accounting. Below is how we price e-commerce projects at BoostLab, what moves the number up or down, and what the store costs every month after launch.</p>
<h2>Online store prices by scope</h2>
<p>Our online stores start at €3,500 and launch in 3-5 weeks. The table shows how typical projects grow from that starting point. Every project gets a fixed quote after a short call.</p>
<table><thead><tr><th>Scope</th><th>What it includes</th><th>Typical timeline</th></tr></thead><tbody>
<tr><td>Starter store (from €3,500)</td><td>Small catalogue, one or two languages, card and bank-link payments, parcel lockers, order emails</td><td>3-5 weeks</td></tr>
<tr><td>Growing store</td><td>Larger catalogue with variants and filters, several languages, discount codes, accounting export, product feeds for ads</td><td>Towards the upper end of 3-5 weeks or longer</td></tr>
<tr><td>Store with custom logic</td><td>B2B prices per customer, customer accounts, subscriptions, warehouse or ERP integration, several countries</td><td>Scoped individually, often in phases</td></tr>
<tr><td>Testing an idea first</td><td>A landing page for one product or pre-orders (from €700)</td><td>5-7 working days</td></tr>
</tbody></table>
<p>If you are not sure the product will sell online, a landing page with pre-orders or a request form is a cheaper way to test demand before investing in a full store. See the <a href="/pricing.html">pricing page</a> for all packages.</p>
<h2>What drives the price</h2>
<ul>
<li><strong>Catalogue size and structure.</strong> The number of products matters less than how they are organised. Variants (size, colour, material), filters, bundles and product attributes take design and development time. Importing an existing catalogue from a spreadsheet or old platform is a separate piece of work.</li>
<li><strong>Payments.</strong> Estonian customers expect bank links (Swedbank, SEB, LHV and others) next to card payments. Providers such as Montonio or Stripe cover these, and each integration includes testing refunds, failed payments and receipts.</li>
<li><strong>Shipping integrations.</strong> Parcel lockers are the default in the Baltics. Connecting Omniva, DPD and SmartPosti so the customer picks a locker at checkout and you print labels from the admin takes real work, especially across several countries.</li>
<li><strong>Accounting export.</strong> Sending orders and invoices to your accounting software automatically saves hours every week, but it depends on what the software accepts.</li>
<li><strong>Languages.</strong> Estonian, English and Russian are common in Estonia, plus Latvian, Lithuanian or Finnish when you sell abroad. Each language needs translated products, categories and emails, plus hreflang so Google shows the right version.</li>
<li><strong>Design.</strong> A custom design costs more than a theme, but it is built around your products and brand rather than around a demo.</li>
<li><strong>Taxes and legal texts.</strong> Prices shown with VAT (24% in Estonia since 2025), VAT rules for other EU countries, terms of sale, return policy and cookie consent all need to be right before launch.</li>
</ul>
<h2>Monthly running costs</h2>
<p>The build is a one-time cost. These are the costs that continue every month:</p>
<ul>
<li><strong>Hosting and domain.</strong> A store needs reliable hosting, SSL and backups. We bill hosting at cost or deploy to your own server.</li>
<li><strong>Payment fees.</strong> Card and bank-link providers charge per transaction, usually a percentage, a fixed fee or both. Compare current tariffs before choosing, because at volume the difference adds up.</li>
<li><strong>Shipping contracts.</strong> Parcel locker prices depend on your contract with each carrier.</li>
<li><strong>Platform subscriptions and apps.</strong> On hosted platforms, the plan fee plus paid apps for reviews, filters, translations or invoices can become a noticeable monthly bill.</li>
<li><strong>Maintenance.</strong> Updates, security patches, small changes and new features. Budget for them from day one.</li>
<li><strong>Marketing.</strong> A store needs traffic. SEO takes months, and ads need both a setup fee and an ad budget. Our <a href="/advertising.html">ads setup</a> starts at €599.</li>
</ul>
<h2>Custom store vs Shopify or WooCommerce</h2>
<p>We build custom stores, but a hosted platform is sometimes the better choice. An honest comparison:</p>
<table><thead><tr><th>Factor</th><th>Shopify</th><th>WooCommerce</th><th>Custom store</th></tr></thead><tbody>
<tr><td>Start</td><td>Fast, ready themes</td><td>Fast with a theme</td><td>3-5 weeks</td></tr>
<tr><td>Upfront cost</td><td>Low</td><td>Low to medium</td><td>From €3,500</td></tr>
<tr><td>Monthly cost</td><td>Plan fee plus paid apps</td><td>Hosting plus paid plugins</td><td>Hosting plus optional support</td></tr>
<tr><td>Local payments and lockers</td><td>Via apps, quality varies</td><td>Via plugins, quality varies</td><td>Integrated directly</td></tr>
<tr><td>Custom logic (B2B prices, rules)</td><td>Limited by the platform</td><td>Possible, but plugins pile up</td><td>Built to fit</td></tr>
<tr><td>Speed and code</td><td>Good, theme dependent</td><td>Depends on plugins</td><td>Lean, only what you use</td></tr>
<tr><td>Ownership</td><td>Vendor platform</td><td>Yours, open source</td><td>Yours</td></tr>
</tbody></table>
<p>Shopify is a good choice for a small catalogue, standard checkout and a team that wants to manage everything itself without a developer. WooCommerce works well if you already run WordPress and keep the plugin list short. A custom store pays off when local payments, shipping and accounting must work without workarounds, when you need B2B pricing or other rules a platform does not support, or when monthly app fees start to exceed what a one-time build would cost.</p>
<h2>What is included with BoostLab</h2>
<p>Every store we build comes mobile-first, with SEO structure for categories and products, schema markup, Google Analytics 4 and e-commerce conversion tracking, product feeds for Google and Meta ads, GDPR cookie consent, an admin panel for products and orders, and a warranty period with free bug fixes. Read more on our <a href="/ecommerce-development.html">e-commerce development</a> page.</p>
<h2>How to get a fixed quote</h2>
<ol>
<li><strong>Count your products and variants.</strong> A rough number and an example product with all its options is enough.</li>
<li><strong>List payments, carriers and countries.</strong> Which bank links, which parcel lockers, which markets.</li>
<li><strong>Name your accounting software.</strong> So we can check how orders and invoices are exported.</li>
<li><strong>Say which languages you need at launch</strong> and which can wait.</li>
<li><strong>Share two or three stores you like</strong> and what exactly you like about them.</li>
</ol>
<p>With that, we send a fixed quote after a free call and show a clickable prototype before development starts. For a broader view of website budgets, see <a href="/blog/how-much-does-a-website-cost-estonia.html">how much a website costs in Estonia</a>.</p>""",
        "faq": [
            ("How much does an online store cost in Estonia?", "With BoostLab, an online store starts at €3,500 and launches in 3-5 weeks. The final price depends on catalogue size, payments, shipping integrations, accounting export and languages, and you get a fixed quote after a free call."),
            ("Should I use Shopify or a custom store?", "Shopify suits a small catalogue and a standard checkout. A custom store pays off when you need local bank links and parcel lockers without workarounds, B2B pricing or other custom rules, or when monthly app fees grow large."),
            ("What are the monthly costs after launch?", "Hosting and domain, payment provider fees per transaction, shipping contracts, optional maintenance and marketing. On hosted platforms, add the plan fee and paid apps."),
        ],
        "services": ["web"],
    },
    "crm-construction": {
        "slug": "crm-for-construction-companies.html",
        "title": "CRM for Construction Companies | BoostLab",
        "desc": "What a CRM for a construction or renovation company needs: leads, estimates, site cards, subcontractors, photo reports, acts, invoices and mobile use.",
        "h1": "CRM for construction and renovation companies",
        "lead": "Construction firms lose money in the gaps between the office, the site and the accountant. Here is what a CRM has to do to close those gaps, and when to build your own.",
        "date": _DATE2, "iso": _ISO2, "minutes": 7,
        "body": """<p>Most construction and renovation companies already have a system. It is usually a mix of email, phone calls, a shared spreadsheet of objects, WhatsApp groups with photos, estimates in Excel and invoices in the accounting software. It works until the company grows past a handful of projects at once. Then requests get lost, estimates are copied from old files with old prices, and nobody knows whether a job made money until weeks after it closed. A CRM built for construction connects these pieces.</p>
<h2>Leads from the website and phone</h2>
<p>Every request should land in one list, whatever the source: the website form, a call, an email or a referral. A good request form asks the questions you need for a first estimate, such as type of work, address, approximate area, desired timeline and photos. Each lead gets a status (new, site visit booked, estimate sent, won, lost) and a responsible person, and the system reminds that person when a lead has not been answered. Over time you see which sources bring jobs, not just requests, which is what you need to decide where to spend on <a href="/advertising.html">advertising</a>.</p>
<h2>Estimates and quotes</h2>
<p>Estimates are where construction companies win or lose margin. In a CRM, an estimate is built from a price list of work items and materials, with quantities, units and your markup. Templates for common jobs (bathroom renovation, roofing, facade, floor) cut preparation time from hours to minutes. The estimate is sent as a branded PDF, versions are kept, and when the client accepts, the same items become the budget for the object. No retyping, no prices from last year.</p>
<h2>Object cards</h2>
<p>Each construction site gets its own card: address, client, contract, budget, schedule, team, subcontractors, documents, photos and all communication. Anyone in the office can open it and answer a client's question without calling the site manager. The object list shows every active site with its stage and whether it is on time and on budget.</p>
<h2>Subcontractors</h2>
<p>Most firms rely on subcontractors for electrics, plumbing, ventilation or finishing. The CRM keeps a register of them with contacts, trades, rates and notes on quality, and links them to objects with agreed amounts and dates. Their invoices are matched against what was agreed, so you see the real cost of each object rather than discovering it at year end.</p>
<h2>Photo reports from the site</h2>
<p>Photos are the most useful record on a construction site and the hardest to find later. With a mobile view, the site manager takes photos straight into the object card, tagged with the date and stage: before work, hidden works before they are covered, finished result. That protects you in disputes, makes acceptance easier and gives you material for your portfolio. Clients can receive a short progress report with photos without anyone writing a separate email.</p>
<h2>Acts and invoices</h2>
<p>Construction is billed in stages. The CRM generates acts of completed work from the estimate items, so the client signs off what was done in that stage, and the invoice follows from the act. Prepayments, stage payments and final payments are tracked against the contract amount. Invoices can be sent to your accounting software rather than typed in again, depending on what that software accepts.</p>
<h2>Material costs and profitability</h2>
<p>When materials, subcontractor invoices and hours are recorded against each object, you can compare planned and actual cost while the job is still running, not after. That shows which types of jobs and which estimates are profitable, and where prices in the price list need to change. Even a simple report of "budget vs actual" per object usually changes how a company quotes.</p>
<h2>Mobile use on site</h2>
<p>A construction CRM that only works on a desktop will not be used on site. Site managers and foremen need a mobile view that loads on a weak connection, with large buttons and only what they need: today's objects, tasks, photo upload, material requests and notes. Office staff keep the full view. For field teams that work offline often, a native mobile app can be added later.</p>
<h2>Build or buy?</h2>
<p>There are ready-made construction management tools and general CRMs such as Pipedrive or HubSpot. They are a reasonable start if you mainly need a sales pipeline and a shared calendar. Signs that a custom CRM makes more sense:</p>
<ul>
<li>Your estimates follow your own price list and logic that does not fit a generic quote tool.</li>
<li>You need leads, estimates, objects, subcontractors, acts and invoices in one place, not in four tools that do not talk to each other.</li>
<li>Your team is large enough that per-user fees become a serious monthly cost.</li>
<li>You want local language versions for office and site staff, and integration with the accounting software you already use.</li>
</ul>
<table><thead><tr><th>Need</th><th>General CRM</th><th>Custom construction CRM</th></tr></thead><tbody>
<tr><td>Lead pipeline</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Estimates from your price list</td><td>Limited or via add-ons</td><td>Built in</td></tr>
<tr><td>Object cards with budget vs actual</td><td>Workarounds</td><td>Built in</td></tr>
<tr><td>Acts of completed work</td><td>Rarely</td><td>Generated from estimate</td></tr>
<tr><td>Photo reports by stage</td><td>File attachments</td><td>Mobile upload into the object</td></tr>
<tr><td>Cost as the team grows</td><td>Per user</td><td>Flat</td></tr>
</tbody></table>
<p>We compare the options in more detail in <a href="/blog/custom-crm-vs-hubspot-pipedrive.html">custom CRM vs HubSpot or Pipedrive</a>.</p>
<h2>How we build it</h2>
<p>A custom CRM with BoostLab starts at €4,500 and the first version goes live from 4 weeks. We start by mapping how a request becomes an estimate, an object, acts and invoices in your company today, then design a clickable prototype that the office and a site manager test before development. The first version usually covers leads, estimates, object cards and photo reports, and acts, subcontractors and cost tracking follow in the next phase. The code and data are yours. Read more on <a href="/crm-development.html">CRM development</a>, see <a href="/pricing.html">pricing</a>, or add a <a href="/web-development.html">website</a> with a request form that sends leads straight into the CRM.</p>""",
        "faq": [
            ("What should a CRM for a construction company include?", "Lead capture from the website and phone, estimates from your price list, object cards with budget and documents, subcontractors, photo reports from site, acts of completed work, invoices and cost tracking per object."),
            ("Can site managers use it on a phone?", "Yes. We build a mobile view for site staff with today's objects, tasks, photo upload and notes. A native app can be added later if teams often work offline."),
            ("How much does a custom construction CRM cost?", "A custom CRM with BoostLab starts at €4,500, with the first version live from 4 weeks. You get a fixed quote after a call and a prototype before development."),
        ],
        "services": ["crm"],
    },
    "google-ads-small-business": {
        "slug": "google-ads-for-small-business-estonia.html",
        "title": "Google Ads for Small Business in Estonia | BoostLab",
        "desc": "Google Ads for a small business in Estonia: budget logic, Search vs Performance Max, keywords, landing pages, conversion tracking and a 30-day plan.",
        "h1": "Google Ads for a small business in Estonia",
        "lead": "Google Ads can bring customers within days or burn a budget just as fast. This is how to set it up so a small business gets requests, not just clicks.",
        "date": _DATE2, "iso": _ISO2, "minutes": 7,
        "body": """<p>Google Ads is the fastest way to appear in front of people who are already searching for what you sell. It is also easy to waste money on, because the default settings are designed to spend your budget, not to protect it. For a small business in Estonia, a few decisions at the start make most of the difference.</p>
<h2>Budget logic</h2>
<p>Google Ads works as an auction. Each time someone searches, advertisers bidding on that search compete, and the price per click depends on the bids, the relevance of the ad and the quality of the landing page. In a small market like Estonia some niches have few advertisers and cheap clicks, while others (law, construction, finance, real estate) are competitive.</p>
<p>Work backwards from your numbers. If a customer is worth a certain amount to you, and you know roughly what share of enquiries become customers, you know what you can afford per enquiry. The budget has to buy enough clicks for the campaign to collect data and get enquiries in the first weeks. For local campaigns we recommend at least €500-1,000 per month in ad spend. The management fee is separate and paid to the agency, while the ad spend is paid directly to Google. With smaller budgets, narrow the campaign to your most profitable service and area rather than spreading thin.</p>
<h2>Search or Performance Max?</h2>
<ul>
<li><strong>Search campaigns</strong> show text ads for the keywords you choose. You see the search terms, control the wording and decide where the money goes. For most small service businesses this is the right starting point.</li>
<li><strong>Performance Max</strong> runs across Search, YouTube, Display, Gmail and Maps from one campaign, with Google choosing placements automatically. It can work well for online stores with a product feed and enough conversion data, but it needs reliable tracking and gives you less control and visibility.</li>
</ul>
<p>Our default for a new account: start with Search on a narrow set of high-intent keywords, prove that it brings enquiries, then test Performance Max or remarketing once there is conversion data.</p>
<h2>Keywords and negative keywords</h2>
<p>Choose keywords that show intent to buy, not just interest. "Bathroom renovation Tallinn price" is worth more than "bathroom ideas". In Estonia, plan keywords in every language your customers search in: Estonian, Russian and often English. Use phrase and exact match to keep control, and check the search terms report every week.</p>
<p>Negative keywords are just as important. Add words that bring the wrong visitors: "free", "job", "salary", "course", "DIY", competitor names you do not want, and services you do not offer. A good negative keyword list built in the first weeks is often the single biggest saving in a small account.</p>
<h2>The landing page decides the result</h2>
<p>Sending ads to the home page is one of the most common reasons campaigns fail. The visitor clicked on a specific offer and should land on a page about that offer, in the language of the ad, with a clear action visible on the phone screen: a form, a call button or a booking link. Page speed and relevance also feed into Google's Quality Score, which affects how much you pay per click. A focused landing page often lowers the cost per enquiry more than any bid change. With BoostLab, a <a href="/web-development.html">landing page</a> starts at €700 and is ready in 5-7 working days. More on the choice in <a href="/blog/landing-page-vs-website.html">landing page vs website</a>.</p>
<h2>Conversion tracking</h2>
<p>Without conversion tracking, Google optimises for clicks, and you cannot tell which keywords bring customers. Before spending, set up tracking for every action that matters:</p>
<ul>
<li>Form submissions (thank-you page or form event).</li>
<li>Clicks on phone numbers and calls from ads.</li>
<li>Clicks on email addresses.</li>
<li>Bookings or purchases, with value where possible.</li>
</ul>
<p>Connect Google Ads and Google Analytics 4, and respect cookie consent. Then compare enquiries per keyword and per campaign, not just clicks and impressions.</p>
<h2>The first 30 days</h2>
<table><thead><tr><th>When</th><th>What to do</th></tr></thead><tbody>
<tr><td>Before launch</td><td>Account in your company's name, conversion tracking tested, landing page ready, keywords and negatives in every language</td></tr>
<tr><td>Days 1-7</td><td>Check daily that ads run, tracking fires and search terms are relevant; add negatives</td></tr>
<tr><td>Days 8-14</td><td>Pause keywords that spend without results, adjust ad texts, check calls and form quality with the team</td></tr>
<tr><td>Days 15-30</td><td>Shift budget to what brings enquiries, test a second ad variant, review the landing page by device</td></tr>
<tr><td>After 30 days</td><td>Report cost per enquiry, decide whether to scale, add remarketing or a new service</td></tr>
</tbody></table>
<p>Do not judge a campaign in the first days. The account needs time and data, and changing everything at once makes it impossible to see what worked.</p>
<h2>Typical mistakes</h2>
<ul>
<li><strong>Broad match without negatives,</strong> so the budget goes to loosely related searches.</li>
<li><strong>No conversion tracking,</strong> or tracking that counts page views as conversions.</li>
<li><strong>Ads in one language</strong> while customers search in two or three.</li>
<li><strong>Sending traffic to the home page</strong> instead of a page for the offer.</li>
<li><strong>Accepting all automatic recommendations</strong> without checking what they change.</li>
<li><strong>A budget split across too many campaigns</strong> so none of them collects enough data.</li>
<li><strong>An account owned by the agency.</strong> With BoostLab, accounts are always created in the client's name, so the data and history stay yours.</li>
</ul>
<h2>How we work</h2>
<p>Our ads campaign setup costs €599: account structure, keywords and negatives, ad texts, conversion tracking and launch. If you want ongoing management together with social media, ads and SMM cost €1,399 per month. Ad spend is paid separately to Google. See <a href="/advertising.html">advertising</a> and <a href="/pricing.html">pricing</a>.</p>""",
        "faq": [
            ("How much should a small business spend on Google Ads in Estonia?", "For local campaigns we recommend at least €500-1,000 per month in ad spend, paid directly to Google. Management fees are separate. With less, focus on one service and area."),
            ("Search or Performance Max for a new account?", "For most small service businesses, start with Search campaigns on high-intent keywords. Performance Max fits better once you have reliable conversion tracking and data, or for online stores with a product feed."),
            ("Who owns the Google Ads account?", "You do. BoostLab creates accounts in the client's name, so the data, history and billing stay with your company."),
        ],
        "services": ["ads", "web"],
    },
    "redesign-without-seo-loss": {
        "slug": "website-redesign-without-losing-seo.html",
        "title": "Website Redesign Without Losing SEO | BoostLab",
        "desc": "How to redesign a website without losing Google rankings: URL inventory, 301 redirect map, content, metadata, hreflang and a post-launch checklist.",
        "h1": "How to redesign a website without losing Google rankings",
        "lead": "A new design should bring more customers, not a drop in traffic. Most ranking losses after a redesign come from a few avoidable mistakes.",
        "date": _DATE2, "iso": _ISO2, "minutes": 7,
        "body": """<p>A redesign is a good moment to fix design, speed and structure. It is also the moment when many websites lose a large part of their Google traffic, sometimes for months. The reason is rarely the design itself. It is changed URLs without redirects, removed content that used to rank, lost titles and descriptions, or a staging setting left switched on. Here is the process we follow to keep rankings through a redesign.</p>
<h2>1. Make a full URL inventory</h2>
<p>Before anything changes, list every URL the current site has. Combine three sources: a crawl of the site, the pages report in Google Search Console and the landing pages in Google Analytics. Add URLs of images and PDFs that get traffic or links. For each URL, record organic clicks, main queries and whether other sites link to it. This list tells you which pages carry your rankings and must be protected, and which can be merged or removed.</p>
<h2>2. Build a 301 redirect map</h2>
<p>Every old URL that changes needs a permanent 301 redirect to the most relevant new page. Not to the home page, which Google may treat like a missing page, but to the page that answers the same question. Keep it as a simple two-column table: old URL, new URL. Rules to follow:</p>
<ul>
<li>Redirect one to one wherever possible, and merged pages to the page that absorbed their content.</li>
<li>Avoid redirect chains (A to B to C). Point old URLs straight to the final address.</li>
<li>Cover variants: with and without trailing slash, www and non-www, http and https, old language prefixes.</li>
<li>Pages that are truly gone with no replacement can return 404 or 410, but only when nothing useful exists.</li>
</ul>
<p>If URLs can stay the same, keep them. The safest redirect is the one you do not need.</p>
<h2>3. Keep the content that ranks</h2>
<p>A new design often comes with shorter, "cleaner" texts. If a page ranks for a query, the content answering that query has to survive the redesign. Shorten what does not help, but keep the headings, sections and answers that match what people search for. When merging two pages, move the useful parts of both. The same applies to internal links: pages that were well linked in the old navigation should stay well linked.</p>
<h2>4. Carry over the metadata</h2>
<p>Titles and meta descriptions, H1 headings, image alt texts, canonical tags and structured data (schema markup) are easy to lose when templates are rebuilt. Export them from the old site and transfer them, improving where needed but without losing the keywords that brought traffic. Check that every page has a unique title and that canonical tags point to the new URLs, not to the staging domain.</p>
<h2>5. Hreflang for multilingual sites</h2>
<p>In the Baltics, most business sites run in two to four languages. If language versions move, for example from a subdomain to a folder, every hreflang tag must point to the new URLs, each version must reference all others and itself, and the redirect map must cover every language. A mistake here can make Google show the Russian page to Estonian searchers or drop one language version altogether.</p>
<h2>6. Prepare Search Console and launch</h2>
<ul>
<li>Make sure the staging site was blocked from indexing, and that the block (noindex, password or robots.txt rule) is removed at launch.</li>
<li>Upload a fresh XML sitemap with the new URLs and submit it in Search Console.</li>
<li>If the domain changes, use the change of address tool in Search Console.</li>
<li>Keep GA4 and conversion tracking working from the first minute, so you can compare before and after.</li>
</ul>
<h2>7. Speed and Core Web Vitals</h2>
<p>A redesign should make the site faster, not slower. Heavy animations, large images and many scripts often arrive with a new design. Test the main templates on a phone before launch and fix what slows them down. A faster site helps both rankings and conversions.</p>
<h2>Post-launch monitoring checklist</h2>
<table><thead><tr><th>When</th><th>Check</th></tr></thead><tbody>
<tr><td>Launch day</td><td>Indexing allowed, sitemap submitted, redirects from the map tested in bulk, no redirect chains, analytics and conversions firing</td></tr>
<tr><td>First week</td><td>Search Console coverage and 404 reports, new URLs being indexed, top pages return 200, hreflang errors</td></tr>
<tr><td>Weeks 2-4</td><td>Clicks and positions for top queries compared with before, pages that lost traffic reviewed one by one</td></tr>
<tr><td>Months 1-3</td><td>Trend back to or above previous level, backlinks pointing to old URLs still redirect, Core Web Vitals in the green</td></tr>
<tr><td>Ongoing</td><td>Keep redirects in place long term, do not delete the redirect map</td></tr>
</tbody></table>
<p>Some movement in positions for a few weeks after a large change is normal while Google processes the new site. A steady drop on specific pages is not normal and usually points to a missing redirect, lost content or a technical block.</p>
<h2>How we handle redesigns</h2>
<p>At BoostLab, migration is part of the project scope, not an extra: URL inventory, redirect map, content and metadata transfer, hreflang, sitemap and Search Console checks after launch. A business website starts at €1,700 and takes 2-3 weeks, and every site comes with SEO structure, schema markup, GA4 and conversion tracking. See <a href="/web-development.html">web development</a>, <a href="/pricing.html">pricing</a> and our <a href="/blog/website-seo-checklist-before-launch.html">SEO checklist before launch</a>.</p>""",
        "faq": [
            ("Will I lose Google rankings after a redesign?", "Not if URLs are mapped with 301 redirects, ranking content and metadata are kept, and indexing is checked at launch. Small fluctuations for a few weeks are normal; a steady drop points to a fixable problem."),
            ("Should I redirect old pages to the home page?", "No. Redirect each old URL to the most relevant new page. Redirecting everything to the home page loses the relevance that made those pages rank."),
            ("How long should 301 redirects stay in place?", "Keep them long term. Links from other sites and bookmarks keep pointing to old URLs for years, and removing redirects loses that value."),
        ],
        "services": ["web"],
    },
})
