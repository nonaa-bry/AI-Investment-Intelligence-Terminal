import os
import sys
import requests
from dotenv import load_dotenv

# =========================
# LOAD API KEYS
# =========================

load_dotenv()

FMP_API_KEY = os.getenv("FMP_API_KEY")

if not FMP_API_KEY:
    raise ValueError("FMP_API_KEY not found")


# =========================
# AGENT 5
# =========================

def valuation_analyst(ticker):

    print(
        f"\n--- [Agent 5: Valuation Analyst] "
        f"Evaluating {ticker} ---"
    )

    try:

        url = (
            f"https://financialmodelingprep.com/"
            f"stable/ratios-ttm"
            f"?symbol={ticker}"
            f"&apikey={FMP_API_KEY}"
        )

        response = requests.get(
            url,
            timeout=20
        )

        data = response.json()

        if not data:

            print(
                "No valuation data found."
            )

            return None

        metrics = data[0]

        pe = metrics.get(
            "priceToEarningsRatioTTM",
            0
        )

        pb = metrics.get(
            "priceToBookRatioTTM",
            0
        )

        ps = metrics.get(
            "priceToSalesRatioTTM",
            0
        )

        peg = metrics.get(
            "priceToEarningsGrowthRatioTTM",
            0
        )

        ev_multiple = metrics.get(
            "enterpriseValueMultipleTTM",
            0
        )

    except Exception as e:

        print(e)

        return None

    score = 0

    # PE

    if pe and pe < 15:
        score += 2
    elif pe and pe < 25:
        score += 1

    # PB

    if pb and pb < 2:
        score += 2
    elif pb and pb < 5:
        score += 1

    # PS

    if ps and ps < 3:
        score += 2
    elif ps and ps < 10:
        score += 1

    # Final Signal

    if score >= 5:
        valuation_signal = "UNDERVALUED"

    elif score >= 3:
        valuation_signal = "FAIR VALUE"

    else:
        valuation_signal = "OVERVALUED"

    report = f"""
VALUATION ANALYSIS REPORT

Ticker:
{ticker}

PE Ratio:
{pe}

PEG Ratio:
{peg}

Price to Book:
{pb}

Price to Sales:
{ps}

Enterprise Value Multiple:
{ev_multiple}

Valuation Signal:
{valuation_signal}

OBSERVATIONS

"""

    if pe:
        report += f"• PE Ratio = {pe}\n"

    if pb:
        report += f"• Price-to-Book = {pb}\n"

    if ps:
        report += f"• Price-to-Sales = {ps}\n"

    if peg:
        report += f"• PEG Ratio = {peg}\n"

    report += (
        f"\nOverall Valuation: "
        f"{valuation_signal}"
    )

    print(
        "\n=== AGENT 5 REPORT ===\n"
    )

    print(
        report
    )

    print(
        "\n======================"
    )

    return {
    "valuation_signal": valuation_signal,
    "pe": pe,
    "pb": pb,
    "ps": ps,
    "peg": peg,
    "ev_multiple": ev_multiple,
    "report": report
}


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":

    ticker = input(
        "Enter Stock Ticker: "
    ).strip().upper()

    result = valuation_analyst(
        ticker
    )

    print("\n")

    print(result)