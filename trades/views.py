

import json
from django.http import JsonResponse
from django.views import View
from .models import Trade
from django.core import serializers
from django.conf import settings
import os

class TradeListView(View):
    def get(self, request):
        file_path = os.path.join(settings.BASE_DIR, 'initial_data.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Optional: If you want to map to the model (not saving to the DB)
        trades = []
        for item in data:
            trade = Trade(
                date=item['date'],
                trade_code=item['trade_code'],
                high=item['high'],
                low=item['low'],
                open=item['open'],
                close=item['close'],
                volume=item['volume']
            )
            trades.append(trade)

        # Convert model instances to dictionary (if needed)
        trades_data = [{
            "date": trade.date,
            "trade_code": trade.trade_code,
            "high": str(trade.high),
            "low": str(trade.low),
            "open": str(trade.open),
            "close": str(trade.close),
            "volume": trade.volume
        } for trade in trades]

        return JsonResponse(trades_data, safe=False)
