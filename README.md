# django_analytics_dashboard

This is a dashboard for visualizing the data given as input in the admin panel of the dashboard.<br>
The master branch uses flexmonster for plotting the data. The dashboard is made using the Django web framework and Python programming language.

Create a virtual environment using the command `virtualenv dash`<br>
Then activate the virtual environment using the command `dash\Scripts\activate` or `source dash/bin/activate` depending on your OS.<br>
Clone this project using the command `git clone https://github.com/aditya172926/django_analytics_dashboard.git`<br>
Then install the packages from the requirements.txt file using `pip install -r requirements.txt` or if you have multiple versions of python installed you can use `pip3 install -r requirements.txt`.<br>

Navigate to the folder in your shell to reach the manage.py file and run the Django server using `python manage.py runserver` or `python3 manage.py runserver`.<br>

Currently the data needs to be filled in the Admin portal to be visualized in the frontend.

# Django Stock data plotting dashboard.
<a href = 'https://github.com/aditya172926/django_analytics_dashboard/tree/dashboard2'>Here</a><br>
This project has been an upgrade and is in the dashboard2 branch of this repository.<br>
Clone the repository dashboar2 branch and run the project.<br>

The project uses specially makes the use of Django web framework, Python programming language, AJAX for asynchronous rendering the plots on the webpage and Plotly for generating the graphs.<br>
The data is generated for this project is from using yfinance.<br>
You can use your own APIs if you want to get the stock data.<br>
The analysis plots that the dashboard can generate are Candlestick plots, barplots, scatter plots, area plots of the stock data.<br>
Also the dashboard displays the volatility in returns, cumulative returns and moving average plots calculated on the provided input as number of days to calculate the rolling mean for.<br>

<br>
The MAC tab in the project stands for Moving Average Crossover which is a simple algorithmic trading strategy and generates the Buy and Sell signals for the stock data provided. The user has to provide with inputs of a short_window and a long_window, also with stock ticker symbol, the start date and end date of the stock data you need.
The Buy and Sell signal is visualized with a plot with markers along with line plot of Close price of stock and moving averages of short_window and long_window respectively.
