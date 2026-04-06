---
name: ads-audit
description: Ad Performance Auditor — analyze existing ad campaigns and identify optimization opportunities
version: 1.0.0
author: AI Ads Strategist
tags: [ads, audit, performance, optimization, analytics]
trigger: /ads audit
output: ADS-AUDIT.md
---

# Ad Performance Auditor

## Skill Purpose
Analyze existing ad campaign performance from user-provided data (screenshots, descriptions, or metrics). Evaluate key performance indicators against industry benchmarks, detect creative fatigue and audience overlap, identify budget waste, and provide prioritized optimization recommendations ranked by expected impact. This is a diagnostic tool — it tells you what is working, what is broken, and what to fix first.

## When to Use
- User wants to audit their existing ad campaigns
- User shares ad performance data (screenshots, CSV, or described metrics)
- User asks "why aren't my ads working?" or "how can I improve my ads?"
- User wants to know if their ad spend is efficient
- User has been running ads for 7+ days and wants a performance check
- Triggered by `/ads audit` or `/ads audit <platform>`

## Data Collection

### Step 1: Gather Performance Data

Ask the user to provide their ad data in any of these formats:

**Option A: Key Metrics (Manual Input)**
Ask for these metrics per campaign/ad set:
| Metric | What to Ask |
|--------|------------|
| Platform | Which platform (Meta, Google, TikTok, LinkedIn, etc.)? |
| Campaign Objective | What's the campaign optimized for (awareness, traffic, conversions, leads)? |
| Time Period | How long has this campaign been running? Date range? |
| Spend | Total amount spent in this period |
| Impressions | Total impressions |
| Reach | Unique people reached (if available) |
| Clicks | Total clicks (link clicks, not all clicks) |
| CTR | Click-through rate (or calculate from impressions/clicks) |
| CPC | Cost per click |
| Conversions | Total conversions (purchases, leads, sign-ups) |
| Conversion Rate | Landing page conversion rate |
| CPA/CPL | Cost per acquisition or cost per lead |
| ROAS | Return on ad spend (revenue / spend) |
| Frequency | Average times each person saw the ad |
| Ad Creative Type | Image, video, carousel, etc. |

**Option B: Screenshot Analysis**
If the user shares screenshots of their ad dashboard:
- Extract all visible metrics from the screenshot
- Note which metrics are missing
- Ask follow-up questions for critical missing data

**Option C: Platform-Specific Export**
Guide the user to export data:
- **Meta**: Ads Manager > Export > Select columns
- **Google**: Reports > Download
- **TikTok**: Analytics > Export
- **LinkedIn**: Campaign Manager > Export

### Step 2: Establish Industry Benchmarks

Use these benchmark ranges by platform and objective. Compare the user's metrics against these:

**Meta (Facebook/Instagram) Benchmarks:**
| Metric | Poor | Below Average | Average | Good | Excellent |
|--------|------|---------------|---------|------|-----------|
| CTR (Link) | <0.5% | 0.5-0.8% | 0.8-1.2% | 1.2-2.0% | >2.0% |
| CPC (Link) | >$3.00 | $2.00-3.00 | $1.00-2.00 | $0.50-1.00 | <$0.50 |
| CPM | >$20 | $15-20 | $10-15 | $5-10 | <$5 |
| Conv. Rate | <1% | 1-2% | 2-5% | 5-10% | >10% |
| ROAS | <1x | 1-2x | 2-4x | 4-8x | >8x |
| Frequency (7d) | >5 | 3-5 | 2-3 | 1.5-2 | 1-1.5 |

**Google Ads (Search) Benchmarks:**
| Metric | Poor | Below Average | Average | Good | Excellent |
|--------|------|---------------|---------|------|-----------|
| CTR | <1% | 1-2% | 2-4% | 4-7% | >7% |
| CPC | >$5.00 | $3.00-5.00 | $1.50-3.00 | $0.75-1.50 | <$0.75 |
| Conv. Rate | <1% | 1-3% | 3-6% | 6-10% | >10% |
| Quality Score | 1-3 | 4-5 | 6-7 | 8-9 | 10 |

**Google Ads (Display) Benchmarks:**
| Metric | Poor | Below Average | Average | Good | Excellent |
|--------|------|---------------|---------|------|-----------|
| CTR | <0.1% | 0.1-0.3% | 0.3-0.5% | 0.5-1.0% | >1.0% |
| CPC | >$2.00 | $1.00-2.00 | $0.50-1.00 | $0.25-0.50 | <$0.25 |
| Conv. Rate | <0.5% | 0.5-1% | 1-2% | 2-4% | >4% |

**TikTok Benchmarks:**
| Metric | Poor | Below Average | Average | Good | Excellent |
|--------|------|---------------|---------|------|-----------|
| CTR | <0.3% | 0.3-0.5% | 0.5-1.0% | 1.0-2.0% | >2.0% |
| CPC | >$2.00 | $1.00-2.00 | $0.50-1.00 | $0.25-0.50 | <$0.25 |
| CPM | >$15 | $10-15 | $6-10 | $3-6 | <$3 |
| Video View Rate | <15% | 15-25% | 25-35% | 35-50% | >50% |

