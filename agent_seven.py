# ============================================
# AGENT 7 - RISK & CONFIDENCE ENGINE
# ============================================

import sys


# ============================================
# MAIN ENGINE
# ============================================

def risk_confidence_engine(
    fundamental_data,
    quant_data,
    macro_data,
    valuation_data,
    sentiment_data
):

    print(
        "\n--- [Agent 7: Risk & Confidence Engine] ---"
    )

    # ============================================
    # FUNDAMENTAL SCORE
    # ============================================

    fundamental_score = 50

    gross_margin = fundamental_data.get(
        "gross_margin",
        0
    )

    operating_margin = fundamental_data.get(
        "operating_margin",
        0
    )

    net_margin = fundamental_data.get(
        "net_margin",
        0
    )

    if gross_margin > 40:
        fundamental_score += 15

    elif gross_margin > 20:
        fundamental_score += 8

    if operating_margin > 20:
        fundamental_score += 15

    elif operating_margin > 10:
        fundamental_score += 8

    if net_margin > 15:
        fundamental_score += 20

    elif net_margin > 5:
        fundamental_score += 10

    fundamental_score = min(
        100,
        fundamental_score
    )

    # ============================================
    # QUANT SCORE
    # ============================================

    quant_score = 50

    rsi = quant_data.get(
        "rsi",
        50
    )

    macd = quant_data.get(
        "macd",
        0
    )

    signal_line = quant_data.get(
        "signal_line",
        0
    )

    current_price = quant_data.get(
        "current_price",
        0
    )

    sma200 = quant_data.get(
        "sma200",
        0
    )

    if 40 <= rsi <= 60:
        quant_score += 20

    elif rsi < 30:
        quant_score += 15

    elif rsi > 70:
        quant_score -= 15

    if macd > signal_line:
        quant_score += 20

    else:
        quant_score -= 20

    if current_price > sma200:
        quant_score += 10

    else:
        quant_score -= 10

    quant_score = max(
        0,
        min(
            100,
            quant_score
        )
    )

    # ============================================
    # MACRO SCORE
    # ============================================

    macro_score = 50

    try:

        fed_rate = float(
            macro_data.get(
                "fed_funds",
                5
            )
        )

        unemployment = float(
            macro_data.get(
                "unemployment",
                5
            )
        )

        treasury = float(
            macro_data.get(
                "treasury_10y",
                4
            )
        )

        if fed_rate < 3:
            macro_score += 20

        elif fed_rate > 5:
            macro_score -= 20

        if unemployment < 5:
            macro_score += 10

        elif unemployment > 7:
            macro_score -= 10

        if treasury < 4:
            macro_score += 10

        elif treasury > 5:
            macro_score -= 10

    except Exception:
        pass

    macro_score = max(
        0,
        min(
            100,
            macro_score
        )
    )

    # ============================================
    # VALUATION SCORE
    # ============================================

    valuation_score = 50

    valuation_signal = valuation_data.get(
        "valuation_signal",
        "FAIR VALUE"
    )

    if valuation_signal == "UNDERVALUED":
        valuation_score += 40

    elif valuation_signal == "FAIR VALUE":
        valuation_score += 10

    elif valuation_signal == "OVERVALUED":
        valuation_score -= 20

    valuation_score = max(
        0,
        min(
            100,
            valuation_score
        )
    )

    # ============================================
    # NEWS SCORE
    # ============================================

    sentiment_score = sentiment_data.get(
        "score",
        50
    )

    sentiment_score = max(
        0,
        min(
            100,
            sentiment_score
        )
    )

    # ============================================
    # FINAL CONFIDENCE
    # ============================================

    confidence = (
        fundamental_score * 0.30
        + quant_score * 0.25
        + valuation_score * 0.20
        + sentiment_score * 0.15
        + macro_score * 0.10
    )

    confidence = round(
        confidence,
        2
    )

    # ============================================
    # RISK LEVEL
    # ============================================

    if confidence >= 80:
        risk_level = "LOW"

    elif confidence >= 50:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"

    # ============================================
    # AGENT RANKING
    # ============================================

    agent_scores = {

        "Fundamental":
        fundamental_score,

        "Quant":
        quant_score,

        "Macro":
        macro_score,

        "Valuation":
        valuation_score,

        "News":
        sentiment_score
    }

    strongest_agent = max(
        agent_scores,
        key=agent_scores.get
    )

    weakest_agent = min(
        agent_scores,
        key=agent_scores.get
    )

    print("\n===== AGENT SCORES =====")

    for name, score in agent_scores.items():

        print(
            f"{name}: {score}"
        )

    print(
        f"\nConfidence: {confidence}%"
    )

    print(
        f"Risk Level: {risk_level}"
    )

    print(
        f"Strongest Agent: {strongest_agent}"
    )

    print(
        f"Weakest Agent: {weakest_agent}"
    )

    # ============================================
    # RETURN RESULTS
    # ============================================

    return {

        "confidence":
        confidence,

        "risk_level":
        risk_level,

        "strongest_agent":
        strongest_agent,

        "weakest_agent":
        weakest_agent,

        "fundamental_score":
        fundamental_score,

        "quant_score":
        quant_score,

        "macro_score":
        macro_score,

        "valuation_score":
        valuation_score,

        "sentiment_score":
        sentiment_score
    }


# ============================================
# TESTING
# ============================================

if __name__ == "__main__":

    sample_fundamental = {

        "gross_margin": 45,

        "operating_margin": 22,

        "net_margin": 18
    }

    sample_quant = {

        "rsi": 55,

        "macd": 1.2,

        "signal_line": 0.8,

        "current_price": 220,

        "sma200": 180
    }

    sample_macro = {

        "fed_funds": 4.25,

        "unemployment": 4.1,

        "treasury_10y": 4.3
    }

    sample_valuation = {

        "valuation_signal":
        "UNDERVALUED"
    }

    sample_sentiment = {

        "score":
        78
    }

    result = risk_confidence_engine(

        sample_fundamental,

        sample_quant,

        sample_macro,

        sample_valuation,

        sample_sentiment
    )

    print("\n")

    print(result)

    sys.exit(0)