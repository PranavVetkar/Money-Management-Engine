# 💰 Money Management Engine (Kelly Criterion)

A Python-based **risk and position sizing tool** that applies the **Kelly Criterion** to determine how much capital should be risked per trade based on historical performance.

This project focuses on **capital growth and drawdown control**, answering a critical trading question:
> *How much should I risk per trade?*

---

## 🚀 What This Project Does

- Implements the **Kelly Criterion** from scratch
- Calculates optimal capital allocation per trade
- Uses **win rate** and **win/loss ratio** as inputs
- Applies **Half-Kelly** for safer real-world usage
- Outputs a practical trade size based on portfolio balance

---

## 🧠 The Kelly Criterion

The Kelly formula determines the fraction of capital to bet:
> f* = (bp − q) / b

Where:
- `p` = probability of winning
- `q` = probability of losing (1 − p)
- `b` = average win / average loss

Because full Kelly can be aggressive, this project uses:

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Pure Python (no external dependencies)**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Money-Management-Engine.git
cd Money-Management-Engine
