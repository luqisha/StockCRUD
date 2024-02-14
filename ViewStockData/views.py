from django.shortcuts import render
from django.conf import settings
from .models import jsonModel
import json
import os

def home(request):

    if jsonModel.objects.all().count() == 0:
        
        file_dir = os.path.join(settings.BASE_DIR, 'data', 'stock_market_data.json')
        
        with open(file_dir) as f:
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
    
    return render(request, 'home.html', {'stocks': jsonModel.objects.all()})