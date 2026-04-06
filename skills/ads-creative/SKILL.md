---
name: ads-creative
description: Creative Brief Generator for designers, video editors, and content teams
version: 1.0.0
author: AI Ads Strategist
tags: [ads, creative, briefs, design, video, ugc]
trigger: /ads creative
output: ADS-CREATIVE-BRIEF.md
---

# Creative Brief Generator

## Skill Purpose
Generate comprehensive, production-ready creative briefs for designers, video editors, and content creators. Each brief includes visual concept descriptions, text overlay copy, format specifications, aspect ratios per platform, color palette suggestions, mood/tone direction, reference descriptions, shot lists for video, and thumbnail/cover image direction. Produces briefs for 5 ad formats: Static Image, Carousel, Short Video (15s), Long Video (60s), and UGC-Style.

## When to Use
- User needs creative direction for ad campaigns
- User wants to brief a designer, video editor, or UGC creator
- User asks for "creative briefs", "ad concepts", "design direction", or "video scripts"
- User wants platform-specific creative specs
- Triggered by `/ads creative <product/service>` or `/ads creative <url>`

## How to Execute

### Step 1: Gather Business Context

If the user provides a URL, fetch it to understand the business:

```
WebFetch(url) -> Extract:
- Business name and industry
- Product/service offering
- Brand colors (from website CSS/design)
- Brand voice and tone (from copy style)
- Target audience signals
- Existing imagery style
- Key value propositions
- Pricing information
- Testimonials or social proof
```

If no URL is provided, ask the user for:
1. Product/service name and description
2. Target audience
3. Key selling points (top 3)
4. Brand colors (hex codes if available)
5. Competitors to differentiate from

### Step 2: Define Brand Visual Identity

Extract or establish the visual identity foundation:

**Color Palette Analysis:**
| Element | Value | Usage |
|---------|-------|-------|
| Primary Color | #XXXXXX | Headlines, CTAs, key elements |
| Secondary Color | #XXXXXX | Accents, supporting elements |
| Background Color | #XXXXXX | Backgrounds, negative space |
| Text Color | #XXXXXX | Body copy, descriptions |
| Accent Color | #XXXXXX | Highlights, urgency elements |

