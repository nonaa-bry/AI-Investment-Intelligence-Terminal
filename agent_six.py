import os
import sys
import requests

from datetime import (
    datetime,
    timedelta
)

from dotenv import load_dotenv


# ============================================
# LOAD API KEY
# ============================================

load_dotenv()

FINNHUB_API_KEY = os.getenv(
    "FINNHUB_API_KEY"
)

if not FINNHUB_API_KEY:

    raise ValueError(
        "FINNHUB_API_KEY not found"
    )


# ============================================
# AGENT 6
# NEWS SENTIMENT ANALYST
# ============================================

def news_sentiment_analyst(
    ticker
):

    print(
        f"\n--- "
        f"[Agent 6: News Sentiment Analyst] "
        f"Analyzing news for {ticker} "
        f"---"
    )

    # ============================================
    # DATE RANGE
    # ============================================

    today = datetime.today()

    start_date = (
        today - timedelta(days=30)
    ).strftime(
        "%Y-%m-%d"
    )

    end_date = today.strftime(
        "%Y-%m-%d"
    )

    # ============================================
    # FETCH NEWS
    # ============================================

    try:

        url = (
            "https://finnhub.io/api/v1/company-news"
            f"?symbol={ticker}"
            f"&from={start_date}"
            f"&to={end_date}"
            f"&token={FINNHUB_API_KEY}"
        )

        response = requests.get(
            url,
            timeout=120
        )

        if response.status_code != 200:

            print(
                f"\n[API ERROR] "
                f"{response.status_code}"
            )

            return None

        news = response.json()

        if not news:

            print(
                "No news found."
            )

            return None

    except Exception as e:

        print(
            f"\n[SYSTEM ERROR] {e}"
        )

        return None

    # ============================================
    # SENTIMENT DICTIONARY
    # ============================================

    positive_words = [

        "growth",
        "beat",
        "surge",
        "profit",
        "record",
        "strong",
        "upgrade",
        "bullish",
        "expansion",
        "partnership",
        "outperform",
        "acquisition"
    ]

    negative_words = [

        "decline",
        "miss",
        "lawsuit",
        "risk",
        "downgrade",
        "loss",
        "weak",
        "fall",
        "bearish",
        "investigation",
        "fraud",
        "recall"
    ]

    positive_score = 0
    negative_score = 0

    headline_text = ""

    # ============================================
    # ANALYZE HEADLINES
    # ============================================

    for article in news[:10]:

        headline = article.get(
            "headline",
            ""
        )

        headline_text += (
            headline + "\n"
        )

        headline_lower = (
            headline.lower()
        )

        for word in positive_words:

            if word in headline_lower:

                positive_score += 1

        for word in negative_words:

            if word in headline_lower:

                negative_score += 1

    # ============================================
    # SCORE
    # ============================================

    sentiment_score = (

        50

        + (positive_score * 10)

        - (negative_score * 10)
    )

    sentiment_score = max(
        0,
        min(
            100,
            sentiment_score
        )
    )

    # ============================================
    # SIGNAL
    # ============================================

    if sentiment_score >= 65:

        sentiment = "POSITIVE"

        signal = "BUY"

    elif sentiment_score <= 35:

        sentiment = "NEGATIVE"

        signal = "SELL"

    else:

        sentiment = "NEUTRAL"

        signal = "HOLD"

    # ============================================
    # REPORT
    # ============================================

    report = f"""
NEWS SENTIMENT REPORT

Ticker:
{ticker}

Sentiment:
{sentiment}

Signal:
{signal}

Sentiment Score:
{sentiment_score}/100

====================================

HEADLINES ANALYZED

{headline_text}

====================================

Positive Mentions:
{positive_score}

Negative Mentions:
{negative_score}

Overall Sentiment:
{sentiment}

====================================
"""

    print(
        "\n=== AGENT 6 REPORT ===\n"
    )

    print(
        report
    )

    print(
        "\n======================"
    )

    # ============================================
    # RETURN
    # ============================================

    return {

        "ticker":
        ticker,

        "sentiment":
        sentiment,

        "signal":
        signal,

        "score":
        sentiment_score,

        "headlines":
        headline_text,

        "positive":
        positive_score,

        "negative":
        negative_score,

        "report":
        report
    }


# ============================================
# TESTING
# ============================================

if __name__ == "__main__":

    try:

        ticker = input(
            "Enter Stock Ticker: "
        ).strip().upper()

        result = news_sentiment_analyst(
            ticker
        )

        print("\n")

        print(result)

    except KeyboardInterrupt:

        sys.exit(0)