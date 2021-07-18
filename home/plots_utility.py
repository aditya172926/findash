import plotly.graph_objs as go
from plotly.offline import plot
from plotly.graph_objs import Candlestick



def plot_candlestick(data, ticker):

    ########## This is used to get the plots on a new webpage not on the same html page.

    # layout = dict(
    #         title = ticker,
    #         xaxis = go.layout.XAxis(title = go.layout.xaxis.Title(text = "Time")),
    #         yaxis = go.layout.YAxis(title = go.layout.yaxis.Title(text = "Price US $"))
    #     )

    # plot_d = [go.Candlestick(x = data.index,
    #             open = data['Open'],
    #             high = data['High'],
    #             low = data['Low'],
    #             close = data['Close'])]
    # plot_div = go.Figure(data = plot_d, layout = layout)


    ########## This is used to get the plots on the same webpage.
    plot_div = plot([Candlestick(x = data.index, 
                    open=data['Open'], 
                    high = data['High'],
                    low = data['Low'],
                    close = data['Close'],
                    name='Candlestick Plot', opacity=0.8,
                )], output_type='div', include_plotlyjs=False, show_link=False)

    return plot_div