**LinkedIn Benchmarks:**
| Metric | Poor | Below Average | Average | Good | Excellent |
|--------|------|---------------|---------|------|-----------|
| CTR | <0.2% | 0.2-0.4% | 0.4-0.7% | 0.7-1.0% | >1.0% |
| CPC | >$10.00 | $7.00-10.00 | $4.00-7.00 | $2.00-4.00 | <$2.00 |
| CPM | >$50 | $35-50 | $20-35 | $10-20 | <$10 |
| Conv. Rate | <1% | 1-2% | 2-4% | 4-7% | >7% |

**Industry Vertical Adjustments:**
- **E-commerce**: CPA benchmarks $15-$45, ROAS target 3-5x
- **SaaS/B2B**: CPA benchmarks $50-$200, focus on CPL not CPA
- **Local Services**: CPA benchmarks $20-$75, call tracking critical
- **Education/Courses**: CPA benchmarks $30-$100, webinar reg focus
- **Real Estate**: CPL benchmarks $20-$80, lead quality matters more than volume

### Step 3: Performance Analysis

Run each of these diagnostic checks:

#### 3A: Efficiency Analysis
Calculate and evaluate:
- **Cost Efficiency Score**: How much value per dollar spent?
- **Click Efficiency**: CTR vs benchmark for this platform/industry
- **Conversion Efficiency**: Conv rate vs benchmark
- **ROAS Check**: Is the return justifying the spend?
- **Budget Utilization**: Is the daily budget being fully spent? Underspending signals targeting too narrow.

#### 3B: Creative Fatigue Detection
Identify if ads have fatigued:
| Signal | Threshold | Status |
|--------|-----------|--------|
| CTR decline | >20% drop over 7 days | Fatigued |
| Frequency | >3 in 7 days | Oversaturated |
| CPC increase | >30% increase over 7 days | Auction pressure |
| Relevance/Quality dropping | Score declining | Creative stale |
| Conversion rate declining | >15% drop | Message exhausted |

**Creative Fatigue Diagnosis:**
- Mild fatigue: CTR dropped 10-20%, frequency 2-3 → Refresh ad copy and images
- Moderate fatigue: CTR dropped 20-40%, frequency 3-5 → New creative concepts needed
- Severe fatigue: CTR dropped >40%, frequency >5 → Pause and relaunch with entirely new creative

#### 3C: Audience Analysis
Evaluate targeting effectiveness:
- **Audience Size**: Too broad (>10M on Meta) or too narrow (<100K)?
- **Audience Overlap**: Multiple ad sets targeting the same people?
- **Demographic Performance**: Which age/gender/location segments convert best?
- **Placement Performance**: Which placements (feed, stories, reels, search, display) perform best?
- **Device Performance**: Mobile vs desktop conversion differences?

#### 3D: Budget Waste Identification
Find where money is being wasted:

| Waste Type | How to Detect | Fix |
|------------|--------------|-----|
| Audience Overlap | Multiple ad sets with >30% audience overlap | Consolidate or exclude |
| Poor Placements | Placements with high spend, low conversion | Exclude underperformers |
| Time-of-Day Waste | Spending during low-converting hours | Dayparting schedule |
| Geographic Waste | Spending in non-converting locations | Geo-targeting refinement |
| Device Mismatch | High mobile clicks but desktop-only landing page | Mobile-optimize LP |
| Broad Match Waste | (Google) Irrelevant search terms eating budget | Negative keywords |
| Frequency Cap Missing | Same person seeing ad 10+ times | Set frequency cap |
| Low Quality Score | (Google) Score <5 driving up CPC | Improve relevance |

#### 3E: Funnel Leak Detection
Identify where conversions are being lost:

```
Impressions (100%) → Clicks (CTR: X%) → Landing Page Views (X%) → Conversions (X%)
                                              ^                        ^
                                              |                        |
                                         LP Load Speed?          LP Conversion?
                                         Bounce Rate?            Form Friction?
                                         Mobile UX?              Offer Mismatch?
```

Calculate drop-off at each stage:
- Impression to Click: Is the ad compelling? (Creative issue)
- Click to Landing Page View: Is the page loading? (Technical issue)
- Landing Page View to Conversion: Is the offer converting? (Offer/UX issue)

### Step 4: Scoring

**Overall Ad Performance Score (0-100):**

| Dimension | Weight | Score Range | Assessment |
|-----------|--------|-------------|------------|
| Cost Efficiency | 25% | 0-25 | CPC, CPM, CPA vs benchmarks |
| Creative Performance | 20% | 0-20 | CTR, engagement, fatigue level |
| Conversion Quality | 25% | 0-25 | Conv rate, ROAS, lead quality |
| Audience Targeting | 15% | 0-15 | Targeting precision, overlap, segmentation |
| Budget Optimization | 15% | 0-15 | Budget utilization, waste, allocation |

