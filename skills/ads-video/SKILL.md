---
name: Video Ad Script Writer
description: Generates complete video ad scripts for 15s, 30s, and 60s formats with shot-by-shot breakdowns, voiceover scripts, on-screen text, B-roll suggestions, music direction, storyboard outlines, and three proven video frameworks
---

# Video Ad Script Writer

## Skill Purpose
Generate complete, production-ready video ad scripts for three standard ad lengths: 15-second (TikTok/Reels/Bumper), 30-second (Pre-roll/Stories), and 60-second (YouTube/Facebook). Each script includes a shot-by-shot breakdown with exact timing, voiceover transcript, on-screen text overlays, B-roll suggestions, music/mood direction, and CTA placement. Scripts are written using three proven video ad frameworks and include a storyboard outline that a video editor or motion designer can follow without additional briefing.

## When to Use
- User runs `/ads video <product>`
- User asks for video ad scripts, video creative, or video content for ads
- Called as a subagent from `/ads strategy` (the main orchestrator)
- User needs scripts for TikTok ads, YouTube pre-roll, Instagram Reels, Facebook video ads, or Stories
- User wants to brief a video editor or freelancer on ad creative

## Input Requirements
- **Required:** Product or service to advertise (name, description, or URL)
- **Optional:** Target audience persona, brand guidelines, existing footage/assets, desired tone, specific platform focus, offer details

## How to Execute

### Step 1: Gather Product & Brand Context

If a URL is provided, fetch it using `WebFetch` and extract:
- Product/service name and description
- Key features and benefits
- Price point and offer structure
- Target audience indicators
- Brand tone and visual style
- Existing video content (YouTube channel, social media)
- Testimonials or case studies
- Competitor positioning

Run supplementary research:
```
WebSearch: "[Product/Brand]" video ad
WebSearch: "[Industry]" best video ad examples
WebSearch: "[Industry]" TikTok ad examples viral
WebSearch: "[Product category]" YouTube ad examples
```

Establish the video brief:

```markdown
## Video Brief

**Product/Service:** [Name]
**Business:** [Company name]
**What it does:** [1-sentence description]
**Who it's for:** [Target persona in 1 sentence]
**Core benefit:** [The #1 reason someone buys this]
**Key differentiator:** [What makes it different from alternatives]
**Price/Offer:** [Current pricing, discount, free trial]
**Desired action:** [What should the viewer DO after watching]
**Tone:** [Professional / Casual / Energetic / Bold / Warm / Edgy / Playful]
**Brand colors:** [Primary and secondary if known]
**Existing assets:** [Footage, product photos, testimonials available]
**Competitors to reference:** [Who they're competing against for attention]
```

### Step 2: Apply Three Video Ad Frameworks

Every script set uses all three frameworks. Each framework produces one version per ad length (15s, 30s, 60s) for a total of 9 scripts.

---

#### Framework 1: Hook-Demo-CTA

**Structure:**
- **Hook (first 20-30% of runtime):** Bold opening statement, shocking stat, or provocative question that stops the scroll
- **Demo (middle 50-60%):** Show the product in action. Prove the claim made in the hook. Use screen recordings, product shots, or demonstrations.
- **CTA (final 10-20%):** Clear call to action with urgency or incentive. On-screen text + verbal CTA.

**Best for:** SaaS demos, product showcases, tool walkthroughs, e-commerce product reveals
**Psychology:** The hook creates attention, the demo creates desire through proof, the CTA creates action through urgency.

---

#### Framework 2: Problem-Solution-Proof

**Structure:**
- **Problem (first 25-30%):** Show or describe the painful problem the audience faces. Make them feel the frustration.
- **Solution (middle 40-50%):** Introduce the product as the answer. Show how it specifically solves the problem stated.
- **Proof (final 20-30%):** Back it up. Testimonial clip, results screenshot, before/after, or stat. End with CTA.

**Best for:** Pain-driven products, service businesses, health/wellness, financial services, any product that solves a clear problem
**Psychology:** Pain activation (amygdala), then relief (dopamine release when solution is shown), then social validation (proof reduces risk).

---

#### Framework 3: UGC-Style Testimonial

**Structure:**
- **Personal hook (first 15-25%):** Person speaking directly to camera with a relatable statement: "I tried everything for [problem] and nothing worked until..."
- **Story/experience (middle 50-60%):** Tell the story of discovering and using the product. Show authentic, unpolished moments. Include specific details and results.
- **Recommendation + CTA (final 15-25%):** Genuine endorsement with specific reasons why. End with "Link in bio" or "Check it out" style CTA.

**Best for:** DTC brands, courses/coaching, beauty/wellness, apps, any product where social proof drives purchase
**Psychology:** Mirror neurons fire when watching someone like us share an experience. UGC-style content bypasses ad skepticism because it looks like organic content.

