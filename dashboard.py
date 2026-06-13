import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

import plotly.graph_objects as go
import plotly.express as px

from agent_one import financial_data_gatherer
from agent_two import quantitative_data_gatherer
from agent_three import macro_risk_manager
from agent_five import valuation_analyst
from agent_six import news_sentiment_analyst
from agent_seven import risk_confidence_engine

# ==================================================

# PAGE CONFIG

# ==================================================

st.set_page_config(
page_title="AI Investment Intelligence Terminal",
page_icon="📈",
layout="wide",
initial_sidebar_state="expanded"
)

# ==================================================

# PREMIUM CSS

# ==================================================

st.markdown(
"""

<style>

.stApp{
    background-color:#0A0F1C;
}

div[data-testid="metric-container"]{
    background:#111827;
    border:1px solid #1F2937;
    padding:18px;
    border-radius:16px;
}

.block-container{
    padding-top:1rem;
}

h1,h2,h3,h4{
    color:white;
}

.buy-box{
    background:#052e16;
    border:1px solid #15803d;
    padding:18px;
    border-radius:12px;
}

.sell-box{
    background:#450a0a;
    border:1px solid #dc2626;
    padding:18px;
    border-radius:12px;
}

.hold-box{
    background:#1e293b;
    border:1px solid #475569;
    padding:18px;
    border-radius:12px;
}

</style>

""",
unsafe_allow_html=True
)

# ==================================================

# HEADER

# ==================================================

st.markdown(
"""

<h1 style='text-align:center'>
📈 AI Investment Intelligence Terminal
</h1>

<h4 style='text-align:center;color:#00D4AA'>
Multi-Agent Equity Research Platform
</h4>
""",
    unsafe_allow_html=True
)

# ==================================================

# SIDEBAR

# ==================================================

with st.sidebar:

    st.title("🧠 Research Hub")

    ticker = st.text_input(
        "Ticker",
        value="AAPL"
    ).upper()

    analyze = st.button(
        "🚀 Run Analysis",
        use_container_width=True
    )

    st.markdown("### Active Agents")
    
    st.success("Fundamental Analyst")
    st.success("Quant Analyst")
    st.success("Macro Risk Manager")
    st.success("Valuation Analyst")
    st.success("News Analyst")
    st.success("Risk Engine")

# ==================================================

# MAIN PIPELINE

# ==================================================

