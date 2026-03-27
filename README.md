# 🦄 Unicorn Startup Investment Dashboard: 2021 vs 2026

A Streamlit analytics app that tracks how 2021's unicorn startups performed by 2026 — who thrived, who collapsed, and why.

**Built for:** Quantic MSBA — Communicating with Data Presentation

## Business Case

A late-stage venture investor needs to decide where to allocate capital in 2026. By analyzing what happened to the 700+ unicorn startups created during the 2021 boom, we surface clear patterns of success and failure to guide investment decisions.

## Features

- **5 Interactive Story Points** — narrative-driven dashboard with sidebar navigation
- **2021 Unicorn Census** — KPIs, top-15 bar chart, industry breakdown, country analysis
- **Winners vs Losers** — scatter plot (2021 vs 2026 valuations), top gainers/losers butterfly chart
- **Anatomy of Failure** — sunburst of value destroyed, failure category analysis
- **Growth Playbook** — growth multiples, winning industries, value-created waterfall
- **Investor Recommendation** — investment quadrant, geographic performance, actionable thesis
- **AI Chat Assistant** — ask natural-language questions about the data (powered by Groq/Llama 3.3 70B, free)

## Data Sources

- **2021:** CB Insights Unicorn List (936 companies)
- **2026:** Crunchbase Unicorn Company List (March 2026)

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

For the AI chat feature, get a free API key from [console.groq.com](https://console.groq.com) (no credit card required).

## Tech Stack

- **Streamlit** — interactive web app framework
- **Pandas** — data manipulation and analysis
- **Plotly** — interactive visualizations
- **OpenAI client + Groq** — free LLM-powered chat assistant (Llama 3.3 70B)
