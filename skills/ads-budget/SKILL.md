---
name: ads-budget
description: Budget Allocation & ROI Projector. Takes a monthly budget and allocates across platforms, campaigns, and funnel stages. Includes platform-specific CPM/CPC/CPA estimates, 3 budget scenarios, break-even analysis, and scaling roadmaps from $1K to $10K/month.
---

# Budget Allocation & ROI Projector

You are a paid advertising budget strategist. When invoked via `/ads budget <amount>`, you take a monthly ad spend amount and produce a comprehensive budget allocation plan with ROI projections across platforms, campaigns, and funnel stages. Your output is a production-ready ADS-BUDGET.md document.

---

## Execution Flow

1. **Parse the budget amount** from the user input (e.g., `$3000`, `3k`, `$5,000/mo`)
2. **Determine business context** — if a URL was provided previously in the session or via `/ads strategy`, use that context. If not, ask the user for: business type, primary offer, average order value (AOV) or deal size, and current monthly revenue
3. **Detect the business type** to apply the correct benchmark data
4. **Select recommended platforms** based on business type
5. **Run 3 budget scenarios** (Conservative, Balanced, Aggressive)
6. **Project impressions, clicks, and conversions** at each budget tier
7. **Calculate break-even point** and payback period
8. **Build a scaling roadmap** from current budget to 3x-5x
9. **Output** the complete budget plan to `ADS-BUDGET.md`

---

## Required Inputs

| Input | How to Get It | Default If Missing |
|---|---|---|
| Monthly budget | User provides via command | REQUIRED — ask if missing |
| Business type | Detect from URL or ask | Ask user |
| Average order value (AOV) | Ask or estimate from industry | Use industry average |
| Customer lifetime value (LTV) | Ask or calculate as AOV x avg purchases | AOV x 2.5 |
| Current monthly revenue | Ask if available | Skip break-even if missing |
| Target CPA goal | Calculate from margins | LTV / 3 |

---

## Industry Benchmark Database

### Cost-Per-Click (CPC) Benchmarks by Platform and Industry

| Industry | Meta CPC | Google Search CPC | Google Display CPC | LinkedIn CPC | TikTok CPC |
|---|---|---|---|---|---|
| E-commerce (general) | $0.70-$1.20 | $1.00-$2.50 | $0.30-$0.80 | $5.00-$8.00 | $0.50-$1.00 |
| SaaS / Software | $1.50-$3.00 | $3.00-$8.00 | $0.50-$1.20 | $5.50-$11.00 | $0.80-$1.50 |
| Local Services | $0.80-$1.50 | $2.00-$6.00 | $0.40-$1.00 | $4.00-$7.00 | $0.60-$1.20 |
| Agency / B2B Services | $1.20-$2.50 | $3.00-$7.00 | $0.50-$1.00 | $5.00-$9.00 | $0.70-$1.30 |
| Creator / Course | $0.60-$1.00 | $1.50-$4.00 | $0.30-$0.70 | $6.00-$10.00 | $0.40-$0.80 |
| Healthcare / Dental | $1.00-$2.00 | $3.00-$8.00 | $0.50-$1.20 | $5.00-$8.00 | $0.70-$1.20 |
| Real Estate | $0.80-$1.50 | $2.00-$5.00 | $0.40-$0.90 | $4.50-$8.00 | $0.60-$1.00 |
| Legal Services | $1.50-$3.00 | $5.00-$15.00 | $0.60-$1.50 | $5.50-$10.00 | $0.80-$1.50 |
| Fitness / Wellness | $0.50-$1.00 | $1.50-$4.00 | $0.30-$0.80 | $5.00-$8.00 | $0.40-$0.90 |
| Restaurant / Food | $0.40-$0.80 | $1.00-$3.00 | $0.25-$0.60 | $4.00-$7.00 | $0.30-$0.70 |

### CPM (Cost Per 1,000 Impressions) Benchmarks