**If no brand colors are available**, recommend a palette based on industry:
- **SaaS/Tech**: Blues, purples, clean whites (#2563EB, #7C3AED, #F8FAFC)
- **E-commerce/Retail**: Bold oranges, blacks, whites (#F97316, #18181B, #FFFFFF)
- **Health/Wellness**: Greens, earth tones, soft whites (#059669, #92400E, #FFF7ED)
- **Finance/Legal**: Navy, gold, charcoal (#1E3A5F, #D4A843, #374151)
- **Food/Restaurant**: Warm reds, yellows, cream (#DC2626, #EAB308, #FFFBEB)
- **Local Services**: Trust blues, professional grays (#1D4ED8, #6B7280, #F3F4F6)
- **Creator/Education**: Vibrant purples, pinks, energetic (#8B5CF6, #EC4899, #F0ABFC)

**Typography Direction:**
| Element | Style | Notes |
|---------|-------|-------|
| Headlines | Bold sans-serif | Maximum impact, 3-7 words |
| Subheadlines | Medium weight | Supporting context |
| Body Copy | Regular weight | Readable at small sizes |
| CTA Text | Bold, contrasting | Action-oriented, urgent |

### Step 3: Define Core Messaging Framework

Before generating briefs, establish the messaging pillars:

**Primary Message:** The single most compelling thing about this product/service (1 sentence)

**Supporting Messages:**
1. Pain point agitation (what problem does this solve?)
2. Unique mechanism (how does it work differently?)
3. Social proof (who else trusts this?)
4. Urgency/scarcity (why act now?)
5. Risk reversal (what if it doesn't work?)

**Headline Formulas to Use Across Briefs:**
- "[Pain Point]? [Solution] in [Timeframe]"
- "Stop [Common Mistake]. Start [Better Way]."
- "[Number] [audience] already [result]. You're next."
- "What if [dream outcome] was actually [easy/affordable/possible]?"
- "[Authority figure] recommends this [product type]. Here's why."

### Step 4: Platform Specifications Reference

Use these specs for all briefs:

**Meta (Facebook/Instagram):**
| Format | Aspect Ratio | Dimensions | Max File Size | Max Duration |
|--------|-------------|------------|---------------|--------------|
| Feed Image | 1:1 | 1080x1080 | 30 MB | N/A |
| Feed Video | 1:1 or 4:5 | 1080x1080 or 1080x1350 | 4 GB | 240 min |
| Stories/Reels | 9:16 | 1080x1920 | 4 GB | 90s (Reels) |
| Carousel | 1:1 | 1080x1080 | 30 MB/card | N/A |

**Google Ads:**
| Format | Aspect Ratio | Dimensions | Notes |
|--------|-------------|------------|-------|
| Display | Various | 300x250, 728x90, 160x600 | Responsive preferred |
| YouTube Pre-roll | 16:9 | 1920x1080 | 6s, 15s, or 30s |
| Discovery | 1.91:1 or 1:1 | 1200x628 or 1200x1200 | Landscape or square |

**TikTok:**
| Format | Aspect Ratio | Dimensions | Duration |
|--------|-------------|------------|----------|
| In-Feed | 9:16 | 1080x1920 | 5-60s (15s optimal) |
| Spark Ads | 9:16 | 1080x1920 | Organic post boosted |

**LinkedIn:**
| Format | Aspect Ratio | Dimensions | Notes |
|--------|-------------|------------|-------|
| Single Image | 1.91:1 | 1200x627 | Professional tone |
| Video | 1:1 or 16:9 | 1080x1080 or 1920x1080 | 15s-30s optimal |
| Carousel | 1:1 | 1080x1080 | 2-10 cards |

**Pinterest:**
| Format | Aspect Ratio | Dimensions | Notes |
|--------|-------------|------------|-------|
| Standard Pin | 2:3 | 1000x1500 | Vertical preferred |
| Video Pin | 2:3 or 9:16 | 1000x1500 | 6-15s optimal |

### Step 5: Generate Creative Briefs

Produce 5 complete briefs, one for each ad format:

---

#### BRIEF 1: Static Image Ad

**Objective:** Stop the scroll with a single compelling image and headline.

**Deliverables:**
- 3 concept variations (A/B/C testing)
- Each concept in 3 sizes: 1:1 (feed), 4:5 (feed optimized), 9:16 (stories)

**For Each Concept, Specify:**

1. **Visual Concept Description**
   - Scene/setting description (be specific: "overhead flat-lay of product on marble countertop with morning light from left" not "product photo")
   - Subject positioning and framing
   - Lighting direction and mood
   - Background treatment (solid color, gradient, lifestyle, texture)
   - Props or supporting elements

2. **Text Overlay Layout**
   - Headline text (max 7 words, positioned top or center)
   - Subheadline text (max 15 words, positioned below headline)
   - CTA button text and placement (bottom third)
   - Text safe zones (keep text within 80% of frame)

3. **Color Application**
   - Background color with hex code
   - Text color with hex code
   - CTA button color with hex code
   - Overlay opacity if applicable

4. **Mood/Tone Direction**
   - Emotional tone (aspirational, urgent, calming, bold, playful)
   - Energy level (high energy, medium, contemplative)
   - Style reference description (describe a reference aesthetic without naming specific ads)

**Concept A:** Problem-focused (show the pain point)
**Concept B:** Solution-focused (show the result/outcome)
**Concept C:** Social proof-focused (show credibility/results)

---

#### BRIEF 2: Carousel Ad (3-5 Slides)

**Objective:** Tell a sequential story that builds curiosity slide by slide.

**Deliverables:**
- 1 primary carousel concept with 5 slides
- 1 alternate carousel concept with 3 slides (shorter version)
- Format: 1:1 (1080x1080) for Meta, 1:1 for LinkedIn

**Carousel Architecture:**

| Slide | Purpose | Content Direction |
|-------|---------|-------------------|
| Slide 1 | Hook/Pattern Interrupt | Bold question or shocking statement. NO product yet. Make them swipe. |
| Slide 2 | Problem Agitation | Expand on the pain. Show consequences of inaction. Data point if available. |
| Slide 3 | Solution Reveal | Introduce the product/service. Show the mechanism. |
| Slide 4 | Proof/Results | Testimonial, case study, before/after, or data. |
| Slide 5 | CTA | Clear call to action. Urgency element. Link or next step. |

**For Each Slide, Specify:**
1. Visual concept (what the image shows)
2. Text overlay (headline + supporting text)
3. Design continuity elements (consistent visual thread across slides)
4. Swipe motivation (why they'll swipe to the next slide)

**Design Continuity Rules:**
- Consistent color scheme across all slides
- Same font family throughout
- Visual element that carries across slides (progress bar, recurring icon, color band)
- Each slide should be comprehensible standalone but better in sequence

---

#### BRIEF 3: Short Video Ad (15 Seconds)

**Objective:** Deliver a complete message in 15 seconds with a strong hook in the first 3 seconds.

**Deliverables:**
- 2 concept variations
- Format: 9:16 (vertical) for Meta Stories/Reels, TikTok; 1:1 (square) for feed
- Captions/subtitles required (85% of social video is watched muted)

**Shot List Template:**

| Timestamp | Duration | Shot Type | Visual | Audio/VO | Text Overlay |
|-----------|----------|-----------|--------|----------|--------------|
| 0:00-0:03 | 3s | Close-up / Pattern interrupt | [Describe exact visual] | [Hook line] | [Bold text overlay] |
| 0:03-0:06 | 3s | Medium / Problem setup | [Describe visual] | [Problem statement] | [Supporting text] |
| 0:06-0:10 | 4s | Wide or Product reveal | [Describe visual] | [Solution intro] | [Product name/benefit] |
| 0:10-0:13 | 3s | Demo or Proof | [Describe visual] | [Evidence/result] | [Data point or testimonial] |
| 0:13-0:15 | 2s | CTA / End card | [Logo + CTA] | [Call to action] | [CTA text + URL] |

**First 3 Seconds (Critical):**
- Must include a visual or verbal hook that creates curiosity
- Options: bold text animation, surprising visual, direct question, controversial statement
- NO logos or brand intros in the first 3 seconds

**Audio Direction:**
- Background music mood (upbeat, dramatic, chill, trending sound)
- Voiceover tone (conversational, authoritative, excited, calm)
- Sound effects cues (whoosh for transitions, ding for reveals)

**Thumbnail/Cover Frame:**
- Which frame to use as thumbnail (typically the hook frame)
- Text overlay for thumbnail (different from first frame)
- Must be compelling enough to click when video is paused

---

#### BRIEF 4: Long Video Ad (60 Seconds)

**Objective:** Build a complete narrative arc: hook, problem, solution, proof, CTA.

**Deliverables:**
- 1 primary concept
- Format: 9:16 and 16:9 versions
- Full script with visual directions

**Narrative Structure:**

| Act | Timestamp | Duration | Purpose | Emotional Arc |
|-----|-----------|----------|---------|---------------|
| Hook | 0:00-0:05 | 5s | Pattern interrupt, question, or bold claim | Curiosity |
| Problem | 0:05-0:15 | 10s | Agitate the pain point, show consequences | Frustration/Fear |
| Bridge | 0:15-0:20 | 5s | Transition from problem to solution | Hope |
| Solution | 0:20-0:35 | 15s | Product demo, mechanism explanation | Interest/Excitement |
| Proof | 0:35-0:50 | 15s | Testimonials, results, data, before/after | Trust/Desire |
| CTA | 0:50-0:60 | 10s | Offer, urgency, clear next step | Urgency/Action |

**Detailed Shot List:**

For each segment, specify:
1. Camera angle and movement (static, pan, zoom, tracking)
2. Subject and framing
3. Lighting (natural, studio, dramatic, soft)
4. Location/set description
5. Props and wardrobe notes
6. Transition type to next shot (cut, fade, swipe, zoom)

**Script Format:**
```
[TIMESTAMP] [SHOT TYPE]
VISUAL: [What the viewer sees]
VO/DIALOGUE: "[What is said]"
TEXT ON SCREEN: "[Overlay text]"
SFX: [Sound effects]
MUSIC: [Music direction]
```

**B-Roll Shot List:**
- 5-8 B-roll shots to supplement the main narrative
- Product close-ups, lifestyle moments, results visuals
- Each B-roll shot: description, duration, where it fits in the edit

---

#### BRIEF 5: UGC-Style Ad

**Objective:** Create authentic, native-looking content that feels like an organic post, not an ad.

**Deliverables:**
- 3 UGC concept variations
- Format: 9:16 (vertical) for TikTok, Reels, Stories
- Raw/authentic aesthetic (NOT polished studio quality)

**UGC Format Options:**

**Format A: Testimonial/Review Style**
- Creator speaks directly to camera
- "I just found this [product] and..."
- Before/after or demonstration
- Authentic reaction shots

**Format B: Day-in-the-Life Integration**
- Product appears naturally in daily routine
- "POV: You finally found [solution to problem]"
- Trending format adaptation
- Lifestyle context

**Format C: Problem-Solution Tutorial**
- "If you're struggling with [problem], try this..."
- Step-by-step demonstration
- Educational value first, product plug second
- Save-worthy content

**For Each UGC Concept, Specify:**

1. **Creator Profile**
   - Ideal creator demographic (age, gender, style)
   - Tone of voice (excited, casual, skeptical-turned-believer, expert)
   - Setting (home, office, outdoors, car — keep it authentic)

2. **Script/Talking Points** (NOT word-for-word — UGC should feel unscripted)
   - Opening hook (first 2 seconds)
   - Key points to hit (3-4 bullet points)
   - Product mention/reveal moment
   - Closing CTA (subtle, not salesy)

3. **Production Notes**
   - Shot on phone (front-facing camera preferred)
   - Natural lighting only
   - No professional editing — use native app transitions
   - Captions in platform-native style (not fancy graphic captions)
   - Trending audio suggestions (describe the type, not specific songs)

4. **Authenticity Checklist**
   - [ ] Looks like it could be a real post
   - [ ] No corporate language or jargon
   - [ ] Imperfect framing is okay (adds authenticity)
   - [ ] Real reaction/emotion visible
   - [ ] Would blend into a normal feed without standing out as "ad"

### Step 6: Cross-Platform Adaptation Matrix

After generating all 5 briefs, provide an adaptation matrix:

| Brief | Meta Feed | Meta Stories | TikTok | YouTube | LinkedIn | Pinterest | Google Display |
|-------|-----------|-------------|--------|---------|----------|-----------|---------------|
| Static Image | 1:1 | 9:16 | N/A | N/A | 1.91:1 | 2:3 | Responsive |
| Carousel | 1:1 (5 slides) | 9:16 (5 slides) | N/A | N/A | 1:1 (5 slides) | N/A | N/A |
| Short Video 15s | 4:5 | 9:16 | 9:16 | 16:9 (bumper) | 1:1 | 9:16 | N/A |
| Long Video 60s | 4:5 | N/A | 9:16 | 16:9 | 16:9 | N/A | N/A |
| UGC-Style | 4:5 | 9:16 | 9:16 | N/A | N/A | N/A | N/A |

### Step 7: Production Checklist

Include a final production checklist in the output:

**Pre-Production:**
- [ ] Brand colors confirmed (hex codes)
- [ ] Logo files obtained (PNG with transparency)
- [ ] Product photography/video assets available
- [ ] Testimonials/reviews selected for social proof
- [ ] Landing page URL confirmed for CTA
- [ ] UTM parameters defined for tracking

**Production:**
- [ ] Static images designed in all required sizes
- [ ] Carousel slides designed with consistent visual thread
- [ ] Video scripts approved before shooting
- [ ] UGC creator briefed and contracted
- [ ] All text overlays checked for readability at mobile size

**Post-Production:**
- [ ] All files exported in correct dimensions and formats
- [ ] Captions/subtitles added to all video content
- [ ] Thumbnail/cover images selected for each video
- [ ] A/B variations labeled clearly (Concept A, B, C)
- [ ] Files organized by platform and format

## Output Format

Save the complete brief as `ADS-CREATIVE-BRIEF.md` in the current working directory.

Structure the output file as:

```markdown
# Creative Brief: [Business/Product Name]
Generated: [Date]

## Brand Visual Identity
[Color palette, typography, mood board direction]

## Core Messaging Framework
[Primary message, supporting messages, headline formulas]

---

## Brief 1: Static Image Ad
[Complete brief with 3 concept variations]

## Brief 2: Carousel Ad (3-5 Slides)
[Complete brief with slide-by-slide direction]

## Brief 3: Short Video Ad (15 Seconds)
[Complete brief with shot list and script]

## Brief 4: Long Video Ad (60 Seconds)
[Complete brief with detailed shot list and full script]

## Brief 5: UGC-Style Ad
[Complete brief with 3 UGC concept variations]

---

## Cross-Platform Adaptation Matrix
[Adaptation table]

## Production Checklist
[Pre-production, production, post-production checklists]

## Next Steps
1. Review and approve creative concepts
2. Brief designers/editors with this document
3. Produce A/B test variations first
4. Launch with `/ads copy <platform>` for matching ad copy
5. Track performance with `/ads audit` after 7 days
```

## Important Rules
- Every visual description must be specific enough for a designer to execute without guessing
- Text overlays must respect mobile readability (minimum apparent font size guidance)
- Always provide A/B/C variations for testing, never a single concept
- UGC briefs should feel authentic, not scripted — provide talking points, not scripts
- Include platform-specific specs for every deliverable
- Color recommendations must include hex codes
- Shot lists must include timestamps, not vague durations
- Carousel slides must each have a reason for the viewer to swipe to the next
- Video hooks must be in the first 3 seconds — no exceptions
- All briefs should connect back to the core messaging framework
- CTA placement should always be in the bottom third of the frame for mobile
- Never assume the viewer has sound on — all video content needs text overlays/captions
