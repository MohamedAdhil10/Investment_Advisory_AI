import numpy as np
import pandas as pd
import random

# Generate Synthetic Stock Prices using GBM
def generate_stock_prices(num_days=252, num_stocks=5, mu=0.05, sigma=0.2, S0=100):
    dt = 1 / num_days
    stock_prices = np.zeros((num_days, num_stocks))
    stock_prices[0, :] = S0
    for t in range(1, num_days):
        stock_prices[t, :] = stock_prices[t - 1, :] * np.exp(
            (mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * np.random.randn(num_stocks)
        )
    return pd.DataFrame(stock_prices, columns=[f'Stock_{i+1}' for i in range(num_stocks)])

# Generate Mutual Fund NAVs
def generate_mutual_fund_navs(num_days=252, num_funds=3):
    navs = np.cumsum(np.random.randn(num_days, num_funds) * 0.5, axis=0) + 100
    return pd.DataFrame(navs, columns=[f'Fund_{i+1}' for i in range(num_funds)])

# Generate User Risk Profiles
def generate_risk_profiles(num_users=100):
    risk_levels = ['Low', 'Medium', 'High']
    users = {
        'User_ID': range(1, num_users+1),
        'Risk_Profile': [random.choice(risk_levels) for _ in range(num_users)]
    }
    return pd.DataFrame(users)

# Generate data
stock_data = generate_stock_prices()
mutual_fund_data = generate_mutual_fund_navs()
risk_profiles = generate_risk_profiles()

# Save data to CSV
stock_data.to_csv("data/stock_data.csv", index=False)
mutual_fund_data.to_csv("data/mutual_fund_data.csv", index=False)
risk_profiles.to_csv("data/risk_profiles.csv", index=False)

print("Data generation completed successfully.")