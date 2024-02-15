from django.shortcuts import render
from django.conf import settings
from .models import jsonModel, sqlModel
from .forms import StockInfoForm
import json
import os
import plotly.graph_objs as go


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
    return render(
        request, 
        'home.html', 
        {
            'trade_code': False,
            'stocks_data': stock_data, 
            'plot_div': False, 
            'form': False
        }
    )




def sql_model_view(request, trade_code=None):

    if trade_code != None:
        stock_data = sqlModel.objects.filter(trade_code=trade_code).order_by('-date')
        dates = [row.date for row in stock_data]
        close = [row.close for row in stock_data]
        volumes = [row.volume for row in stock_data]

        # Determining scale so that both line and bar plot can be shown in the same graph
        scale = (max(close) - min(close)) / (max(volumes) - min(volumes))  

        line_plot = go.Scatter(x=dates, y=close, mode='lines', name='Closing Price', marker_color='rgb(255, 120, 20)')
        bar_plot = go.Bar(x=dates, y=volumes, name='Volume', yaxis='y2', marker_color='rgb(50, 20, 140)')
        
        layout = go.Layout(
            xaxis=dict(
                title='Date',
                dtick='D',
            ),
            yaxis=dict(
                title='Close Price',
                side='left',
                overlaying='y2'
            ),
            yaxis2=dict(
                title='Volume',
                side='right',
                scaleratio=scale  # Ratio of the scale for secondary y-axis to the primary y-axis
            )
        )
        
        fig = go.Figure(data=[line_plot, bar_plot], layout=layout)
        plot_div = fig.to_html(full_html=False)

        return render(
            request, 
            'home.html', 
            {
                'trade_code': trade_code,
                'stocks_data': stock_data, 
                'plot_div': plot_div, 
                'form': StockInfoForm()
            }
        )
    

    else:
        stock_data = sqlModel.objects.all().order_by('date')
        return render(
            request, 
            'home.html', 
            {
                'trade_code': False,
                'stocks_data': stock_data, 
                'plot_div': False, 
                'form': StockInfoForm()
            }
        )



    
        