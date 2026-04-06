---
name: ads-quick
description: 60-Second Ad Readiness Snapshot — quick assessment without subagents
version: 1.0.0
author: AI Ads Strategist
tags: [ads, quick, snapshot, assessment, readiness]
trigger: /ads quick
output: Terminal output (no file saved)
---

# 60-Second Ad Readiness Snapshot

## Skill Purpose
Perform a rapid ad readiness assessment of a website or business without launching subagents. Fetches the homepage, evaluates value proposition strength, offer clarity, CTA quality, landing page readiness, and trust signal presence. Outputs a compact scorecard with a platform recommendation and estimated starting budget. The entire output must be under 40 lines.

## When to Use
- User wants a quick gut-check before investing in a full ad strategy
- User asks "should I run ads?" or "am I ready for ads?"
- User wants a fast assessment without waiting for the full 5-agent analysis
- User is exploring whether paid advertising makes sense for their business
- Triggered by `/ads quick <url>`

## When NOT to Use
- User wants a detailed, comprehensive strategy (use `/ads strategy` instead)
- User already has ad data to analyze (use `/ads audit` instead)
- User needs creative briefs (use `/ads creative` instead)
- No URL is provided (this skill requires a URL to fetch)

## How to Execute

### Step 1: Fetch and Analyze the Homepage

Use `WebFetch` to retrieve the homepage content. Extract these elements:

```
WebFetch(url) -> Analyze:
1. Headline / Hero Section — What is the main promise?
2. Value Proposition — Is it clear what they sell and why it matters?
3. CTA(s) — What action are they asking visitors to take?
4. Offer — Is there a specific offer (pricing, free trial, discount)?
5. Trust Signals — Reviews, testimonials, badges, client logos, certifications?
6. Visual Quality — Professional images, consistent branding, modern design?
7. Mobile Indicators — Responsive hints, fast-loading signals?
8. Contact Info — Phone, email, chat, address visible?
```

### Step 2: Score 5 Dimensions

Rate each dimension on a 0-20 scale:

**1. Value Proposition Strength (0-20)**
| Score | Criteria |
|-------|----------|
| 17-20 | Crystal clear what they do, for whom, and why it's better. Unique mechanism stated. |
| 13-16 | Clear offering, target audience implied, some differentiation. |
| 9-12 | Generic value prop, could apply to many businesses. |
| 5-8 | Vague or buried value proposition. Requires effort to understand. |
| 0-4 | No clear value proposition. Visitor would not know what this business does. |

**2. Offer Clarity (0-20)**
| Score | Criteria |
|-------|----------|
| 17-20 | Specific offer with pricing, clear next step, and urgency/scarcity element. |
| 13-16 | Offer is visible but lacks urgency or specific pricing. |
| 9-12 | Generic "contact us" or "learn more" without a defined offer. |
| 5-8 | No clear offer — visitor must dig to find what to do next. |
| 0-4 | No offer whatsoever. No pricing, no CTA, no next step. |

**3. CTA Quality (0-20)**
| Score | Criteria |
|-------|----------|
| 17-20 | Strong, specific CTA above the fold. Action-oriented language. Multiple CTAs in logical places. |
| 13-16 | CTA exists above the fold but is generic ("Learn More", "Contact Us"). |
| 9-12 | CTA exists but is below the fold or hard to find. |
| 5-8 | Weak or confusing CTAs. Multiple competing actions with no hierarchy. |
| 0-4 | No CTA visible. No clear path for the visitor to take action. |

**4. Landing Page Readiness (0-20)**
| Score | Criteria |
|-------|----------|
| 17-20 | Fast-loading, mobile-friendly, professional design, conversion-optimized layout. |
| 13-16 | Good design, loads reasonably, but not optimized for conversions. |
| 9-12 | Functional but dated design, some UX issues, average load time. |
| 5-8 | Slow, outdated, poor mobile experience, or cluttered layout. |
| 0-4 | Broken, extremely slow, or unprofessional. Would hurt ad performance. |

**5. Trust Signal Presence (0-20)**
| Score | Criteria |
|-------|----------|
| 17-20 | Multiple trust signals: reviews with star ratings, testimonials with names/photos, client logos, certifications, media mentions. |
| 13-16 | Some trust signals present (reviews or testimonials, but not both). |
| 9-12 | Minimal trust signals — maybe a generic "trusted by" without specifics. |
| 5-8 | Almost no social proof. Only basic contact info as trust signal. |
| 0-4 | No trust signals. Anonymous website with no credibility markers. |

**Ad Readiness Score** = Sum of all 5 dimensions (0-100)

### Step 3: Determine Platform Recommendation

Based on the business type and readiness score, recommend the best starting platform:

| Business Type | Primary Platform | Why | Min Budget/Month |
|---------------|-----------------|-----|-----------------|
| Local Service | Google Ads (Search) | High-intent search traffic | $500-$1,500 |
| E-commerce | Meta (FB/IG) | Visual products, impulse purchases | $1,000-$3,000 |
| SaaS B2B | LinkedIn + Google | Professional targeting, search intent | $2,000-$5,000 |
| SaaS B2C | Meta + Google | Broad reach + search capture | $1,000-$3,000 |
| Restaurant | Meta (Local) | Visual food content, local targeting | $300-$800 |
| Course/Creator | YouTube + Meta | Video content, retargeting | $1,000-$2,500 |
| Agency/Consulting | LinkedIn + Google | B2B targeting, authority | $1,500-$4,000 |

