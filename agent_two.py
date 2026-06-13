import sys
import yfinance as yf


# =========================
# AGENT 2
# =========================

def quantitative_data_gatherer(ticker):

    print(
        f"\n--- [Agent 2: Quant Analyst] "
        f"Calculating indicators for {ticker} ---"
    )

    try:

        print("Fetching market data...")

        df = yf.Ticker(
            ticker
        ).history(
            period="1y"
        )

        if df.empty:

            print(
                f"No data found for {ticker}"
            )

            return None

        # RSI

        delta = df["Close"].diff()

        gain = (
            delta.where(
                delta > 0,
                0
            )
            .rolling(14)
            .mean()
        )

        loss = (
            (-delta.where(
                delta < 0,
                0
            ))
            .rolling(14)
            .mean()
        )

        rs = gain / loss

        df["RSI"] = (
            100
            - (
                100
                / (1 + rs)
            )
        )

        # MACD

        ema12 = (
            df["Close"]
            .ewm(
                span=12,
                adjust=False
            )
            .mean()
        )

        ema26 = (
            df["Close"]
            .ewm(
                span=26,
                adjust=False
            )
            .mean()
        )

        df["MACD"] = (
            ema12 - ema26
        )

        df["Signal_Line"] = (
            df["MACD"]
            .ewm(
                span=9,
                adjust=False
            )
            .mean()
        )

        df["MACD_Histogram"] = (
            df["MACD"]
            - df["Signal_Line"]
        )

        # Moving Averages

        df["SMA20"] = (
            df["Close"]
            .rolling(20)
            .mean()
        )

        df["SMA50"] = (
            df["Close"]
            .rolling(50)
            .mean()
        )

        df["SMA200"] = (
            df["Close"]
            .rolling(200)
            .mean()
        )

        latest = df.iloc[-1]

        current_price = float(
            latest["Close"]
        )

        rsi_val = float(
            latest["RSI"]
        )

        macd_val = float(
            latest["MACD"]
        )

        signal_val = float(
            latest["Signal_Line"]
        )

        hist_val = float(
            latest["MACD_Histogram"]
        )

        sma20 = float(
            latest["SMA20"]
        )

        sma50 = float(
            latest["SMA50"]
        )

        sma200 = float(
            latest["SMA200"]
        )

        quant_signal = "HOLD"

        if (
            rsi_val < 30
            and macd_val > signal_val
        ):
            quant_signal = "BUY"

        elif (
            rsi_val > 70
            and macd_val < signal_val
        ):
            quant_signal = "SELL"

    except Exception as e:

        print(
            f"\n[SYSTEM ERROR] {e}"
        )

        return None

    report = f"""
QUANTITATIVE ANALYSIS REPORT

Ticker: {ticker}

Current Price:
${current_price:.2f}

RSI:
{rsi_val:.2f}

MACD:
{macd_val:.4f}

Signal Line:
{signal_val:.4f}

Histogram:
{hist_val:.4f}

SMA20:
{sma20:.2f}

SMA50:
{sma50:.2f}

SMA200:
{sma200:.2f}

Signal:
{quant_signal}

OBSERVATIONS:

"""

    if rsi_val > 70:

        report += (
            "RSI indicates OVERBOUGHT conditions.\n"
        )

    elif rsi_val < 30:

        report += (
            "RSI indicates OVERSOLD conditions.\n"
        )

    else:

        report += (
            "RSI is NEUTRAL.\n"
        )

    if macd_val > signal_val:

        report += (
            "MACD indicates BULLISH momentum.\n"
        )

    else:

        report += (
            "MACD indicates BEARISH momentum.\n"
        )

    if current_price > sma50:

        report += (
            "Price is ABOVE SMA50.\n"
        )

    else:

        report += (
            "Price is BELOW SMA50.\n"
        )

    print(
        "\n=== AGENT 2 REPORT ===\n"
    )

    print(
        report
    )

    print(
        "\n======================"
    )

    return {
    "ticker": ticker,
    "report": report,
    "signal": quant_signal,
    "current_price": current_price,
    "rsi": rsi_val,
    "macd": macd_val,
    "signal_line": signal_val,
    "histogram": hist_val,
    "sma20": sma20,
    "sma50": sma50,
    "sma200": sma200,
    "df": df
}


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":

    try:

        ticker = input(
            "Enter stock ticker: "
        ).strip().upper()

        quantitative_data_gatherer(
            ticker
        )

    except KeyboardInterrupt:

        sys.exit(0)
