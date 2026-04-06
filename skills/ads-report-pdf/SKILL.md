---
name: ads-report-pdf
description: Professional PDF Ad Strategy Report Generator
version: 1.0.0
author: AI Ads Strategist
tags: [ads, pdf, report, strategy, client-ready]
trigger: /ads report-pdf
output: ADS-STRATEGY-REPORT.pdf
---

# PDF Ad Strategy Report Generator

## Skill Purpose
Generate a polished, client-ready PDF advertising strategy report using the ReportLab Python library. This skill scans the current working directory for all ads output files, extracts scores, audience personas, campaign structure, budget allocation, and competitive intelligence, compiles them into structured JSON, and produces a professional PDF with a cover page featuring an Ad Readiness Score gauge, audience persona cards, campaign funnel diagram, budget allocation chart, competitive positioning map, creative direction summary, and a prioritized 90-day action plan.

## When to Use
- User wants a PDF version of the ad strategy report (not just Markdown)
- User is preparing a deliverable for a client or stakeholder presentation
- User asks for a "polished report", "client-ready report", or "PDF report"
- User wants a visual report with charts, scores, and professional formatting
- Triggered by `/ads report-pdf` or `/ads report-pdf <business name>`

## When to Use PDF vs Markdown

| Format | Best For | Pros | Cons |
|--------|---------|------|------|
| **PDF** | Client presentations, email attachments, proposals, sales collateral | Professional appearance, charts and gauges, printable, consistent formatting | Requires Python script, harder to edit |
| **Markdown** | Internal use, quick reference, iterative editing, version control | Easy to edit, fast to generate, git-friendly | Less visually polished, no charts |

**Rule of thumb:** If the report goes to a client, prospect, or executive, use PDF. If it is for internal use or further editing, use Markdown.

## How to Execute

### Step 1: Check for PDF Generation Script

First, check if the dedicated PDF generation script exists:

```bash
ls ~/.claude/skills/ads/scripts/generate_ads_pdf.py 2>/dev/null
```

**If the script exists:** Use it directly (skip to Step 4).
**If the script does not exist:** Generate the PDF inline using ReportLab (follow all steps).

### Step 2: Collect All Available Data

Scan the current working directory for all ads skill outputs. Search for these files:

**Primary data sources (search for all of these):**
- `ADS-STRATEGY-*.md` — Full strategy report (composite scores, all sections)
- `ADS-AUDIENCE*.md` — Audience personas, targeting parameters
- `ADS-COPY-*.md` — Platform-specific ad copy
- `ADS-HOOKS*.md` — Scroll-stopping hooks
- `ADS-CREATIVE-BRIEF*.md` — Creative briefs for all formats
- `ADS-VIDEO-SCRIPTS*.md` — Video ad scripts
- `ADS-FUNNEL*.md` — Campaign funnel architecture
- `ADS-BUDGET*.md` — Budget allocation plan
- `ADS-COMPETITORS*.md` — Competitive intelligence
- `ADS-KEYWORDS*.md` — Keyword strategy (Google Ads)
- `ADS-TESTING-PLAN*.md` — A/B testing plan
- `ADS-LANDING*.md` — Landing page audit
- `ADS-AUDIT*.md` — Performance audit results

**Search command:**
```bash
ls ADS-*.md 2>/dev/null
```

**For each file found**, extract:
- Scores and ratings
- Key findings and recommendations
- Audience personas and segments
- Campaign structure details
- Budget allocations and projections
- Competitive positioning data
- Top ad copy and hooks
- Action items and timelines

### Step 3: Structure the JSON Data

Compile all extracted data into a structured JSON object for the PDF generator:

