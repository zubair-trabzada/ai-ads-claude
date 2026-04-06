---
name: Scroll-Stopping Hook Generator
description: Generates 20+ scroll-stopping ad hooks organized by psychological angle (pain, curiosity, social proof, contrarian, urgency) with platform-specific formatting, A/B variations, and psychology breakdowns
---

# Scroll-Stopping Hook Generator

## Skill Purpose
Generate 20+ battle-tested hooks that stop the scroll across every major ad platform. Hooks are the single most important element in any ad — the first 1-3 seconds determine whether your ad gets watched or ignored. This skill produces hooks organized by psychological angle, each with platform-specific formatting, an A/B variation, a psychology breakdown explaining why it works, and guidance on where to use it. Output is ready to plug directly into ad copy, video scripts, or email subject lines.

## When to Use
- User runs `/ads hooks`
- User asks for scroll-stopping hooks, opening lines, or attention-grabbers
- Called as a subagent from `/ads strategy` (the main orchestrator)
- User needs hooks for ad creative, video intros, or email campaigns
- User wants to improve CTR on existing ads by testing new hooks

## Input Requirements
- **Required:** Business context — a URL, product/service description, or prior strategy data
- **Optional:** Target persona, specific platform focus, industry vertical, offer details

## How to Execute

### Step 1: Gather Business & Audience Context

If a URL is provided, fetch it using `WebFetch` and extract:
- Business name, industry, and niche
- Core value proposition and USPs
- Target audience indicators
- Pain points the product/service solves
- Price point and offer structure
- Social proof assets (review count, client count, awards)
- Competitor landscape

Run supplementary research:
```
WebSearch: "[Industry]" best performing ad hooks
WebSearch: "[Industry]" viral ad examples
WebSearch: "[Product category]" ad copy examples high CTR
```

Establish the hook foundation:

```markdown
## Hook Foundation

**Business:** [Name]
**Product/Service:** [What they sell]
**Target Audience:** [Primary persona in 1 sentence]
**Core Pain Point:** [The #1 problem the audience has]
**Core Desire:** [The #1 outcome the audience wants]
**USP:** [What makes this different from competitors]
**Proof Points:** [Stats, results, testimonials available]
**Offer:** [Current promotion, pricing, free trial]
```

### Step 2: Generate Hooks by Psychological Angle

Generate **20+ hooks minimum** distributed across 5 psychological angles:

---

#### Angle 1: Pain/Problem Hooks (5 minimum)

These hooks work by calling out a pain the audience already feels. They create instant recognition — "that's me!" — which stops the scroll.

**Psychology:** Loss aversion. People are 2x more motivated to avoid pain than to gain pleasure. Pain hooks activate the amygdala's threat detection system.

**Template patterns:**
- "Stop [doing painful thing] and start [doing desired thing]"
- "If you're still [painful situation], here's why..."
- "[Number]% of [audience] are making this [topic] mistake"
- "The [topic] mistake that's costing you [specific loss]"
- "You're losing [specific amount] every [time period] because..."

For each hook:

```markdown
### Hook P[number]: [Hook Text]

**Full text:** [The complete hook — 1-2 sentences max]
**A/B variation:** [Alternate version testing a different angle or word choice]
**Character count:** [count] characters
**Best platform(s):** [where this hook performs best]
**Funnel stage:** [TOFU / MOFU / BOFU]
**Why it works:** [2-3 sentences on the psychology — which cognitive bias, emotional trigger, or pattern interrupt is at play]
**How to use it:**
- **Facebook/Instagram ad:** [how to format — as primary text opening, headline, or text overlay]
- **TikTok/Reels:** [how to deliver — on-screen text, voiceover opening, or both]
- **Google ad:** [how to adapt — as headline, description opening]
- **YouTube pre-roll:** [how to deliver in first 5 seconds]
- **Email subject line:** [adapted version for email]
**Emoji treatment:** [which emojis to add and where, or "none — let the words hit"]
**Hashtag pairing:** [2-3 relevant hashtags if used on social]
```

