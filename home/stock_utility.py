import yfinance as yf
import pandas as pd

def get_stock_data(start, end, ticker):
    data = yf.download(ticker, start, end)
    if data is not None:
        print('Got data for ticker {}'.format(ticker))
    return data

def read_csv_file(file_name):
    df = pd.read_csv(file_name)
    print(df.head())
    return 'Success'