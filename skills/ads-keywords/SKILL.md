---
name: Google Ads Keyword Strategy
description: Builds a complete Google Ads keyword strategy with search intent mapping, ad group structure, match type recommendations, negative keyword lists, estimated CPC ranges, Quality Score optimization, and ready-to-implement campaign architecture
---

# Google Ads Keyword Strategy

## Skill Purpose
Build a complete, implementation-ready Google Ads keyword strategy from scratch. This skill maps search intent across the entire buyer journey, organizes keywords into tightly themed ad groups, recommends match types, builds comprehensive negative keyword lists, estimates CPC ranges by cluster, provides Quality Score optimization tips, and outputs a campaign structure with headline and description suggestions for every ad group. The output is detailed enough that an ad buyer can build the campaigns in Google Ads Manager without additional research.

## When to Use
- User runs `/ads keywords <url>`
- User asks for Google Ads keyword research, keyword strategy, or search campaign planning
- Called as a subagent from `/ads strategy` (the main orchestrator)
- User wants to launch or improve Google search campaigns
- User needs keyword grouping, negative keywords, or ad group architecture

## Input Requirements
- **Required:** A business URL to analyze
- **Optional:** Target location/geography, monthly budget, existing Google Ads data, specific products/services to focus on, competitor URLs

## How to Execute

### Step 1: Business & Market Intelligence

Fetch the business URL using `WebFetch` and extract:

| Data Point | Where to Find |
|---|---|
| Business name | Page title, logo, about page |
| Industry/category | Services, products, positioning |
| Products/services offered | Product pages, service pages, pricing page |
| Geographic focus | Service areas, locations, shipping scope |
| Price positioning | Pricing page, product prices, "starting at" text |
| Current SEO keywords | Meta titles, H1s, page URLs, blog topics |
| Value proposition | Hero section, tagline, about page |
| Competitor names | "Why choose us" sections, comparison pages |
| Customer language | Testimonials, reviews, FAQ content |

Run keyword research searches:
```
WebSearch: "[Business type]" Google Ads keywords
WebSearch: "[Industry]" high intent keywords
WebSearch: "[Product/service]" search terms people use
WebSearch: "[Business Name]" competitors Google Ads
WebSearch: "[Industry]" average CPC Google Ads 2025
WebSearch: site:[competitor URL] (to understand competitor positioning)
```

### Step 2: Search Intent Mapping

Map all discovered keywords into four intent categories:

```markdown
## Search Intent Map

### 1. Informational Intent (Top of Funnel — Awareness)
Users researching, learning, or exploring. Not ready to buy yet.

**Signal words:** how to, what is, why, guide, tips, best practices, examples, tutorial, learn
**Campaign role:** Brand awareness, content marketing, remarketing list building
**Bid strategy:** Low bids, target impression share, or skip if budget is tight

| Keyword | Est. Monthly Volume | Est. CPC | Competition | Notes |
|---|---|---|---|---|
| [keyword 1] | [volume range] | $[range] | Low/Med/High | [note] |
| [keyword 2] | [volume range] | $[range] | Low/Med/High | [note] |
| [keyword 3] | [volume range] | $[range] | Low/Med/High | [note] |
| [keyword 4] | [volume range] | $[range] | Low/Med/High | [note] |
| [keyword 5] | [volume range] | $[range] | Low/Med/High | [note] |
[...continue for 10-15 keywords]

### 2. Navigational Intent (Mid-Funnel — Consideration)
Users looking for a specific brand, product, or website. May be comparing options.

**Signal words:** [brand name], [product name], login, pricing, reviews, vs, compare, alternative to
**Campaign role:** Brand defense, competitor conquesting, comparison capture
**Bid strategy:** High bids on branded terms, moderate on competitor terms

| Keyword | Est. Monthly Volume | Est. CPC | Competition | Notes |
|---|---|---|---|---|
| [keyword 1] | [volume range] | $[range] | Low/Med/High | [note] |
| [keyword 2] | [volume range] | $[range] | Low/Med/High | [note] |
[...continue for 5-10 keywords]

### 3. Commercial Investigation Intent (Mid-to-Bottom Funnel)
Users actively comparing solutions before purchasing. High-value traffic.

**Signal words:** best, top, review, comparison, vs, alternative, which, recommended
**Campaign role:** Consideration capture, competitive differentiation
**Bid strategy:** Moderate-to-high bids, maximize conversions

| Keyword | Est. Monthly Volume | Est. CPC | Competition | Notes |
|---|---|---|---|---|
| [keyword 1] | [volume range] | $[range] | Low/Med/High | [note] |
| [keyword 2] | [volume range] | $[range] | Low/Med/High | [note] |
[...continue for 10-15 keywords]

### 4. Transactional Intent (Bottom of Funnel — Conversion)
Users ready to buy, sign up, or take action. Highest-value keywords.

**Signal words:** buy, order, hire, book, schedule, get quote, pricing, cost, near me, free trial, sign up, discount, coupon
**Campaign role:** Direct conversion, lead generation, sales
**Bid strategy:** Highest bids, target CPA or maximize conversions

| Keyword | Est. Monthly Volume | Est. CPC | Competition | Notes |
|---|---|---|---|---|
| [keyword 1] | [volume range] | $[range] | Low/Med/High | [note] |
| [keyword 2] | [volume range] | $[range] | Low/Med/High | [note] |
[...continue for 15-20 keywords]
```