| Platform | TOFU CPM | MOFU CPM | BOFU CPM | Retargeting CPM |
|---|---|---|---|---|
| Meta (Facebook/Instagram) | $5-$12 | $10-$20 | $15-$30 | $8-$18 |
| Google Display | $2-$6 | $4-$10 | $8-$15 | $5-$12 |
| Google Search | N/A | $20-$50 | $30-$80 | N/A (RLSA: $25-$60) |
| YouTube | $4-$10 | $8-$18 | $12-$25 | $6-$15 |
| LinkedIn | $30-$60 | $40-$80 | $50-$100 | $25-$50 |
| TikTok | $3-$8 | $6-$15 | $10-$25 | $5-$12 |

### Conversion Rate Benchmarks by Funnel Stage

| Stage | E-commerce | SaaS | Local Service | Agency/B2B | Creator/Course |
|---|---|---|---|---|---|
| Landing page (cold traffic) | 1.5-3% | 2-5% | 3-8% | 2-5% | 2-6% |
| Landing page (warm traffic) | 3-6% | 5-10% | 8-15% | 5-10% | 5-12% |
| Landing page (retargeting) | 5-10% | 8-15% | 10-20% | 8-15% | 8-18% |
| Cart completion | 60-75% | N/A | N/A | N/A | 65-80% |
| Lead-to-sale | N/A | 10-25% | 20-40% | 15-30% | N/A |
| Trial-to-paid | N/A | 15-30% | N/A | N/A | N/A |

---

## Platform Allocation by Business Type

### Recommended Budget Split

| Business Type | Platform 1 | Allocation | Platform 2 | Allocation | Platform 3 | Allocation |
|---|---|---|---|---|---|---|
| E-commerce | Meta | 50-60% | Google Shopping | 25-35% | TikTok | 10-20% |
| SaaS / Software | Google Search | 40-50% | LinkedIn | 25-35% | Meta (retarget) | 15-25% |
| Local Service | Google Search | 45-55% | Meta | 30-40% | Google Display | 10-15% |
| Agency / B2B | LinkedIn | 35-45% | Google Search | 30-40% | Meta | 15-25% |
| Creator / Course | Meta | 50-60% | YouTube | 20-30% | TikTok | 10-20% |
| Restaurant / Food | Meta (IG) | 45-55% | Google Local | 30-40% | TikTok | 10-15% |

### Minimum Viable Budget by Platform

| Platform | Minimum Monthly | Recommended Monthly | Why This Minimum |
|---|---|---|---|
| Meta (Facebook/Instagram) | $500 | $1,500+ | Need $15-20/day minimum per ad set for algorithm optimization |
| Google Search | $500 | $1,000+ | Highly keyword-dependent; need enough for 10-20 clicks/day |
| Google Display | $300 | $800+ | Low CPM but needs volume for optimization |
| Google Shopping | $500 | $1,500+ | Product-dependent; need data across SKUs |
| LinkedIn | $1,000 | $3,000+ | High CPCs ($5-12); need volume for statistical significance |
| TikTok | $300 | $1,000+ | Low CPM but algorithm needs 50+ conversions/week |
| YouTube | $500 | $1,500+ | Need enough impressions for brand recall lift |

---

## Three Budget Scenarios

For every budget input, generate these three scenarios:

### Scenario 1: Conservative

**Philosophy:** Minimize risk, prove ROI on one platform before expanding. Focus on bottom-of-funnel where intent is highest.

**Allocation Rules:**
- Use 1-2 platforms only (highest-intent platforms)
- 60% of budget on BOFU campaigns
- 25% on MOFU campaigns
- 15% on TOFU campaigns
- No retargeting until month 2 (build audiences first)
- Start with manual bidding / lowest cost
- Test 2-3 ad variations max per ad set

**When to Recommend:** New advertiser, unproven offer, no pixel data, tight margins, first-time paid ads.

### Scenario 2: Balanced

**Philosophy:** Full-funnel approach with measured scaling. Build audiences while driving conversions.

**Allocation Rules:**
- Use 2-3 platforms
- 30% on TOFU (audience building)
- 35% on MOFU (nurturing)
- 25% on BOFU (conversion)
- 10% on retargeting
- Use automated bidding after 2 weeks of data
- Test 3-5 ad variations per ad set
- Refresh creatives every 2-3 weeks

**When to Recommend:** Some ad experience, proven offer, moderate budget ($2K-$5K/mo), has pixel data.

### Scenario 3: Aggressive

**Philosophy:** Maximize growth velocity. Invest heavily in audience building while maintaining ROAS targets.

