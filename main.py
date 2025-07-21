from smartapi import SmartConnect
import datetime

# Set your simulated Angel One credentials
API_KEY = "FLfQ4vBO"
CLIENT_CODE = "K50911931"
PASSWORD = "Ajitbabu@123"
TOTP_SECRET = "4CZSNDX24JIKYLEGXZLEPVK6U4"  # If 2FA is enabled

# Simulated AI decision (buy if price < 1000)
def simple_trading_logic(price):
    return "BUY" if price < 1000 else "HOLD"

def main():
    obj = SmartConnect(api_key=API_KEY)
    
    # Login
    data = obj.generateSession(CLIENT_CODE, PASSWORD, TOTP_SECRET)
    auth_token = data['data']['jwtToken']
    refresh_token = data['data']['refreshToken']
    
    # Get example stock price
    instrument = "RELIANCE-EQ"
    exchange = "NSE"
    ltp = obj.ltpData(exchange, instrument)['data']['ltp']
    print(f"Current Price of {instrument}: ₹{ltp}")

    # Decision
    decision = simple_trading_logic(ltp)
    print("AI Decision:", decision)

    if decision == "BUY":
        print("Simulating BUY order...")
        # Do not place real order, just log simulation
        # obj.placeOrder(...) ← skipped

if __name__ == "__main__":
    main()

import yfinance as yf
from prophet import Prophet
import pandas as pd

def predict_price(stock="RELIANCE.NS"):
    df = yf.download(stock, period="30d", interval="1h")
    df.reset_index(inplace=True)
    df = df[['Datetime', 'Close']].rename(columns={"Datetime": "ds", "Close": "y"})

    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=1)
    forecast = model.predict(future)

    predicted_price = forecast.iloc[-1]['yhat']
    print(f"🔮 Predicted next price for {stock}: ₹{predicted_price:.2f}")
    return predicted_price
positions = []
profit = 0

def trade_logic():
    global profit
    predicted = predict_price()
    current = yf.download("RELIANCE.NS", period="1d", interval="1m").Close.iloc[-1]

    if predicted > current * 1.01:
        print("🟢 Simulated Buy at ₹", current)
        positions.append(current)
    elif positions:
        bought = positions.pop(0)
        gain = current - bought
        profit += gain
        print(f"🔴 Simulated Sell at ₹{current:.2f}, Gain: ₹{gain:.2f}")
import smtplib
from email.message import EmailMessage
import datetime

def send_report():
    msg = EmailMessage()
    msg["Subject"] = "📊 Daily AI Trader Report"
    msg["From"] = "kakumanuajitbabu@gmail.com"
    msg["To"] = "kakumanuajitbabu@gmail.com"

    msg.set_content(f"""
🧾 Daily Report: {datetime.date.today().strftime('%d %B %Y')}

📈 Net Profit: ₹{profit:.2f}
📊 Open Positions: {len(positions)}

– AI Trading Bot
""")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("kakumanuajitbabu@gmail.com", "yyesizymvfzamdcg")
        server.send_message(msg)
        print("📤 Report sent to your Gmail")
import schedule
import time

if __name__ == "__main__":
    main()  # run login + ltp

    schedule.every(1).minutes.do(trade_logic)
    schedule.every().day.at("15:30").do(send_report)

    while True:
        schedule.run_pending()
        time.sleep(1)

