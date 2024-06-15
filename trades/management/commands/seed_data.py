from django.core.management.base import BaseCommand
from trades.models import Trade
import os
from django.conf import settings
import json
import decimal


class Command(BaseCommand): 
    help = 'Displays stats related to Article and Comment models'

    def handle(self, *args, **kwargs): 
            file_path = os.path.join(settings.BASE_DIR, 'initial_data.json')
            with open(file_path, 'r') as file:
                    data = json.load(file)
                    # print(data)
            Trade.objects.all().delete()
            trades = []
            self.stdout.write(self.style.SUCCESS(f'Seeding started'))
            for item in data:
                try:
                # Clean and convert numerical values
                      
                    trade = Trade(
                            date=item['date'],
                            trade_code=item['trade_code'],
                            high=self.transformToDecimal(item['high']),
                            low=self.transformToDecimal(item['low']),
                            open=self.transformToDecimal(item['open']),
                            close=self.transformToDecimal(item['close']),
                            volume=self.transformToDecimal(item['volume'])
                            )
                    trades.append(trade)
                    
                    # Print success message
                    # self.stdout.write(self.style.SUCCESS(f'Successfully saved trade data for {item["trade_code"]} on {item["date"]}'))
                except (decimal.InvalidOperation, ValueError) as e:
                    print(item)
                    self.stderr.write(self.style.ERROR(f'Error processing data for {item["trade_code"]} on {item["date"]}: {e}'))
                except KeyError as e:
                       self.stderr.write(self.style.ERROR(f'Missing key {e} in data for {item["trade_code"]} on {item["date"]}'))
            Trade.objects.bulk_create(trades)
            self.stdout.write(self.style.SUCCESS(f'Seeding done'))
    
    def transformToDecimal(self, value):
        return decimal.Decimal(value.replace(',', ''))