```json
{
  "report_metadata": {
    "business_name": "[Business Name]",
    "website_url": "[URL]",
    "industry": "[Industry]",
    "report_date": "[YYYY-MM-DD]",
    "generated_by": "AI Ads Strategist"
  },
  "ad_readiness_score": {
    "composite_score": 0,
    "audience_clarity": {"score": 0, "weight": 25, "findings": []},
    "creative_quality": {"score": 0, "weight": 20, "findings": []},
    "funnel_architecture": {"score": 0, "weight": 20, "findings": []},
    "competitive_position": {"score": 0, "weight": 15, "findings": []},
    "budget_efficiency": {"score": 0, "weight": 20, "findings": []}
  },
  "audience_personas": [
    {
      "name": "[Persona Name]",
      "age_range": "[Age Range]",
      "role_title": "[Role/Title]",
      "pain_points": [],
      "motivations": [],
      "platforms": [],
      "targeting_params": {}
    }
  ],
  "campaign_structure": {
    "funnel_stages": [],
    "campaigns": [],
    "retargeting_flows": []
  },
  "budget_allocation": {
    "total_monthly_budget": 0,
    "platform_split": {},
    "funnel_stage_split": {},
    "projected_metrics": {
      "estimated_impressions": 0,
      "estimated_clicks": 0,
      "estimated_conversions": 0,
      "projected_cpa": 0,
      "projected_roas": 0
    }
  },
  "competitive_intelligence": {
    "competitors_analyzed": [],
    "positioning_gaps": [],
    "messaging_opportunities": []
  },
  "top_ad_copy": {
    "best_hooks": [],
    "top_headlines": [],
    "best_ctas": []
  },
  "action_plan": {
    "week_1": [],
    "week_2_4": [],
    "month_2_3": []
  },
  "critical_findings": [],
  "quick_wins": []
}
```

### Step 4: Generate the PDF

Run the PDF generation script with the compiled JSON data:

```bash
python3 ~/.claude/skills/ads/scripts/generate_ads_pdf.py
```

If the script does not exist, generate it inline. The script must produce a PDF with these sections:

#### PDF Structure and Pages

