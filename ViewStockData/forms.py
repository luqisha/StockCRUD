from django import forms
from .models import sqlModel

class StockInfoForm(forms.Form):
    trade_codes = sorted(set(row.trade_code for row in sqlModel.objects.all()))
    drop_down_choices = [(trade_code, trade_code) for trade_code in trade_codes]
    drop_down_choices.insert(0, ("default", "Choose a stock"))

    stock_name = forms.ChoiceField(choices=drop_down_choices, widget=forms.Select(attrs={'class': 'form-control form-control-sm text-center'}))
