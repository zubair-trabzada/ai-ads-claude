---
name: Audience Persona Builder
description: Builds 5-7 detailed audience personas from a URL with demographics, psychographics, pain points, buying triggers, platform-specific targeting parameters, persona scoring, and negative audiences
---

# Audience Persona Builder

## Skill Purpose
Build 5-7 hyper-detailed audience personas from a business URL. Each persona goes far beyond basic demographics — it maps psychographic profiles, buying triggers, objections, content consumption habits, platform presence, and ready-to-use targeting parameters for Meta, Google, LinkedIn, TikTok, and Pinterest. Includes persona relevance scoring (1-5) and a negative audience section defining who NOT to target. Produces a single, copy-paste-ready deliverable that an ad buyer can immediately use to build campaigns.

## When to Use
- User runs `/ads audience <url>`
- User asks to build audience personas, customer profiles, or targeting research
- Called as a subagent from `/ads strategy` (the main orchestrator)
- User wants to know "who should I target?" for a business
- User needs platform-specific targeting parameters for campaign setup

## Input Requirements
- **Required:** A business URL to analyze
- **Optional:** Industry context, existing customer data, geographic focus, budget range

## How to Execute

### Step 1: Business Intelligence Gathering

Fetch the business URL using `WebFetch` and extract:

| Data Point | Where to Find |
|---|---|
| Business name | Page title, logo, about page |
| Industry/category | Services offered, product types |
| Value proposition | Hero section, tagline, about page |
| Price positioning | Pricing page, product prices, "starting at" language |
| Geographic focus | Service areas, locations, shipping info |
| Current customers | Testimonials, case studies, reviews |
| Product/service types | Product pages, service descriptions |
| Brand tone | Copy style, imagery, color palette |
| Trust signals | Certifications, awards, years in business, client logos |
| Content topics | Blog posts, resources, FAQ sections |

Run supplementary searches:

```
WebSearch: "[Business Name]" reviews
WebSearch: "[Business Name]" customers testimonials
WebSearch: "[Industry]" target audience demographics
WebSearch: "[Industry]" buyer persona research 2025
WebSearch: "[Competitor]" "who buys" OR "target market" OR "customer profile"
```

### Step 2: Industry Audience Intelligence

Based on the detected industry, pull standard audience benchmarks:

**SaaS/Software:**
- Decision makers: CTOs, VPs Engineering, Product Managers, IT Directors
- Influencers: Individual contributors who discover tools
- Budget holders: CFOs, COOs, department heads
- Research behavior: G2 reviews, Product Hunt, Reddit, comparison articles

**E-commerce:**
- Impulse buyers vs. researchers
- Price-sensitive vs. quality-focused segments
- Brand loyal vs. deal hunters
- Social commerce behavior: Instagram shops, TikTok shop, Pinterest

**Local Services:**
- Emergency/urgent need buyers
- Planned purchase/project buyers
- Referral-driven customers
- Neighborhood/community-oriented segments

**Agency/Professional Services:**
- Decision timeline: 30-90 day sales cycles
- Committee buyers vs. solo decision makers
- Budget-constrained vs. ROI-focused
- Relationship-driven vs. results-driven

**Creator/Course:**
- Aspiration-driven buyers
- Career changers vs. skill upgraders
- DIY vs. guided learning preference
- Community seekers vs. content consumers

### Step 3: Build Persona Profiles

Build **5-7 personas** following this exact structure for each:

---

#### Persona Template