### Step 3: Keyword Grouping Into Ad Groups

Organize keywords into tightly themed ad groups. Each ad group should contain **3-5 closely related keywords** that can share the same ad copy.

```markdown
## Ad Group Architecture

### Campaign: [Campaign Name — e.g., "Brand", "Non-Brand Core", "Competitor", "Long-Tail"]
**Campaign type:** Search
**Bidding strategy:** [Recommended strategy]
**Daily budget suggestion:** $[amount]
**Geographic targeting:** [Location]

---

#### Ad Group 1: [Theme Name]
**Intent:** [Informational / Commercial / Transactional]
**Theme:** [What unifies these keywords — e.g., "pricing queries", "comparison shoppers", "emergency need"]

| # | Keyword | Match Type | Rationale | Est. CPC |
|---|---|---|---|---|
| 1 | [keyword] | [Exact / Phrase / Broad] | [why this match type] | $[est.] |
| 2 | [keyword] | [Exact / Phrase / Broad] | [rationale] | $[est.] |
| 3 | [keyword] | [Exact / Phrase / Broad] | [rationale] | $[est.] |
| 4 | [keyword] | [Exact / Phrase / Broad] | [rationale] | $[est.] |
| 5 | [keyword] | [Exact / Phrase / Broad] | [rationale] | $[est.] |

**Ad Copy for This Ad Group:**

| Element | Version A | Version B |
|---|---|---|
| Headline 1 (30 chars) | [headline] ([count]) | [headline] ([count]) |
| Headline 2 (30 chars) | [headline] ([count]) | [headline] ([count]) |
| Headline 3 (30 chars) | [headline] ([count]) | [headline] ([count]) |
| Description 1 (90 chars) | [description] ([count]) | [description] ([count]) |
| Description 2 (90 chars) | [description] ([count]) | [description] ([count]) |
| Display Path 1 | [path] | [path] |
| Display Path 2 | [path] | [path] |

**Landing page recommendation:** [Where this ad group should send traffic and why]

---

#### Ad Group 2: [Theme Name]
[...repeat the same structure]

#### Ad Group 3: [Theme Name]
[...repeat]

[...continue for all ad groups — aim for 8-15 ad groups total across campaigns]
```

### Step 4: Match Type Strategy

