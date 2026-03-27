# Presentation Specification & Speaker Guide
## Unicorn Startup Investment Dashboard: 2021 vs 2026
### Quantic MSBA — Communicating with Data

---

## Problem Statement & Business Case
**Stakeholder:** A late-stage venture capital investor deciding where to allocate $500M+ in 2026.

**Decision to make:** Which sectors, geographies, and company types should receive capital — and which should be avoided?

**Why this data answers it:** By tracking what happened to the 700+ unicorns created during the unprecedented 2021 startup boom, we can identify clear, data-backed patterns of success and failure that directly inform investment strategy.

**Narrative arc:** Boom → Bust → Lessons → Actionable recommendation. Each story point builds on the last.

---

## Suggested Presentation Flow (~8 minutes)

### Opening (30 seconds)
> "Imagine you're an investor in 2021. Over 700 companies just crossed a billion-dollar valuation. Where do you put your money? Fast-forward to 2026 — some of those bets returned 287x. Others went to zero. This dashboard tells you why."

---

### Story Point 1: The 2021 Unicorn Boom (~1.5 min)
**Page:** "1. The 2021 Unicorn Boom"

**What the audience sees:**
- 4 KPI metric cards at the top (Total Unicorns, Combined Valuation, Top Industry, Top Country)
- Horizontal bar chart: Top 15 most valued unicorns
- Side-by-side: Industry breakdown bar chart + Top 15 countries bar chart

**What to say:**
> "In 2021, cheap capital and post-COVID digital acceleration created over 936 unicorn startups worth $2.7 trillion combined. The top 15 alone — led by Bytedance at $140B and SpaceX at $100B — accounted for a massive share of total value. Fintech dominated with the most companies, while the US led by country count. This was the greatest period of startup creation in history."

**Key insight to emphasize:** The sheer scale of the boom — this sets up the dramatic contrast in the next slide.

**Design choices to mention:**
- KPI cards give instant context before any chart
- Horizontal bar chart chosen so company names are readable
- Color encodes Industry to show sector concentration at a glance
- Country chart uses color intensity to show that the US had both the most unicorns AND the most combined value

---

### Story Point 2: Winners vs Losers (~1.5 min)
**Page:** "2. Winners vs Losers"

**What the audience sees:**
- 4 KPI cards (Collapsed count, Value Destroyed, Thriving count, Value Created)
- Scatter plot: 2021 valuation vs 2026 valuation (log scale) with a 45° "no change" reference line
- Side-by-side butterfly chart: Top 10 Value Creators vs Top 10 Value Destroyers

**What to say:**
> "Five years later, the picture is dramatically different. 21 companies collapsed entirely, destroying over $100B in value. But 30 companies are thriving, and they created far more value than was lost. The scatter plot tells the story at a glance — dots above the gray diagonal line grew; dots below it shrank. You can immediately see that the winners massively outpaced the losers."

> "The butterfly chart on the bottom makes the contrast visceral: OpenAI created +$837B in value on the left, while FTX destroyed $25B on the right."

**Key insight to emphasize:** Value creation far outpaced value destruction — but it was concentrated in a few big winners.

**Design choices to mention:**
- Log scale on both axes so companies at very different scales are all visible
- The 45° reference line is the single most important visual element — it instantly answers "did this company grow or shrink?"
- Butterfly/diverging layout puts winners and losers in direct visual opposition — this is a classic storytelling technique from Cole Nussbaumer Knaflic's "Storytelling with Data"

---

### Story Point 3: What Killed Them (~1.5 min)
**Page:** "3. What Killed Them"

**What the audience sees:**
- Sunburst chart: failure categories → individual companies (sized by value destroyed)
- Side-by-side: bar chart of value destroyed per company + Notable Failures callout text
- Pie chart: share of value destroyed by failure category

**What to say:**
> "The failures weren't random — they cluster into clear categories. Click into the sunburst to explore: Unsustainable Unit Economics was the biggest killer, followed by Crypto Contagion and Fraud. The notable failures panel highlights the most dramatic collapses — FTX lost $25B to fraud, Thrasio lost $10B when the Amazon aggregator model failed, and Hopin lost $7.75B when virtual event demand evaporated after COVID."

> "The pie chart summarizes it: these eight failure categories explain virtually all value destruction."

**Key insight to emphasize:** Failures were predictable in hindsight — companies lacking real unit economics, exposed to crypto, or riding temporary COVID demand were systematically punished.

**Design choices to mention:**
- Sunburst chart provides hierarchical drill-down (category → company) in one compact visual — the audience can explore interactively
- The notable failures text panel adds narrative context that pure data cannot — this follows the principle of combining data with story
- Consistent red/orange color palette across all failure charts ties the visual language together

---

### Story Point 4: What Made Them Win (~1.5 min)
**Page:** "4. What Made Them Win"

**What the audience sees:**
- Horizontal bar chart: Top 15 winners by growth multiple (e.g., OpenAI 287x)
- Side-by-side: Industry average change % (diverging bar) + Key Success Patterns text
- Waterfall chart: cumulative value created by top 10 winners

