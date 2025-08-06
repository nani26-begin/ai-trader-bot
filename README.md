# 📈 AI Trading Bot for Indian Stock Market (Angel One SmartAPI)

Welcome to the AI Trading Bot – a powerful, automated trading assistant designed to analyze the stock market, predict profitable trades, and execute them based on smart AI strategies. This bot is integrated with **Angel One's SmartAPI**, making it fully functional for the Indian stock market.

---

## 🔍 What This AI Trading Bot Can Do

* 📊 **Daily Stock Prediction**: Uses machine learning models like LSTM, ARIMA, or Simple Moving Averages to forecast stock trends.
* 🧠 **Smart Decision Making**: Automatically identifies buy/sell signals based on predicted patterns and technical indicators.
* 💹 **Paper Trading (Simulation)**: Runs in a simulation mode without using real money to test and refine strategies.
* 🤖 **Automated Execution**: Can optionally place real trades via SmartAPI when confidence thresholds are met.
* 📧 **Email Reporting**: Sends a detailed daily report (Profit/Loss, Holdings, Actions) to your email every market day at 4 PM IST.
* 📈 **Track High Performers**: Monitors and logs high-performing stocks over time.
* 🪙 **Works with Small Balances**: Supports trading simulations even with low budgets (e.g., ₹100), making it beginner-friendly.

---

## 🎯 Problems It Solves

✅ **Emotional Trading**: Eliminates emotional bias by following a disciplined, rule-based approach.

✅ **Time Management**: Saves hours of manual analysis by automating prediction and execution.

✅ **Lack of Technical Knowledge**: Beginners can benefit from AI-based trading decisions without deep knowledge of charts or indicators.

✅ **Missed Opportunities**: Captures high-potential trades consistently using daily market data.

✅ **Post-market Summary**: Keeps you informed even if you don’t monitor markets live, via detailed email summaries.

---

## ⚙️ How It Works (Overview)

1. **Collects Live Market Data** using Angel One SmartAPI.
2. **Processes and Cleans Data** for model input.
3. **Applies Prediction Model** (e.g., SMA crossover, LSTM, or custom logic).
4. **Makes Trade Decisions** and simulates or executes orders.
5. **Stores Logs** including trade history, stock performance, and balance.
6. **Sends Daily Email Reports** to your registered email account.

---

## 🚀 Features

* ✅ Angel One SmartAPI integration
* ✅ Fully automated run at 4:00 PM IST
* ✅ Gmail report delivery
* ✅ Modular prediction engine (easily switch models)
* ✅ Simulated and real-money trading modes
* ✅ Daily log history & stock tracking

---

## 📬 Daily Email Includes

* 🔁 Trades Executed
* 💸 Profit/Loss Summary
* 📌 Holdings Overview
* 📈 High-performing stocks
* 💼 Investment breakdown

---

## 💡 Use Cases

* ✅ Beginner investors looking for AI-assisted trading
* ✅ Algo trading enthusiasts testing ML models
* ✅ Freelancers managing small-cap portfolios
* ✅ Developers building trading automation apps

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, Numpy**
* **Angel One SmartAPI**
* **SMTP for email reports**
* **Sklearn, Prophet, LSTM (optional)**
* **n8n.io (for no-code workflows, optional)**

---

## 🧠 Future Improvements

* ☁️ Cloud deployment with scheduling (e.g., using GitHub Actions, AWS Lambda)
* 📱 Telegram/WhatsApp alerts
* 📊 Dashboard for real-time tracking
* 🤝 Integration with other brokers (Zerodha, Upstox)
* 🧩 More advanced ML models


Great! Here's a complete and professional set of additional files and sections to include in your GitHub repository for your **AI Trading Bot** project:

---

## 📂 1. `LICENSE` (MIT License – You Can Modify This If Needed)

```text
MIT License

Copyright (c) 2025 Kakumanu Ajit Babu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[... MIT boilerplate continues ...]

```

You can copy-paste this directly or choose a different license [here](https://choosealicense.com/).

---

## 📁 2. `.gitignore`

```bash
# Python
__pycache__/
*.py[cod]
*.ipynb_checkpoints
.env
.env.*
*.log

# Jupyter
.ipynb_checkpoints/

# Mac
.DS_Store

# VS Code
.vscode/

# Secrets
*.key
*.json
*.sqlite
```

This prevents sensitive files, caches, and local config files from being uploaded.

---

## ⚙️ 3. Installation Instructions (Add to README)

### 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ai-trading-bot.git
cd ai-trading-bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧾 4. Environment Variables

Create a `.env` file in the root directory and add:

```dotenv
SMARTAPI_CLIENT_ID=your_client_id
SMARTAPI_CLIENT_SECRET=your_secret
SMARTAPI_API_KEY=your_api_key
SMARTAPI_REFRESH_TOKEN=your_refresh_token

EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_specific_password
EMAIL_RECEIVER=receiver_email@gmail.com
```

> ⚠️ Never hard-code secrets or commit `.env` files.

---

## ▶️ 5. How to Run

```bash
# Activate your environment
source venv/bin/activate

# Run the bot manually
python main.py
```

Or use `cron`, `Task Scheduler`, or `n8n.io` to schedule it daily at 4 PM IST.

---

## 🧪 6. Requirements File (`requirements.txt`)

```txt
pandas
numpy
requests
matplotlib
scikit-learn
prophet
ta
yfinance
smartapi-python
smtplib
email-validator
dotenv
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧾 Folder Structure (Optional Section in README)

```
ai-trading-bot/
│
├── main.py                     # Entry point
├── strategy/                   # Folder for strategies like LSTM, SMA, etc.
│   ├── sma_crossover.py
│   └── lstm_model.py
├── data/                       # Temporary CSVs or logs
├── logs/                       # Trading history & debug logs
├── email_report.py             # Gmail email handler
├── trade_executor.py           # Executes or simulates orders
├── requirements.txt
├── .gitignore
├── .env                        # NOT pushed to GitHub
└── README.md
```