### Step 3: Write Scripts for Each Length

---

#### 15-Second Scripts (TikTok / Reels / Bumper Ads)

Constraints:
- Total runtime: 15 seconds
- Word count (voiceover): 30-40 words max
- On-screen text: 2-3 text cards max
- One single focused message — no room for multiple points
- Hook must land in first 1.5 seconds

For each of the 3 frameworks, produce a script in this format:

```markdown
### 15s Script [Number] — [Framework Name]

**Platform(s):** TikTok In-Feed, Instagram Reels, YouTube Bumper
**Aspect ratio:** 9:16 (vertical)
**Total runtime:** 15 seconds
**Word count:** [count] words

---

| Time | Visual / Shot | On-Screen Text | Voiceover / Audio | Music/SFX |
|---|---|---|---|---|
| 0:00-0:02 | [Shot description — camera angle, subject, action] | [Bold text overlay] | "[Spoken words]" | [Music mood: energetic opener / bass drop / trending sound] |
| 0:02-0:05 | [Shot description] | [Text overlay if any] | "[Spoken words]" | [Music continues / transitions] |
| 0:05-0:10 | [Shot description] | [Text overlay if any] | "[Spoken words]" | [Music mood] |
| 0:10-0:13 | [Shot description] | [Text overlay if any] | "[Spoken words]" | [Music builds] |
| 0:13-0:15 | [CTA shot — product shot, logo, URL] | [CTA text: "Shop Now" / "Link in bio" / "Try free"] | "[CTA spoken]" | [Music resolves / sting] |

**B-Roll suggestions:**
- [Suggestion 1 — specific, filmable scene]
- [Suggestion 2]
- [Suggestion 3]

**Storyboard outline:**
| Frame | Description | Notes |
|---|---|---|
| Frame 1 | [What the viewer sees — composition, subject, text position] | [Production note] |
| Frame 2 | [description] | [note] |
| Frame 3 | [description] | [note] |
| Frame 4 | [description — CTA frame] | [note] |

**Director's notes:**
- [Pacing note — fast cuts, slow reveal, etc.]
- [Tone note — energy level, facial expressions, urgency]
- [Platform-specific note — TikTok native feel vs. polished for YouTube]
```

---

#### 30-Second Scripts (Pre-Roll / Stories / Standard Social)

Constraints:
- Total runtime: 30 seconds
- Word count (voiceover): 65-80 words
- On-screen text: 4-6 text cards
- Hook must land in first 3 seconds
- For YouTube pre-roll: hook before the 5-second skip button
- Can include 1 testimonial quote or stat card

For each of the 3 frameworks, produce a script in this format:

```markdown
### 30s Script [Number] — [Framework Name]

**Platform(s):** YouTube Pre-Roll, Facebook Feed Video, Instagram Stories (multi-card)
**Aspect ratio:** 16:9 (landscape for YouTube) / 9:16 (vertical for Stories) / 1:1 (square for Feed)
**Total runtime:** 30 seconds
**Word count:** [count] words

---

| Time | Visual / Shot | On-Screen Text | Voiceover / Audio | Music/SFX |
|---|---|---|---|---|
| 0:00-0:03 | [Hook shot — must capture attention before skip] | [Bold hook text] | "[Hook line]" | [Attention-grabbing opener] |
| 0:03-0:07 | [Shot description] | [Text overlay] | "[Spoken words]" | [Music mood] |
| 0:07-0:12 | [Shot description — demo/problem visualization] | [Text overlay] | "[Spoken words]" | [Music transitions] |
| 0:12-0:18 | [Shot description — solution/product in action] | [Key benefit text] | "[Spoken words]" | [Music builds] |
| 0:18-0:24 | [Shot description — proof/testimonial/result] | [Proof text — stat or quote] | "[Spoken words]" | [Music continues] |
| 0:24-0:28 | [CTA shot — product, offer, urgency element] | [Offer/CTA text] | "[CTA spoken]" | [Music resolves] |
| 0:28-0:30 | [End card — logo, URL, CTA button] | [Brand + CTA] | "[Final line]" | [Music sting / outro] |

**B-Roll suggestions:**
- [Suggestion 1 — specific, filmable scene]
- [Suggestion 2]
- [Suggestion 3]
- [Suggestion 4]
- [Suggestion 5]

**Storyboard outline:**
| Frame | Time | Description | Camera | Text Position |
|---|---|---|---|---|
| Frame 1 | 0:00-0:03 | [description] | [angle/movement] | [where text appears] |
| Frame 2 | 0:03-0:07 | [description] | [angle] | [text position] |
| Frame 3 | 0:07-0:12 | [description] | [angle] | [text position] |
| Frame 4 | 0:12-0:18 | [description] | [angle] | [text position] |
| Frame 5 | 0:18-0:24 | [description] | [angle] | [text position] |
| Frame 6 | 0:24-0:30 | [CTA card] | [static/zoom] | [centered] |

**Director's notes:**
- [Pacing and energy direction]
- [Transition style between shots — cut, dissolve, swipe, zoom]
- [Color grading / visual mood direction]
- [Audio mixing notes — music vs. voiceover balance]
```

