import os
import sys
import requests
from dotenv import load_dotenv

# =========================
# LOAD API KEYS
# =========================

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")

if not FRED_API_KEY:
    raise ValueError("FRED_API_KEY not found")


# =========================
# FRED DATA FETCHER
# =========================

def get_latest_fred_value(series_id):

    url = (
        f"https://api.stlouisfed.org/fred/series/observations"
        f"?series_id={series_id}"
        f"&api_key={FRED_API_KEY}"
        f"&file_type=json"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"FRED Error: {response.status_code}"
        )

    data = response.json()

    observations = data["observations"]

    if not observations:
        raise Exception(
            f"No data returned for {series_id}"
        )

    return observations[-1]["value"]


# =========================
# AGENT 3
# =========================

def macro_risk_manager():

    print(
        "\n--- [Agent 3: Macro Risk Manager] ---"
    )

    try:

        print(
            "Fetching macroeconomic data from FRED..."
        )

        fed_funds = get_latest_fred_value(
            "FEDFUNDS"
        )

        inflation = get_latest_fred_value(
            "CPIAUCSL"
        )

        unemployment = get_latest_fred_value(
            "UNRATE"
        )

        treasury_10y = get_latest_fred_value(
            "GS10"
        )

    except Exception as e:

        print(
            f"\n[SYSTEM ERROR] {e}"
        )

        return None

    risk_level = "LOW"

    try:

        if float(fed_funds) > 4:
            risk_level = "HIGH"

        elif float(fed_funds) > 2:
            risk_level = "MEDIUM"

    except:
        risk_level = "MEDIUM"

    report = f"""
MACRO RISK REPORT

Federal Funds Rate:
{fed_funds}

Inflation Index:
{inflation}

Unemployment Rate:
{unemployment}

10-Year Treasury Yield:
{treasury_10y}

Risk Level:
{risk_level}

OBSERVATIONS

• Higher rates increase borrowing costs

• Higher inflation pressures equities

• Higher unemployment may indicate economic slowdown

• Treasury yields reflect bond market expectations
"""

    print(
        "\n=== AGENT 3 REPORT ===\n"
    )

    print(
        report
    )

    print(
        "\n======================"
    )

    return {
    "fed_funds": fed_funds,
    "inflation": inflation,
    "unemployment": unemployment,
    "treasury_10y": treasury_10y,
    "report": report
}


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":

    try:

        result = macro_risk_manager()

        print("\n")

        print(result)

    except KeyboardInterrupt:

        sys.exit(0)