```markdown
## Match Type Recommendations

### When to Use Each Match Type

| Match Type | Use When | Pros | Cons | Budget Impact |
|---|---|---|---|---|
| **Exact** [keyword] | High-intent, proven converters | Highest relevance, best CTR, lowest CPC waste | Limited reach, misses variations | Low waste, high ROAS |
| **Phrase** "keyword" | Core terms where word order matters | Balances reach and relevance, catches long-tail | Can match irrelevant queries with added words | Moderate waste, needs negatives |
| **Broad** keyword | Discovery, new keyword finding, large budgets | Maximum reach, finds new opportunities | Matches loosely related queries, needs heavy negative lists | Highest waste without optimization |

### Match Type Distribution Recommendation

**For new campaigns (first 30 days):**
| Match Type | % of Keywords | Purpose |
|---|---|---|
| Exact | 50% | Core high-intent terms — protect budget |
| Phrase | 35% | Capture variations and long-tail |
| Broad | 15% | Discovery — find new converting queries |

**After optimization (day 31+):**
| Match Type | % of Keywords | Purpose |
|---|---|---|
| Exact | 40% | Proven winners from search term reports |
| Phrase | 40% | Expanded reach on validated themes |
| Broad | 20% | Continued discovery with Smart Bidding |

### Match Type Progression Strategy
1. **Week 1-2:** Launch with exact and phrase only. Build baseline data.
2. **Week 3-4:** Review search term report. Add converting queries as exact match. Add non-converting queries as negatives.
3. **Month 2:** Introduce broad match on top-performing ad groups with Target CPA bidding.
4. **Monthly:** Harvest search term report. Graduate performing broad queries to phrase/exact. Add negatives for waste.
```

### Step 5: Negative Keyword List

```markdown
## Negative Keyword Lists

### Campaign-Level Negatives (apply to ALL campaigns)
These keywords should NEVER trigger your ads:

#### Job/Career Related
- jobs, careers, hiring, salary, interview, resume, glassdoor, indeed, linkedin
- [industry]-specific job terms: [list]

#### Educational/Research (exclude if not selling education)
- how to become, certification, degree, course, training, class, university, school
- tutorial, free course, pdf, download, template

#### DIY/Free Seekers (exclude if selling premium services)
- free, cheap, discount, coupon, promo code, deal, budget
- DIY, do it yourself, homemade, self, own

#### Unrelated Industries
- [list industry-specific irrelevant terms that share keywords with the business]

#### Competitor Brand Terms (exclude from non-brand campaigns)
- [competitor 1 name]
- [competitor 2 name]
- [competitor 3 name]

#### Geographic Exclusions (if targeting specific areas)
- [cities/states/countries outside service area]

---

### Ad Group-Level Negatives
Apply these to prevent ad groups from cannibalizing each other:

| Ad Group | Negative Keywords | Reason |
|---|---|---|
| [Ad Group 1] | [keywords to exclude] | [prevent overlap with Ad Group X] |
| [Ad Group 2] | [keywords to exclude] | [prevent overlap] |
| [Ad Group 3] | [keywords to exclude] | [prevent overlap] |

---

### Negative Keyword Discovery Process
Run these searches monthly to find new negatives:

1. **Search Term Report:** Review actual queries that triggered your ads. Add irrelevant ones as negatives.
2. **Google Keyword Planner:** Search your keywords and look for irrelevant related terms.
3. **Autocomplete audit:** Type each keyword into Google and note irrelevant autocomplete suggestions.
4. **Competitor analysis:** Search competitor brand terms + your keywords to find disambiguation needs.
```

### Step 6: CPC & Budget Estimation

