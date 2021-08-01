import yfinance as yf
import pandas as pd
import numpy as np
from .plots_utility import *

def get_stock_data(start, end, ticker):
    data = yf.download(ticker, start, end)
    if data is not None:
        print('Got data for ticker {}'.format(ticker))
    return data

def read_csv_file(file_name):
    df = pd.read_csv(file_name)
    print(df.head())
    return 'Success'

def calculate_returns(data, ticker, plot_type):
    df = data[['Adj Close']].pct_change()
    df.columns = ['Returns']
    df.fillna(0, inplace=True)
    if plot_type == 'returns':
        pg = Plotting_graphs(df, ticker, column_name='Returns')
    elif plot_type == 'cumulative_returns':
        cumulative_daily_return = (1+df).cumprod()
        pg = Plotting_graphs(cumulative_daily_return, ticker, column_name='Returns')
    else:
        return 'Graph not found'
    plot_div = pg.plot_scatter()
    del(df)
    return plot_div

def calculate_moving_average(data, ticker, window_length):
    moving_avg = data[['Adj Close']]
    moving_avg[window_length] = moving_avg.rolling(window_length).mean()
    print(moving_avg)
    plot_div = plot_moving_average(moving_avg)
    return plot_div
