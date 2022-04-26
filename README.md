# Django Analytics Dashboard

<i>This project is strictly for <u>education purposes</u> only, not for any type of advise for trading or investments of any kind.</i>

Project Link -> [FinDash](https://findash1729.herokuapp.com/)

This is the 2nd dashboard version. Implemented more features in this dashboard and make future versions for mostly finance related tasks.

This project has been an upgrade and is in the main branch of this repository.<br>
Clone the repository main branch and run the project.<br>

The project uses specially makes the use of 
 - <b>Django web framework
 - Python programming language
 - AJAX</b> for asynchronous rendering the plots on the webpage
 - <b>Plotly</b> for generating the interactive graphs.<br>
 - <b>yfinance</b> package for getting the data
You can use your own APIs if you want to get the stock data.<br>
The analysis plots that the dashboard can generate are Candlestick plots, barplots, scatter plots, area plots of the stock data.<br>
## Types of Plots
 - Candlestick
 - Cumulative Returns
 - Volatility
 - Moving Averages
 - Barplots
 - Scatter
 - Area
 
Moving average plots calculated on the provided input as number of days to calculate the rolling mean for.<br>

## Functionalities
 - Moving Average Crossover strategy

The <b>Moving Average Crossover, MAC</b> tab in the project is a simple algorithmic trading strategy and generates the Buy and Sell signals for the stock data provided. The user has to provide with inputs of a short_window and a long_window, also with stock ticker symbol, the start date and end date of the stock data you need.
The Buy and Sell signal is visualized with a plot with markers along with line plot of Close price of stock and moving averages of short_window and long_window respectively.