---

#### Angle 2: Curiosity/Question Hooks (5 minimum)

These hooks create an information gap that the viewer must close. The brain cannot tolerate an open loop — curiosity is physically uncomfortable until resolved.

**Psychology:** The Zeigarnik Effect. Unfinished thoughts create cognitive tension. Question hooks exploit the brain's compulsion to find answers.

**Template patterns:**
- "What happens when you [unexpected action] with [topic]?"
- "I tested [thing] for [time period]. Here's what happened..."
- "The [topic] secret that [authority] don't want you to know"
- "Why do [successful people] always [unexpected behavior]?"
- "I asked [number] [experts] one question. Their answer shocked me."
- "This [simple thing] changed my [topic] forever. (Not what you think.)"

For each hook, use the same template as Angle 1.

---

#### Angle 3: Social Proof/Authority Hooks (5 minimum)

These hooks leverage other people's actions or endorsements to trigger herd behavior. If others are doing it, it must be good.

**Psychology:** Social proof (Cialdini). Authority bias. The bandwagon effect. We look to others' behavior to determine the correct course of action, especially under uncertainty.

**Template patterns:**
- "[Number] [audience type] already [action]. Here's why."
- "[Authority figure/company] uses this [product/strategy]. You should too."
- "We helped [X] clients [achieve result] in [timeframe]"
- "Rated [X] stars by [number] [audience]. Here's what they're saying..."
- "[Well-known company] switched to [product/approach]. Their results?"
- "The [product/method] that [impressive stat] people can't stop talking about"

For each hook, use the same template as Angle 1.

---

#### Angle 4: Contrarian/Controversial Hooks (3 minimum)

These hooks challenge conventional wisdom or say something the audience doesn't expect. They create a pattern interrupt — the brain flags unexpected information as important.

**Psychology:** The Von Restorff effect (isolation effect). Information that stands out from its surroundings is remembered better. Contrarian takes also trigger the brain's prediction error response, releasing dopamine and increasing attention.

**Template patterns:**
- "[Common advice] is actually killing your [metric]. Here's proof."
- "Unpopular opinion: [contrarian take about industry]"
- "Everything you've been told about [topic] is wrong."
- "I stopped [common practice] and [positive result] happened."
- "The [industry] lie nobody talks about"

For each hook, use the same template as Angle 1.

**Important:** Contrarian hooks must be defensible. Never make false claims. The contrarian take should challenge a genuine misconception or offer a legitimate alternative perspective.

---

#### Angle 5: Urgency/Scarcity Hooks (2 minimum)

These hooks create time pressure or exclusivity. They work best at the bottom of the funnel when the audience is already aware and considering.

**Psychology:** Scarcity principle (Cialdini) and loss aversion (Kahneman). The fear of missing out (FOMO) is a stronger motivator than the joy of gaining. Time-bound offers trigger the brain's urgency response, shortcutting deliberation.

**Template patterns:**
- "Last chance: [offer] ends [specific time]"
- "Only [number] spots left for [offer/program]"
- "[Offer] expires in [time]. Don't say I didn't warn you."
- "This [deal/opportunity] won't come back. Here's why."
- "We're closing [offer] to new [customers/members] on [date]"

For each hook, use the same template as Angle 1.

**Important:** Urgency hooks must be truthful. False scarcity destroys trust and violates platform policies. Only use when there is genuine scarcity or a real deadline.

### Step 3: Platform-Specific Formatting Guide

Include a comprehensive formatting reference:

