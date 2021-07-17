from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

def indexplot(request):
    xdata = [0,1,2,3,4,5]
    ydata = [x**2 for x in xdata]
    plot_div = plot([Scatter(x = xdata, y=ydata, mode='lines', name='Line Plot', opacity=0.8,
                marker_color = 'green')], output_type='div', include_plotlyjs=False, show_link=False)
    args = {'plot_div': plot_div}
    return render(request, 'home/index.html', args)