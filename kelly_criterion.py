import pandas as pd

class KellyCalculator:
    def __init__(self, win_rate, win_loss_ratio):
        self.p = win_rate # Probability of win (e.g., 0.51)
        self.q = 1 - win_rate # Probability of loss
        self.b = win_loss_ratio # Average Win / Average Loss

    def calculate_kelly_fraction(self):
        # Kelly Formula: f = (bp - q) / b
        f_star = (self.b * self.p - self.q) / self.b
        
        # Professional traders often use "Half-Kelly" to stay safe
        safe_f = f_star / 2
        return max(0, safe_f) # Never return a negative bet size

# --- Simulation ---
# Let's assume your Day 16 Neural Net had a 51% win rate
# And your average winning trade is 2% while your average loss is 1% (b = 2)
win_rate = 0.51
win_loss_ratio = 2.0 

calc = KellyCalculator(win_rate, win_loss_ratio)
suggested_risk = calc.calculate_kelly_fraction()

print(f"--- Risk Management Report ---")
print(f"Historical Win Rate: {win_rate*100}%")
print(f"Suggested Portfolio Risk per Trade: {suggested_risk*100:.2f}%")

# Apply to a $1000 balance
balance = 1000
trade_amount = balance * suggested_risk
print(f"With a $1,000 balance, you should only trade: ${trade_amount:.2f}")