if analyze:

    progress = st.progress(0)

    progress.progress(10)

    fundamental_data = financial_data_gatherer(
        ticker
    )

    progress.progress(25)

    quant_data = quantitative_data_gatherer(
        ticker
    )

    progress.progress(40)

    macro_data = macro_risk_manager()

    progress.progress(55)

    valuation_data = valuation_analyst(
        ticker
    )

    progress.progress(70)

    news_data = news_sentiment_analyst(
        ticker
    )

    progress.progress(85)

    risk_data = risk_confidence_engine(
        fundamental_data,
        quant_data,
        macro_data,
        valuation_data,
        news_data
    )

    progress.progress(100)

    if not all([
        fundamental_data,
        quant_data,
        macro_data,
        valuation_data,
        news_data,
        risk_data
    ]):

        st.error(
            "One or more agents failed."
        )

        st.stop()

    st.success(
        "Research Pipeline Completed Successfully"
    )

    # ==========================================
    # COMPANY DATA
    # ==========================================

    try:

        info = yf.Ticker(
            ticker
        ).info

    except:

        info = {}

    company_name = info.get(
        "longName",
        ticker
    )

    confidence = risk_data["confidence"]

    risk_level = risk_data["risk_level"]

    strongest_agent = risk_data["strongest_agent"]

    weakest_agent = risk_data["weakest_agent"]

    valuation_signal = valuation_data[
        "valuation_signal"
    ]

    sentiment = news_data[
        "sentiment"
    ]

    sentiment_score = news_data[
        "score"
    ]

    df = quant_data["df"].copy()

    # ==========================================
    # TABS
    # ==========================================

    overview_tab, technical_tab, risk_tab = st.tabs(
        [
            "📊 Overview",
            "📈 Technical",
            "⚠️ Risk"
        ]
    )

    with overview_tab:

        # ==========================================
        # AI DECISION CENTER
        # ==========================================

        if confidence >= 80:

            signal = "STRONG BUY"

        elif confidence >= 65:

            signal = "BUY"

        elif confidence >= 50:

            signal = "HOLD"

        elif confidence >= 35:

            signal = "SELL"

        else:

            signal = "STRONG SELL"

        st.subheader(
            "🧠 AI Decision Center"
        )

        if "BUY" in signal:

            st.markdown(
                f"""
<div class="buy-box">

<h3>{company_name}</h3>

<b>Ticker:</b> {ticker}<br>

<b>Recommendation:</b> {signal}<br>

<b>Confidence:</b> {confidence:.2f}%<br>

<b>Risk Level:</b> {risk_level}

</div>
""",
                unsafe_allow_html=True
            )

        elif "SELL" in signal:

            st.markdown(
                f"""
<div class="sell-box">

<h3>{company_name}</h3>

<b>Ticker:</b> {ticker}<br>

<b>Recommendation:</b> {signal}<br>

<b>Confidence:</b> {confidence:.2f}%<br>

<b>Risk Level:</b> {risk_level}

</div>
""",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
<div class="hold-box">

<h3>{company_name}</h3>

<b>Ticker:</b> {ticker}<br>

<b>Recommendation:</b> {signal}<br>

<b>Confidence:</b> {confidence:.2f}%<br>

<b>Risk Level:</b> {risk_level}

</div>
""",
                unsafe_allow_html=True
            )

        st.markdown("---")

        # ==========================================
        # KPI DASHBOARD
        # ==========================================

        k1, k2, k3, k4 = st.columns(4)

        with k1:

            st.metric(
                "Confidence",
                f"{confidence:.1f}%"
            )

        with k2:

            st.metric(
                "Risk Level",
                risk_level
            )

        with k3:

            st.metric(
                "Valuation",
                valuation_signal
            )

        with k4:

            st.metric(
                "Sentiment",
                sentiment
            )

        st.markdown("---")

        k5, k6, k7 = st.columns(3)

        with k5:

            st.metric(
                "Strongest Agent",
                strongest_agent
            )

        with k6:

            st.metric(
                "Weakest Agent",
                weakest_agent
            )

        with k7:

            st.metric(
                "News Score",
                f"{sentiment_score}/100"
            )

        st.markdown("---")

        # ==========================================
        # FINANCIAL HEALTH
        # ==========================================

        st.subheader(
            "💰 Financial Health"
        )

        f1, f2, f3, f4 = st.columns(4)

        with f1:

            st.metric(
                "Revenue",
                f"${fundamental_data['revenue']:,.0f}"
            )

        with f2:

            st.metric(
                "Gross Margin",
                f"{fundamental_data['gross_margin']:.2f}%"
            )

        with f3:

            st.metric(
                "Operating Margin",
                f"{fundamental_data['operating_margin']:.2f}%"
            )

        with f4:

            st.metric(
                "Net Margin",
                f"{fundamental_data['net_margin']:.2f}%"
            )

        st.markdown("---")

        # ==========================================
        # FUNDAMENTAL SNAPSHOT
        # ==========================================

        st.subheader(
            "📊 Fundamental Snapshot"
        )

        snapshot_df = pd.DataFrame(
            {
                "Metric": [
                    "Gross Margin",
                    "Operating Margin",
                    "Net Margin"
                ],
                "Value": [
                    fundamental_data[
                        "gross_margin"
                    ],
                    fundamental_data[
                        "operating_margin"
                    ],
                    fundamental_data[
                        "net_margin"
                    ]
                ]
            }
        )

        fundamental_chart = px.bar(
            snapshot_df,
            x="Metric",
            y="Value",
            text="Value",
            title="Profitability Metrics"
        )

        fundamental_chart.update_layout(
            template="plotly_dark",
            height=450
        )

        st.plotly_chart(
            fundamental_chart,
            use_container_width=True
        )

    with technical_tab:
        # =========================================
        # MARKET INTELLIGENCE
        # ==========================================
        
        st.subheader(
            "📈 Market Intelligence"
        )

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["SMA20"],
            name="SMA20"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["SMA50"],
            name="SMA50"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["SMA200"],
            name="SMA200"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=650,
        xaxis_rangeslider_visible=False,
        title=f"{ticker} Price Action"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
    st.markdown("---")

    # ==========================================
    # TECHNICAL INDICATORS
    # ==========================================

    st.subheader(
        "⚙️ Technical Indicators"
    )

    t1, t2, t3, t4 = st.columns(4)

    with t1:

        st.metric(
            "RSI",
            f"{quant_data['rsi']:.2f}"
        )

    with t2:

        st.metric(
            "MACD",
            f"{quant_data['macd']:.2f}"
        )

    with t3:

        st.metric(
            "Signal Line",
            f"{quant_data['signal_line']:.2f}"
        )

    with t4:

        st.metric(
            "Current Price",
            f"${quant_data['current_price']:.2f}"
        )

    st.markdown("---")

    # ==========================================
    # AGENT INTELLIGENCE
    # ==========================================

    st.subheader(
        "🎯 Agent Intelligence"
    )

    scores_df = pd.DataFrame(
        {
            "Agent": [
                "Fundamental",
                "Quant",
                "Macro",
                "Valuation",
                "News"
            ],
            "Score": [
                risk_data["fundamental_score"],
                risk_data["quant_score"],
                risk_data["macro_score"],
                risk_data["valuation_score"],
                risk_data["sentiment_score"]
            ]
        }
    )

    col1, col2 = st.columns(2)

    with col1:

        bar_chart = px.bar(
            scores_df,
            x="Agent",
            y="Score",
            text="Score",
            title="Agent Score Comparison"
        )

        bar_chart.update_layout(
            template="plotly_dark",
            height=500
        )

        st.plotly_chart(
            bar_chart,
            use_container_width=True
        )

    with col2:

        radar_scores = scores_df["Score"].tolist()
        radar_agents = scores_df["Agent"].tolist()

        radar_scores.append(
            radar_scores[0]
        )

        radar_agents.append(
            radar_agents[0]
        )

        radar = go.Figure()

        radar.add_trace(
            go.Scatterpolar(
                r=radar_scores,
                theta=radar_agents,
                fill="toself",
                name="Agent Scores"
            )
        )

        radar.update_layout(
            template="plotly_dark",
            height=500,
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            )
        )

        st.plotly_chart(
            radar,
            use_container_width=True
        )

    st.markdown("---")

    # ==========================================
    # AGENT LEADERBOARD
    # ==========================================

    st.subheader(
        "🏆 Agent Leaderboard"
    )

    leaderboard = (
        scores_df
        .sort_values(
            "Score",
            ascending=False
        )
        .reset_index(
            drop=True
        )
    )

    leaderboard.index += 1

    st.dataframe(
        leaderboard,
        use_container_width=True
    )
    
    st.markdown("---")

    with risk_tab:

        # ==========================================
        # NEWS INTELLIGENCE
        # ==========================================
        
        st.subheader(
            "📰 News Intelligence"
        )

    st.text_area(
        "Recent Headlines",
        news_data["headlines"],
        height=250
    )

    st.markdown("---")

    # ==========================================
    # MONTE CARLO SIMULATION
    # ==========================================

    st.subheader(
        "🎲 Monte Carlo Price Simulation"
    )

    returns = (
        df["Close"]
        .pct_change()
        .dropna()
    )

    last_price = float(
        df["Close"].iloc[-1]
    )

    simulations = 500

    days = 30

    simulation_df = pd.DataFrame()

    for x in range(simulations):

        prices = [last_price]

        for y in range(days):
            
            daily_return = np.random.normal(
                
            returns.mean(),
            returns.std()
            )
            
            prices.append(
                max(
                    0,
                    prices[-1] * (1 + daily_return)
                )
            )
    simulation_df[x] = prices

    mc_fig = go.Figure()

    for column in simulation_df.columns:

        mc_fig.add_trace(
            go.Scatter(
                y=simulation_df[column],
                mode="lines",
                opacity=0.15,
                showlegend=False
            )
        )

    mc_fig.update_layout(
        template="plotly_dark",
        height=600,
        title="30-Day Monte Carlo Simulation"
    )

    st.plotly_chart(
        mc_fig,
        use_container_width=True
    )

    st.markdown("---")

    # ==========================================
    # PRICE DISTRIBUTION
    # ==========================================

    st.subheader(
        "📊 Expected Price Distribution"
    )

    final_prices = simulation_df.iloc[-1]

    hist_fig = px.histogram(
        final_prices,
        nbins=40,
        title="Projected Price Distribution (30 Days)"
    )

    hist_fig.update_layout(
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(
        hist_fig,
        use_container_width=True
    )

    expected_price = final_prices.mean()

    best_case = final_prices.max()

    worst_case = final_prices.min()

    p1, p2, p3 = st.columns(3)

    with p1:

        st.metric(
            "Expected Price",
            f"${expected_price:.2f}"
        )

    with p2:

        st.metric(
            "Best Case",
            f"${best_case:.2f}"
        )

    with p3:

        st.metric(
            "Worst Case",
            f"${worst_case:.2f}"
        )

    st.markdown("---")

    # ==========================================
    # EXECUTIVE SUMMARY
    # ==========================================

    st.subheader(
        "🧠 Executive Summary"
    )

    summary = f"""

Ticker: {ticker}

Company: {company_name}

AI Recommendation: {signal}

Confidence Score: {confidence:.2f}%

Risk Level: {risk_level}

Valuation Signal: {valuation_signal}

News Sentiment: {sentiment}

Strongest Agent: {strongest_agent}

Weakest Agent: {weakest_agent}

Expected 30-Day Price:
${expected_price:.2f}

Best Case:
${best_case:.2f}

Worst Case:
${worst_case:.2f}
"""

    st.text_area(
        "Investment Memo",
        summary,
        height=350
    )

    st.download_button(
        label="📥 Download Summary",
        data=summary,
        file_name=f"{ticker}_summary.txt",
        mime="text/plain"
    )

    st.markdown("---")

    # ==========================================
    # FOOTER
    # ==========================================

    st.markdown("---")

    st.caption(
        "AI Investment Intelligence Platform | Multi-Agent Research Terminal | Built with Python, Streamlit, Plotly & AI Agents"
    )