from django.urls import path
from .views import stock_detail

urlpatterns = [
    path('', stock_detail, name='stock_detail'),
]