```markdown
### Persona [Number]: [Persona Name] — "[Memorable Tagline]"

**Relevance Score:** [1-5 stars] ★★★★☆
**Revenue Potential:** [Low / Medium / High / Very High]
**Estimated Audience Size:** [Small / Medium / Large]
**Acquisition Difficulty:** [Easy / Moderate / Hard]
**Recommended Priority:** [Primary / Secondary / Tertiary]

---

#### Demographics
| Attribute | Detail |
|---|---|
| Age range | [range] |
| Gender split | [percentage breakdown] |
| Income level | [range and bracket] |
| Education | [level] |
| Job titles | [3-5 specific titles] |
| Company size | [employee range or N/A] |
| Location type | [urban/suburban/rural + specific geos if applicable] |
| Family status | [single/married/parent + relevance] |
| Device usage | [mobile-first / desktop-heavy / multi-device] |

#### Psychographics
| Attribute | Detail |
|---|---|
| Core values | [3-4 values] |
| Aspirations | [what they want to become/achieve] |
| Fears | [what keeps them up at night] |
| Identity | [how they see themselves] |
| Decision style | [analytical/emotional/social proof/authority-driven] |
| Brand affinities | [brands they already buy from] |
| Media consumption | [podcasts, YouTube channels, newsletters, blogs] |
| Social behavior | [lurker/engager/creator + which platforms] |

#### Pain Points (ranked by intensity)
1. **[Pain Point 1]** — [1-2 sentence description of the pain and its impact]
2. **[Pain Point 2]** — [description]
3. **[Pain Point 3]** — [description]
4. **[Pain Point 4]** — [description]
5. **[Pain Point 5]** — [description]

#### Buying Triggers
What makes this persona pull out their wallet RIGHT NOW:
- **Trigger 1:** [specific event or realization]
- **Trigger 2:** [specific event or realization]
- **Trigger 3:** [specific event or realization]
- **Trigger 4:** [specific event or realization]

#### Objections & Hesitations
What stops them from buying:
| Objection | Severity | How to Overcome |
|---|---|---|
| [objection 1] | High/Med/Low | [counter-strategy for ad copy] |
| [objection 2] | High/Med/Low | [counter-strategy] |
| [objection 3] | High/Med/Low | [counter-strategy] |
| [objection 4] | High/Med/Low | [counter-strategy] |

#### Content Consumption Habits
| Platform | Behavior | Content Types They Engage With |
|---|---|---|
| YouTube | [how they use it] | [specific content types] |
| Instagram | [how they use it] | [specific content types] |
| TikTok | [how they use it] | [specific content types] |
| LinkedIn | [how they use it] | [specific content types] |
| Podcasts | [which ones] | [topics] |
| Newsletters | [which ones] | [topics] |
| Reddit | [subreddits] | [discussion types] |
| Google Search | [what they search for] | [query patterns] |

#### Platform Targeting Parameters

**Meta (Facebook/Instagram):**
- Interests: [10-15 specific targetable interests]
- Behaviors: [5-7 behavioral targeting options]
- Lookalike source: [what custom audience to seed from]
- Exclusions: [who to exclude within this targeting]

**Google Ads:**
- Search keywords: [10-15 keywords this persona would search]
- In-market audiences: [Google's in-market segments]
- Affinity audiences: [Google's affinity segments]
- Custom intent keywords: [5-7 high-intent keywords]

**LinkedIn:**
- Job titles: [5-7 exact titles]
- Job functions: [2-3 functions]
- Industries: [3-5 industries]
- Company sizes: [ranges]
- Seniority levels: [levels]
- Skills: [5-7 skills to target]
- Groups: [relevant LinkedIn groups]

**TikTok:**
- Interest categories: [TikTok's interest targeting]
- Behavioral targeting: [video interaction types]
- Creator categories: [types of creators they follow]
- Hashtag targeting: [relevant hashtags]

**Pinterest:**
- Interest targeting: [Pinterest interest categories]
- Keyword targeting: [search terms on Pinterest]
- Actalike audiences: [seed audience description]

#### The Perfect Ad for This Persona
- **Hook angle:** [what opening line would stop their scroll]
- **Emotional trigger:** [the core emotion to tap into]
- **Proof type:** [what evidence convinces them — stats, testimonials, demos, case studies]
- **CTA style:** [soft ask vs. hard ask, what language works]
- **Creative format:** [video/image/carousel + style — UGC, polished, meme, etc.]
```

### Step 4: Persona Scoring Matrix

After building all personas, create a comparison matrix:

```markdown
## Persona Scoring Matrix

| Persona | Relevance (1-5) | Revenue Potential | Audience Size | Acquisition Cost | Priority |
|---|---|---|---|---|---|
| [Persona 1] | ★★★★★ | Very High | Medium | Moderate | Primary |
| [Persona 2] | ★★★★☆ | High | Large | Easy | Primary |
| [Persona 3] | ★★★★☆ | Medium | Large | Easy | Secondary |
| [Persona 4] | ★★★☆☆ | High | Small | Hard | Secondary |
| [Persona 5] | ★★★☆☆ | Medium | Medium | Moderate | Tertiary |
| [Persona 6] | ★★☆☆☆ | Low | Large | Easy | Tertiary |
```

**Scoring criteria:**
- **Relevance (1-5):** How closely this persona matches the business's ideal customer
  - 5 = Perfect match, highest conversion probability
  - 4 = Strong match, proven buyer profile
  - 3 = Moderate match, needs nurturing
  - 2 = Weak match, low conversion expected
  - 1 = Marginal match, only target if budget allows
- **Revenue Potential:** Expected lifetime value of this persona
- **Audience Size:** How large is this segment on ad platforms
- **Acquisition Cost:** Estimated relative cost to acquire this persona
- **Priority:** Primary (target first), Secondary (expand to), Tertiary (test with remaining budget)

### Step 5: Negative Audiences

Define who NOT to target. This section saves ad spend and improves ROAS.

