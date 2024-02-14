from django.shortcuts import render
from django.conf import settings
from .models import jsonModel, sqlModel
import json
import os

def json_model_view(request):

    if jsonModel.objects.all().count() == 0:
        
        file_path = os.path.join(settings.BASE_DIR, 'data', 'stock_market_data.json')
        
        with open(file_path) as f:
            data = json.load(f)
            for item in data:
                jsonModel.objects.create(
                    date= item['date'],
                    trade_code= item['trade_code'],
                    high= item['high'],
                    low= item['low'],
                    open= item['open'],
                    close= item['close'],
                    volume= int(item['volume'].replace(',', '')),
                )
    stock_data = jsonModel.objects.all()
    return render(request, 'home.html', {'stocks': stock_data})



def sql_model_view(request):
    stock_data = sqlModel.objects.all()
    return render(request, 'home.html', {'stocks': stock_data})