```markdown
## Platform-Specific Hook Formatting

### Facebook/Instagram Feed Ads
- **Character guidance:** Keep hooks under 125 characters to display above the fold (before "See More")
- **Emoji usage:** 1-2 emojis max at the start or end — never in the middle of a sentence
- **Line breaks:** Use a line break after the hook to create visual separation
- **Hashtags:** 0 in ad copy (use in organic posts only, 3-5 max)
- **Format:** Text-first, then visual reinforcement

### TikTok / Instagram Reels
- **Delivery:** Hook must be spoken in the first 1.5 seconds AND shown as on-screen text
- **Text overlay:** Large, bold, centered text — 5-8 words max on screen
- **Emoji usage:** Sparingly in on-screen text, more in captions
- **Hashtags:** 3-5 in caption, include 1 trending hashtag
- **Format:** Video-first, text supports the visual

### Google Ads (Search)
- **Headline limit:** 30 characters per headline — hooks must be compressed
- **No emojis:** Google Ads does not allow emojis in ad copy
- **Keyword integration:** Include the target keyword naturally in the hook
- **Punctuation:** Use periods and exclamation points strategically (Google shows them)
- **Format:** Intent-matching — the hook must answer what they searched for

### LinkedIn
- **Tone:** Professional but human — avoid jargon, corporate-speak, and buzzwords
- **Emoji usage:** Minimal (0-1 per post) — overuse damages credibility
- **Hashtags:** 3-5 in Sponsored Content, placed at the end
- **Format:** Text hooks work best, followed by a supporting statistic
- **Line breaks:** Use frequently — LinkedIn's feed compresses long paragraphs

### YouTube Pre-Roll
- **Timing:** Hook must land in the first 5 seconds (before the skip button)
- **Delivery:** Both spoken (voiceover) and shown (on-screen text)
- **No emojis:** On-screen text should be clean and bold
- **Hashtags:** Not applicable
- **Format:** Open with the hook verbally, reinforce with on-screen text and a relevant visual

### Pinterest
- **Placement:** Hook goes in the Pin title (100 chars) and the first line of description
- **Emoji usage:** Moderate — Pinterest is more visual, emojis help text stand out
- **Hashtags:** 2-5 in description, relevant to search intent
- **Format:** Keyword-rich — Pinterest is a search engine, hooks should include searchable terms

### Email Subject Lines
- **Character guidance:** 40-60 characters for desktop, under 35 for mobile preview
- **Emoji usage:** 1 emoji at the start can increase open rates by 10-15%
- **Personalization:** Include [First Name] or [Company] where possible
- **Preview text:** 40-90 characters that complement (not repeat) the subject line
- **Format:** Create curiosity gap — never give away the answer in the subject line
```

### Step 4: Hook Performance Prediction

Rate each hook's expected performance:

```markdown
## Hook Performance Predictions

| # | Hook (shortened) | Angle | Expected CTR Impact | Confidence | Best Platform |
|---|---|---|---|---|---|
| P1 | [first 40 chars...] | Pain | High (+30-50%) | Medium | Meta |
| P2 | [first 40 chars...] | Pain | Medium (+15-30%) | High | Google |
| C1 | [first 40 chars...] | Curiosity | Very High (+50%+) | Medium | TikTok |
| [etc.] | | | | | |

**CTR Impact Rating:**
- Very High: Expected to outperform average hooks by 50%+
- High: Expected to outperform by 30-50%
- Medium: Expected to outperform by 15-30%
- Baseline: Expected to perform at industry average

**Confidence Rating:**
- High: Based on proven patterns and strong audience match
- Medium: Based on solid principles but needs testing
- Low: Experimental angle, high variance expected
```

### Step 5: Hook Testing Strategy

