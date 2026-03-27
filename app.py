"""
Startup Unicorn Investment Dashboard: 2021 vs 2026
Communicating with Data Presentation — Quantic MSBA

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

try:
    from openai import OpenAI
    LLM_AVAILABLE = True
except ImportError:
    LLM_AVAILABLE = False

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Unicorn Startups: 2021 vs 2026",
    page_icon="🦄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# CUSTOM CSS
# ──────────────────────────────────────────────
st.markdown("""
<style>
/* ── Dark gradient sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
}
section[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}
section[data-testid="stSidebar"] a {
    color: #bb86fc !important;
}

/* ── Styled metric cards ── */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    padding: 16px 20px;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
}
div[data-testid="stMetric"] label {
    color: rgba(255,255,255,0.8) !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
}
div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
}

/* ── Page title styling ── */
h1 {
    background: linear-gradient(90deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800 !important;
}

/* ── Blockquote accent ── */
blockquote {
    border-left: 4px solid #764ba2 !important;
    background: rgba(118, 75, 162, 0.05);
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
}

/* ── Subheader styling ── */
h2, h3 {
    color: #e0e0e0 !important;
}

/* ── Chat input styling ── */
.stChatInput textarea {
    border-radius: 12px !important;
}

/* ── Divider ── */
hr {
    border-color: rgba(118, 75, 162, 0.3) !important;
}
</style>
""", unsafe_allow_html=True)

STATUS_COLORS = {
    "Thriving": "#2E8B57",
    "Stable": "#DAA520",
    "Declining": "#FF8C00",
    "Collapsed": "#DC143C",
    "IPO": "#4169E1",
    "Acquired": "#8A2BE2",
}

FAILURE_COLORS = {
    "Fraud": "#8B0000",
    "Crypto Contagion": "#DC143C",
    "Post-COVID Demand Drop": "#FF8C00",
    "Unsustainable Unit Economics": "#FA8072",
    "Technology Not Ready": "#FF69B4",
    "Market Correction": "#CD5C5C",
    "Governance & Mismanagement": "#B22222",
    "Competitive Displacement": "#FF4500",
}

# ──────────────────────────────────────────────
# LOAD DATA
# ──────────────────────────────────────────────
@st.cache_data
def load_data():
    base = os.path.dirname(__file__)
    data_dir = os.path.join(base, "data")

    # Full 2021 dataset
    df_2021 = pd.read_csv(os.path.join(data_dir, "startups_2021.csv"))

    # Merged comparison (pre-computed with all derived columns)
    merged_path = os.path.join(data_dir, "startups_merged.csv")
    if os.path.exists(merged_path):
        df_merged = pd.read_csv(merged_path)
    else:
        # Fallback: build merge from raw files
        df_2026_raw = pd.read_csv(os.path.join(data_dir, "startups_2026.csv"))
        df_merged = df_2021.merge(
            df_2026_raw, on="Company", how="inner", suffixes=("_2021", "_2026")
        )
        df_merged.rename(
            columns={
                "valuation_usd_b": "Valuation_2021_B",
                "valuation_2026_usd_b": "Valuation_2026_B",
                "status": "Status",
                "reason_for_change": "Reason_For_Change",
                "failure_category": "Failure_Category",
                "success_category": "Success_Category",
            },
            inplace=True,
        )
        df_merged["Valuation_Change_B"] = (
            df_merged["Valuation_2026_B"] - df_merged["Valuation_2021_B"]
        )
        df_merged["Valuation_Change_Pct"] = (
            (df_merged["Valuation_Change_B"] / df_merged["Valuation_2021_B"]) * 100
        ).fillna(0)
        df_merged["Growth_Multiple"] = (
            df_merged["Valuation_2026_B"] / df_merged["Valuation_2021_B"]
        ).fillna(0).replace([float("inf")], 0)
        df_merged["Value_Created_B"] = df_merged["Valuation_Change_B"].clip(lower=0)
        df_merged["Value_Destroyed_B"] = (-df_merged["Valuation_Change_B"]).clip(lower=0)
        df_merged["Industry_2021"] = df_merged.get("Industry", df_merged.get("Industry_2021", ""))

    return df_2021, df_merged


df_2021, df_merged = load_data()

# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────
st.sidebar.markdown(
    "<h2 style='text-align:center; margin-bottom:0;'>🦄</h2>"
    "<h3 style='text-align:center; margin-top:0; "
    "background:linear-gradient(90deg,#667eea,#bb86fc); "
    "-webkit-background-clip:text; -webkit-text-fill-color:transparent;'>"
    "Unicorn Dashboard</h3>",
    unsafe_allow_html=True,
)
st.sidebar.caption("2021 vs 2026 · Investment Intelligence")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Story Points",
    [
        "📈 The 2021 Unicorn Boom",
        "⚖️ Winners vs Losers",
        "💀 What Killed Them",
        "🚀 What Made Them Win",
        "🎯 Investor Recommendation",
        "🤖 Ask the Data",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown("**📊 Data Sources**")
st.sidebar.markdown(
    "- 2021: [CB Insights Global Unicorn Club](https://www.cbinsights.com/research-unicorn-companies) "
    "(936 companies, scraped Q4 2021)"
)
st.sidebar.markdown(
    "- 2026: [Crunchbase Unicorn Board](https://news.crunchbase.com/unicorn-company-list) "
    "(March 2026)"
)
st.sidebar.markdown(
    "- Supplementary: [PitchBook](https://pitchbook.com/), "
    "SEC/bankruptcy filings, company press releases"
)
st.sidebar.markdown("---")
st.sidebar.markdown("*Quantic MSBA — Communicating with Data*")


# ══════════════════════════════════════════════
# STORY POINT 1: THE 2021 UNICORN BOOM
# ══════════════════════════════════════════════
if page == "📈 The 2021 Unicorn Boom":
    st.title("📈 The 2021 Unicorn Boom")
    st.markdown(
        "> In 2021, cheap capital and post-COVID digital acceleration created **700+ unicorn startups** "
        "worth a combined **$2.7 trillion+**. It was the greatest period of startup creation in history."
    )

    # KPI row
    col1, col2, col3, col4 = st.columns(4)
    total_val = df_2021["valuation_usd_b"].sum()
    col1.metric("Total Unicorns", f"{len(df_2021):,}")
    col2.metric("Combined Valuation", f"${total_val:,.0f}B")
    col3.metric("Top Industry", df_2021["Industry"].mode()[0])
    col4.metric("Top Country", df_2021["Country"].mode()[0])

    # Top 15 bar chart
    st.subheader("Top 15 Most Valued Unicorns in 2021")
    top15 = df_2021.nlargest(15, "valuation_usd_b")
    fig1 = px.bar(
        top15.sort_values("valuation_usd_b"),
        x="valuation_usd_b",
        y="Company",
        orientation="h",
        color="Industry",
        text="valuation_usd_b",
        labels={"valuation_usd_b": "Valuation ($B)", "Company": ""},
        height=500,
    )
    fig1.update_traces(texttemplate="$%{text:.1f}B", textposition="outside")
    fig1.update_layout(xaxis_title="Valuation ($ Billion)", showlegend=True)
    st.plotly_chart(fig1, use_container_width=True)

    # Industry treemap
    st.subheader("Unicorn Landscape by Industry & Valuation Band")
    col_a, col_b = st.columns(2)

    with col_a:
        ind_bar = (
            df_2021.groupby("Industry")
            .agg(count=("Company", "count"), total_val=("valuation_usd_b", "sum"))
            .reset_index()
            .sort_values("total_val", ascending=False)
        )
        fig_ind_bar = px.bar(
            ind_bar,
            x="Industry",
            y="total_val",
            color="count",
            color_continuous_scale="Greens",
            text="count",
            title="Unicorns by Industry (Size = Total Valuation)",
            labels={"total_val": "Total Valuation ($B)", "count": "# Companies"},
            height=450,
        )
        fig_ind_bar.update_traces(texttemplate="%{text}", textposition="outside")
        fig_ind_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_ind_bar, use_container_width=True)

    with col_b:
        country_agg = (
            df_2021.groupby("Country")
            .agg(count=("Company", "count"), total_val=("valuation_usd_b", "sum"))
            .reset_index()
            .nlargest(15, "count")
        )
        fig_country = px.bar(
            country_agg.sort_values("count"),
            x="count",
            y="Country",
            orientation="h",
            color="total_val",
            color_continuous_scale="Greens",
            title="Top 15 Countries by Unicorn Count",
            labels={"count": "Number of Unicorns", "total_val": "Total Value ($B)"},
            height=450,
        )
        st.plotly_chart(fig_country, use_container_width=True)


# ══════════════════════════════════════════════
# STORY POINT 2: WINNERS VS LOSERS
# ══════════════════════════════════════════════
elif page == "⚖️ Winners vs Losers":
    st.title("⚖️ Winners vs Losers: The 2021→2026 Shift")
    st.markdown(
        "> Five years later, the landscape is dramatically different. Some companies grew **100x+**, "
        "while others lost **everything**. Here's how $2.7T in value was redistributed."
    )

    # Exclude IPO/Acquired for cleaner comparison
    df_active = df_merged[~df_merged["Status"].isin(["IPO", "Acquired"])].copy()

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    collapsed = df_active[df_active["Status"] == "Collapsed"]
    thriving = df_active[df_active["Status"] == "Thriving"]
    col1.metric("Companies Collapsed", f"{len(collapsed)}")
    col2.metric("Value Destroyed", f"${df_active['Value_Destroyed_B'].sum():,.1f}B")
    col3.metric("Companies Thriving", f"{len(thriving)}")
    col4.metric("Value Created", f"${df_active['Value_Created_B'].sum():,.1f}B")

    # Scatter plot: 2021 vs 2026
    st.subheader("2021 Valuation vs 2026 Valuation")
    fig_scatter = px.scatter(
        df_active[df_active["Valuation_2021_B"] > 0],
        x="Valuation_2021_B",
        y="Valuation_2026_B",
        color="Status",
        color_discrete_map=STATUS_COLORS,
        size="Valuation_2021_B",
        hover_name="Company",
        hover_data=["Reason_For_Change", "Growth_Multiple"],
        labels={
            "Valuation_2021_B": "2021 Valuation ($B)",
            "Valuation_2026_B": "2026 Valuation ($B)",
        },
        height=550,
        log_x=True,
        log_y=True,
    )
    # Add 45-degree reference line
    max_val = max(
        df_active["Valuation_2021_B"].max(), df_active["Valuation_2026_B"].max()
    )
    fig_scatter.add_trace(
        go.Scatter(
            x=[0.1, max_val],
            y=[0.1, max_val],
            mode="lines",
            line=dict(dash="dash", color="gray"),
            name="No Change Line",
            showlegend=True,
        )
    )
    fig_scatter.add_annotation(
        x=2, y=2.3, text="Above line = GREW", showarrow=False, font=dict(color="green")
    )
    fig_scatter.add_annotation(
        x=2, y=1.7, text="Below line = SHRANK", showarrow=False, font=dict(color="red")
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Butterfly chart: top gainers vs losers
    st.subheader("Top 20 Biggest Movers (Absolute Change)")
    top_gainers = df_active.nlargest(10, "Value_Created_B")
    top_losers = df_active.nlargest(10, "Value_Destroyed_B")

    col_l, col_r = st.columns(2)
    with col_l:
        fig_gain = px.bar(
            top_gainers.sort_values("Value_Created_B"),
            x="Value_Created_B",
            y="Company",
            orientation="h",
            color="Success_Category",
            text="Value_Created_B",
            title="🟢 Top 10 Value Creators",
            labels={"Value_Created_B": "Value Added ($B)", "Company": ""},
            height=400,
            color_discrete_sequence=px.colors.sequential.Greens_r,
        )
        fig_gain.update_traces(texttemplate="+$%{text:.0f}B", textposition="outside")
        st.plotly_chart(fig_gain, use_container_width=True)

    with col_r:
        fig_lose = px.bar(
            top_losers.sort_values("Value_Destroyed_B"),
            x="Value_Destroyed_B",
            y="Company",
            orientation="h",
            color="Failure_Category",
            text="Value_Destroyed_B",
            title="🔴 Top 10 Value Destroyers",
            labels={"Value_Destroyed_B": "Value Lost ($B)", "Company": ""},
            height=400,
            color_discrete_map=FAILURE_COLORS,
        )
        fig_lose.update_traces(texttemplate="-$%{text:.0f}B", textposition="outside")
        st.plotly_chart(fig_lose, use_container_width=True)


# ══════════════════════════════════════════════
# STORY POINT 3: WHAT KILLED THEM
# ══════════════════════════════════════════════
elif page == "💀 What Killed Them":
    st.title("💀 What Killed Them: Anatomy of Failure")
    st.markdown(
        "> Over **$100B+ in value was destroyed** between 2021 and 2026. "
        "The causes fall into clear patterns: **fraud, crypto contagion, post-COVID demand collapse**, "
        "and **unsustainable unit economics**."
    )

    df_failed = df_merged[
        df_merged["Status"].isin(["Collapsed", "Declining"])
    ].copy()
    df_failed = df_failed[df_failed["Failure_Category"].notna() & (df_failed["Failure_Category"] != "")]

    # Failure category sunburst
    st.subheader("Value Destroyed by Failure Category")
    fig_sun = px.sunburst(
        df_failed,
        path=["Failure_Category", "Company"],
        values="Value_Destroyed_B",
        color="Failure_Category",
        color_discrete_map=FAILURE_COLORS,
        title="Where Did the Money Go? (Size = Value Destroyed)",
        height=500,
    )
    st.plotly_chart(fig_sun, use_container_width=True)

    # Detailed table
    st.subheader("Collapsed Companies Detail")
    col_a, col_b = st.columns([2, 1])

    with col_a:
        fig_bar = px.bar(
            df_failed.sort_values("Value_Destroyed_B", ascending=False),
            x="Company",
            y="Value_Destroyed_B",
            color="Failure_Category",
            color_discrete_map=FAILURE_COLORS,
            hover_data=["Reason_For_Change"],
            title="Value Destroyed Per Company ($B)",
            labels={"Value_Destroyed_B": "Value Lost ($B)", "Company": ""},
            height=450,
        )
        fig_bar.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_b:
        st.markdown("### 🔍 Notable Failures")
        st.markdown(
            """
            **FTX ($25B → $0)** — Massive fraud; CEO convicted

            **Argo AI ($7.25B → $0)** — Ford/VW pulled funding; autonomous tech not ready

            **Hopin ($7.75B → $0)** — Virtual events demand evaporated post-COVID

            **Vice Media ($5.7B → $0)** — Digital media economics failed

            **Celsius ($3B → $0)** — Crypto lending collapse; CEO arrested

            **Convoy ($2.75B → $0)** — Digital freight; high burn rate

            **Thrasio ($10B → $0)** — Amazon aggregator model fundamentally broken
            """
        )

    # Summary by category
    st.subheader("Failure Categories Summary")
    cat_summary = (
        df_failed.groupby("Failure_Category")
        .agg(
            Companies=("Company", "count"),
            Total_Value_Lost=("Value_Destroyed_B", "sum"),
        )
        .reset_index()
        .sort_values("Total_Value_Lost", ascending=False)
    )
    fig_pie = px.pie(
        cat_summary,
        values="Total_Value_Lost",
        names="Failure_Category",
        title="Share of Value Destroyed by Category",
        color="Failure_Category",
        color_discrete_map=FAILURE_COLORS,
        height=400,
    )
    st.plotly_chart(fig_pie, use_container_width=True)


# ══════════════════════════════════════════════
# STORY POINT 4: WHAT MADE THEM WIN
# ══════════════════════════════════════════════
elif page == "🚀 What Made Them Win":
    st.title("🚀 What Made Them Win: The Growth Playbook")
    st.markdown(
        "> The biggest winners share clear patterns: **AI/LLM revolution, enterprise revenue models, "
        "defense tech demand, and data infrastructure**. Companies with real revenue and strong moats "
        "dramatically outperformed hype-driven startups."
    )

    df_winners = df_merged[df_merged["Status"] == "Thriving"].copy()
    df_winners = df_winners[df_winners["Valuation_Change_B"] > 0]

    # Top winners by growth multiple
    st.subheader("Top 15 Winners by Growth Multiple (2021→2026)")
    top_multi = df_winners.nlargest(15, "Growth_Multiple")
    fig_multi = px.bar(
        top_multi.sort_values("Growth_Multiple"),
        x="Growth_Multiple",
        y="Company",
        orientation="h",
        color="Success_Category",
        text="Growth_Multiple",
        labels={"Growth_Multiple": "Growth Multiple (x)", "Company": ""},
        height=550,
        color_discrete_sequence=px.colors.sequential.Greens_r,
    )
    fig_multi.update_traces(texttemplate="%{text:.1f}x", textposition="outside")
    st.plotly_chart(fig_multi, use_container_width=True)

    # Winning industries
    st.subheader("Winning vs Losing Industries")
    col_l, col_r = st.columns(2)

    with col_l:
        df_active = df_merged[~df_merged["Status"].isin(["IPO", "Acquired"])].copy()
        ind_perf = (
            df_active.groupby("Industry_2021")
            .agg(
                avg_change=("Valuation_Change_Pct", "mean"),
                count=("Company", "count"),
                total_created=("Value_Created_B", "sum"),
            )
            .reset_index()
        )
        ind_perf = ind_perf[ind_perf["count"] >= 2]  # at least 2 companies
        ind_perf = ind_perf.sort_values("avg_change", ascending=False)

        fig_ind = px.bar(
            ind_perf,
            x="avg_change",
            y="Industry_2021",
            orientation="h",
            color="avg_change",
            color_continuous_scale=["red", "yellow", "green"],
            title="Average Valuation Change % by Industry",
            labels={"avg_change": "Avg Change %", "Industry_2021": ""},
            height=400,
        )
        st.plotly_chart(fig_ind, use_container_width=True)

    with col_r:
        st.markdown("### 🏆 Key Success Patterns")
        st.markdown(
            """
            **1. AI Revolution (7 of top 10 winners)**
            - OpenAI: $2.9B → $840B (287x)
            - Scale AI: $7.3B → $29B (4x)
            - Cerebras: $4B → $23B (5.75x)

            **2. Defense Tech Surge**
            - Anduril: $4.6B → $31B (6.7x)
            - Applied Intuition: $3.6B → $15B (4.2x)

            **3. Fintech Infrastructure**
            - Stripe: $95B → $159B
            - Ramp: $3.9B → $32B (8.2x)
            - Revolut: $33B → $75B

            **4. Data Infrastructure**
            - Databricks: $38B → $134B (3.5x)
            - VAST Data: $3.7B → $30B (8.1x)
            - ClickHouse: $2B → $15B (7.5x)
            """
        )

    # Value created waterfall
    st.subheader("Total Value Created by Top 10 Winners")
    top10_val = df_winners.nlargest(10, "Value_Created_B")
    fig_water = go.Figure(
        go.Waterfall(
            orientation="v",
            x=top10_val["Company"],
            y=top10_val["Value_Created_B"],
            text=[f"+${v:.0f}B" for v in top10_val["Value_Created_B"]],
            textposition="outside",
            connector=dict(line=dict(color="rgb(63, 63, 63)")),
            increasing=dict(marker=dict(color="#2E8B57")),
        )
    )
    fig_water.update_layout(
        title="Value Created by Top 10 Winners ($B)",
        yaxis_title="Value Created ($B)",
        height=400,
    )
    st.plotly_chart(fig_water, use_container_width=True)


# ══════════════════════════════════════════════
# STORY POINT 5: INVESTOR RECOMMENDATION
# ══════════════════════════════════════════════
elif page == "🎯 Investor Recommendation":
    st.title("🎯 Investor Recommendation: Where to Bet in 2026")
    st.markdown(
        "> Based on five years of unicorn data, here's where a late-stage investor should — "
        "and shouldn't — allocate capital."
    )

    df_active = df_merged[
        (~df_merged["Status"].isin(["IPO", "Acquired"]))
        & (df_merged["Valuation_2026_B"] > 0)
        & (df_merged["Valuation_2021_B"] > 0)
    ].copy()

    # Quadrant chart
    st.subheader("Investment Quadrant: Growth Rate vs Current Size")
    median_val = df_active["Valuation_2026_B"].median()
    median_chg = df_active["Valuation_Change_Pct"].median()

    fig_quad = px.scatter(
        df_active,
        x="Valuation_2026_B",
        y="Valuation_Change_Pct",
        color="Status",
        color_discrete_map=STATUS_COLORS,
        size="Valuation_2026_B",
        hover_name="Company",
        hover_data=["Reason_For_Change", "Industry_2021"],
        text="Company",
        labels={
            "Valuation_2026_B": "Current Valuation 2026 ($B)",
            "Valuation_Change_Pct": "Valuation Change (%)",
        },
        height=600,
    )
    fig_quad.update_traces(textposition="top center", textfont_size=9)
    # Quadrant lines
    fig_quad.add_hline(y=median_chg, line_dash="dash", line_color="gray")
    fig_quad.add_vline(x=median_val, line_dash="dash", line_color="gray")
    # Quadrant labels
    fig_quad.add_annotation(
        x=median_val * 0.3, y=median_chg + 500,
        text="⭐ HIGH GROWTH\nREASONABLE SIZE\n(Best Bets)", showarrow=False,
        font=dict(size=12, color="green"),
    )
    fig_quad.add_annotation(
        x=max(df_active["Valuation_2026_B"]) * 0.7, y=median_chg + 500,
        text="🏆 HIGH GROWTH\nLARGE CAP\n(Proven Winners)", showarrow=False,
        font=dict(size=12, color="blue"),
    )
    fig_quad.add_annotation(
        x=median_val * 0.3, y=median_chg - 50,
        text="⚠️ LOW GROWTH\nSMALL SIZE\n(Caution)", showarrow=False,
        font=dict(size=12, color="orange"),
    )
    st.plotly_chart(fig_quad, use_container_width=True)

    # Geographic analysis
    st.subheader("Geographic Performance")
    df_geo = df_active.copy()
    country_perf = (
        df_geo.groupby("Country")
        .agg(
            avg_change=("Valuation_Change_Pct", "mean"),
            total_created=("Value_Created_B", "sum"),
            count=("Company", "count"),
        )
        .reset_index()
    )
    country_perf = country_perf[country_perf["count"] >= 2]

    fig_geo = px.bar(
        country_perf.sort_values("total_created", ascending=False).head(10),
        x="Country",
        y="total_created",
        color="avg_change",
        color_continuous_scale=["red", "yellow", "green"],
        title="Total Value Created by Country ($B)",
        labels={"total_created": "Value Created ($B)", "avg_change": "Avg Change %"},
        height=400,
    )
    st.plotly_chart(fig_geo, use_container_width=True)

    # Final recommendations
    st.subheader("📋 Investment Thesis Summary")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            ### ✅ INVEST IN
            | Sector | Why | Example Companies |
            |--------|-----|-------------------|
            | **AI Infrastructure** | Foundation of the AI economy; 287x growth (OpenAI) | OpenAI, Scale AI, Cerebras, ElevenLabs |
            | **Defense Tech** | Government spending surge; strong moats | Anduril, Applied Intuition |
            | **Data Platforms** | Essential for AI training & enterprise analytics | Databricks, VAST Data, ClickHouse |
            | **Enterprise Fintech** | Revenue-backed, not hype-backed | Stripe, Ramp, Revolut, Deel |
            """
        )

    with col2:
        st.markdown(
            """
            ### ❌ AVOID
            | Sector | Why | Cautionary Tales |
            |--------|-----|------------------|
            | **Crypto Speculation** | Fraud, contagion, regulatory risk | FTX, Celsius, BlockFi |
            | **Quick Commerce** | Unsustainable unit economics | Gorillas, Getir, goPuff |
            | **Virtual Events** | Post-COVID demand collapsed | Hopin, Clubhouse |
            | **Founder-Hype Companies** | Governance failures | Better.com, Bolt, BYJU's |
            """
        )

    st.markdown("---")
    st.markdown(
        "### 🔑 Key Takeaway\n"
        "> **Companies with enterprise revenue models, AI-native products, and strong fundamentals "
        "outperformed hype-driven, consumer-centric startups by 10-100x.** "
        "The 2021 bubble punished companies without real unit economics — "
        "investors in 2026 should demand proof of durable revenue before writing checks."
    )

    st.markdown("---")
    st.caption(
        "Data Sources: "
        "[CB Insights Global Unicorn Club](https://www.cbinsights.com/research-unicorn-companies) (2021, 936 companies) · "
        "[Crunchbase Unicorn Board](https://news.crunchbase.com/unicorn-company-list) (March 2026) · "
        "Supplementary data from [PitchBook](https://pitchbook.com/), SEC/bankruptcy filings, and company press releases. "
        "Dashboard created for Quantic MSBA — Communicating with Data Presentation."
    )


