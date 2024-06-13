

import json
from django.http import JsonResponse
from django.views import View
from .models import Trade
from django.core import serializers
from django.conf import settings
import os

class TradeListView(View):
    def get(self, request):
        print("Request Object:", request)
        params = request.GET
        page = params.get("page", 1)
        limit = params.get("limit", 10)
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
        
        # start = int(page - 1) * limit
        # end = page*limit
        # print("start", start)
        # print("end", end)
        # sliced_trades_data = trades_data[start:end]

        return JsonResponse(trades_data, safe=False)
