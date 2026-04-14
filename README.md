# Binance Futures Trading Bot (USDT-M)

A professional Python-based Command Line Interface (CLI) application designed to interact with the Binance Futures Testnet. This bot allows users to place Market and Limit orders with a clean, modular architecture focused on reliability, validation, and structured logging.

---

## 🚀 Key Features

* **CLI Command Support**
  Easily place orders using terminal arguments.

* **Market & Limit Orders**
  Supports both MARKET and LIMIT order types.

* **Dual-Side Trading**
  Supports both **BUY** and **SELL** operations.

* **Input Validation**
  Ensures correctness of:

  * Symbol
  * Side
  * Order Type
  * Quantity
  * Price (for LIMIT orders)

* **Clear Output Summary**
  Displays:

  * Order ID
  * Status
  * Executed Quantity
  * Average Price

* **Structured Logging**
  Logs all:

  * API requests
  * API responses
  * Errors
    into a persistent file: `trading_bot.log`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <https://github.com/sukritmajumdar-jgec6009/binance-futures-bot>
cd binance_bot
```

### 2. Install Requirements

Recommended: Use a virtual environment (Python 3.x)

```bash
pip install -r requirements.txt
```

### 3. Configure API Credentials

Create a `.env` file in the root directory:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

## 📈 Running the Bot

### Required Arguments

* `--symbol`
* `--side`
* `--type`
* `--quantity`
* `--price` (only for LIMIT orders)

---

### ▶️ MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### ▶️ LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000
```

---

## 📁 Project Structure

```
binance_bot/
│
├── bot/
│   ├── client.py          # Binance API client initialization
│   ├── orders.py          # Core order logic & execution
│   ├── validators.py      # Input validation logic
│   ├── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── trading_bot.log        # Log file (auto-generated)
├── requirements.txt
└── .env
```

---

## 📝 Assumptions & Environment

* **Platform**: Binance Futures Testnet (USDT-M)
* **Credentials**: User must have:

  * Testnet account
  * API key & secret
* **Assets**: Designed for USDT-margined futures contracts

---

