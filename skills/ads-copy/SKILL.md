---
name: Platform-Specific Ad Copy Generator
description: Generates 10+ ad copy variations for any major ad platform with A/B testing, character-count compliance, and four proven copy frameworks (PAS, AIDA, BAB, 4Ps)
---

# Platform-Specific Ad Copy Generator

## Skill Purpose
Generate 10+ production-ready ad copy variations for a specified advertising platform. Every ad is written to exact platform specifications (character limits, format requirements, best practices), includes A/B variations, and uses proven direct-response copy frameworks. Output is copy-paste ready — an ad buyer can drop these directly into the ad platform without editing.

## When to Use
- User runs `/ads copy <platform>`
- User asks to generate ad copy for a specific platform
- Called as a subagent from `/ads strategy` (the main orchestrator)
- User needs ready-to-use ad text for any major ad platform
- User wants multiple copy variations for A/B testing

## Input Requirements
- **Required:** Target platform (google, meta, linkedin, tiktok, youtube, pinterest)
- **Required:** Business context — either a URL to analyze, or prior audience/strategy data
- **Optional:** Specific product/service to advertise, audience persona to target, offer/promotion details, tone preferences

## Supported Platforms & Ad Formats

### Google Ads
| Format | Headlines | Descriptions | Other |
|---|---|---|---|
| Responsive Search Ad (RSA) | Up to 15 headlines (30 chars each) | Up to 4 descriptions (90 chars each) | Display URL paths (15 chars each) |
| Display Ad | 1-5 headlines (30 chars), 1 long headline (90 chars) | 1-5 descriptions (90 chars) | Business name (25 chars) |
| Performance Max | 5 headlines (30 chars), 5 long headlines (90 chars) | 5 descriptions (90 chars) | Call-to-action text |

### Meta (Facebook/Instagram)
| Format | Primary Text | Headline | Description | Other |
|---|---|---|---|---|
| Facebook Feed | 125 chars (visible), 500+ allowed | 40 chars | 30 chars | CTA button |
| Instagram Feed | 125 chars (visible), 2200 max | 40 chars | N/A | CTA button |
| Stories/Reels | Minimal text overlay | Short overlay text | N/A | Swipe-up CTA |

### LinkedIn
| Format | Intro Text | Headline | Description | Other |
|---|---|---|---|---|
| Sponsored Content | 150 chars (truncated), 600 max | 70 chars | 100 chars (optional) | CTA button |
| Message Ads | 500 chars subject, 1500 body | N/A | N/A | CTA button + banner |
| Text Ads | N/A | 25 chars | 75 chars | 50x50 image |

### TikTok
| Format | Ad Text | Display Name | Other |
|---|---|---|---|
| In-Feed | 100 chars | 40 chars | CTA button, hashtags |
| TopView | 100 chars | 40 chars | First ad users see |
| Spark Ads | Use original post caption | Original creator | Boost existing content |

### YouTube
| Format | Script Length | On-Screen Text | Other |
|---|---|---|---|
| Bumper Ad (6s) | ~15-20 words | 1-2 text overlays | Non-skippable |
| Pre-roll (15s) | ~35-45 words | 2-3 text overlays | Skippable after 5s |
| Non-skip (30s) | ~70-90 words | 3-5 text overlays | Non-skippable |

### Pinterest
| Format | Title | Description | Other |
|---|---|---|---|
| Standard Pin | 100 chars | 500 chars | Link URL |
| Video Pin | 100 chars | 500 chars | Link URL |
| Carousel | 100 chars per card | 500 chars | 2-5 cards |

## How to Execute

### Step 1: Gather Business Context

If a URL is provided, fetch it using `WebFetch` and extract:
- Business name and industry
- Core value proposition
- Key products/services and pricing
- Target audience indicators
- Tone of voice and brand personality
- Unique selling points (USPs)
- Social proof elements (reviews, client count, years in business)
- Current offers or promotions

If audience data exists from a prior `/ads audience` run, reference the top personas.

Run supplementary research:
```
WebSearch: "[Business Name]" ads OR advertising
WebSearch: "[Industry]" best performing ad copy examples
WebSearch: "[Industry]" [platform] ad examples
```

### Step 2: Define Copy Inputs

Before writing any ad, establish these foundational elements:

```markdown
## Copy Foundation

**Business:** [Name]
**Industry:** [Category]
**Platform:** [Selected platform]
**Primary Offer:** [What they're selling/promoting]
**USP:** [What makes them different — the #1 differentiator]
**Target Persona:** [Primary persona from audience research]
**Desired Action:** [What do we want the viewer to DO]
**Tone:** [Professional / Casual / Bold / Playful / Urgent / Authoritative]
**Proof Points:** [Stats, testimonials, awards, client count, results]
**Price/Offer:** [Pricing, discount, free trial, free consultation]
```

