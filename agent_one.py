import os
import sys
import requests

from dotenv import load_dotenv


# ============================================
# LOAD API KEY
# ============================================

load_dotenv()

FMP_API_KEY = os.getenv(
    "FMP_API_KEY"
)

if not FMP_API_KEY:

    raise ValueError(
        "FMP_API_KEY not found in .env file"
    )


# ============================================
# FORENSIC ANALYSIS
# ============================================

def fallback_analysis(financials):

    revenue = financials.get(
        "revenue",
        0
    )

    gross_profit = financials.get(
        "grossProfit",
        0
    )

    operating_income = financials.get(
        "operatingIncome",
        0
    )

    net_income = financials.get(
        "netIncome",
        0
    )

    gross_margin = (
        gross_profit / revenue * 100
    ) if revenue else 0

    operating_margin = (
        operating_income / revenue * 100
    ) if revenue else 0

    net_margin = (
        net_income / revenue * 100
    ) if revenue else 0

    report = "\n=== FUNDAMENTAL ANALYSIS REPORT ===\n\n"

    report += (
        f"Revenue: "
        f"${revenue:,.0f}\n"
    )

    report += (
        f"Gross Margin: "
        f"{gross_margin:.2f}%\n"
    )

    report += (
        f"Operating Margin: "
        f"{operating_margin:.2f}%\n"
    )

    report += (
        f"Net Margin: "
        f"{net_margin:.2f}%\n\n"
    )

    report += (
        "FORENSIC OBSERVATIONS:\n"
    )

    # Gross Margin

    if gross_margin > 40:

        report += (
            "• Strong gross profitability.\n"
        )

    elif gross_margin > 20:

        report += (
            "• Acceptable gross profitability.\n"
        )

    else:

        report += (
            "• Weak gross profitability.\n"
        )

    # Operating Margin

    if operating_margin > 20:

        report += (
            "• Excellent operating efficiency.\n"
        )

    elif operating_margin > 10:

        report += (
            "• Average operating efficiency.\n"
        )

    else:

        report += (
            "• High operating expenses.\n"
        )

    # Net Margin

    if net_margin > 15:

        report += (
            "• Strong bottom-line earnings.\n"
        )

    elif net_margin > 5:

        report += (
            "• Moderate profitability.\n"
        )

    else:

        report += (
            "• Thin earnings profile.\n"
        )

    return {

        "report":
        report,

        "revenue":
        revenue,

        "gross_margin":
        gross_margin,

        "operating_margin":
        operating_margin,

        "net_margin":
        net_margin
    }


# ============================================
# AGENT 1
# ============================================

def financial_data_gatherer(
    ticker
):

    print(
        f"\n--- "
        f"[Agent 1: Fundamental Analyst] "
        f"Fetching data for {ticker} "
        f"---"
    )

    url = (
        "https://financialmodelingprep.com"
        "/stable/income-statement"
        f"?symbol={ticker}"
        f"&limit=1"
        f"&apikey={FMP_API_KEY}"
    )

    try:

        response = requests.get(
            url,
            timeout=20
        )

        if response.status_code != 200:

            print(
                f"\n[API ERROR] "
                f"Status Code: "
                f"{response.status_code}"
            )

            return None

        data = response.json()

        if not data:

            print(
                f"\nNo data found "
                f"for {ticker}"
            )

            return None

        latest_financials = data[0]

    except Exception as e:

        print(
            f"\n[SYSTEM ERROR] {e}"
        )

        return None

    analysis = fallback_analysis(
        latest_financials
    )

    print(
        "\n=== AGENT 1 REPORT ===\n"
    )

    print(
        analysis["report"]
    )

    print(
        "\n======================"
    )

    return {

        "ticker":
        ticker,

        "report":
        analysis["report"],

        "revenue":
        analysis["revenue"],

        "gross_margin":
        analysis["gross_margin"],

        "operating_margin":
        analysis["operating_margin"],

        "net_margin":
        analysis["net_margin"]
    }


# ============================================
# TESTING
# ============================================

if __name__ == "__main__":

    try:

        ticker = input(
            "Enter stock ticker: "
        ).strip().upper()

        result = financial_data_gatherer(
            ticker
        )

        print("\n")

        print(result)

    except KeyboardInterrupt:

        sys.exit(0)