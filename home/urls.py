from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexplot, name='index'),
    path('stock', views.GetStockData.as_view(), name='stock'),
]