# ══════════════════════════════════════════════
# STORY POINT 6: ASK THE DATA (LLM ASSISTANT)
# ══════════════════════════════════════════════
elif page == "🤖 Ask the Data":
    st.title("🤖 Ask the Data: AI-Powered Insights")
    st.markdown(
        "> Use natural language to ask questions about the unicorn datasets. "
        "Powered by Groq (free, Llama 3.3 70B), this assistant has full context on all 936 unicorns "
        "and the 2021→2026 comparison data."
    )

    # ── Load API key from .streamlit/secrets.toml ──
    if not LLM_AVAILABLE:
        st.error("The `openai` package is not installed. Run: `pip install openai`")
        st.stop()

    api_key = st.secrets.get("GROQ_API_KEY", "")
    if not api_key:
        st.error(
            "Groq API key not found. Add it to `.streamlit/secrets.toml`:\n\n"
            '```\nGROQ_API_KEY = "gsk_your_key_here"\n```'
        )
        st.stop()

    st.markdown(
        "**Example questions you can ask:**\n"
        "- Which industries had the highest failure rate between 2021 and 2026?\n"
        "- What do the top 5 winners have in common?\n"
        "- How much total value was destroyed by crypto-related companies?\n"
        "- Compare the performance of US vs non-US unicorns.\n"
        "- What investment advice would you give based on this data?"
    )

    # ── Build data context for the LLM (compact to stay within free tier) ──
    @st.cache_data
    def build_data_context(_df_2021, _df_merged):
        total_2021 = len(_df_2021)
        total_val_2021 = _df_2021["valuation_usd_b"].sum()
        top_industries = _df_2021["Industry"].value_counts().head(5).to_dict()
        top_countries = _df_2021["Country"].value_counts().head(5).to_dict()

        status_counts = _df_merged["Status"].value_counts().to_dict()
        total_created = _df_merged["Value_Created_B"].sum()
        total_destroyed = _df_merged["Value_Destroyed_B"].sum()

        # Compact: top 10 winners
        winners = _df_merged[_df_merged["Status"] == "Thriving"].nlargest(10, "Value_Created_B")
        w_lines = "\n".join(
            f"- {r.Company}: ${r.Valuation_2021_B}B→${r.Valuation_2026_B}B ({r.Growth_Multiple:.1f}x) [{r.Success_Category}]"
            for _, r in winners.iterrows()
        )

        # Compact: top 10 losers
        losers = _df_merged[_df_merged["Value_Destroyed_B"] > 0].nlargest(10, "Value_Destroyed_B")
        l_lines = "\n".join(
            f"- {r.Company}: ${r.Valuation_2021_B}B→${r.Valuation_2026_B}B lost ${r.Value_Destroyed_B:.1f}B [{r.Failure_Category}]"
            for _, r in losers.iterrows()
        )

        # Compact: failure categories
        fail_df = _df_merged[_df_merged["Failure_Category"].notna() & (_df_merged["Failure_Category"] != "")]
        fc = fail_df.groupby("Failure_Category").agg(
            n=("Company", "count"), lost=("Value_Destroyed_B", "sum")
        ).sort_values("lost", ascending=False)
        fc_lines = "\n".join(f"- {cat}: {r.n} companies, ${r.lost:.1f}B lost" for cat, r in fc.iterrows())

        # Compact: all 93 companies (just name, status, change)
        all_cos = "\n".join(
            f"- {r.Company} [{r.Status}] ${r.Valuation_2021_B}B→${r.Valuation_2026_B}B ({r.Industry_2021}, {r.Country})"
            for _, r in _df_merged.iterrows()
        )

        return f"""You are a data analyst for a Unicorn Startup Dashboard.

2021 Census: {total_2021} unicorns, ${total_val_2021:,.0f}B total.
Top industries: {top_industries}
Top countries: {top_countries}

2021→2026 Comparison ({len(_df_merged)} tracked): {status_counts}
Value created: ${total_created:,.0f}B | Value destroyed: ${total_destroyed:,.0f}B

Top 10 Winners:
{w_lines}

Top 10 Losers:
{l_lines}

Failure Categories:
{fc_lines}

All Tracked Companies:
{all_cos}

Answer accurately and concisely. Cite specific numbers."""

    system_prompt = build_data_context(df_2021, df_merged)

    # ── Configure Groq (OpenAI-compatible API) ──
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )
    MODEL_ID = "llama-3.3-70b-versatile"

    # ── Chat interface ──
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Display chat history
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    if prompt := st.chat_input("Ask a question about the unicorn data..."):
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call Groq
        with st.chat_message("assistant"):
            with st.spinner("Analyzing data..."):
                try:
                    messages = [
                        {"role": "system", "content": system_prompt},
                    ] + [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.chat_messages
                    ]
                    response = client.chat.completions.create(
                        model=MODEL_ID,
                        messages=messages,
                        temperature=0.3,
                        max_tokens=1000,
                    )
                    answer = response.choices[0].message.content
                    st.markdown(answer)
                    st.session_state.chat_messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error: {e}")

    # Clear chat button
    if st.session_state.chat_messages:
        if st.button("Clear Chat"):
            st.session_state.chat_messages = []
            st.rerun()
