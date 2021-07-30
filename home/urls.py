from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardIndex.as_view(), name='index'),
    path('stock', views.GetStockData.as_view(), name='stock'),
    path('read_data', views.ReadDataView, name='read_data'),
]