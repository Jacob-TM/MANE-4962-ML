# LSTM-Based Stock Market Prediction  
**Jacob Mitchell**

## Project Description and Objective

This project explores the use of Long Short-Term Memory (LSTM) neural networks for short-term stock market prediction. The main objective is to forecast next-day closing prices for stocks by leveraging both structured market data (open, high, low, close, volume) and unstructured financial news headlines. The model is designed to automatically uncover patterns in both historical price sequences and relevant news text, with the goal of gaining a measurable predictive edge—particularly for volatile stocks where traditional models struggle.

## Datasets Used

- **Stock Price Data**: Daily historical price and volume data for NVIDIA (NVDA) and Procter & Gamble (PG) from 2015 to 2025, collected from the NASDAQ website.
- **News Headlines**: Thousands of finance-related headlines from 2015–2025, compiled from public Kaggle datasets and custom web scraping of NVIDIA's official news archive. Headlines are paired by date with stock price data.
SOURCE1: https://www.kaggle.com/datasets/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests
SOURCE2: https://nvidianews.nvidia.com/news
SOURCE3: https://www.nasdaq.com/market-activity

## Model/Method Overview

- **Model Type**: Dual-input LSTM neural network  
  - *Numeric Input*: Processes sequences of daily stock features (open, high, low, close, volume), normalized to [0, 1] using MinMax scaling.
  - *Text Input*: Tokenizes daily news headlines, which are fed as sequences into the network without prior sentiment analysis.
  - Both branches are merged and passed through dense layers to predict the next day's closing price.
- **Preprocessing Steps**:
  - Missing non-trading days are forward-filled to maintain continuity.
  - Headlines are tokenized and padded for model input alignment.
  - Dataset is split chronologically (80/20) to simulate real-world forecasting.

## Instructions to Run the Code

1. **Clone the repository** and navigate to the project folder.
2. **Install dependencies**: pip install -r requirements.txt
3. **Place the datasets** in the specified data directory (see code comments for exact paths).
4. **Run the main training script**: in the \notebooks\model_v1.ipynb
5. **Review results and visualizations**, which are saved in the \results directory.

## Results
# NVIDIA-Training
Loss (MSE): 1.566e-4
MAE: 0.0074

# NVIDIA-Validation
Loss (MSE): 0.0796
MAE: 0.1831


# PG-Training
Loss (MSE): 2.110e-4
MAE: 0.00981

# PG-Validation
Loss (MSE): 2.763e-4
MAE: 0.01174
# 
# 
*For any questions or suggestions, feel free to contact Jacob Mitchell @ jacobmitchell8370@gmail.com.*