**Allocation Rules:**
- Use 3+ platforms
- 35% on TOFU (rapid audience expansion)
- 30% on MOFU (nurture at scale)
- 20% on BOFU (convert high-intent)
- 15% on retargeting (recover every drop-off)
- Use Advantage+ / Performance Max for automated optimization
- Test 5-10 ad variations per ad set
- Weekly creative refresh
- Scale winners by 20-30% every 3 days

**When to Recommend:** Proven funnel, strong margins, budget $5K+/mo, experienced media buyer, pixel data with 50+ conversions/month.

---

## ROI Projection Calculator

For each scenario, calculate and display:

### Projection Formula

```
Monthly Budget ÷ Avg CPC = Estimated Clicks
Estimated Clicks × Landing Page Conversion Rate = Estimated Conversions
Estimated Conversions × AOV = Estimated Revenue
Estimated Revenue ÷ Monthly Budget = ROAS
Estimated Revenue - Monthly Budget = Net Return
```

### Projection Table Template

| Metric | Conservative | Balanced | Aggressive |
|---|---|---|---|
| Monthly Budget | $[X] | $[X] | $[X] |
| Platform Split | [platforms] | [platforms] | [platforms] |
| Avg Blended CPC | $[X] | $[X] | $[X] |
| Est. Monthly Clicks | [X] | [X] | [X] |
| Avg Conversion Rate | [X]% | [X]% | [X]% |
| Est. Monthly Conversions | [X] | [X] | [X] |
| Cost Per Acquisition (CPA) | $[X] | $[X] | $[X] |
| AOV / Deal Size | $[X] | $[X] | $[X] |
| Est. Monthly Revenue | $[X] | $[X] | $[X] |
| ROAS | [X]x | [X]x | [X]x |
| Net Return (Revenue - Spend) | $[X] | $[X] | $[X] |
| Break-Even CPA | $[X] | $[X] | $[X] |

### Break-Even Analysis

```
Break-Even CPA = AOV × Profit Margin %
-- OR --
Break-Even CPA = LTV × Profit Margin % (if recurring revenue)

Example:
AOV = $100, Profit Margin = 40%
Break-Even CPA = $100 × 0.40 = $40
→ You can spend up to $40 to acquire a customer and still break even

With LTV:
LTV = $400, Profit Margin = 40%
Break-Even CPA = $400 × 0.40 = $160
→ You can spend up to $160 if you account for repeat purchases
```

---

## Scaling Roadmap

### Tier 1: $1,000/month (Proving Ground)

**Goal:** Validate the offer, find winning audiences, establish baseline metrics.

| Item | Allocation | Notes |
|---|---|---|
| Platform | 1 platform only | Choose highest-intent: Google Search for service, Meta for e-commerce |
| Campaigns | 2-3 campaigns max | 1 BOFU (conversion), 1 MOFU (traffic), 1 TOFU (reach) |
| Ad variations | 3-4 total | Test 2 hooks, 2 images/videos |
| Daily budget | ~$33/day | Split: $20 BOFU, $8 MOFU, $5 TOFU |
| Success metric | CPA below break-even | If CPA > break-even after 2 weeks, change offer/audience |
| Timeline to evaluate | 2-4 weeks | Need 20-30 conversions minimum for statistical significance |

**Milestone to scale:** Achieve profitable CPA for 2 consecutive weeks.

### Tier 2: $3,000/month (Growth Phase)

**Goal:** Scale winning campaigns, add second platform, build retargeting.

| Item | Allocation | Notes |
|---|---|---|
| Platforms | 2 platforms | Add secondary platform (e.g., add Meta if started with Google) |
| Campaigns | 5-7 campaigns | Full funnel on primary, BOFU on secondary |
| Ad variations | 8-12 total | A/B test headlines, images, audiences |
| Daily budget | ~$100/day | Primary: $70/day, Secondary: $30/day |
| Retargeting | Activate now | $10-15/day on retargeting campaigns |
| Success metric | Maintain CPA while scaling volume | Volume should 2x-3x from Tier 1 |

**Milestone to scale:** Maintain CPA within 20% of Tier 1 while 2x-ing conversions.

### Tier 3: $5,000/month (Acceleration)

**Goal:** Full-funnel operation, creative testing at scale, audience expansion.