### Step 3: Generate Ad Variations Using 4 Copy Frameworks

For each ad, apply one of the four frameworks:

#### Framework 1: PAS (Problem-Agitate-Solve)
- **Problem:** State the pain point the audience feels
- **Agitate:** Twist the knife — make them feel the cost of inaction
- **Solve:** Present the product/service as the relief

#### Framework 2: AIDA (Attention-Interest-Desire-Action)
- **Attention:** Bold opening that stops the scroll
- **Interest:** Interesting fact, story, or angle that pulls them in
- **Desire:** Paint the outcome — what life looks like after buying
- **Action:** Clear, compelling CTA

#### Framework 3: BAB (Before-After-Bridge)
- **Before:** Their current painful situation
- **After:** The transformed state they want
- **Bridge:** The product/service that gets them there

#### Framework 4: 4Ps (Promise-Picture-Proof-Push)
- **Promise:** Bold claim or guarantee
- **Picture:** Vivid image of the result
- **Proof:** Evidence (testimonial, stat, case study)
- **Push:** Urgency or scarcity to act now

### Step 4: Write Platform-Specific Ads

Generate **at least 10 ad variations** with A/B pairs for each. Use this structure:

---

#### Ad Variation Template (Google RSA Example)

```markdown
### Ad [Number] — [Framework Used] | Angle: [Pain/Benefit/Social Proof/Urgency]

**Version A:**

| Element | Copy | Chars |
|---|---|---|
| Headline 1 | [headline text] | [count]/30 |
| Headline 2 | [headline text] | [count]/30 |
| Headline 3 | [headline text] | [count]/30 |
| Description 1 | [description text] | [count]/90 |
| Description 2 | [description text] | [count]/90 |
| Display Path 1 | [path text] | [count]/15 |
| Display Path 2 | [path text] | [count]/15 |
| CTA | [call to action] | — |

**Version B (A/B Variation):**

| Element | Copy | Chars |
|---|---|---|
| Headline 1 | [alternate headline] | [count]/30 |
| Headline 2 | [alternate headline] | [count]/30 |
| Headline 3 | [alternate headline] | [count]/30 |
| Description 1 | [alternate description] | [count]/90 |
| Description 2 | [alternate description] | [count]/90 |
| Display Path 1 | [path text] | [count]/15 |
| Display Path 2 | [path text] | [count]/15 |
| CTA | [call to action] | — |

**Why this works:** [2-3 sentences explaining the psychology and angle]
**Best for:** [which audience persona / funnel stage]
**Testing note:** [what's being tested between A and B]
```

#### Ad Variation Template (Meta Example)

```markdown
### Ad [Number] — [Framework Used] | Angle: [Pain/Benefit/Social Proof/Urgency]

**Version A:**

| Element | Copy | Chars |
|---|---|---|
| Primary Text | [full ad copy — can be multi-line, include emojis where appropriate] | [count] |
| Headline | [headline text] | [count]/40 |
| Description | [description text] | [count]/30 |
| CTA Button | [Shop Now / Learn More / Sign Up / Get Offer / Book Now / Contact Us] | — |

**Version B (A/B Variation):**

| Element | Copy | Chars |
|---|---|---|
| Primary Text | [alternate copy] | [count] |
| Headline | [alternate headline] | [count]/40 |
| Description | [alternate description] | [count]/30 |
| CTA Button | [alternate CTA] | — |

**Why this works:** [explanation]
**Best for:** [persona / funnel stage]
**Testing note:** [what's being tested]
```

### Step 5: Ad Distribution Across Frameworks and Angles

Ensure the 10+ ads are distributed across frameworks and angles:

| # | Framework | Angle | Funnel Stage |
|---|---|---|---|
| Ad 1-2 | PAS | Pain/Problem | TOFU (awareness) |
| Ad 3-4 | AIDA | Benefit/Transformation | TOFU (awareness) |
| Ad 5-6 | BAB | Before/After | MOFU (consideration) |
| Ad 7-8 | 4Ps | Social Proof/Authority | MOFU (consideration) |
| Ad 9-10 | PAS | Urgency/Scarcity | BOFU (conversion) |
| Ad 11-12 | AIDA | Objection Handling | BOFU (conversion) |

### Step 6: Platform-Specific Best Practices

Include a best practices section at the end of the output:

**Google Ads:**
- Pin Headline 1 with brand name or primary keyword for RSAs
- Use keyword insertion syntax: {KeyWord:Default Text}
- Include numbers and percentages (they increase CTR)
- Every headline should make sense standalone and in combination
- Use at least 1 headline with a CTA, 1 with a benefit, 1 with a keyword

