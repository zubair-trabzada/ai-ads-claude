#!/usr/bin/env python3
"""
AI Ads Strategy PDF Report Generator — AI Ads Claude Code Skills
Generates professional, client-ready PDF ad strategy reports with score gauges,
horizontal bar charts, audience personas, campaign structures, ad copy samples,
and budget/ROI projections.

Requires: reportlab (pip install reportlab)

Usage:
  python3 generate_ads_pdf.py                        # Demo mode
  python3 generate_ads_pdf.py --demo                 # Demo mode (explicit)
  python3 generate_ads_pdf.py data.json               # From JSON
  python3 generate_ads_pdf.py data.json output.pdf    # From JSON with custom output
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String
except ImportError:
    print("Error: reportlab is required. Install with: pip install reportlab")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Color palette
# ---------------------------------------------------------------------------
COLORS = {
    "primary": HexColor("#1a1a2e"),       # Deep navy
    "accent": HexColor("#2563eb"),         # Ads blue
    "highlight": HexColor("#f97316"),      # Bright orange
    "success": HexColor("#22c55e"),        # Success green
    "warning": HexColor("#eab308"),        # Warning amber
    "danger": HexColor("#ef4444"),         # Danger red
    "light_bg": HexColor("#f0f4f8"),
    "text": HexColor("#1e293b"),
    "text_light": HexColor("#64748b"),
    "border": HexColor("#cbd5e1"),
    "white": white,
    "black": black,
}


def score_color(score):
    """Return color based on score value."""
    if score >= 80:
        return COLORS["success"]
    elif score >= 60:
        return COLORS["accent"]
    elif score >= 40:
        return COLORS["warning"]
    else:
        return COLORS["danger"]


def score_grade(score):
    """Return letter grade from score."""
    if score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "C-"
    elif score >= 50:
        return "D+"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "D-"
    else:
        return "F"


def draw_score_gauge(score, size=120):
    """Create a circular score gauge drawing."""
    d = Drawing(size + 20, size + 20)

    cx = size / 2 + 10
    cy = size / 2 + 10

    # Background circle
    d.add(Circle(cx, cy, size / 2,
                 fillColor=COLORS["light_bg"], strokeColor=COLORS["border"], strokeWidth=2))

    # Score arc (colored ring)
    color = score_color(score)
    inner_r = size / 2 - 8
    d.add(Circle(cx, cy, inner_r,
                 fillColor=color, strokeColor=None))

    # White center
    d.add(Circle(cx, cy, inner_r - 12,
                 fillColor=COLORS["white"], strokeColor=None))

    # Score text
    d.add(String(cx, cy - 4, str(int(score)),
                 fontSize=28, fillColor=COLORS["primary"],
                 textAnchor="middle", fontName="Helvetica-Bold"))

    # "/ 100" label
    d.add(String(cx, cy - 20, "/ 100",
                 fontSize=9, fillColor=COLORS["text_light"],
                 textAnchor="middle", fontName="Helvetica"))

    return d


def create_bar_chart(categories, scores, width=470, height=180):
    """Create horizontal bar charts for category scores."""
    d = Drawing(width, height)

    bar_height = 20
    gap = 10
    max_bar_width = width - 190
    start_y = height - 25
    label_x = 5
    bar_x = 165

    for i, (cat, score) in enumerate(zip(categories, scores)):
        y = start_y - i * (bar_height + gap)

        # Category label
        d.add(String(label_x, y + 5, cat[:25],
                     fontSize=9, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica"))

        # Background bar
        d.add(Rect(bar_x, y, max_bar_width, bar_height,
                   fillColor=COLORS["light_bg"], strokeColor=None, rx=3))

        # Score bar
        bar_width = max((score / 100) * max_bar_width, 2)
        color = score_color(score)
        d.add(Rect(bar_x, y, bar_width, bar_height,
                   fillColor=color, strokeColor=None, rx=3))

        # Score label
        d.add(String(bar_x + max_bar_width + 10, y + 5, f"{int(score)}/100",
                     fontSize=10, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica-Bold"))

    return d


# ---------------------------------------------------------------------------
# Custom styles
# ---------------------------------------------------------------------------
def get_styles():
    """Create custom paragraph styles."""
    styles = getSampleStyleSheet()

    custom = {
        "title": ParagraphStyle(
            "AdsTitle", parent=styles["Title"],
            fontSize=32, textColor=COLORS["primary"],
            spaceAfter=4, fontName="Helvetica-Bold",
            leading=38
        ),
        "subtitle": ParagraphStyle(
            "AdsSubtitle", parent=styles["Normal"],
            fontSize=14, textColor=COLORS["text_light"],
            spaceAfter=6, fontName="Helvetica"
        ),
        "heading": ParagraphStyle(
            "AdsHeading", parent=styles["Heading1"],
            fontSize=20, textColor=COLORS["primary"],
            spaceBefore=16, spaceAfter=10,
            fontName="Helvetica-Bold"
        ),
        "subheading": ParagraphStyle(
            "AdsSubheading", parent=styles["Heading2"],
            fontSize=14, textColor=COLORS["accent"],
            spaceBefore=12, spaceAfter=6,
            fontName="Helvetica-Bold"
        ),
        "body": ParagraphStyle(
            "AdsBody", parent=styles["Normal"],
            fontSize=10, textColor=COLORS["text"],
            spaceAfter=6, fontName="Helvetica", leading=14
        ),
        "body_small": ParagraphStyle(
            "AdsBodySmall", parent=styles["Normal"],
            fontSize=8, textColor=COLORS["text"],
            spaceAfter=4, fontName="Helvetica", leading=11
        ),
        "footer": ParagraphStyle(
            "AdsFooter", parent=styles["Normal"],
            fontSize=8, textColor=COLORS["text_light"],
            fontName="Helvetica"
        ),
        "grade_large": ParagraphStyle(
            "AdsGrade", parent=styles["Title"],
            fontSize=18, textColor=COLORS["primary"],
            spaceAfter=6, fontName="Helvetica-Bold",
            alignment=1
        ),
    }
    return custom


# ---------------------------------------------------------------------------
# Table style helper
# ---------------------------------------------------------------------------
def standard_table_style(extra=None):
    """Return a standard table style with optional extras."""
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    if extra:
        cmds.extend(extra)
    return TableStyle(cmds)


# ---------------------------------------------------------------------------
# Report generator
# ---------------------------------------------------------------------------
def generate_report(data, output_path):
    """Generate a professional ads strategy PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    S = get_styles()
    elements = []

    company = data.get("company_name", data.get("url", "Company"))
    date_str = data.get("date", datetime.now().strftime("%B %d, %Y"))
    overall_score = data.get("overall_score", 0)
    grade = score_grade(overall_score)

    # =====================================================================
    # PAGE 1 — COVER
    # =====================================================================
    elements.append(Spacer(1, 1.2 * inch))
    elements.append(Paragraph("AI Ads Strategy Report", S["title"]))
    elements.append(Spacer(1, 40))
    elements.append(Paragraph(company, ParagraphStyle(
        "CompanyName", parent=S["subtitle"], fontSize=18,
        textColor=COLORS["accent"], spaceAfter=4
    )))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Generated: {date_str}", S["subtitle"]))
    elements.append(Spacer(1, 50))

    # Score gauge
    gauge = draw_score_gauge(overall_score, size=120)
    elements.append(gauge)
    elements.append(Spacer(1, 40))

    # Grade
    color = score_color(overall_score)
    elements.append(Paragraph(
        f'Ad Readiness Score: <font color="{color.hexval()}">{int(overall_score)}/100</font> '
        f'(Grade: <font color="{color.hexval()}">{grade}</font>)',
        S["grade_large"]
    ))

    elements.append(Spacer(1, 30))

    # Executive summary
    exec_summary = data.get("executive_summary",
        "This report provides a comprehensive advertising strategy analysis covering "
        "audience targeting, creative quality, funnel architecture, competitive positioning, "
        "and budget allocation. Each dimension is scored and accompanied by actionable recommendations."
    )
    elements.append(Paragraph(exec_summary, S["body"]))

    elements.append(PageBreak())

    # =====================================================================
    # PAGE 2 — SCORE DASHBOARD
    # =====================================================================
    elements.append(Paragraph("Score Dashboard", S["heading"]))
    elements.append(Spacer(1, 6))

    categories = data.get("categories", {})
    default_cats = {
        "Audience Clarity": {"score": 72, "weight": "25%"},
        "Creative Quality": {"score": 65, "weight": "20%"},
        "Funnel Architecture": {"score": 58, "weight": "20%"},
        "Competitive Position": {"score": 70, "weight": "15%"},
        "Budget Efficiency": {"score": 62, "weight": "20%"},
    }
    if not categories:
        categories = default_cats

    cat_names = list(categories.keys())
    cat_scores = [categories[c].get("score", 50) if isinstance(categories[c], dict)
                  else categories[c] for c in cat_names]

    # Bar chart
    chart = create_bar_chart(cat_names, cat_scores)
    elements.append(chart)
    elements.append(Spacer(1, 16))

    # Score breakdown table
    score_data = [["Category", "Score", "Weight", "Status"]]
    for name, score in zip(cat_names, cat_scores):
        weight = categories[name].get("weight", "--") if isinstance(categories[name], dict) else "--"
        if score >= 75:
            status = "Strong"
        elif score >= 50:
            status = "Needs Work"
        else:
            status = "Critical"
        score_data.append([name, f"{int(score)}/100", weight, status])

    score_table = Table(score_data, colWidths=[160, 80, 60, 100])
    score_style_extra = [("ALIGN", (1, 0), (-1, -1), "CENTER")]
    # Color-code status column
    for i, score in enumerate(cat_scores, 1):
        color = score_color(score)
        score_style_extra.append(("TEXTCOLOR", (3, i), (3, i), color))
        score_style_extra.append(("FONTNAME", (3, i), (3, i), "Helvetica-Bold"))
    score_table.setStyle(standard_table_style(score_style_extra))
    elements.append(score_table)

    elements.append(PageBreak())

    # =====================================================================
    # PAGE 3 — AUDIENCE PERSONAS
    # =====================================================================
    elements.append(Paragraph("Audience Personas", S["heading"]))
    elements.append(Spacer(1, 6))

    personas = data.get("personas", [])
    if not personas:
        personas = [
            {
                "name": "Startup Sarah",
                "demographics": "28-35, Female, Urban, $75K-$120K income",
                "platforms": "Instagram, LinkedIn, YouTube",
                "targeting": "Interest: SaaS, Startup, Entrepreneurship. Lookalike: Website visitors"
            },
            {
                "name": "Enterprise Eric",
                "demographics": "40-55, Male, Suburban, $150K+ income",
                "platforms": "LinkedIn, Google Search, YouTube",
                "targeting": "Job Title: VP/Director/C-Suite. Industry: Technology, Finance"
            },
            {
                "name": "Freelancer Fiona",
                "demographics": "25-38, Any gender, Urban/Remote, $45K-$80K income",
                "platforms": "Instagram, TikTok, Facebook Groups",
                "targeting": "Interest: Freelancing, Side Hustle, Productivity tools"
            },
        ]

    persona_data = [["Persona", "Demographics", "Platforms", "Targeting Parameters"]]
    for p in personas:
        persona_data.append([
            Paragraph(p.get("name", ""), S["body_small"]),
            Paragraph(p.get("demographics", ""), S["body_small"]),
            Paragraph(p.get("platforms", ""), S["body_small"]),
            Paragraph(p.get("targeting", ""), S["body_small"]),
        ])

    persona_table = Table(persona_data, colWidths=[90, 120, 100, 160])
    persona_table.setStyle(standard_table_style([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(persona_table)

    # Targeting recommendations
    elements.append(Spacer(1, 14))
    elements.append(Paragraph("Targeting Recommendations", S["subheading"]))
    recs = data.get("targeting_recommendations", [
        "Start with Lookalike audiences based on existing customers or email lists",
        "Layer interest-based targeting with demographic filters for precision",
        "Use retargeting pools segmented by funnel stage (visited vs. engaged vs. converted)",
        "Test broad vs. narrow audiences — let platform algorithms optimize delivery",
    ])
    for i, rec in enumerate(recs, 1):
        elements.append(Paragraph(f"{i}. {rec}", S["body"]))

    elements.append(PageBreak())

    # =====================================================================
    # PAGE 4 — CAMPAIGN STRUCTURE (Funnel Stages)
    # =====================================================================
    elements.append(Paragraph("Campaign Structure", S["heading"]))
    elements.append(Spacer(1, 6))

    funnel_stages = data.get("funnel_stages", [])
    if not funnel_stages:
        funnel_stages = [
            {
                "stage": "TOFU (Awareness)",
                "objective": "Brand awareness, reach, video views",
                "budget_pct": "35%",
                "platforms": "Meta, YouTube, TikTok",
                "ad_types": "Video ads, carousel, story ads",
                "kpis": "CPM, VTR, Reach"
            },
            {
                "stage": "MOFU (Consideration)",
                "objective": "Traffic, engagement, lead generation",
                "budget_pct": "25%",
                "platforms": "Meta, Google, LinkedIn",
                "ad_types": "Lead forms, content ads, webinar promos",
                "kpis": "CPC, CTR, CPL"
            },
            {
                "stage": "BOFU (Conversion)",
                "objective": "Conversions, sales, sign-ups",
                "budget_pct": "25%",
                "platforms": "Google Search, Meta, LinkedIn",
                "ad_types": "Search ads, dynamic product, testimonial",
                "kpis": "CPA, ROAS, Conv Rate"
            },
            {
                "stage": "Retargeting",
                "objective": "Re-engage, upsell, reduce churn",
                "budget_pct": "15%",
                "platforms": "Meta, Google Display, YouTube",
                "ad_types": "Dynamic retargeting, abandoned cart, win-back",
                "kpis": "ROAS, Frequency, CPA"
            },
        ]

    funnel_data = [["Funnel Stage", "Objective", "Budget", "Platforms", "Ad Types", "KPIs"]]
    for stage in funnel_stages:
        funnel_data.append([
            Paragraph(stage.get("stage", ""), S["body_small"]),
            Paragraph(stage.get("objective", ""), S["body_small"]),
            stage.get("budget_pct", ""),
            Paragraph(stage.get("platforms", ""), S["body_small"]),
            Paragraph(stage.get("ad_types", ""), S["body_small"]),
            Paragraph(stage.get("kpis", ""), S["body_small"]),
        ])

    funnel_table = Table(funnel_data, colWidths=[80, 90, 50, 80, 90, 80])
    funnel_table.setStyle(standard_table_style([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
    ]))
    elements.append(funnel_table)

    # Budget allocation summary
    elements.append(Spacer(1, 14))
    elements.append(Paragraph("Budget Flow", S["subheading"]))
    elements.append(Paragraph(
        "TOFU (35%) captures cold audiences with high-reach formats. "
        "MOFU (25%) nurtures engaged prospects with educational content. "
        "BOFU (25%) drives conversions with high-intent targeting. "
        "Retargeting (15%) recaptures lost prospects and drives repeat purchases.",
        S["body"]
    ))

    elements.append(PageBreak())

    # =====================================================================
    # PAGE 5 — AD COPY SAMPLES
    # =====================================================================
    elements.append(Paragraph("Ad Copy Samples", S["heading"]))
    elements.append(Spacer(1, 6))

    ad_samples = data.get("ad_samples", [])
    if not ad_samples:
        ad_samples = [
            {
                "platform": "Meta (Facebook)",
                "headline": "Stop Wasting Ad Spend",
                "primary_text": "87% of small businesses lose money on ads because they skip strategy. Get a free AI-powered ad audit and find out where your budget is leaking.",
                "cta": "Get Free Audit"
            },
            {
                "platform": "Google Search",
                "headline": "AI Ad Strategy Tool | Free Audit",
                "primary_text": "See exactly where your ad budget is going wrong. AI-powered analysis across 5 dimensions. Results in 60 seconds.",
                "cta": "Start Free Audit"
            },
            {
                "platform": "LinkedIn",
                "headline": "Your Competitors Are Outspending You",
                "primary_text": "We analyzed 1,000+ ad accounts. The top performers all share 5 traits. Find out if your campaigns measure up with our free Ad Readiness Score.",
                "cta": "Get Your Score"
            },
            {
                "platform": "Instagram Story",
                "headline": "Is Your Ad Budget Working?",
                "primary_text": "Swipe up to get your free Ad Readiness Score. AI analyzes your audience, creative, funnel, and budget in under 60 seconds.",
                "cta": "Swipe Up"
            },
            {
                "platform": "YouTube Pre-Roll",
                "headline": "The #1 Reason Ads Fail",
                "primary_text": "It's not your budget. It's not your creative. It's your targeting. Watch how AI fixes ad targeting in 60 seconds.",
                "cta": "Learn More"
            },
            {
                "platform": "TikTok",
                "headline": "POV: Your ads finally work",
                "primary_text": "I ran this AI tool on my ad account and it found $2,300/mo in wasted spend. Here's exactly what it flagged.",
                "cta": "Try It Free"
            },
        ]

    ad_data = [["Platform", "Headline", "Primary Text", "CTA"]]
    for ad in ad_samples:
        ad_data.append([
            Paragraph(ad.get("platform", ""), S["body_small"]),
            Paragraph(ad.get("headline", ""), S["body_small"]),
            Paragraph(ad.get("primary_text", ""), S["body_small"]),
            Paragraph(ad.get("cta", ""), S["body_small"]),
        ])

    ad_table = Table(ad_data, colWidths=[80, 100, 200, 70])
    ad_table.setStyle(standard_table_style([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    elements.append(ad_table)

    elements.append(PageBreak())

    # =====================================================================
    # PAGE 6 — BUDGET & ROI PROJECTIONS
    # =====================================================================
    elements.append(Paragraph("Budget & ROI Projections", S["heading"]))
    elements.append(Spacer(1, 6))

    # Budget allocation table (pie chart data as table)
    elements.append(Paragraph("Budget Allocation by Platform", S["subheading"]))

    budget_alloc = data.get("budget_allocation", [])
    if not budget_alloc:
        budget_alloc = [
            {"platform": "Meta (Facebook/Instagram)", "allocation": "35%", "monthly": "$1,750"},
            {"platform": "Google Ads (Search + Display)", "allocation": "30%", "monthly": "$1,500"},
            {"platform": "YouTube Ads", "allocation": "15%", "monthly": "$750"},
            {"platform": "LinkedIn Ads", "allocation": "10%", "monthly": "$500"},
            {"platform": "TikTok Ads", "allocation": "5%", "monthly": "$250"},
            {"platform": "Pinterest Ads", "allocation": "5%", "monthly": "$250"},
        ]

    alloc_data = [["Platform", "Allocation", "Monthly Budget"]]
    for item in budget_alloc:
        alloc_data.append([
            item.get("platform", ""),
            item.get("allocation", ""),
            item.get("monthly", ""),
        ])

    alloc_table = Table(alloc_data, colWidths=[220, 100, 120])
    alloc_table.setStyle(standard_table_style([
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ]))
    elements.append(alloc_table)

    elements.append(Spacer(1, 20))

    # Projected metrics
    elements.append(Paragraph("Projected Monthly Metrics", S["subheading"]))

    projections = data.get("projections", {})
    if not projections:
        projections = {
            "total_budget": "$5,000/mo",
            "impressions": "250,000 - 400,000",
            "clicks": "3,500 - 6,000",
            "ctr": "1.4% - 1.8%",
            "conversions": "85 - 150",
            "cpa": "$33 - $59",
            "roas": "3.2x - 5.8x",
            "revenue_estimate": "$16,000 - $29,000",
        }

    proj_data = [["Metric", "Projected Range"]]
    metric_labels = {
        "total_budget": "Total Monthly Budget",
        "impressions": "Impressions",
        "clicks": "Clicks",
        "ctr": "Click-Through Rate (CTR)",
        "conversions": "Conversions",
        "cpa": "Cost Per Acquisition (CPA)",
        "roas": "Return on Ad Spend (ROAS)",
        "revenue_estimate": "Estimated Revenue",
    }
    for key, label in metric_labels.items():
        value = projections.get(key, "--")
        proj_data.append([label, value])

    proj_table = Table(proj_data, colWidths=[240, 200])
    proj_style_extra = [("ALIGN", (1, 0), (1, -1), "CENTER")]
    # Highlight ROAS row
    roas_row = list(metric_labels.keys()).index("roas") + 1
    proj_style_extra.append(("TEXTCOLOR", (1, roas_row), (1, roas_row), COLORS["success"]))
    proj_style_extra.append(("FONTNAME", (1, roas_row), (1, roas_row), "Helvetica-Bold"))
    # Highlight revenue row
    rev_row = list(metric_labels.keys()).index("revenue_estimate") + 1
    proj_style_extra.append(("TEXTCOLOR", (1, rev_row), (1, rev_row), COLORS["success"]))
    proj_style_extra.append(("FONTNAME", (1, rev_row), (1, rev_row), "Helvetica-Bold"))
    proj_table.setStyle(standard_table_style(proj_style_extra))
    elements.append(proj_table)

    elements.append(Spacer(1, 24))

    # Footer
    elements.append(Paragraph(
        "Generated by AI Ads Strategist for Claude Code",
        S["footer"]
    ))

    # Build PDF
    doc.build(elements)
    return output_path


# ---------------------------------------------------------------------------
# Demo data
# ---------------------------------------------------------------------------
def get_demo_data():
    """Return sample data for demo mode."""
    return {
        "company_name": "Acme Growth Co.",
        "url": "https://acmegrowth.com",
        "date": datetime.now().strftime("%B %d, %Y"),
        "overall_score": 67,
        "executive_summary": (
            "Acme Growth Co. has a solid product offering but is underperforming across "
            "key advertising dimensions. Audience targeting lacks precision, creative assets "
            "need stronger hooks, and the funnel architecture has gaps between consideration "
            "and conversion stages. This report outlines a complete ad strategy with platform-specific "
            "recommendations, budget allocation, and projected ROI."
        ),
        "categories": {
            "Audience Clarity": {"score": 72, "weight": "25%"},
            "Creative Quality": {"score": 65, "weight": "20%"},
            "Funnel Architecture": {"score": 58, "weight": "20%"},
            "Competitive Position": {"score": 70, "weight": "15%"},
            "Budget Efficiency": {"score": 62, "weight": "20%"},
        },
        "personas": [
            {
                "name": "Startup Sarah",
                "demographics": "28-35, Female, Urban, $75K-$120K income",
                "platforms": "Instagram, LinkedIn, YouTube",
                "targeting": "Interest: SaaS, Startup, Entrepreneurship. Lookalike: Website visitors"
            },
            {
                "name": "Enterprise Eric",
                "demographics": "40-55, Male, Suburban, $150K+ income",
                "platforms": "LinkedIn, Google Search, YouTube",
                "targeting": "Job Title: VP/Director/C-Suite. Industry: Technology, Finance"
            },
            {
                "name": "Freelancer Fiona",
                "demographics": "25-38, Any gender, Urban/Remote, $45K-$80K income",
                "platforms": "Instagram, TikTok, Facebook Groups",
                "targeting": "Interest: Freelancing, Side Hustle, Productivity tools"
            },
        ],
        "targeting_recommendations": [
            "Start with Lookalike audiences based on existing customers or email lists",
            "Layer interest-based targeting with demographic filters for precision",
            "Use retargeting pools segmented by funnel stage (visited vs. engaged vs. converted)",
            "Test broad vs. narrow audiences — let platform algorithms optimize delivery",
        ],
        "funnel_stages": [
            {
                "stage": "TOFU (Awareness)",
                "objective": "Brand awareness, reach, video views",
                "budget_pct": "35%",
                "platforms": "Meta, YouTube, TikTok",
                "ad_types": "Video ads, carousel, story ads",
                "kpis": "CPM, VTR, Reach"
            },
            {
                "stage": "MOFU (Consideration)",
                "objective": "Traffic, engagement, lead generation",
                "budget_pct": "25%",
                "platforms": "Meta, Google, LinkedIn",
                "ad_types": "Lead forms, content ads, webinar promos",
                "kpis": "CPC, CTR, CPL"
            },
            {
                "stage": "BOFU (Conversion)",
                "objective": "Conversions, sales, sign-ups",
                "budget_pct": "25%",
                "platforms": "Google Search, Meta, LinkedIn",
                "ad_types": "Search ads, dynamic product, testimonial",
                "kpis": "CPA, ROAS, Conv Rate"
            },
            {
                "stage": "Retargeting",
                "objective": "Re-engage, upsell, reduce churn",
                "budget_pct": "15%",
                "platforms": "Meta, Google Display, YouTube",
                "ad_types": "Dynamic retargeting, abandoned cart, win-back",
                "kpis": "ROAS, Frequency, CPA"
            },
        ],
        "ad_samples": [
            {
                "platform": "Meta (Facebook)",
                "headline": "Stop Wasting Ad Spend",
                "primary_text": "87% of small businesses lose money on ads because they skip strategy. Get a free AI-powered ad audit and find out where your budget is leaking.",
                "cta": "Get Free Audit"
            },
            {
                "platform": "Google Search",
                "headline": "AI Ad Strategy Tool | Free Audit",
                "primary_text": "See exactly where your ad budget is going wrong. AI-powered analysis across 5 dimensions. Results in 60 seconds.",
                "cta": "Start Free Audit"
            },
            {
                "platform": "LinkedIn",
                "headline": "Your Competitors Are Outspending You",
                "primary_text": "We analyzed 1,000+ ad accounts. The top performers all share 5 traits. Find out if your campaigns measure up.",
                "cta": "Get Your Score"
            },
            {
                "platform": "Instagram Story",
                "headline": "Is Your Ad Budget Working?",
                "primary_text": "Swipe up to get your free Ad Readiness Score. AI analyzes your audience, creative, funnel, and budget in under 60 seconds.",
                "cta": "Swipe Up"
            },
            {
                "platform": "YouTube Pre-Roll",
                "headline": "The #1 Reason Ads Fail",
                "primary_text": "It's not your budget. It's not your creative. It's your targeting. Watch how AI fixes ad targeting in 60 seconds.",
                "cta": "Learn More"
            },
            {
                "platform": "TikTok",
                "headline": "POV: Your ads finally work",
                "primary_text": "I ran this AI tool on my ad account and it found $2,300/mo in wasted spend. Here's exactly what it flagged.",
                "cta": "Try It Free"
            },
        ],
        "budget_allocation": [
            {"platform": "Meta (Facebook/Instagram)", "allocation": "35%", "monthly": "$1,750"},
            {"platform": "Google Ads (Search + Display)", "allocation": "30%", "monthly": "$1,500"},
            {"platform": "YouTube Ads", "allocation": "15%", "monthly": "$750"},
            {"platform": "LinkedIn Ads", "allocation": "10%", "monthly": "$500"},
            {"platform": "TikTok Ads", "allocation": "5%", "monthly": "$250"},
            {"platform": "Pinterest Ads", "allocation": "5%", "monthly": "$250"},
        ],
        "projections": {
            "total_budget": "$5,000/mo",
            "impressions": "250,000 - 400,000",
            "clicks": "3,500 - 6,000",
            "ctr": "1.4% - 1.8%",
            "conversions": "85 - 150",
            "cpa": "$33 - $59",
            "roas": "3.2x - 5.8x",
            "revenue_estimate": "$16,000 - $29,000",
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--demo":
        # Demo mode
        data = get_demo_data()
        output = "ADS-STRATEGY-REPORT-sample.pdf"
        generate_report(data, output)
        print(f"Sample report generated: {output}")
        return

    # JSON input mode
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "ADS-STRATEGY-REPORT.pdf"

    with open(input_file, "r") as f:
        data = json.load(f)

    generate_report(data, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