---

#### 60-Second Scripts (YouTube / Facebook / Long-Form Social)

Constraints:
- Total runtime: 60 seconds
- Word count (voiceover): 130-160 words
- On-screen text: 6-10 text cards
- Full narrative arc — beginning, middle, end
- Room for 1-2 testimonial clips, multiple product shots, and a strong CTA sequence
- Hook must still land in first 3 seconds

For each of the 3 frameworks, produce a script in this format:

```markdown
### 60s Script [Number] — [Framework Name]

**Platform(s):** YouTube In-Stream, Facebook Feed Video, LinkedIn Video
**Aspect ratio:** 16:9 (primary), adaptable to 9:16 and 1:1
**Total runtime:** 60 seconds
**Word count:** [count] words

---

| Time | Visual / Shot | On-Screen Text | Voiceover / Audio | Music/SFX |
|---|---|---|---|---|
| 0:00-0:03 | [Hook shot] | [Hook text] | "[Hook line]" | [Attention opener] |
| 0:03-0:08 | [Context/problem setup] | [Supporting text] | "[Lines]" | [Music mood] |
| 0:08-0:15 | [Problem deepens / agitate] | [Pain point text] | "[Lines]" | [Music tension builds] |
| 0:15-0:22 | [Solution introduction] | [Product/brand reveal text] | "[Lines]" | [Music shift — hopeful] |
| 0:22-0:32 | [Demo / how it works / key features] | [Feature/benefit callouts] | "[Lines]" | [Music upbeat] |
| 0:32-0:42 | [Proof — testimonial, results, case study] | [Proof stat or quote] | "[Lines]" | [Music maintains] |
| 0:42-0:50 | [Additional benefit or second proof point] | [Secondary benefit text] | "[Lines]" | [Music builds to climax] |
| 0:50-0:55 | [CTA — offer reveal, urgency] | [Offer text + CTA] | "[CTA spoken]" | [Music peaks] |
| 0:55-0:60 | [End card — logo, URL, tagline] | [Brand + final CTA] | "[Closing line]" | [Music resolves] |

**B-Roll suggestions:**
- [Suggestion 1 — opening establishing shot]
- [Suggestion 2 — problem visualization]
- [Suggestion 3 — product detail shots]
- [Suggestion 4 — customer reaction / testimonial setting]
- [Suggestion 5 — lifestyle / aspirational imagery]
- [Suggestion 6 — CTA / urgency visual]

**Storyboard outline:**
| Frame | Time | Description | Camera | Text Position | Transition |
|---|---|---|---|---|---|
| Frame 1 | 0:00-0:03 | [description] | [angle] | [position] | [cut/dissolve] |
| Frame 2 | 0:03-0:08 | [description] | [angle] | [position] | [transition] |
| Frame 3 | 0:08-0:15 | [description] | [angle] | [position] | [transition] |
| Frame 4 | 0:15-0:22 | [description] | [angle] | [position] | [transition] |
| Frame 5 | 0:22-0:32 | [description] | [angle] | [position] | [transition] |
| Frame 6 | 0:32-0:42 | [description] | [angle] | [position] | [transition] |
| Frame 7 | 0:42-0:50 | [description] | [angle] | [position] | [transition] |
| Frame 8 | 0:50-0:60 | [CTA + end card] | [static] | [centered] | [fade] |

**Director's notes:**
- [Overall narrative arc and emotional journey]
- [Pacing: where to speed up, where to breathe]
- [Talent direction — who's on camera, what energy]
- [Color grading and visual style]
- [Audio: music genre, tempo, voiceover tone]
- [Adaptation notes for vertical (9:16) version]
```

### Step 4: Platform-Specific Adaptation Notes