**Meta (Facebook/Instagram):**
- First line must hook — only 125 chars show before "See More"
- Use line breaks and emojis to improve readability
- Social proof in primary text outperforms features
- Questions as headlines drive 30-50% more engagement
- Stories ads: keep text minimal, let visuals carry the message

**LinkedIn:**
- Professional tone but not boring — conversational authority works best
- Stats and data outperform emotional appeals
- Tag company pages in Sponsored Content for social proof
- Message Ads: personalize the subject line and keep body under 500 words
- Questions in intro text drive 50% more clicks

**TikTok:**
- Write like a creator, not a brand
- Use trending language and casual tone
- Hashtag strategy: 3-5 relevant hashtags, 1 branded
- Spark Ads (boosting organic posts) outperform traditional ads 2:1
- First 2 seconds determine if they watch or scroll

**YouTube:**
- Bumper (6s): One message, one visual, one CTA — that's it
- Pre-roll (15s): Hook in first 5 seconds before skip button appears
- Include a clear verbal CTA + on-screen CTA
- Cards and end screens extend engagement

**Pinterest:**
- Use keyword-rich descriptions (Pinterest is a search engine)
- 500-character descriptions perform best
- Include pricing in Pin titles when relevant
- Vertical format (2:3 aspect ratio) gets 60% more engagement
- Call-to-action language increases click-through by 70%

### Step 7: Headline Bank

Include a supplementary headline bank organized by angle:

```markdown
## Headline Bank (Quick-Reference)

### Benefit-Driven Headlines
1. [headline] ([char count])
2. [headline] ([char count])
3. [headline] ([char count])
4. [headline] ([char count])
5. [headline] ([char count])

### Pain-Point Headlines
1. [headline] ([char count])
2. [headline] ([char count])
3. [headline] ([char count])
4. [headline] ([char count])
5. [headline] ([char count])

### Social Proof Headlines
1. [headline] ([char count])
2. [headline] ([char count])
3. [headline] ([char count])

### Urgency/Scarcity Headlines
1. [headline] ([char count])
2. [headline] ([char count])
3. [headline] ([char count])

### Question Headlines
1. [headline] ([char count])
2. [headline] ([char count])
3. [headline] ([char count])
```

## Output Format

Save the complete output to `ADS-COPY-[PLATFORM].md` in the current working directory.

Replace `[PLATFORM]` with the actual platform name in caps: `GOOGLE`, `META`, `LINKEDIN`, `TIKTOK`, `YOUTUBE`, `PINTEREST`.

**File structure:**
```
# Ad Copy — [Platform]: [Business Name]
> Generated [date] | Source: [URL]
> Platform: [Platform] | Formats: [list of ad formats covered]
> Framework Mix: PAS, AIDA, BAB, 4Ps

## Copy Foundation
[copy inputs section]

## Ad Variations

### Ad 1 — [Framework] | [Angle]
[full ad with A/B variation]

### Ad 2 — [Framework] | [Angle]
[full ad with A/B variation]

[...continue for all 10+ ads]

## Headline Bank
[organized headline collection]

## Platform Best Practices
[platform-specific tips]

## Next Steps
1. Upload ads to [Platform] Ads Manager
2. Set up A/B tests: start with Ad [X]a vs Ad [X]b
3. Run `/ads hooks` to generate additional scroll-stopping openers
4. Run `/ads video <product>` if video ads are needed
5. Monitor CTR for first 72 hours, pause underperformers at [threshold]
```

## Quality Checklist
Before delivering the output, verify:
- [ ] At least 10 ad variations generated
- [ ] Every ad has an A/B variation
- [ ] All character counts are within platform limits
- [ ] Character counts are displayed next to every copy element
- [ ] All 4 copy frameworks are represented
- [ ] Ads cover TOFU, MOFU, and BOFU funnel stages
- [ ] Each ad includes "why this works" explanation
- [ ] Platform-specific formatting is correct (emojis for Meta, professional for LinkedIn, etc.)
- [ ] CTA buttons/text match platform options
- [ ] Headline bank is included
- [ ] Best practices section is included
- [ ] Output file is named correctly: ADS-COPY-[PLATFORM].md

## Copy Quality Standards

Every piece of ad copy must follow these rules:
1. **Specific over vague** — "Save 3 hours per week" beats "Save time"
2. **Numbers beat words** — "4.9-star rated" beats "highly rated"
3. **You over we** — "You'll get..." beats "We offer..."
4. **Active voice only** — "Cut your costs by 40%" beats "Costs can be reduced"
5. **One CTA per ad** — Never split attention between two actions
6. **Proof over claims** — "Trusted by 10,000+ businesses" beats "The best solution"
7. **Benefit over feature** — "Sleep better tonight" beats "Memory foam mattress"
8. **Platform-native tone** — TikTok reads like a friend, LinkedIn reads like a thought leader, Google reads like an answer