```markdown
## CPC & Budget Estimates

### Estimated CPC by Keyword Cluster

| Cluster / Ad Group | Avg. Est. CPC | CPC Range | Monthly Volume (est.) | Monthly Spend (est.) | Intent Level |
|---|---|---|---|---|---|
| [Cluster 1] | $[avg] | $[low]-$[high] | [volume] | $[spend at 100% IS] | High |
| [Cluster 2] | $[avg] | $[low]-$[high] | [volume] | $[spend] | High |
| [Cluster 3] | $[avg] | $[low]-$[high] | [volume] | $[spend] | Medium |
| [Cluster 4] | $[avg] | $[low]-$[high] | [volume] | $[spend] | Medium |
| [Cluster 5] | $[avg] | $[low]-$[high] | [volume] | $[spend] | Low |

**Notes on estimates:**
- CPC estimates are based on industry benchmarks and competitive analysis
- Actual CPCs will vary based on Quality Score, bid strategy, and competition
- New accounts typically pay 10-20% more until Quality Score history is established

### Budget Allocation by Campaign

| Campaign | Recommended Daily Budget | Monthly Budget | Priority |
|---|---|---|---|
| [Campaign 1 — Brand] | $[daily] | $[monthly] | High — protect brand terms |
| [Campaign 2 — Core Non-Brand] | $[daily] | $[monthly] | High — main conversion driver |
| [Campaign 3 — Commercial] | $[daily] | $[monthly] | Medium — comparison shoppers |
| [Campaign 4 — Long-Tail] | $[daily] | $[monthly] | Medium — high ROAS, low volume |
| [Campaign 5 — Competitor] | $[daily] | $[monthly] | Low — expensive, test first |
| **Total** | **$[total daily]** | **$[total monthly]** | |

### Budget Scenarios

| Scenario | Monthly Budget | Focus | Expected Clicks/mo | Expected Conversions/mo |
|---|---|---|---|---|
| Starter | $[amount] | Brand + top 2 transactional ad groups | [clicks] | [conversions] |
| Growth | $[amount] | All transactional + commercial ad groups | [clicks] | [conversions] |
| Aggressive | $[amount] | Full coverage including competitor + broad | [clicks] | [conversions] |
```

### Step 7: Quality Score Optimization

```markdown
## Quality Score Optimization Guide

### What Determines Quality Score (1-10)

| Factor | Weight | How to Improve |
|---|---|---|
| **Expected CTR** | ~39% | Write compelling ad copy with strong hooks. Use dynamic keyword insertion. Include numbers and CTAs. Test 3+ headline variations. |
| **Ad Relevance** | ~22% | Keep ad groups tight (3-5 keywords). Use keywords in headlines. Match ad copy to search intent. Never mix intents in one ad group. |
| **Landing Page Experience** | ~39% | Fast load time (<3s). Mobile-friendly. Content matches ad promise. Clear CTA above fold. Trust signals visible. HTTPS required. |

### Quality Score Action Plan

**For scores 1-4 (Poor):**
1. Break the ad group into smaller, tighter themes
2. Rewrite ad copy to directly address the keyword intent
3. Create a dedicated landing page for this ad group
4. Pause and rebuild — low QS keywords drain budget

**For scores 5-6 (Average):**
1. Test new headline variations (3+ per RSA)
2. Improve landing page load speed
3. Add more relevant content to landing page
4. Check that the ad's CTA matches the landing page CTA

**For scores 7-8 (Good):**
1. Test new description variations for incremental CTR gains
2. Experiment with bid strategy (Target CPA vs. Maximize Conversions)
3. Expand with phrase/broad match on these proven ad groups

**For scores 9-10 (Excellent):**
1. Increase budget — these are your best performers
2. Use as templates for new ad groups
3. Monitor weekly to maintain quality

### Landing Page Recommendations by Ad Group

| Ad Group | Recommended Landing Page | Key Elements Needed |
|---|---|---|
| [Ad Group 1] | [URL or page description] | [headline match, CTA, trust signals] |
| [Ad Group 2] | [URL or page description] | [elements needed] |
| [Ad Group 3] | [URL or page description] | [elements needed] |
| [Ad Group 4] | [URL or page description] | [elements needed] |
```

### Step 8: Campaign Launch Checklist

