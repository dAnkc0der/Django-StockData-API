# from django.urls import path
# from .views import stock_detail

# urlpatterns = [
#     path('', stock_detail, name='stock_detail'),
# ]

# stock/urls.py
from django.urls import path
from .views import StockDataView

urlpatterns = [
    path('stock/<str:symbol>/', StockDataView.as_view(), name='stock-data'),
]
