import plotly.graph_objs as go
from plotly.offline import plot
from plotly.graph_objs import Candlestick
import plotly.express as px
import pandas as pd


class Plotting_graphs:
    def __init__(self, data, ticker):
        self.data = data
        self.ticker = ticker
        self.layout = dict(
                title = ticker,
                xaxis = dict(
                    rangeselector=dict(
                        buttons = list([
                            dict(count=1,
                                label = "1m",
                                step = "month",
                                stepmode = "backward"),
                            dict(count=6,
                                label = "6m",
                                step = "month",
                                stepmode = "backward"),
                            dict(count=1,
                                label = "YTD",
                                step = "year",
                                stepmode = "todate"),
                            dict(count=1,
                                label = "1y",
                                step = "year",
                                stepmode = "backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(visible=True),
                    type = "date"
                ),
                yaxis = go.layout.YAxis(title = go.layout.yaxis.Title(text = "Price US $")),
                height=700,
            )


    def plot_candlestick(self):

        ########## This is used to get the plots on a new webpage not on the same html page.

        plot_d = [go.Candlestick(x = self.data.index,
                    open = self.data['Open'],
                    high = self.data['High'],
                    low = self.data['Low'],
                    close = self.data['Close'])]
        plot_div = go.Figure(data = plot_d, layout = self.layout)
        
        

        # This line of code can take the plot_d and the layout together and plot the graph offline on the same page
        plot_html = plot(plot_div, output_type='div', include_plotlyjs=False, show_link=False)

        ########## This is used to get the plots on the same webpage.
        # plot_div = plot([Candlestick(x = data.index, 
        #                 open=data['Open'], 
        #                 high = data['High'],
        #                 low = data['Low'],
        #                 close = data['Close'],
        #                 name='Candlestick Plot', opacity=0.8,
        #             )], output_type='div', include_plotlyjs=False, show_link=False)
        # print('PLot done')

        return plot_html

    def plot_scatter(self):
        fig = go.Figure([go.Scatter(x = self.data.index, y=self.data['Close'])], layout = self.layout)
        plot_html = plot(fig, output_type='div', include_plotlyjs=False, show_link=False)
        return plot_html

    def plot_bar(self):
        fig = go.Figure([go.Bar(x = self.data.index, y=self.data['Close'])], layout = self.layout)
        # fig = px.bar(self.data, x = self.data.index, y=self.data['Close'], layout=self.layout)
        plot_html = plot(fig, output_type='div', include_plotlyjs=False, show_link=False)
        return plot_html

    def area_plot(self):
        fig = px.area(self.data, x=self.data.index, y=self.data['Close'])
        plot_html = plot(fig, output_type='div', include_plotlyjs=False, show_link=False)
        return plot_html
        
def plot_csv_file(file_name):
    data = pd.read_csv(file_name)
    fig = go.Figure([go.Scatter(x = data.index, y=data['Close'])])
    plot_html = plot(fig, output_type='div', include_plotlyjs=False, show_link=False)
    return plot_html