**Secondary Platform Recommendation:**
After the primary platform is established (30-60 days), recommend a secondary platform:
| Primary | Secondary | Why Add It |
|---------|-----------|-----------|
| Google Search | Meta (retargeting) | Capture search visitors who did not convert |
| Meta | Google Search | Catch high-intent searchers your social ads prompted |
| LinkedIn | Google Search | Capture branded searches from LinkedIn awareness |
| YouTube | Meta | Retarget video viewers with direct response ads |

### Step 4: Estimate CPC and CPA Ranges

Provide realistic cost expectations based on industry and platform:

**CPC Ranges by Industry and Platform:**
| Industry | Google Search CPC | Meta CPC | LinkedIn CPC | TikTok CPC |
|----------|------------------|----------|-------------|-----------|
| Local Services | $3-$12 | $0.80-$2.50 | N/A | $0.50-$1.50 |
| E-commerce | $0.50-$3 | $0.40-$1.50 | N/A | $0.20-$0.80 |
| SaaS B2B | $3-$15 | $1.50-$4.00 | $4-$12 | N/A |
| SaaS B2C | $1-$5 | $0.50-$2.00 | N/A | $0.30-$1.00 |
| Education/Courses | $1-$6 | $0.60-$2.00 | $3-$8 | $0.25-$0.80 |
| Restaurant/Hospitality | $0.50-$3 | $0.30-$1.00 | N/A | $0.20-$0.60 |
| Agency/Consulting | $3-$10 | $1.00-$3.50 | $5-$12 | N/A |

**Expected CPA by Business Type:**
| Business Type | Low CPA | Avg CPA | High CPA | Notes |
|---------------|---------|---------|----------|-------|
| Local Service (lead) | $15 | $35 | $75 | Phone call or form submission |
| E-commerce (purchase) | $10 | $30 | $60 | Depends heavily on AOV |
| SaaS B2B (demo/trial) | $50 | $150 | $300 | Higher LTV justifies higher CPA |
| SaaS B2C (sign-up) | $5 | $25 | $60 | Free trial vs paid sign-up |
| Course (enrollment) | $20 | $60 | $120 | Webinar funnel reduces CPA |
| Restaurant (visit) | $3 | $10 | $25 | Tracked via offer redemption |

### Step 5: Competitive Quick Check

Before finalizing the snapshot, do one quick competitive signal check:

**WebSearch query:**
```
"[Industry]" "[City]" ads OR advertising OR sponsored
```

Note: Are competitors actively advertising? If yes, the market is validated but competitive. If no, there may be an opportunity or the market may not support paid ads.

### Step 6: Generate Readiness Verdict

| Score Range | Verdict | Recommendation |
|-------------|---------|---------------|
| 80-100 | Ready to Launch | Start ads immediately. Focus on testing and scaling. |
| 60-79 | Almost Ready | Fix 1-2 gaps first, then launch. Estimate 1-2 weeks of prep. |
| 40-59 | Needs Work | Significant improvements needed before ads will be effective. 2-4 weeks. |
| 20-39 | Not Ready | Major landing page and offer issues. Fix fundamentals first. 4-8 weeks. |
| 0-19 | Rebuild Required | Website/offer needs major overhaul before any ad spend. |

## Output Format

Output directly to terminal. Do NOT save a file. Keep output under 40 lines.

```
============================================
  AD READINESS SNAPSHOT: [Business Name]
  URL: [url]
============================================

  AD READINESS SCORE: [XX]/100 — [Verdict]

  SCORECARD:
  Value Proposition ... [XX]/20 [status word]
  Offer Clarity ....... [XX]/20 [status word]
  CTA Quality ......... [XX]/20 [status word]
  Landing Page ........ [XX]/20 [status word]
  Trust Signals ....... [XX]/20 [status word]

  TOP 3 STRENGTHS:
  1. [strength]
  2. [strength]
  3. [strength]

  TOP 3 GAPS TO FIX:
  1. [gap + specific fix]
  2. [gap + specific fix]
  3. [gap + specific fix]

  RECOMMENDED PLATFORM: [Platform]
  ESTIMATED STARTING BUDGET: $[X]-$[Y]/month
  EXPECTED CPC RANGE: $[X]-$[Y]

  NEXT STEP: [One specific action to take]
  Full strategy: /ads strategy [url]
============================================
```

## Important Rules
- This is a SPEED tool — complete the entire analysis in under 60 seconds
- Do NOT launch any subagents — this is a single-pass analysis
- Output must be under 40 lines — be concise
- Do NOT save a file — output to terminal only
- Always end with a recommendation to run `/ads strategy` for the full analysis
- If the homepage cannot be fetched, explain the issue and suggest the user provide a different URL
- Be honest about readiness — do not inflate scores to be encouraging
- Budget recommendations should be realistic monthly minimums, not aspirational
- Always consider the business type when recommending platforms
- One specific next step is more valuable than a list of generic advice