```markdown
## Negative Audiences — Who NOT to Target

### Hard Exclusions (always exclude)
| Audience | Why Exclude | Platform Exclusion Method |
|---|---|---|
| [audience 1] | [reason — tire kickers, wrong intent, etc.] | [how to exclude on Meta, Google, etc.] |
| [audience 2] | [reason] | [exclusion method] |
| [audience 3] | [reason] | [exclusion method] |
| [audience 4] | [reason] | [exclusion method] |
| [audience 5] | [reason] | [exclusion method] |

### Soft Exclusions (exclude in early campaigns, test later)
| Audience | Why Consider Excluding | When to Test |
|---|---|---|
| [audience 1] | [reason] | [conditions for testing] |
| [audience 2] | [reason] | [conditions] |
| [audience 3] | [reason] | [conditions] |

### Negative Keyword Themes (Google Ads)
- [theme 1]: [list of negative keywords]
- [theme 2]: [list of negative keywords]
- [theme 3]: [list of negative keywords]
- [theme 4]: [list of negative keywords]

### Audience Suppression Lists
- **Existing customers:** Suppress from acquisition campaigns (upload customer email list)
- **Past converters:** Suppress from top-of-funnel (use pixel data)
- **Job seekers:** Exclude "[company name] jobs/careers" searches
- **Competitors' employees:** Exclude unless running competitive conquesting
- **Students/researchers:** Exclude unless product is education-focused
```

### Step 6: Cross-Persona Insights

```markdown
## Cross-Persona Insights

### Shared Pain Points Across All Personas
1. [pain point that appears in 3+ personas]
2. [pain point that appears in 3+ personas]
3. [pain point that appears in 3+ personas]

### Universal Buying Triggers
1. [trigger that works across most personas]
2. [trigger that works across most personas]

### Platform Priority Ranking
Based on where these personas spend time:
1. **[Platform]** — Reaches [X] of [Y] personas, best for [objective]
2. **[Platform]** — Reaches [X] of [Y] personas, best for [objective]
3. **[Platform]** — Reaches [X] of [Y] personas, best for [objective]
4. **[Platform]** — Reaches [X] of [Y] personas, best for [objective]

### Campaign Structure Recommendation
- **Campaign 1 (Primary):** Target Personas [X, Y] on [Platform] — [objective]
- **Campaign 2 (Secondary):** Target Personas [X, Y] on [Platform] — [objective]
- **Campaign 3 (Testing):** Target Persona [X] on [Platform] — [objective]

### Messaging Theme Matrix
| Theme | Persona 1 | Persona 2 | Persona 3 | Persona 4 | Persona 5 |
|---|---|---|---|---|---|
| [theme 1] | Strong | Moderate | Weak | Strong | Moderate |
| [theme 2] | Weak | Strong | Strong | Moderate | Weak |
| [theme 3] | Moderate | Moderate | Strong | Strong | Strong |
```

## Output Format

Save the complete analysis to `ADS-AUDIENCE.md` in the current working directory.

**File structure:**
```
# Audience Persona Report: [Business Name]
> Generated [date] | Source: [URL]
> Ad Readiness — Audience Clarity Score: [X/100]

## Executive Summary
[3-4 sentences: who the ideal customers are, which platforms to prioritize, key insight]

## Persona 1: [Name]
[full persona template]

## Persona 2: [Name]
[full persona template]

[...continue for all 5-7 personas]

## Persona Scoring Matrix
[comparison table]

## Negative Audiences
[full negative audience section]

## Cross-Persona Insights
[shared insights and recommendations]

## Next Steps
1. Start with Persona [X] on [Platform] — highest relevance + largest audience
2. Build lookalike audiences from [seed source]
3. Run `/ads copy <platform>` to generate ad copy tailored to top personas
4. Run `/ads hooks` to generate scroll-stopping hooks for each persona
5. Set up A/B tests between Persona [X] and Persona [Y] messaging
```

## Quality Checklist
Before delivering the output, verify:
- [ ] At least 5 personas built with full detail
- [ ] Every persona has all sections filled (demographics, psychographics, pain points, triggers, objections, content habits, platform targeting)
- [ ] Platform targeting parameters are specific and actionable (not generic)
- [ ] Meta interests are real targetable interests in Ads Manager
- [ ] Google keywords are actual search terms people use
- [ ] LinkedIn titles are real job titles
- [ ] Relevance scoring is applied and justified
- [ ] Negative audiences section is complete
- [ ] Cross-persona insights identify patterns
- [ ] Campaign structure recommendation is included
- [ ] Output is saved to ADS-AUDIENCE.md

## Audience Clarity Score (0-100)

Calculate and report at the top of the file:

| Factor | Weight | Scoring |
|---|---|---|
| Persona specificity | 25% | Generic (0-40) / Detailed (41-70) / Hyper-specific (71-100) |
| Targeting actionability | 25% | Vague (0-40) / Usable (41-70) / Copy-paste ready (71-100) |
| Pain point depth | 20% | Surface-level (0-40) / Researched (41-70) / Customer-voice (71-100) |
| Platform coverage | 15% | 1-2 platforms (0-40) / 3-4 platforms (41-70) / 5+ platforms (71-100) |
| Negative audience quality | 15% | Missing (0) / Basic (1-40) / Detailed with methods (41-100) |

**Composite Score** = Weighted average across all factors