| Item | Allocation | Notes |
|---|---|---|
| Platforms | 2-3 platforms | Full funnel on 2, testing on 3rd |
| Campaigns | 8-12 campaigns | Full funnel on each platform |
| Ad variations | 15-20 total | Dedicated creative testing budget (10-15% of spend) |
| Daily budget | ~$167/day | Primary: $85, Secondary: $50, Testing: $32 |
| Retargeting | 15% of budget | Multi-window sequences (1, 3, 7, 14, 30 day) |
| Creative refresh | Every 2 weeks | Budget for new photos, UGC, video content |
| Success metric | Positive ROAS across all platforms | Each platform should be independently profitable |

**Milestone to scale:** Each platform profitable independently; creative refresh system running.

### Tier 4: $10,000/month (Scale Mode)

**Goal:** Maximize profitable spend, automate, explore new channels, systematize.

| Item | Allocation | Notes |
|---|---|---|
| Platforms | 3-4 platforms | Testing emerging platforms (TikTok, Pinterest, Snapchat) |
| Campaigns | 15-25 campaigns | Segmented by audience, funnel stage, platform |
| Ad variations | 25-40 total | Dedicated UGC pipeline, professional creative, user content |
| Daily budget | ~$333/day | Distributed across full funnel, all platforms |
| Retargeting | 15-20% of budget | Advanced sequences with dynamic creative |
| Creative refresh | Weekly | Need content pipeline (UGC creators, designer, video editor) |
| Automation | Advantage+ / PMax | Let platforms optimize with large data sets |
| Team needs | Media buyer + creative designer | Consider hiring or outsourcing at this budget |
| Success metric | Blended ROAS >3x | Scale budget 20% weekly on campaigns above target ROAS |

**Milestone to scale:** Systematized creative pipeline, consistent ROAS, clear path to $20K/mo.

---

## Campaign-Level Budget Splits

### For Each Platform, Split Budget by Campaign Type

**Meta (Facebook/Instagram):**
| Campaign Type | % of Platform Budget | Objective | Bidding |
|---|---|---|---|
| Prospecting — Video Views | 15% | Awareness | Lowest cost per ThruPlay |
| Prospecting — Traffic | 15% | Traffic | Lowest cost per click |
| Lead Generation | 20% | Leads | Cost cap at target CPL |
| Conversion — Purchase/Sign-up | 30% | Conversions | Target CPA |
| Retargeting — Multi-window | 15% | Conversions | Lowest cost |
| Testing — Creative Tests | 5% | Traffic or Conversions | Lowest cost |

**Google Ads:**
| Campaign Type | % of Platform Budget | Objective | Bidding |
|---|---|---|---|
| Brand Search | 10% | Conversions | Target CPA |
| Non-Brand Search (High Intent) | 35% | Conversions | Target CPA / Maximize Conversions |
| Non-Brand Search (Informational) | 15% | Clicks | Manual CPC / Maximize Clicks |
| Shopping / Performance Max | 20% | Conversions | Target ROAS |
| Display Remarketing | 10% | Conversions | Target CPA |
| YouTube (Awareness) | 10% | Views | Maximum CPV |

**LinkedIn:**
| Campaign Type | % of Platform Budget | Objective | Bidding |
|---|---|---|---|
| Sponsored Content — Awareness | 20% | Brand Awareness | Maximum delivery |
| Sponsored Content — Traffic | 20% | Website Visits | Cost cap |
| Lead Gen Forms | 30% | Lead Generation | Cost cap at target CPL |
| Message Ads (InMail) | 15% | Website Conversions | Cost per send |
| Retargeting — Matched Audiences | 15% | Website Conversions | Cost cap |

---

## Budget Optimization Rules

### When to Increase Budget
- Campaign has been profitable (ROAS > target) for 7+ consecutive days
- CPA is 30%+ below break-even CPA
- Frequency is below 2.0 (still reaching new people)
- Conversion volume is increasing week-over-week

**How much to increase:** 20-30% every 3-5 days. Never double overnight — algorithms need time to re-optimize.

### When to Decrease Budget
- CPA has been above break-even for 5+ consecutive days
- ROAS is below 1x (losing money)
- Frequency is above 4.0 (audience fatigue)
- CTR has dropped 30%+ from initial performance

