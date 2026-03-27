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

### Opening (45 seconds)

> "Good [morning/afternoon]. My name is [YOUR NAME] and today I'm presenting a data-driven investment analysis built as an interactive Streamlit application."

> "Here's the scenario. Imagine you're a late-stage venture capital investor in 2021. The market is booming. Over 900 startups have just crossed a billion-dollar valuation — what we call unicorns. Combined, they're worth $2.7 trillion. The question is: where do you put your money?"

> "Now fast-forward five years to 2026. Some of those bets returned 287 times the original investment. Others went to absolute zero. This dashboard analyzes exactly what happened — who won, who lost, why — and turns those lessons into an actionable investment recommendation."

> "Let me walk you through the six story points of this dashboard."

---

### Story Point 1: The 2021 Unicorn Boom (~1.5 min)
**Page:** "1. The 2021 Unicorn Boom"

**What the audience sees:**
- 4 KPI metric cards at the top (Total Unicorns, Combined Valuation, Top Industry, Top Country)
- Horizontal bar chart: Top 15 most valued unicorns
- Side-by-side: Industry breakdown bar chart + Top 15 countries bar chart

**What to say:**

> "Let's start with the context. At the top you can see four key metrics: 936 total unicorns, $2.7 trillion in combined valuation, Fintech as the dominant industry, and the United States as the top country. These KPI cards give the audience instant context before diving into any chart."

> [Point to the bar chart] "This horizontal bar chart shows the top 15 most valued unicorns in 2021. Bytedance led at $140 billion, followed by SpaceX at $100 billion and Stripe at $95 billion. I chose a horizontal layout specifically so the company names are easy to read, and the color encoding shows which industry each company belongs to. You can immediately see that Fintech dominates — multiple companies in green."

> [Point to bottom-left chart] "On the bottom left, I've broken down all 936 unicorns by industry. The bar height shows total valuation, and the color intensity shows how many companies are in each sector. Fintech and Internet Software had the most companies, but notice that Artificial Intelligence — despite fewer companies — commanded significant total value. That's a signal we'll come back to."

> [Point to bottom-right chart] "On the right, the top 15 countries by unicorn count. The United States dominates with over 450 unicorns — more than all other countries combined. China is second, followed by India and the UK. The color intensity shows total dollar value, so you can see the US also leads in combined valuation, not just count."

> "The takeaway from this slide: 2021 was the greatest period of startup creation in history. But the question is — five years later, how much of this $2.7 trillion survived? Let's find out."

**Transition to next slide:** This sets up the dramatic contrast — the audience now has the baseline.

**Design choices to mention if asked:**
- KPI cards give instant context before any chart (pre-attentive processing)
- Horizontal bar chart chosen so company names are readable without rotation
- Color encodes Industry using Plotly's default qualitative palette for categorical distinction
- Country chart uses sequential green color intensity to encode a second variable (total value) within the same bar chart

---

### Story Point 2: Winners vs Losers (~1.5 min)
**Page:** "2. Winners vs Losers"

**What the audience sees:**
- 4 KPI cards (Collapsed count, Value Destroyed, Thriving count, Value Created)
- Scatter plot: 2021 valuation vs 2026 valuation (log scale) with a 45° "no change" reference line
- Side-by-side butterfly chart: Top 10 Value Creators vs Top 10 Value Destroyers

**What to say:**

> "Now we jump forward to 2026, and the picture is dramatically different. Look at the KPI cards at the top: 21 companies collapsed entirely. Over $100 billion in value was destroyed. But on the flip side — 30 companies are thriving, and they collectively created far more value than was lost."

> [Point to scatter plot] "This is the most important chart in the entire dashboard. Each dot is a company. The x-axis is their 2021 valuation, the y-axis is their 2026 valuation. I've added a gray diagonal line — this is the 'no change' line. Any company above this line grew in value. Any company below it shrank. And companies sitting at the very bottom? They went to zero."

> "Notice two things. First, the green 'Thriving' dots in the upper-right are far above the line — these companies didn't just grow, they grew massively. Second, the red 'Collapsed' dots are clustered at the bottom — total value destruction. I used a logarithmic scale on both axes so that companies at very different sizes — from $2 billion to $800 billion — are all visible on the same chart."

> [Scroll to butterfly chart] "Now let me make this even more concrete. This side-by-side comparison shows the top 10 value creators on the left in green, and the top 10 value destroyers on the right in red. OpenAI created $837 billion in new value — it went from a $2.9 billion startup to an $840 billion company. SpaceX added $700 billion. On the other side, FTX destroyed $25 billion through fraud, and Klarna lost $45.6 billion when it IPO'd at a fraction of its 2021 peak."

> "The pattern is already emerging: the winners won big, and they were concentrated in specific sectors. Let's dig into what killed the losers first."

**Transition to next slide:** You've established the winners vs losers. Now zoom into failures.

