from django.shortcuts import render
import yfinance as yf
from .models import Stock
from .forms import StockForm

def fetch_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data

def stock_detail(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            data = fetch_stock_data(symbol)

            stock_instance = Stock(
                symbol=symbol,
                date=data.index[0].date(),
                open_price=data['Open'][0],
                high_price=data['High'][0],
                low_price=data['Low'][0],
                close_price=data['Close'][0],
                volume=data['Volume'][0]
            )
            stock_instance.save()

            context = {'stock_data': data.to_html(), 'form': form}
            return render(request, 'stock/stock_detail.html', context)
    else:
        form = StockForm()

    context = {'form': form}
    return render(request, 'stock/stock_form.html', context)