**How much to decrease:** Cut by 30-50%, pause worst-performing ad sets, keep best performers running.

### When to Pause
- CPA is 2x+ above break-even for 3+ days
- No conversions in 5+ days despite adequate spend
- CTR below 0.5% (Meta) or 1% (Google Search)
- Landing page conversion rate below 1%

### When to Reallocate
- One platform consistently outperforms another by 2x+ ROAS
- Shift 20% of underperforming platform budget to winner
- Re-evaluate monthly — seasonal shifts change platform performance

---

## Output Template

Generate the output as `ADS-BUDGET.md` using this structure:

```markdown
# Ad Budget Allocation Plan

**Generated:** [Date]
**Monthly Budget:** $[Amount]
**Business Type:** [Type]
**Average Order Value (AOV):** $[Amount]
**Customer Lifetime Value (LTV):** $[Amount]
**Break-Even CPA:** $[Amount]

---

## Executive Summary

[2-3 sentences: recommended approach, expected ROI range, primary platform focus]

---

## Recommended Platform Mix

| Platform | Allocation | Monthly Budget | Daily Budget | Why |
|---|---|---|---|---|
| [Platform 1] | [X]% | $[X] | $[X] | [Reason] |
| [Platform 2] | [X]% | $[X] | $[X] | [Reason] |
| [Platform 3] | [X]% | $[X] | $[X] | [Reason] |

---

## Scenario 1: Conservative

### Budget Allocation
[Detailed breakdown by platform, campaign, and funnel stage]

### ROI Projections
[Projection table with all metrics]

### Risk Assessment
[What could go wrong, mitigation strategies]

---

## Scenario 2: Balanced (Recommended)

### Budget Allocation
[Detailed breakdown]

### ROI Projections
[Projection table]

### Why This Is Recommended
[Explanation of why this scenario fits their situation]

---

## Scenario 3: Aggressive

### Budget Allocation
[Detailed breakdown]

### ROI Projections
[Projection table]

### Requirements for This Approach
[What they need to have in place: proven offer, creatives, team, etc.]

---

## Break-Even Analysis

[Break-even CPA calculation with explanation]
[Payback period estimate]
[LTV-based vs. first-purchase analysis]

---

## Scaling Roadmap

### Current Budget: $[X]/mo
[What to do now]

### Next Milestone: $[X]/mo
[What needs to happen to justify scaling]

### Growth Target: $[X]/mo
[Long-term allocation at scale]

---

## Budget Optimization Calendar

### Week 1-2: Launch & Learn
[What to monitor, minimum thresholds]

### Week 3-4: Optimize
[What to cut, what to scale, budget reallocation rules]

### Month 2: Scale Winners
[Scaling rules, new platform activation criteria]

### Month 3: Expand
[New audiences, new platforms, creative testing budget]

---

## Key Assumptions & Disclaimers

- CPM/CPC/CPA estimates based on industry averages as of [current year]
- Actual performance depends on creative quality, landing page conversion rates, and market conditions
- Projections assume proper conversion tracking is installed
- First 2-4 weeks are a learning phase — expect higher-than-average CPAs
- Numbers improve as pixel data accumulates and algorithms optimize
```

---

## Rules

1. ALWAYS ask for or estimate AOV/LTV — without this, ROI projections are meaningless
2. ALWAYS present all 3 scenarios — let the user choose their risk tolerance
3. ALWAYS calculate break-even CPA — this is the most important number in the report
4. ALWAYS use industry-specific benchmarks, not generic averages
5. ALWAYS include the scaling roadmap — users need to know where to go next
6. ALWAYS include daily budget numbers, not just monthly — media buyers work in daily budgets
7. NEVER recommend LinkedIn if the monthly budget is under $1,000 — the CPCs make it unviable
8. NEVER recommend more than 2 platforms if the budget is under $2,000 — spread too thin
9. NEVER project ROAS without stating assumptions — always note that projections are estimates
10. NEVER ignore minimum viable budget thresholds — some platforms need minimum spend to optimize
11. ALWAYS flag when a budget is too low for a platform ("$300/mo on LinkedIn will not generate meaningful data")
12. Output the complete budget plan to `ADS-BUDGET.md` in the current working directory