**What to say:**
> "The winners tell an equally clear story. OpenAI grew 287x — from $2.9B to $840B. Seven of the top ten winners are AI-related. The growth multiple chart makes this unmistakable."

> "The industry performance chart on the left shows that AI, Defense Tech, and Data Infrastructure industries averaged the highest valuation growth, while consumer-facing sectors like E-commerce struggled. The four patterns on the right — AI Revolution, Defense Tech, Fintech Infrastructure, and Data Platforms — represent the winning playbook."

> "The waterfall chart shows how concentrated value creation was: OpenAI and SpaceX alone account for over $1.5 trillion of new value."

**Key insight to emphasize:** The winners had enterprise revenue models, strong moats, and rode structural trends (AI, defense spending, data infrastructure) — not hype.

**Design choices to mention:**
- Growth multiple is more meaningful than absolute dollar change for investors evaluating returns
- The diverging red-to-green color scale on the industry chart instantly shows which industries won vs lost
- The waterfall chart shows cumulative contribution — a visual that executives recognize from financial reporting

---

### Story Point 5: Investor Recommendation (~1.5 min)
**Page:** "5. Investor Recommendation"

**What the audience sees:**
- Investment quadrant scatter plot (Growth % vs Current Size) with labeled quadrants
- Geographic performance bar chart
- Two-column INVEST IN / AVOID summary tables with specific sector advice

**What to say:**
> "So where should our investor allocate capital? The quadrant chart maps every tracked company by current valuation vs growth rate. The upper-left quadrant — high growth, reasonable size — represents the best bets: companies like Ramp, VAST Data, and Anduril that have proven hypergrowth but haven't reached massive scale yet."

> "The geographic chart confirms the US dominates value creation, but Israel punches above its weight with Wiz. The final thesis is clear: invest in AI infrastructure, defense tech, data platforms, and enterprise fintech. Avoid crypto speculation, quick commerce, virtual events, and founder-hype companies."

**Key insight to emphasize:** This is the actionable output — the entire story builds to this recommendation. Read the key takeaway quote aloud.

**Design choices to mention:**
- The quadrant chart is the signature visualization — it's the format investors actually use (BCG matrix style)
- Median-based dividing lines ensure balanced quadrants
- The INVEST IN / AVOID tables use a format executives can immediately act on — sector, rationale, and examples

---

### Story Point 6: Ask the Data (Live Demo, ~30 sec)
**Page:** "6. Ask the Data 🤖"

**What to say:**
> "Finally, the dashboard includes an AI-powered chat assistant. Using Groq's Llama 3.3 70B model — completely free — stakeholders can ask natural-language questions about the data. For example: 'What do the top 5 winners have in common?' The model has full context on all 93 tracked companies and responds with data-backed answers."

**Demo tip:** Have one question pre-typed or ready to paste. Don't wait for a slow response on camera.

---

### Closing (30 seconds)
> "To summarize: the 2021 unicorn boom created $2.7 trillion in value. By 2026, companies with enterprise revenue, AI-native products, and real fundamentals outperformed hype-driven startups by 10-100x. The data tells us exactly where to invest — and where to stay away."

---

## Rubric Alignment Checklist

**Persuasive BI case (Score 5):** The problem statement identifies a real stakeholder (VC investor), a real decision (capital allocation), and uses real data to answer it.

**Strategic alignment:** Every story point builds toward the final investment recommendation — nothing is decorative.

**Executive appeal:** The narrative follows a classic tension-resolution arc (boom → who won/lost → why → what to do now). Numbers are always contextualized with insight.

**Dashboard design:** Wide layout, KPI cards for instant context, consistent color encoding, interactive Plotly charts with hover details.

**Course concepts applied:**
- User-centric Design: sidebar navigation lets the stakeholder explore at their own pace
- Business Intelligence: KPIs, aggregated metrics, quadrant analysis
- Storytelling with Data: narrative titles, context annotations, progressive disclosure
- Data Visualization: appropriate chart types for each question, Bertin's visual variables (position, size, color, text)

**Time target:** ~8 minutes following this guide (within the 5-10 minute requirement).

---

## Technical Notes for Q&A

- **Data source:** 2021 data from CB Insights unicorn list (936 companies). 2026 comparison data assembled from Crunchbase (March 2026) covering 93 tracked companies.
- **Derived metrics:** Growth Multiple, Value Created/Destroyed, Valuation Change %, failure/success categories — all pre-computed in the merged dataset.
- **LLM integration:** Groq API (free tier, 14,400 req/day) running Llama 3.3 70B via OpenAI-compatible endpoint. System prompt includes compact summaries of both datasets.
- **No database required:** CSV data extracts satisfy the assignment's "PostgreSQL database or data extract" requirement.
- **GitHub repo:** https://github.com/JayNdiru/Streamlit_Dashboard (public, accessible to graders).
