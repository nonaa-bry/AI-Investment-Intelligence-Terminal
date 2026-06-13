import sys


# ============================================
# AGENT 4
# FINAL DECISION ENGINE v2
# ============================================

def final_decision_engine(

    ticker,

    confidence,

    risk_level,

    strongest_agent,

    weakest_agent,

    fundamental_report,

    quant_report,

    macro_report,

    valuation_report,

    sentiment_report

):

    print(
        "\n--- [Agent 4: Final Decision Engine] ---"
    )

    # ============================================
    # RECOMMENDATION
    # ============================================

    if confidence >= 80:

        decision = "STRONG BUY"

    elif confidence >= 65:

        decision = "BUY"

    elif confidence >= 50:

        decision = "HOLD"

    elif confidence >= 35:

        decision = "SELL"

    else:

        decision = "STRONG SELL"

    # ============================================
    # INVESTMENT THESIS
    # ============================================

    thesis = []

    if decision in [
        "BUY",
        "STRONG BUY"
    ]:

        thesis.append(
            "Company demonstrates favorable investment characteristics."
        )

        thesis.append(
            "Multi-agent analysis supports a constructive outlook."
        )

    elif decision == "HOLD":

        thesis.append(
            "Current risk-reward profile appears balanced."
        )

        thesis.append(
            "Investors should monitor future catalysts."
        )

    else:

        thesis.append(
            "Current conditions suggest elevated downside risk."
        )

        thesis.append(
            "Further due diligence is recommended before allocating capital."
        )

    # ============================================
    # EXECUTIVE SUMMARY
    # ============================================

    executive_summary = f"""

EXECUTIVE SUMMARY

Ticker:
{ticker}

Confidence Score:
{confidence:.2f}%

Risk Level:
{risk_level}

Recommendation:
{decision}

Strongest Agent:
{strongest_agent}

Weakest Agent:
{weakest_agent}

"""

    # ============================================
    # FINAL REPORT
    # ============================================

    report = f"""

========================================================
AI INVESTMENT INTELLIGENCE REPORT
========================================================

{executive_summary}

========================================================
INVESTMENT THESIS
========================================================

"""

    for point in thesis:

        report += f"• {point}\n"

    report += f"""

========================================================
FUNDAMENTAL ANALYSIS
========================================================

{fundamental_report}

========================================================
TECHNICAL ANALYSIS
========================================================

{quant_report}

========================================================
MACRO ANALYSIS
========================================================

{macro_report}

========================================================
VALUATION ANALYSIS
========================================================

{valuation_report}

========================================================
NEWS SENTIMENT ANALYSIS
========================================================

{sentiment_report}

========================================================
FINAL RECOMMENDATION
========================================================

Recommendation:
{decision}

Confidence:
{confidence:.2f}%

Risk Level:
{risk_level}

Strongest Agent:
{strongest_agent}

Weakest Agent:
{weakest_agent}

========================================================
DISCLAIMER
========================================================

This report is generated using a
multi-agent investment intelligence
framework and should not be considered
financial advice.

========================================================
"""

    print(
        "\n=== FINAL INVESTMENT MEMO ===\n"
    )

    print(
        report
    )

    print(
        "\n=============================="
    )

    return report


# ============================================
# TESTING
# ============================================

if __name__ == "__main__":

    report = final_decision_engine(

        ticker="AAPL",

        confidence=82.4,

        risk_level="LOW",

        strongest_agent="Valuation",

        weakest_agent="Macro",

        fundamental_report=
        "Strong profitability and margins.",

        quant_report=
        "Bullish MACD crossover detected.",

        macro_report=
        "Interest rates remain elevated.",

        valuation_report=
        "Stock appears undervalued.",

        sentiment_report=
        "Positive news sentiment."
    )

    print("\n")

    print(report)

    sys.exit(0)