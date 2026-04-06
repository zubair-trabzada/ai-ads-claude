#!/bin/bash
# ============================================================================
# AI Ads Strategist — Uninstaller
# ============================================================================
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

echo ""
echo -e "${BLUE}Uninstalling AI Ads Strategist...${NC}"
echo ""

# Remove skills
SKILLS=(
    ads
    ads-audience
    ads-competitors
    ads-keywords
    ads-copy
    ads-hooks
    ads-creative
    ads-video
    ads-funnel
    ads-budget
    ads-testing
    ads-landing
    ads-audit
    ads-report-pdf
    ads-quick
)

for skill in "${SKILLS[@]}"; do
    if [ -d "$SKILLS_DIR/$skill" ]; then
        rm -rf "$SKILLS_DIR/$skill"
        echo -e "  ${GREEN}✓${NC} Removed $skill"
    fi
done

# Remove agents
AGENTS=(
    ads-audience
    ads-creative
    ads-funnel
    ads-competitive
    ads-budget
)

for agent in "${AGENTS[@]}"; do
    if [ -f "$AGENTS_DIR/$agent.md" ]; then
        rm "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} Removed agent: $agent"
    fi
done

echo ""
echo -e "${GREEN}Uninstall complete.${NC} All AI Ads Strategist skills and agents have been removed."
echo -e "Your Claude Code installation is otherwise unchanged."
echo ""
