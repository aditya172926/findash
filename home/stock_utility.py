import yfinance as yf

def get_stock_data(start, end, ticker):
    data = yf.download(ticker, start, end)
    if data is not None:
        print('Got data for ticker {}'.format(ticker))
    return data