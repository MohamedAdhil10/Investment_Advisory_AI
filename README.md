AI-Powered Investment Advisory

Project Overview

This project is designed to simulate financial market data, develop an AI agent for investment recommendations, and handle real-world financial scenarios. The key tasks include:

1. Data Generation: Creating synthetic stock price movements, mutual fund NAVs, and user risk profiles.


2. AI Agent for Investment Advisory: Implementing an NLP-based query system, stock price forecasting, and portfolio optimization.


3. Real-World Scenario Handling: Addressing AI adaptability in volatile markets, error handling, and explainability.



Repository Structure

│── 📄 README.md
│── 📂 data
│   │── stock_data.csv
│   │── mutual_fund_data.csv
│   │── risk_profiles.csv
│── 📂 notebooks
│   │── intern_assignment.ipynb
│── 📂 src
│   │── ai_agent.py
│   │── data_generation.py
│── 📄 report.pdf

Installation & Setup

Prerequisites

Ensure you have the following installed:

Python 3.8+

Virtual environment (optional but recommended)


Required Libraries

pip install numpy pandas matplotlib scikit-learn tensorflow transformers pypfopt

Running the Project

Step 1: Generate Data

Run the data_generation.py script to generate synthetic financial data.

python src/data_generation.py

This will create CSV files in the data directory.

Step 2: AI Investment Advisor

Run the ai_agent.py script to interact with the AI agent.

python src/ai_agent.py

This script supports:

NLP Query Understanding: Uses FinBERT to analyze user queries.

Stock Price Forecasting: Implements an LSTM model for time-series prediction.

Portfolio Optimization: Uses Modern Portfolio Theory for asset allocation.


Step 3: View Jupyter Notebook

Open the notebook for detailed explanation and execution steps.

jupyter notebook notebooks/intern_assignment.ipynb

Submission Guidelines

Code Repository: Submit via GitHub/GitLab with a structured README.

Report: Include a PDF covering model justifications and findings.


Evaluation Criteria

AI/ML Expertise: Correct use of machine learning models.

Mathematical Rigor: Accuracy in risk calculations and forecasts.

Logical Reasoning: AI system's alignment with market behavior.

Code Quality & Documentation: Clean, modular, and well-documented code.


Bonus Challenge

For advanced implementation, try:

Reinforcement Learning for an AI-driven trading bot.

Sentiment analysis of financial news to enhance predictions.


Contact

For any queries, please reach out to the project mentor or team lead.

