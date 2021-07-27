from django.shortcuts import render
from django.views.generic import TemplateView
from plotly.offline import plot
from plotly.graph_objs import Scatter
from .forms import StockQueryForm, CsvFiles
from .stock_utility import get_stock_data
from .plots_utility import Plotting_graphs
from .models import StockCsvFiles

# def indexplot(request):
#     # xdata = [0,1,2,3,4,5]
#     # ydata = [x**2 for x in xdata]
#     # plot_div = plot([Scatter(x = xdata, y=ydata, mode='lines', name='Line Plot', opacity=0.8,
#     #             marker_color = 'green')], output_type='div', include_plotlyjs=False, show_link=False)
#     # args = {'plot_div': plot_div}

#     args = {'plot_div': 'testing'}
#     return render(request, 'index.html', args)

class DashboardIndex(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        form = CsvFiles()
        args = {'form': form}
        return render(request, self.template_name, args)
    def post(self, request):
        form = CsvFiles(request.POST, request.FILES)
        if form.is_valid():
            # csv_file = request.FILES['csv_file']
            # csv_file_name = default_storage.save(csv_file.name, csv_file)
            # file_url = default_storage.url(csv_file_name)
            form.save()
        args = {
            'form': form,
            'text': 'done'
        }
        return render(request, self.template_name, args)
    

class GetStockData(TemplateView):
    template_name = 'home/stock.html'
    def get(self, request):
        form = StockQueryForm()
        stock_files = StockCsvFiles.objects.all()
        args = {
            'form': form,
            'stock_files': stock_files
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = StockQueryForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            data = get_stock_data(request.POST['start'], request.POST['end'], ticker)
            pg = Plotting_graphs(data, ticker)
            bar_plot_div = pg.plot_bar()
            candlestick_plot_div = pg.plot_candlestick()
            scatter_plot_div = pg.plot_scatter()
            area_plot_div = pg.area_plot()
        args = {
                'form': form, 
                'bar_plot_div': bar_plot_div,
                'candlestick_plot_div': candlestick_plot_div,
                'scatter_plot_div': scatter_plot_div,
                'area_plot_div': area_plot_div
            }
        return render(request, self.template_name, args)
