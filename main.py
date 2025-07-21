from smartapi import SmartConnect
import datetime

# Set your simulated Angel One credentials
API_KEY = "your_api_key"
CLIENT_CODE = "your_client_code"
PASSWORD = "your_password"
TOTP_SECRET = "your_totp_secret"  # If 2FA is enabled

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