**Design choices to mention if asked:**
- Log scale on both axes ensures companies from $1B to $800B are all visible
- The 45° reference line is the single most important design decision — it instantly answers "did this company grow or shrink?" without reading any numbers
- Butterfly/diverging layout puts winners and losers in direct visual opposition — inspired by Cole Nussbaumer Knaflic's "Storytelling with Data" diverging bar technique
- Status colors are consistent across all pages (green=Thriving, red=Collapsed) for visual continuity

---

### Story Point 3: What Killed Them (~1.5 min)
**Page:** "3. What Killed Them"

**What the audience sees:**
- Sunburst chart: failure categories → individual companies (sized by value destroyed)
- Side-by-side: bar chart of value destroyed per company + Notable Failures callout text
- Pie chart: share of value destroyed by failure category

**What to say:**

> "Over $100 billion in value was destroyed between 2021 and 2026. But the failures weren't random. They fall into clear, identifiable categories — and that's what this page reveals."

> [Point to sunburst] "This sunburst chart organizes every failed company by its failure category. The outer ring shows individual companies; the inner ring shows the category. The size of each segment represents how much value was destroyed. You can click into any section to drill down."

> "The biggest category is Unsustainable Unit Economics — companies like Getir, Gorillas, and Convoy that were burning cash faster than they could generate revenue. Quick commerce was a $20+ billion graveyard. The second biggest is Crypto Contagion — FTX, Celsius, BlockFi, and Dapper Labs all collapsed when the crypto bubble burst. And then we have outright Fraud — FTX alone destroyed $25 billion when its CEO was convicted of stealing customer funds."

> [Point to bar chart and notable failures] "This bar chart on the left ranks every failed company by dollars lost, and the notable failures panel on the right tells the human story behind each one. FTX — $25 billion, fraud. Thrasio — $10 billion, the Amazon aggregator model was fundamentally broken. Hopin went from $7.75 billion to zero when virtual events demand disappeared after COVID. Argo AI — $7.25 billion, Ford and Volkswagen pulled funding because autonomous vehicle technology simply wasn't ready."

> [Point to pie chart] "The pie chart at the bottom summarizes the proportional share. These eight failure categories explain virtually all value destruction. And here's the crucial insight for our investor: every single one of these failures was predictable. Companies without real unit economics, companies riding temporary COVID demand, companies in the crypto speculation wave — they were all systematically punished."

> "So if that's what killed the losers, what made the winners succeed? Let's look at the other side."

**Transition to next slide:** Pivot from failure patterns to success patterns.

**Design choices to mention if asked:**
- Sunburst provides hierarchical drill-down (category → company) in one compact interactive visual
- The notable failures text panel adds qualitative narrative context that data alone cannot convey — this follows the principle of combining quantitative and qualitative storytelling
- All failure visualizations use a consistent red/orange palette to maintain visual language
- Pie chart used specifically here because we're showing parts of a whole (share of total destruction)

---

### Story Point 4: What Made Them Win (~1.5 min)
**Page:** "4. What Made Them Win"

**What the audience sees:**
- Horizontal bar chart: Top 15 winners by growth multiple (e.g., OpenAI 287x)
- Side-by-side: Industry average change % (diverging bar) + Key Success Patterns text
- Waterfall chart: cumulative value created by top 10 winners

**What to say:**

> "Now the exciting part — what made the winners win. And the patterns here are just as clear as the failures."

> [Point to growth multiple chart] "This chart ranks the top 15 companies by growth multiple — meaning how many times their valuation increased from 2021 to 2026. The standout is OpenAI at 287x. It went from a $2.9 billion research lab to an $840 billion company — the largest private company in history. But look at the rest of this list: Whatnot grew 8x, VAST Data grew 8x, Ramp grew 8.2x, ClickHouse grew 7.5x. I used growth multiple instead of absolute dollar change because that's what investors care about — return on investment."

> [Point to industry chart] "On the bottom left, I've calculated the average valuation change percentage by industry. The color scale goes from red for negative to green for positive. Artificial Intelligence leads by a wide margin, followed by Data Management and Hardware — which includes AI chip companies like Cerebras. Meanwhile, E-commerce and Consumer sectors averaged negative or flat returns. The data is clear: enterprise and infrastructure sectors crushed consumer-facing sectors."

> [Point to success patterns text] "On the right, I've distilled the data into four winning patterns. Pattern one: the AI Revolution — seven of the top ten winners are AI companies. OpenAI, Scale AI, Cerebras, ElevenLabs. Pattern two: Defense Tech — Anduril grew 6.7x as government spending surged. Pattern three: Fintech Infrastructure — Stripe, Ramp, and Revolut all had real enterprise revenue backing their valuations. Pattern four: Data Platforms — Databricks grew from $38 billion to $134 billion because every AI company needs data infrastructure."

> [Point to waterfall chart] "This waterfall chart shows the cumulative value created by the top 10 winners. Notice how just two companies — OpenAI and SpaceX — account for over $1.5 trillion of new value. The value creation is heavily concentrated at the top, which tells our investor: picking the right sector matters more than picking many companies."

> "So now we know what failed and what succeeded. Let's turn these patterns into a concrete investment recommendation."

**Transition to next slide:** You've built the evidence base. Now deliver the verdict.

