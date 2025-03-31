import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.risk_models import CovarianceShrinkage
from pypfopt.expected_returns import mean_historical_return
from transformers import pipeline

# Load Data
stock_data = pd.read_csv("data/stock_data.csv")

# NLP-Based Query Understanding
nlp_pipeline = pipeline("text-classification", model="ProsusAI/finbert")

def analyze_query(query):
    return nlp_pipeline(query)

# Stock Price Forecasting with LSTM
def create_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# Portfolio Optimization using Markowitz MPT
def optimize_portfolio(stock_data):
    mu = mean_historical_return(stock_data)
    S = CovarianceShrinkage(stock_data).ledoit_wolf()
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    return cleaned_weights

print("AI Investment Advisor is ready.")