from django.core.management.base import BaseCommand
from ViewStockData.models import sqlModel
from django.conf import settings
import json
import os

class Command(BaseCommand):
    def handle(self):

        file_path = os.path.join(settings.BASE_DIR, 'data', 'stock_market_data.json')

        try:
            with open(file_path) as f:
                data = json.load(f)

            for item in data:
                sqlModel.objects.create(
                    date=item['date'],
                    trade_code=item['trade_code'],
                    high=item['high'],
                    low=item['low'],
                    open=item['open'],
                    close=item['close'],
                    volume=int(item['volume'].replace(',', '')) 
                )

            self.stdout.write(self.style.SUCCESS('Data successfully loaded!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data: {e}!'))