```markdown
## Platform Adaptation Guide

### TikTok Adaptation
- Film in 9:16 vertical
- Use trending sounds when possible (search TikTok Creative Center for trending audio)
- First frame must have text + movement — static opens get swiped
- UGC-style (iPhone quality) outperforms polished production 3:1
- Add captions — 80% of TikTok is watched with sound off
- End with a question or controversial take to drive comments (algorithm fuel)

### Instagram Reels Adaptation
- 9:16 vertical, keep safe zones in mind (bottom 20% covered by UI)
- Instagram favors original audio over repurposed TikTok audio
- Carousel ads (static) outperform Reels for some B2B — test both
- Stories ads: use native sticker/text styles for authenticity
- Use the "Remind Me" CTA for event/launch campaigns

### YouTube Adaptation
- 16:9 landscape is primary format
- Hook must land before the 5-second skip button on pre-roll
- Bumper ads (6s): distill the 15s script to one single message
- Add end screens and cards pointing to landing page or next video
- Consider running both skippable and non-skippable to compare CPV

### Facebook Adaptation
- Square (1:1) outperforms landscape in Facebook Feed
- Add captions (SRT file) — 85% of Facebook video is watched muted
- Facebook rewards longer watch time — 60s scripts can run well if engaging
- Carousel video ads: cut the 60s into 3-4 cards
- In-stream ads: viewers cannot skip, so lead with value not hype

### LinkedIn Adaptation
- Keep it professional but not stiff — authority + relatability
- Product demos and case study videos outperform lifestyle content
- Optimal length: 15-30 seconds for awareness, 30-60 for consideration
- Native video (uploaded directly) gets 5x more reach than YouTube links
- Include subtitles — autoplay is muted in LinkedIn feed
```

### Step 5: Production Checklist

```markdown
## Production Checklist

### Pre-Production
- [ ] Script approved by stakeholder
- [ ] Talent/spokesperson confirmed (or self-shot UGC)
- [ ] Product samples/screenshots ready for demo shots
- [ ] B-roll shot list printed and shared with videographer
- [ ] Music tracks selected and licensed (check ad usage rights)
- [ ] On-screen text formatted and ready for editor
- [ ] Brand assets (logo, colors, fonts) packaged for editor

### Production
- [ ] Film in 9:16 AND 16:9 (or film wide and crop)
- [ ] Capture 3x more footage than needed (gives editor options)
- [ ] Film multiple takes of the hook — this is the most important shot
- [ ] Get at least 2 testimonial clips (even if only 1 makes the cut)
- [ ] Capture product close-ups from multiple angles
- [ ] Record clean voiceover audio separately from on-camera audio

### Post-Production
- [ ] Edit to exact timings in the script
- [ ] Add captions/subtitles (SRT or burned-in)
- [ ] Export in all required aspect ratios (16:9, 9:16, 1:1)
- [ ] Color grade to match brand palette
- [ ] Add end card with CTA, logo, and URL
- [ ] Deliver final files in platform-specific specs (resolution, codec, file size)
```

## Output Format

Save the complete output to `ADS-VIDEO-SCRIPTS.md` in the current working directory.

**File structure:**
```
# Video Ad Scripts: [Product/Business Name]
> Generated [date] | Source: [URL/product info]
> Scripts: 9 total (3 frameworks x 3 lengths)
> Frameworks: Hook-Demo-CTA, Problem-Solution-Proof, UGC-Style Testimonial

## Video Brief
[product and brand context]

## 15-Second Scripts
### 15s Script 1 — Hook-Demo-CTA
### 15s Script 2 — Problem-Solution-Proof
### 15s Script 3 — UGC-Style Testimonial

## 30-Second Scripts
### 30s Script 1 — Hook-Demo-CTA
### 30s Script 2 — Problem-Solution-Proof
### 30s Script 3 — UGC-Style Testimonial

## 60-Second Scripts
### 60s Script 1 — Hook-Demo-CTA
### 60s Script 2 — Problem-Solution-Proof
### 60s Script 3 — UGC-Style Testimonial

## Platform Adaptation Guide
[platform-specific notes]

## Production Checklist
[pre/production/post checklists]

## Next Steps
1. Share scripts with video editor / filmmaker
2. Film the top-priority script first: [recommendation]
3. Run `/ads hooks` to generate alternative hook options
4. Run `/ads copy <platform>` for companion text ads
5. Test 15s versions first (cheapest to produce), scale winning framework to 30s and 60s
```

## Quality Checklist
Before delivering the output, verify:
- [ ] 9 scripts total (3 frameworks x 3 lengths)
- [ ] Every script has shot-by-shot timing breakdown
- [ ] Voiceover word counts are within limits (15s: 30-40, 30s: 65-80, 60s: 130-160)
- [ ] On-screen text overlays are specified for every shot
- [ ] B-roll suggestions are specific and filmable
- [ ] Music/mood direction is provided for each script
- [ ] Storyboard outlines are included for every script
- [ ] CTA is clear and placed correctly in every script
- [ ] 15s hooks land in the first 1.5 seconds
- [ ] 30s hooks land before the 5-second skip button
- [ ] Platform adaptation guide covers all major platforms
- [ ] Production checklist is complete
- [ ] Scripts are specific to the product (not generic templates)
- [ ] Output is saved to ADS-VIDEO-SCRIPTS.md
