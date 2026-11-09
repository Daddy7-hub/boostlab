# `<lang>_blog3.py` - five posts about how we work (written natively per language)

Executed after `<lang>_blog2.py`. It must ONLY add posts:

```python
T["blog"]["posts"].update({
    "smm-how-we-work": {...},
    "smm-cost": {...},
    "mobile-app-cost": {...},
    "how-we-work": {...},
    "b2b-email-campaign": {...},
})
```

Same keys as existing posts: `slug, title (<=60), desc (120-155), h1, lead (1-2 sentences), date, iso, minutes, body (HTML), faq (3 pairs), services (list of keys)`.
Date: 6 November 2026 localized like existing posts, iso "2026-11-06". Allowed body tags: p, h2, h3, ul, ol, li, strong, em, table, thead, tbody, tr, th, td, a.
These posts explain OUR way of working - write in first person plural ("we"), concrete and calm, no hype. 800-1100 words (ET/LT may be ~15% fewer).
Every post must link (absolute same-language paths) to its service page AND to 1-2 related existing posts; end with a short paragraph inviting the reader to get a free estimate (link to the pricing page or service page; no phone/email in the body).
No em/en dashes (use "-"). Do NOT invent statistics, client names, case results or awards.

Fixed facts:
- SMM packages: ads campaign setup €599 one-time (Google Ads or Meta, audience/keyword research, up to 5 creatives, conversion tracking, report); Ads + SMM €1,399/month (Google & Meta management, 12 posts/month, stories & reels, community management, monthly report, A/B tests); Dedicated specialist €2,500/month (personal account manager, full ad management, 20+ posts/month, content strategy, weekly reports). Channels: Instagram, Facebook, TikTok, LinkedIn, Telegram. Content in the customer's languages (ET, RU, EN, LT). Content planned a month ahead and approved by the client before publishing. Ad accounts are created in the client's name. Recommended ad spend at least €500-1,000/month, separate from fees.
- Mobile apps: React Native for iOS + Android from one codebase; native when heavy graphics/special hardware; adding an app to an existing platform from €4,970 (Google Play) and €5,970 (App Store); standalone apps quoted after a call; typical 6-12 weeks to the stores; we handle store accounts, listings, review process, updates; push, payments, maps, camera, QR, offline mode.
- How we work: 30-minute call, then a fixed quote; clickable prototype approved before code; clean code, CMS/admin panel, analytics and SEO from the start; payment usually 50% before start and 50% at launch, bigger projects in milestones; after full payment the client owns the code and data; warranty period with free bug fixes (typically 1-3 months); hosting at cost; support plans optional; no licence fees. Studio in Tallinn, 200+ websites a year, 2 large international projects (RentMe, BalticLeads). Prices: landing €700, business site €1,700, online store €3,500, platform/CRM €4,500.
- B2B email campaigns: we pick target companies in BalticLeads (1.4M companies from EE/LV/LT/FI, official registers, AI search), write the offer, build a landing page, send from warmed-up mailboxes with SPF/DKIM/DMARC, moderate volume, unsubscribe link in every email, track replies in a CRM. Legal (not legal advice): cold B2B email to companies is opt-out based in EE, LV and LT (LT since 22 April 2026); role addresses (info@, sales@) are company contact data; named person addresses are personal data under GDPR - inform (Art. 14) and honour objections immediately. Personal webmail addresses are hidden in BalticLeads. Campaign setup from €599.

Topics and services:
1. smm-how-we-work - how we run social media for a business: strategy and tone of voice, monthly content plan and approval, production (photo, reels, stories, carousels), publishing rhythm, community replies and lead hand-off, monthly report and what we change based on it, what we need from the client. services ["smm"].
2. smm-cost - how much SMM costs in Estonia and what is included: our three packages as a table, what affects price, ad spend vs fee, how to choose, what results to expect realistically in month 1-3 (qualitative, no invented numbers). services ["smm", "ads"].
3. mobile-app-cost - how much a mobile app costs and when a business actually needs one (vs a mobile website/PWA): cost drivers, cross-platform vs native, store publishing, maintenance. services ["apps", "platforms"].
4. how-we-work - how we work from brief to launch and after: the steps above, communication, what the client gets, payment, ownership, support. services ["web", "crm", "platforms", "apps", "ads", "smm"].
5. b2b-email-campaign - how we run a B2B email campaign that gets replies: targeting, offer, email copy principles, deliverability, volumes, follow-ups, legal basics, measuring. services ["leadgen", "ads"].
