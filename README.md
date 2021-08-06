# django_analytics_dashboard

<i>This project is strictly for <u>education purposes</u> only, not for any type of advise for trading or investments of any kind.</i>

This is the 2nd dashboard version. We implemented more features in this dashboard and make future versions for mostly finance related tasks.

This project has been an upgrade and is in the dashboard2 branch of this repository.<br>
Clone the repository dashboar2 branch and run the project.<br>

The project uses specially makes the use of <b>Django web framework, Python programming language, AJAX</b> for asynchronous rendering the plots on the webpage and <b>Plotly</b> for generating the graphs.<br>
The data is generated for this project is from using yfinance.<br>
You can use your own APIs if you want to get the stock data.<br>
The analysis plots that the dashboard can generate are Candlestick plots, barplots, scatter plots, area plots of the stock data.<br>
Also the dashboard displays the volatility in returns, cumulative returns and moving average plots calculated on the provided input as number of days to calculate the rolling mean for.<br>

<br>
The MAC tab in the project stands for <b>Moving Average Crossover</b> which is a simple algorithmic trading strategy and generates the Buy and Sell signals for the stock data provided. The user has to provide with inputs of a short_window and a long_window, also with stock ticker symbol, the start date and end date of the stock data you need.
The Buy and Sell signal is visualized with a plot with markers along with line plot of Close price of stock and moving averages of short_window and long_window respectively.
