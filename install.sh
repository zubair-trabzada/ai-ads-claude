#!/bin/bash
# ============================================================================
# AI Ads Strategist — Claude Code Skills Installer
# 16 Skills · 5 Agents · 6 Platforms · PDF Reports
# ============================================================================
set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${BLUE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                                                              ║${NC}"
echo -e "${BLUE}║${NC}   ${CYAN}AI Ads Strategist — Claude Code Skills${NC}                    ${BLUE}║${NC}"
echo -e "${BLUE}║${NC}   ${GREEN}16 Skills · 5 Agents · 6 Platforms · PDF Reports${NC}          ${BLUE}║${NC}"
echo -e "${BLUE}║                                                              ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# ---------------------------------------------------------------------------
# Detect script directory (handle both local and curl | bash)
# ---------------------------------------------------------------------------
GITHUB_REPO="zubair-trabzada/ai-ads-claude"
TEMP_DIR=""

if [ -n "${BASH_SOURCE[0]}" ] && [ "${BASH_SOURCE[0]}" != "bash" ]; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    if [ -f "$SCRIPT_DIR/install.sh" ] && [ -d "$SCRIPT_DIR/skills" ]; then
        SOURCE_DIR="$SCRIPT_DIR"
        echo -e "${GREEN}Installing from local directory:${NC} $SOURCE_DIR"
    else
        SCRIPT_DIR=""
    fi
fi

if [ -z "${SCRIPT_DIR:-}" ] || [ ! -d "${SOURCE_DIR:-}" ]; then
    echo -e "${YELLOW}Cloning from GitHub...${NC}"
    TEMP_DIR=$(mktemp -d)
    if command -v git &>/dev/null; then
        git clone --depth 1 "https://github.com/$GITHUB_REPO.git" "$TEMP_DIR/repo" 2>/dev/null
        SOURCE_DIR="$TEMP_DIR/repo"
    else
        echo -e "${RED}Error: git is required for remote installation.${NC}"
        echo "Install git or run install.sh from a local clone."
        exit 1
    fi
    echo -e "${GREEN}Cloned successfully.${NC}"
fi

# ---------------------------------------------------------------------------
# Target directories
# ---------------------------------------------------------------------------
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

# ---------------------------------------------------------------------------
# Check for Claude Code
# ---------------------------------------------------------------------------
echo -e "${BLUE}Checking prerequisites...${NC}"
if command -v claude &>/dev/null; then
    echo -e "  ${GREEN}✓${NC} Claude Code found"
else
    echo -e "  ${YELLOW}⚠${NC} Claude Code CLI not found (skills will still be installed)"
fi

# ---------------------------------------------------------------------------
# Create directories
# ---------------------------------------------------------------------------
echo -e "${BLUE}Creating directories...${NC}"
mkdir -p "$SKILLS_DIR/ads/scripts"
echo -e "  ${GREEN}✓${NC} Skills directory ready"

mkdir -p "$AGENTS_DIR"
echo -e "  ${GREEN}✓${NC} Agents directory ready"

# ---------------------------------------------------------------------------
# Install main skill orchestrator
# ---------------------------------------------------------------------------
echo -e "${BLUE}Installing skills...${NC}"

INSTALL_COUNT=0

if [ -f "$SOURCE_DIR/ads/SKILL.md" ]; then
    cp "$SOURCE_DIR/ads/SKILL.md" "$SKILLS_DIR/ads/SKILL.md"
    echo -e "  ${GREEN}✓${NC} ads (orchestrator)"
    INSTALL_COUNT=$((INSTALL_COUNT + 1))
fi

# ---------------------------------------------------------------------------
# Install 14 sub-skills
# ---------------------------------------------------------------------------
SKILLS=(
    ads-strategy
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
    if [ -f "$SOURCE_DIR/skills/$skill/SKILL.md" ]; then
        mkdir -p "$SKILLS_DIR/$skill"
        cp "$SOURCE_DIR/skills/$skill/SKILL.md" "$SKILLS_DIR/$skill/SKILL.md"
        echo -e "  ${GREEN}✓${NC} $skill"
        INSTALL_COUNT=$((INSTALL_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $skill (not found in source)"
    fi
done

# ---------------------------------------------------------------------------
# Install 5 agents
# ---------------------------------------------------------------------------
echo -e "${BLUE}Installing agents...${NC}"

AGENT_COUNT=0
AGENTS=(
    ads-audience
    ads-creative
    ads-funnel
    ads-competitive
    ads-budget
)

for agent in "${AGENTS[@]}"; do
    if [ -f "$SOURCE_DIR/agents/$agent.md" ]; then
        cp "$SOURCE_DIR/agents/$agent.md" "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} $agent"
        AGENT_COUNT=$((AGENT_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $agent (not found in source)"
    fi
done

# ---------------------------------------------------------------------------
# Install Python scripts
# ---------------------------------------------------------------------------
echo -e "${BLUE}Installing scripts...${NC}"

SCRIPT_COUNT=0
for script in "$SOURCE_DIR"/scripts/*.py; do
    if [ -f "$script" ]; then
        cp "$script" "$SKILLS_DIR/ads/scripts/"
        echo -e "  ${GREEN}✓${NC} $(basename "$script")"
        SCRIPT_COUNT=$((SCRIPT_COUNT + 1))
    fi
done

# ---------------------------------------------------------------------------
# Check Python dependencies
# ---------------------------------------------------------------------------
echo -e "${BLUE}Checking Python environment...${NC}"

if command -v python3 &>/dev/null; then
    PY_VERSION=$(python3 --version 2>&1)
    PY_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)")
    PY_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)")
    if [ "$PY_MAJOR" -ge 3 ] && [ "$PY_MINOR" -ge 8 ]; then
        echo -e "  ${GREEN}✓${NC} $PY_VERSION"
    else
        echo -e "  ${YELLOW}⚠${NC} $PY_VERSION (Python 3.8+ recommended)"
    fi
else
    echo -e "  ${RED}✗${NC} Python 3 not found — required for PDF reports"
fi

# Check reportlab
if python3 -c "import reportlab" 2>/dev/null; then
    echo -e "  ${GREEN}✓${NC} reportlab installed"
else
    echo -e "  ${YELLOW}⚠${NC} reportlab not installed (needed for PDF reports)"
    echo -e "      Install with: ${CYAN}pip3 install reportlab${NC}"
fi

# ---------------------------------------------------------------------------
# Cleanup temp dir if used
# ---------------------------------------------------------------------------
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
    echo -e "  ${GREEN}✓${NC} Cleaned up temporary files"
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Installation Complete!                                      ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${CYAN}Skills:${NC}    $INSTALL_COUNT installed  →  $SKILLS_DIR"
echo -e "  ${CYAN}Agents:${NC}    $AGENT_COUNT installed  →  $AGENTS_DIR"
echo -e "  ${CYAN}Scripts:${NC}   $SCRIPT_COUNT installed  →  $SKILLS_DIR/ads/scripts"
echo ""

# ---------------------------------------------------------------------------
# Command reference
# ---------------------------------------------------------------------------
echo -e "${BLUE}Command Reference:${NC}"
echo ""
echo -e "  ${CYAN}/ads strategy <url>${NC}         Full ad strategy (5 parallel agents)"
echo -e "  ${CYAN}/ads quick <url>${NC}            60-second ad readiness snapshot"
echo -e "  ${CYAN}/ads audience <url>${NC}         Build audience personas"
echo -e "  ${CYAN}/ads competitors <url>${NC}      Competitive ad intelligence"
echo -e "  ${CYAN}/ads keywords <url>${NC}         Google Ads keyword strategy"
echo -e "  ${CYAN}/ads copy <platform>${NC}        Platform-specific ad copy"
echo -e "  ${CYAN}/ads hooks${NC}                  Generate scroll-stopping hooks"
echo -e "  ${CYAN}/ads creative <product>${NC}     Creative briefs for designers"
echo -e "  ${CYAN}/ads video <product>${NC}        Video ad scripts (15s/30s/60s)"
echo -e "  ${CYAN}/ads funnel <url>${NC}           Full ads funnel architecture"
echo -e "  ${CYAN}/ads budget <amount>${NC}        Budget allocation across platforms"
echo -e "  ${CYAN}/ads testing <campaign>${NC}     A/B testing plan"
echo -e "  ${CYAN}/ads landing <url>${NC}          Landing page audit + rewrite"
echo -e "  ${CYAN}/ads audit${NC}                  Audit existing ad performance"
echo -e "  ${CYAN}/ads report-pdf${NC}             Professional PDF strategy report"
echo ""
echo -e "  ${YELLOW}Tip:${NC} Start with ${CYAN}/ads strategy <url>${NC} for a full ad strategy audit!"
echo ""