**Score Interpretation:**
- 80-100: Excellent — minor optimizations only
- 60-79: Good — solid foundation with optimization opportunities
- 40-59: Needs Work — significant improvements needed in multiple areas
- 20-39: Poor — fundamental strategy issues to address
- 0-19: Critical — major problems, consider pausing and restructuring

### Step 5: Generate Recommendations

Produce recommendations in 3 tiers, ordered by expected impact:

**Tier 1: Immediate Actions (This Week)**
Actions that can be done today with no additional resources:
- Pause underperforming ad sets
- Adjust budgets toward top performers
- Add negative keywords (Google)
- Adjust frequency caps
- Fix audience overlap
- Update ad copy with top-performing hooks

**Tier 2: Short-Term Optimizations (Next 2 Weeks)**
Actions that require some creative or strategic work:
- Launch new creative variations
- Test new audiences
- A/B test landing pages
- Implement retargeting
- Adjust bidding strategy
- Expand to new placements

**Tier 3: Strategic Changes (Next 30 Days)**
Actions that require planning and significant effort:
- Restructure campaign architecture
- Build new funnel stages
- Create new creative concepts
- Expand to new platforms
- Redesign landing pages
- Implement conversion tracking improvements

### Step 6: Projected Impact

For each Tier 1 recommendation, estimate:
| Action | Current Metric | Expected Improvement | Confidence |
|--------|---------------|---------------------|------------|
| [action] | [current value] | [projected value] | High/Medium/Low |

## Output Format

Save as `ADS-AUDIT.md` in the current working directory.

```markdown
# Ad Performance Audit: [Business/Campaign Name]
**Audit Date:** [Date]
**Period Analyzed:** [Date Range]
**Platform(s):** [Platforms]
**Total Spend Analyzed:** $[Amount]

---

## Overall Ad Performance Score: [X]/100
[Visual score bar or assessment]

## Executive Summary
- **Top Finding:** [Single most impactful finding]
- **Biggest Waste:** $[Amount] wasted on [what]
- **Biggest Opportunity:** [What could improve results most]
- **Estimated Improvement:** [X]% improvement possible with Tier 1 changes

---

## Performance Dashboard

### Key Metrics vs Benchmarks
| Metric | Your Value | Industry Avg | Status | Gap |
|--------|-----------|-------------|--------|-----|
| CTR | X% | X% | [emoji-free status] | +/-X% |
| CPC | $X | $X | [status] | +/-$X |
| Conv Rate | X% | X% | [status] | +/-X% |
| ROAS | Xx | Xx | [status] | +/-Xx |
| Frequency | X | X | [status] | +/-X |

### Scoring Breakdown
| Dimension | Score | Key Finding |
|-----------|-------|-------------|
| Cost Efficiency | X/25 | [finding] |
| Creative Performance | X/20 | [finding] |
| Conversion Quality | X/25 | [finding] |
| Audience Targeting | X/15 | [finding] |
| Budget Optimization | X/15 | [finding] |

---

## Detailed Analysis

### Creative Fatigue Assessment
[Fatigue level, evidence, recommendation]

### Audience Analysis
[Targeting assessment, overlap issues, segment performance]

### Budget Waste Report
| Waste Type | Estimated Waste | Fix |
|------------|----------------|-----|
| [type] | $[amount] | [fix] |

### Funnel Leak Analysis
[Stage-by-stage drop-off analysis]

---

## Recommendations

### Tier 1: Immediate Actions (This Week)
| # | Action | Expected Impact | Effort |
|---|--------|----------------|--------|
| 1 | [action] | [impact] | Low |

### Tier 2: Short-Term (Next 2 Weeks)
| # | Action | Expected Impact | Effort |
|---|--------|----------------|--------|
| 1 | [action] | [impact] | Medium |

### Tier 3: Strategic (Next 30 Days)
| # | Action | Expected Impact | Effort |
|---|--------|----------------|--------|
| 1 | [action] | [impact] | High |

---

## Projected Impact of Tier 1 Changes
| Action | Current | Projected | Confidence |
|--------|---------|-----------|------------|
| [action] | [value] | [value] | High/Med/Low |

## Next Steps
1. Implement Tier 1 actions immediately
2. Re-audit in 7 days with `/ads audit`
3. Use `/ads creative` to generate fresh creative if fatigue detected
4. Use `/ads funnel` to restructure campaign architecture if needed
5. Generate new copy with `/ads copy <platform>`
```

## Important Rules
- Never make assumptions about missing data — ask for it or flag it as unavailable
- Always compare to platform-specific benchmarks, not cross-platform averages
- Industry vertical matters — adjust benchmarks accordingly
- Frequency is one of the most overlooked metrics — always check it
- ROAS alone is not enough — consider contribution margin and LTV
- Budget waste identification should always include estimated dollar amounts
- Recommendations must be specific and actionable, not generic best practices
- Tier 1 recommendations should be achievable without additional creative assets
- Always consider seasonality when evaluating performance trends
- If data is insufficient for a thorough audit, say so clearly and specify what is needed
- A declining CTR with stable conversions might be fine — context matters
- Never recommend increasing budget on a campaign that has fundamental creative/targeting issues