```markdown
## A/B Testing Strategy

### Phase 1: Angle Testing (Week 1-2)
Test one hook from each angle against each other:
- Ad Set A: [Best Pain hook]
- Ad Set B: [Best Curiosity hook]
- Ad Set C: [Best Social Proof hook]
- Ad Set D: [Best Contrarian hook]
- Budget: Equal split across all 4 ad sets
- Metric: CTR (click-through rate)
- Winner criteria: Highest CTR after 1,000 impressions per ad set

### Phase 2: Variation Testing (Week 3-4)
Take the winning angle and test A/B variations:
- Ad A: [Winning hook — Version A]
- Ad B: [Winning hook — Version B]
- Budget: 50/50 split
- Metric: CTR + conversion rate
- Winner criteria: Highest conversion rate after 500 clicks per ad

### Phase 3: Scaling (Week 5+)
Take the overall winner and:
- Scale budget by 20% every 3 days
- Create 3 new hooks in the winning angle
- Refresh creative every 2-3 weeks to avoid ad fatigue
- Monitor frequency — if above 3.0, rotate new hooks in
```

## Output Format

Save the complete output to `ADS-HOOKS.md` in the current working directory.

**File structure:**
```
# Scroll-Stopping Hooks: [Business Name]
> Generated [date] | Source: [URL]
> Total hooks: [count] | Angles covered: 5
> Top recommended hook: [Hook #] — [shortened text]

## Hook Foundation
[business and audience context]

## Pain/Problem Hooks (5)
[hooks P1 through P5 with full detail]

## Curiosity/Question Hooks (5)
[hooks C1 through C5 with full detail]

## Social Proof/Authority Hooks (5)
[hooks S1 through S5 with full detail]

## Contrarian/Controversial Hooks (3)
[hooks X1 through X3 with full detail]

## Urgency/Scarcity Hooks (2)
[hooks U1 through U2 with full detail]

## Platform-Specific Formatting Guide
[formatting reference]

## Hook Performance Predictions
[prediction table]

## A/B Testing Strategy
[testing plan]

## Quick-Reference Hook List
[numbered list of all hooks — just the text, no formatting, for easy scanning]

## Next Steps
1. Start with hooks [X, Y, Z] — highest predicted performance
2. Run `/ads copy <platform>` to build full ad copy around winning hooks
3. Run `/ads video <product>` to turn hooks into video ad scripts
4. Set up A/B tests following the Phase 1 plan above
5. Refresh hooks every 3-4 weeks to prevent creative fatigue
```

## Quality Checklist
Before delivering the output, verify:
- [ ] At least 20 hooks generated total
- [ ] Pain/Problem: at least 5 hooks
- [ ] Curiosity/Question: at least 5 hooks
- [ ] Social Proof/Authority: at least 5 hooks
- [ ] Contrarian/Controversial: at least 3 hooks
- [ ] Urgency/Scarcity: at least 2 hooks
- [ ] Every hook has an A/B variation
- [ ] Every hook has platform-specific usage guidance
- [ ] Every hook has a "why it works" psychology explanation
- [ ] Character counts are included for every hook
- [ ] Platform formatting guide is complete for all 7 channels
- [ ] Hook performance predictions are provided
- [ ] A/B testing strategy is actionable
- [ ] Quick-reference list is included at the end
- [ ] Hooks are specific to the business (not generic templates)
- [ ] No false claims in contrarian hooks
- [ ] No fake scarcity in urgency hooks
- [ ] Output is saved to ADS-HOOKS.md

## Hook Quality Standards

Every hook must pass these tests:
1. **The 3-second test:** Would this make someone stop mid-scroll? If you have to think about it, the hook isn't strong enough.
2. **The specificity test:** Does it include a specific number, timeframe, or detail? "Save money" fails. "Save $347/month" passes.
3. **The relevance test:** Does the target audience immediately see themselves in this hook? Generic hooks get generic results.
4. **The curiosity gap test:** Does it create an open loop the reader MUST close? If the hook gives away the answer, it's a headline, not a hook.
5. **The truth test:** Is every claim defensible? Hooks that overpromise destroy trust and get ads rejected.
6. **The platform test:** Does this hook fit the platform's culture? LinkedIn hooks that read like TikTok captions (and vice versa) will fail.
7. **The say-it-out-loud test:** For video hooks, read it aloud. If it's awkward to say, rewrite it. The best video hooks are conversational.