**Page 1: Cover Page**
- Report title: "Advertising Strategy Report"
- Business name and logo placeholder
- Website URL
- Report date
- "Prepared by AI Ads Strategist"
- Ad Readiness Score gauge (large, centered) — color-coded:
  - 80-100: Green (#059669)
  - 60-79: Blue (#2563EB)
  - 40-59: Yellow (#D97706)
  - 20-39: Orange (#EA580C)
  - 0-19: Red (#DC2626)

**Page 2: Executive Summary**
- Ad Readiness Score breakdown (5 categories with individual scores)
- Horizontal bar chart showing each category score vs maximum
- 3 critical findings (bulleted, bold)
- 3 quick wins (bulleted, with estimated impact)
- Overall verdict statement

**Page 3: Audience Analysis**
- Audience Clarity Score: X/100
- Persona cards (2-3 personas), each containing:
  - Persona name and demographic summary
  - Top 3 pain points
  - Top 3 motivations
  - Preferred platforms
  - Targeting parameters summary
- Platform presence chart (bar chart by platform)

**Page 4: Creative Direction**
- Creative Quality Score: X/100
- Top 5 hooks with platform recommendations
- Best headline/copy examples (3-5)
- Creative format recommendations table
- A/B testing priorities

**Page 5: Campaign Architecture**
- Funnel Architecture Score: X/100
- Funnel diagram (visual flow):
  ```
  AWARENESS → CONSIDERATION → CONVERSION → RETENTION
  [Campaign]    [Campaign]     [Campaign]    [Campaign]
  [Budget %]    [Budget %]     [Budget %]    [Budget %]
  ```
- Campaign structure table (campaign name, objective, audience, platform)
- Retargeting flow description

**Page 6: Competitive Positioning**
- Competitive Position Score: X/100
- Competitor comparison table (name, estimated spend, key message, gap)
- Positioning opportunities (bulleted)
- Messaging differentiation recommendations

**Page 7: Budget Allocation**
- Budget Efficiency Score: X/100
- Pie chart: Platform budget allocation
- Bar chart: Funnel stage budget allocation
- Projected metrics table:
  | Metric | Month 1 | Month 2 | Month 3 |
  |--------|---------|---------|---------|
  | Spend | $X | $X | $X |
  | Impressions | X | X | X |
  | Clicks | X | X | X |
  | Conversions | X | X | X |
  | CPA | $X | $X | $X |
  | ROAS | Xx | Xx | Xx |
- Scaling roadmap (when to increase budget and by how much)

**Page 8: 90-Day Action Plan**
- Color-coded priority table:
  - Week 1 (Red/Urgent): Immediate setup actions
  - Weeks 2-4 (Orange/Important): Launch and initial optimization
  - Month 2-3 (Blue/Strategic): Scale and expand
- Each action item includes: task, owner, platform, estimated impact
- Key milestones and check-in points

**Page 9: Appendix (if data available)**
- Full keyword list (if `/ads keywords` was run)
- Complete ad copy library (if `/ads copy` was run)
- Landing page audit summary (if `/ads landing` was run)
- A/B testing plan (if `/ads testing` was run)

#### PDF Design Specifications

**Layout:**
- Page size: Letter (8.5" x 11")
- Margins: 0.75" all sides
- Header: Business name (left), page number (right)
- Footer: "Generated by AI Ads Strategist" (center)

**Colors:**
- Primary: #1E3A5F (dark navy — headers, titles)
- Secondary: #2563EB (blue — accents, highlights, links)
- Background: #F8FAFC (light gray — section backgrounds)
- Text: #1F2937 (dark gray — body text)
- Success: #059669 (green — positive scores, strengths)
- Warning: #D97706 (amber — medium scores, caution)
- Danger: #DC2626 (red — low scores, critical issues)

**Typography:**
- Headings: Helvetica-Bold, 16pt (h1), 13pt (h2), 11pt (h3)
- Body: Helvetica, 10pt
- Tables: Helvetica, 9pt
- Captions: Helvetica, 8pt, gray

**Charts (ReportLab Drawing):**
- Score gauge: Arc/donut chart with score number centered
- Bar charts: Horizontal bars with value labels
- Pie charts: With percentage labels and legend
- Funnel diagram: Trapezoid shapes with labels

### Step 5: Post-Generation

After generating the PDF:

1. Verify the file was created:
```bash
ls -la ADS-STRATEGY-REPORT.pdf
```

2. Report the file size and location to the user

3. Suggest next steps:
   - Review the PDF and share with the client or team
   - Run `/ads audit` after 7 days of campaign data
   - Use individual skills to regenerate specific sections

## Handling Missing Data

Not all skills may have been run before generating the PDF. Handle gracefully:

| Data Available | Behavior |
|---------------|----------|
| Full strategy run (all 5 agents) | Generate complete report with all pages |
| Partial data (some agents) | Generate report with available sections, mark missing sections as "Not Yet Analyzed" |
| Only quick snapshot | Generate a mini-report (cover + executive summary + action plan) |
| No data files found | Inform user to run `/ads strategy <url>` first |

**Minimum required data:** At least one `ADS-*.md` file must exist. If none are found, display:
```
No ad strategy data found in current directory.
Run '/ads strategy <url>' first to generate the analysis,
then use '/ads report-pdf' to create the PDF report.
```

## Output

The final output is a single PDF file: `ADS-STRATEGY-REPORT.pdf`

Saved to the current working directory alongside the Markdown source files.

## Important Rules
- Always check for existing data files before generating — never create a PDF with empty/placeholder data
- The PDF must be client-presentable without any editing
- Score gauges must use color coding to make performance instantly visible
- Charts must have clear labels — no unlabeled axes or legends
- If the script fails, provide the exact error message and suggest installing ReportLab: `pip3 install reportlab`
- The cover page score gauge is the most important visual — it must be prominent and accurate
- Budget projections must be labeled as estimates, not guarantees
- Always include the 90-day action plan — it is the most actionable section for clients
- Page numbers and headers/footers must be consistent across all pages
- If data is partial, clearly mark which sections have full data vs estimates
- The PDF filename should always be `ADS-STRATEGY-REPORT.pdf` for consistency
- File size should be under 5 MB — optimize chart rendering if needed
