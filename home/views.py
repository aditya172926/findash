from django.shortcuts import render
from django.views.generic import TemplateView
from plotly.offline import plot
from plotly.graph_objs import Scatter
import yfinance as yf
from .forms import StockQueryForm

def indexplot(request):
    xdata = [0,1,2,3,4,5]
    ydata = [x**2 for x in xdata]
    plot_div = plot([Scatter(x = xdata, y=ydata, mode='lines', name='Line Plot', opacity=0.8,
                marker_color = 'green')], output_type='div', include_plotlyjs=False, show_link=False)
    args = {'plot_div': plot_div}
    return render(request, 'index.html', args)

class GetStockData(TemplateView):
    template_name = 'home/stock.html'
    def get(self, request):
        form = StockQueryForm()
        args = {
            'form': form
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = StockQueryForm(request.POST)
        if form.is_valid():
            start = request.POST['start']
            end = request.POST['end']
            ticker = request.POST['ticker']
        data = yf.download(ticker, start, end)
        args = {'form': form, 'data': data}
        return render(request, self.template_name, args)