```markdown
## Google Ads Campaign Launch Checklist

### Account Setup
- [ ] Conversion tracking installed (Google Tag or GA4 events)
- [ ] Google Analytics 4 linked to Google Ads
- [ ] Remarketing tag installed
- [ ] Phone call tracking set up (if applicable)
- [ ] Business data verified (address, phone, hours)

### Campaign Configuration
- [ ] Campaign type: Search
- [ ] Network: Search only (uncheck Display Network partners)
- [ ] Location targeting: [specific locations, not "people interested in"]
- [ ] Language targeting: [language]
- [ ] Bid strategy: [recommended strategy]
- [ ] Daily budget: [amount]
- [ ] Ad schedule: [recommended hours/days]
- [ ] Device bid adjustments: [recommendations]

### Ad Group Setup
- [ ] 3-5 keywords per ad group (tightly themed)
- [ ] Match types assigned per strategy
- [ ] Negative keywords applied at campaign and ad group level
- [ ] RSA with 15 headlines and 4 descriptions per ad group
- [ ] At least 2 ads per ad group for A/B testing
- [ ] Ad extensions added: sitelinks, callouts, structured snippets, call, location

### Ad Extensions Recommendations
| Extension Type | Content |
|---|---|
| Sitelinks (4-6) | [specific page links with descriptions] |
| Callouts (4-6) | [short benefit phrases, 25 chars each] |
| Structured Snippets | [header: type, values: list] |
| Call Extension | [phone number if applicable] |
| Location Extension | [address if applicable] |
| Price Extension | [price offerings if applicable] |

### Week 1 Monitoring Plan
- [ ] Day 1: Verify ads are serving, check for disapprovals
- [ ] Day 2: Review search term report for irrelevant queries
- [ ] Day 3: Check impression share — are budgets limiting?
- [ ] Day 5: First CTR assessment — pause ads below 2% CTR
- [ ] Day 7: Review conversion data, adjust bids on top performers
```

## Output Format

Save the complete output to `ADS-KEYWORDS.md` in the current working directory.

**File structure:**
```
# Google Ads Keyword Strategy: [Business Name]
> Generated [date] | Source: [URL]
> Total keywords: [count] | Ad groups: [count] | Campaigns: [count]
> Estimated monthly budget range: $[min] - $[max]

## Business Context
[business summary and targeting parameters]

## Search Intent Map
### Informational Keywords
### Navigational Keywords
### Commercial Investigation Keywords
### Transactional Keywords

## Ad Group Architecture
### Campaign 1: [Name]
#### Ad Group 1-N with keywords, match types, and ad copy

### Campaign 2: [Name]
[...]

## Match Type Strategy
[recommendations and progression plan]

## Negative Keyword Lists
[campaign-level and ad group-level negatives]

## CPC & Budget Estimates
[cluster estimates, budget allocation, scenarios]

## Quality Score Optimization
[improvement guide, landing page recommendations]

## Campaign Launch Checklist
[setup, configuration, monitoring plan]

## Next Steps
1. Set up conversion tracking before launching any campaign
2. Build Campaign 1 ([name]) first — highest priority
3. Run `/ads copy google` for additional ad copy variations
4. Run `/ads landing <url>` to audit landing pages before driving traffic
5. Review search term report after 7 days and add negatives
6. Expand to Campaign 2 after Campaign 1 reaches positive ROAS
```

## Quality Checklist
Before delivering the output, verify:
- [ ] All 4 search intent categories are covered with keywords
- [ ] At least 40 total keywords researched and categorized
- [ ] Keywords are grouped into 8-15 tightly themed ad groups
- [ ] Each ad group has 3-5 keywords maximum
- [ ] Match types are assigned with rationale for each keyword
- [ ] Every ad group has headline and description suggestions (A/B)
- [ ] All character counts are within Google Ads limits (H: 30, D: 90)
- [ ] Negative keyword list covers at least 4 categories
- [ ] CPC estimates are provided per cluster
- [ ] Budget scenarios cover starter, growth, and aggressive tiers
- [ ] Quality Score optimization guide is actionable
- [ ] Landing page recommendations are included per ad group
- [ ] Campaign launch checklist is complete
- [ ] Ad extension recommendations are specific
- [ ] Output is saved to ADS-KEYWORDS.md
