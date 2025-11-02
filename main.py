# ==========================================================
# 🚀 SQUEEZE RADAR → DISCORD AUTO ALERT BOT
# ==========================================================

import os
import time
import requests
import random

# === SETTINGS ===
TICKERS = [t.strip().upper() for t in os.getenv("TICKERS", "AMC,GME,FFAI,MNOV,EPWK,PLUG,NAK,ADTX,BIYA").split(",")]
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Safety check
if not WEBHOOK_URL:
    print("❌ Missing Discord webhook URL (DISCORD_WEBHOOK_URL not set).")
    exit(1)

print(f"🟢 Loaded tickers: {TICKERS}")
print("🚀 Squeeze Radar live and monitoring...")

# === MOCK SIGNAL GENERATOR ===
# (Replace this with your actual scanner logic later)
def scan_for_squeezes():
    """Fake example that randomly triggers squeeze alerts."""
    trigger = random.choice([True, False, False, False]) # 25% chance
    if trigger:
        sym = random.choice(TICKERS)
        price = round(random.uniform(0.5, 10.0), 2)
        condition = random.choice([
            "Squeeze forming + MACD bullish",
            "High RVOL + Volume divergence",
            "Breakout above VWAP",
        ])
        return {"symbol": sym, "price": price, "condition": condition}
    return None


# === DISCORD ALERT ===
def send_to_discord(symbol, price, condition):
    msg = {
        "content": f"🚨 **{symbol}** — Momentum Building!\n💰 Price: ${price}\n📈 {condition}\n\nWatching for confirmation..."
    }
    try:
        response = requests.post(WEBHOOK_URL, json=msg)
        if response.status_code == 204:
            print(f"✅ Sent alert for {symbol} to Discord.")
        else:
            print(f"⚠️ Discord response: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending alert: {e}")


# === LOOP ===
while True:
    try:
        signal = scan_for_squeezes()
        if signal:
            send_to_discord(signal["symbol"], signal["price"], signal["condition"])
        time.sleep(60) # scan every minute
    except KeyboardInterrupt:
        print("🛑 Exiting gracefully.")
        break
    except Exception as e:
        print(f"⚠️ Runtime error: {e}")
        time.sleep(10)
