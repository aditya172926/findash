from os import name
import yfinance as yf
import pandas as pd
import numpy as np
from .plots_utility import *
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def get_stock_data(start, end, ticker):
    data = yf.download(ticker, start, end)
    if data is not None:
        print('Got data for ticker {}'.format(ticker))
    return data

def read_csv_file(file_name):
    df = pd.read_csv(file_name)
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
    plot_div = plot_moving_average(moving_avg)
    return plot_div

def calculate_moving_average_crossover(data, ticker, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    short_window = int(short_window)
    long_window = int(long_window)
    # Create short simple moving average over the short window
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average over the long window
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create Signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    # fig = plt.figure()

    # ax1 = fig.add_subplot(111, ylabel='Price is $')

    # # Plot the closing price
    # data['Close'].plot(ax=ax1, color='r', lw=2.)

    # # Plot the short and long moving averages
    # signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

    # # PLot the buy signals
    # ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], 
    #         '^', markersize=10, color='g')

    # # Plot the sell signals
    # ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 
    #         'v', markersize=10, color='k')

    # plt.show()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='lines'))
    fig.add_trace(go.Scatter(x=signals.index, y = signals['short_mavg'], mode='lines', name=str(short_window)))
    fig.add_trace(go.Scatter(x=signals.index, y = signals['long_mavg'], mode='lines', name=str(long_window)))
    fig.add_trace(go.Scatter(mode = 'markers', x = signals.loc[signals.positions == 1.0].index, y = signals.short_mavg[signals.positions == 1.0], 
                            name='Buy', 
                            marker_symbol = 'triangle-up',
                            marker = dict(color='green', size=10)
                            ))
    fig.add_trace(go.Scatter(mode = 'markers', x = signals.loc[signals.positions == -1.0].index, y = signals.short_mavg[signals.positions == -1.0], 
                            name='Sell',
                            marker_symbol='triangle-down',
                            marker = dict(color='red', size=10)
                            ))
    plot_html = plot(fig, output_type='div', include_plotlyjs=False, show_link=False)
    return plot_html