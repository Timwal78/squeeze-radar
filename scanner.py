# ============================================================
# 🧠 BEASTMODE SQUEEZE RADAR — TEMP VERSION (AlphaVantage)
# ============================================================
import os, time, requests

TICKERS = os.getenv("TICKERS", "AMC,YYAI,GME,EPWK,NAK,FFAI,CDTG").split(",")
ALPHA_KEY = os.getenv("F6GL94S34HLAKT6I")
DISCORD_WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1432825526564683886/PHhN0YPIc45_lMhUHP0bAf9lIPPLi6IQpQYD9hYTwNRJNznhcNqbmTjCJkm483RVeKd_L")

ALPHA_URL = "https://www.alphavantage.co/query"

def get_quote(symbol):
    try:
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": ALPHA_KEY
        }
        r = requests.get(ALPHA_URL, params=params)
        data = r.json().get("Global Quote", {})
        price = float(data.get("05. price", 0))
        change = float(data.get("10. change percent", "0%").replace("%", ""))
        volume = int(data.get("06. volume", 0))
        return symbol, price, volume, change
    except Exception as e:
        print(f"[ERROR] {symbol} → {e}")
        return symbol, 0, 0, 0

def post_to_discord(quotes):
    lines = [
        f"**{sym}** — ${price:.2f} | Vol: {vol:,} | Δ {chg:+.2f}%"
        for sym, price, vol, chg in quotes
    ]
    payload = {"content": "\n".join(lines[:25])}
    try:
        r = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if r.status_code != 204:
            print(f"[WARN] Discord {r.status_code}: {r.text}")
    except Exception as e:
        print(f"[ERROR] Discord send failed → {e}")

def main():
    print("🚀 BEASTMODE RADAR (ALPHA MODE) — 5-MIN LOOP")
    while True:
        results = [get_quote(t) for t in TICKERS]
        post_to_discord(results)
        print("⏳ Sleeping 5 minutes…")
        time.sleep(300)

if __name__ == "__main__":
    main()