**Design choices to mention if asked:**
- Growth multiple is more meaningful than absolute dollar change for investors evaluating returns
- Diverging red-to-green color scale on the industry chart leverages pre-attentive processing — the eye immediately separates winners from losers
- Waterfall chart is a visual format executives recognize from financial reporting — it communicates cumulative contribution naturally
- The text panel pairs quantitative patterns with named companies, making abstract trends concrete

---

### Story Point 5: Investor Recommendation (~1.5 min)
**Page:** "5. Investor Recommendation"

**What the audience sees:**
- Investment quadrant scatter plot (Growth % vs Current Size) with labeled quadrants
- Geographic performance bar chart
- Two-column INVEST IN / AVOID summary tables with specific sector advice

**What to say:**

> "This is where everything comes together — the actionable recommendation for our investor."

> [Point to quadrant chart] "This is the signature chart of the dashboard — an investment quadrant. The x-axis shows each company's current 2026 valuation, and the y-axis shows how much they grew since 2021. The dashed lines divide the chart at the median, creating four quadrants."

> "Upper-left is where you want to be — high growth, reasonable size. These are companies like Ramp, VAST Data, Anduril, and Whatnot that have proven massive growth but haven't reached the scale of a Databricks or SpaceX yet. They represent the best risk-adjusted bets for a late-stage investor."

> "Upper-right is proven winners — OpenAI, SpaceX, Databricks. They've already grown massively, so the upside is more limited, but they're safe bets. Bottom-left — marked with the caution symbol — is low growth, small size. Companies here are stagnating and should be avoided."

> [Point to geographic chart] "The geographic chart confirms that the United States dominates value creation by a wide margin. But there's a notable outlier — Israel, driven almost entirely by Wiz, a cloud security company that turned down a $23 billion acquisition from Google. Geography matters: the US AI and defense tech ecosystems have no global equivalent right now."

> [Point to INVEST IN / AVOID tables] "And here's the final thesis, laid out in a format an investment committee can act on immediately. On the left — INVEST IN: AI Infrastructure, the foundation of the AI economy, with 287x growth from OpenAI as proof. Defense Tech, driven by government spending surge. Data Platforms, essential for AI training. Enterprise Fintech, revenue-backed not hype-backed."

> "On the right — AVOID: Crypto Speculation because of fraud and contagion risk. Quick Commerce because the unit economics never worked. Virtual Events because COVID demand was temporary. And Founder-Hype companies where governance failures destroyed billions."

> [Read the key takeaway] "Let me read the key takeaway directly: Companies with enterprise revenue models, AI-native products, and strong fundamentals outperformed hype-driven, consumer-centric startups by 10 to 100x. The 2021 bubble punished companies without real unit economics. Investors in 2026 should demand proof of durable revenue before writing checks."

**Transition to next slide:** You've delivered the core recommendation. The LLM demo is the cherry on top.

**Design choices to mention if asked:**
- Quadrant chart mirrors the BCG matrix / GE-McKinsey matrix that investors and strategy consultants already use — familiar = trustworthy
- Median-based dividing lines ensure statistically balanced quadrants, not arbitrary thresholds
- INVEST IN / AVOID tables are deliberately formatted as sector → rationale → examples so an executive can act on them in a meeting

---

### Story Point 6: Ask the Data (Live Demo, ~45 sec)
**Page:** "6. Ask the Data 🤖"

**What to say:**

> "The last feature of this dashboard goes beyond static charts. I've integrated a large language model — specifically Llama 3.3 70B running on Groq — that allows stakeholders to ask natural-language questions about the data in real time. And critically, this is completely free — no API costs, no credit card required."

> "The AI assistant has full context on all 93 tracked companies — their valuations, growth rates, failure categories, and success patterns. Let me show you a quick example."

> [Type or paste: "What do the top 5 winners have in common?"] "I'm asking: what do the top five winners have in common? And you can see the model responds with a data-backed answer, citing specific numbers from our dataset."

> "This feature was inspired by the assignment's suggestion to incorporate a large-language-model assistant, and it demonstrates how conversational business intelligence can make data exploration accessible to non-technical stakeholders — they don't need to know SQL or Python, they just ask a question in plain English."

**Demo tip:** Have the Groq API key already pasted in the sidebar before recording. Pre-type your question so you can submit it immediately. Groq responses typically arrive in under 2 seconds.

---

### Closing (45 seconds)

> "Let me bring it all together. In 2021, cheap capital created over 900 unicorn startups worth $2.7 trillion. Five years later, the data reveals a clear verdict."

> "The losers shared predictable traits — unsustainable unit economics, crypto exposure, temporary COVID demand, and governance failures. They destroyed over $100 billion."

> "The winners shared equally clear traits — enterprise revenue models, AI-native products, defense tech demand, and data infrastructure. They created over $1.5 trillion in new value."

> "For our investor, the recommendation is specific and actionable: allocate capital to AI infrastructure, defense tech, data platforms, and enterprise fintech. Avoid crypto speculation, quick commerce, and hype-driven companies."

> "The data doesn't just tell a story — it tells you exactly what to do next. Thank you."

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
