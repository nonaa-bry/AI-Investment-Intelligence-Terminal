# ============================================
# MASTER ORCHESTRATOR
# ============================================

from pdf_generator import generate_pdf

from agent_one import financial_data_gatherer
from agent_two import quantitative_data_gatherer
from agent_three import macro_risk_manager
from agent_four import final_decision_engine
from agent_five import valuation_analyst
from agent_six import news_sentiment_analyst
from agent_seven import risk_confidence_engine


# ============================================
# INPUT
# ============================================

ticker = input(
    "Enter Stock Ticker: "
).strip().upper()

print("\nRUNNING ALL AGENTS...\n")


# ============================================
# AGENT 1
# ============================================

fundamental_data = financial_data_gatherer(
    ticker
)

if not fundamental_data:

    raise Exception(
        "Agent 1 Failed"
    )


# ============================================
# AGENT 2
# ============================================

quant_data = quantitative_data_gatherer(
    ticker
)

if not quant_data:

    raise Exception(
        "Agent 2 Failed"
    )


# ============================================
# AGENT 3
# ============================================

macro_data = macro_risk_manager()

if not macro_data:

    raise Exception(
        "Agent 3 Failed"
    )


# ============================================
# AGENT 5
# ============================================

valuation_data = valuation_analyst(
    ticker
)

if not valuation_data:

    raise Exception(
        "Agent 5 Failed"
    )


# ============================================
# AGENT 6
# ============================================

news_data = news_sentiment_analyst(
    ticker
)

if not news_data:

    raise Exception(
        "Agent 6 Failed"
    )


# ============================================
# AGENT 7
# ============================================

risk_data = risk_confidence_engine(

    fundamental_data,

    quant_data,

    macro_data,

    valuation_data,

    news_data
)

if not risk_data:

    raise Exception(
        "Agent 7 Failed"
    )


# ============================================
# AGENT 4
# ============================================

final_report = final_decision_engine(

    ticker=ticker,

    confidence=risk_data["confidence"],

    risk_level=
    risk_data["risk_level"],

    strongest_agent=
    risk_data["strongest_agent"],

    weakest_agent=
    risk_data["weakest_agent"],

    fundamental_report=
    fundamental_data["report"],

    quant_report=
    quant_data["report"],

    macro_report=
    macro_data["report"],

    valuation_report=
    valuation_data["report"],

    sentiment_report=
    news_data["report"]
)

if final_report is None:

    final_report = """
FINAL DECISION UNAVAILABLE

Please review the individual
agent reports manually.
"""


# ============================================
# PDF EXPORT
# ============================================

generate_pdf(

    ticker,

    fundamental_data["report"],

    quant_data["report"],

    macro_data["report"],

    final_report
)


# ============================================
# SUMMARY
# ============================================

print("\n")

print("=" * 50)

print("AI INVESTMENT SUMMARY")

print("=" * 50)

print(
    f"Confidence: "
    f"{risk_data['confidence']}%"
)

print(
    f"Risk Level: "
    f"{risk_data['risk_level']}"
)

print(
    f"Strongest Agent: "
    f"{risk_data['strongest_agent']}"
)

print(
    f"Weakest Agent: "
    f"{risk_data['weakest_agent']}"
)

print("\nAgent Scores:")

print(
    f"Fundamental: "
    f"{risk_data['fundamental_score']}"
)

print(
    f"Quant: "
    f"{risk_data['quant_score']}"
)

print(
    f"Macro: "
    f"{risk_data['macro_score']}"
)

print(
    f"Valuation: "
    f"{risk_data['valuation_score']}"
)

print(
    f"News: "
    f"{risk_data['sentiment_score']}"
)

print("\n")

print(
    f"Valuation Signal: "
    f"{valuation_data['valuation_signal']}"
)

print(
    f"News Sentiment: "
    f"{news_data['sentiment']}"
)

print(
    f"Quant Signal: "
    f"{quant_data['signal']}"
)

print("\n")

print(
    "Research Pipeline Completed Successfully."
)