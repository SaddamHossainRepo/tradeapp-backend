

import json
from django.http import JsonResponse
from django.views import View

from . serializers import TradeSerializer
from .models import Trade
from django.core import serializers
from django.conf import settings
import os
from django.core.paginator import Paginator

class TradeListView(View):
    def get(self, request):
        print("Request Object:", request)
        params = request.GET
        page = int(params.get("page", 1))
        limit = int(params.get("limit", 10))
        offset = int((page-1)*limit)
        
        trades = Trade.objects.order_by('id')
        # Slicing the queryset using limit and offset
        paginator = Paginator(trades, limit)
        page_obj = paginator.page(page)
        total_trades = Trade.objects.count()  # Total number of records
        
        trade_list = list(page_obj.object_list.values())  # Convert queryset to list of dictionaries
        
        response = {
            'data': trade_list,
            'total': total_trades,
            'limit': limit,
            'offset': offset,
        }
        return JsonResponse(trade_list, safe=False)
    
    def add_trade(self, request):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete_trade(request, id):
        try:
            trade = Trade.objects.get(pk=id)
            trade.delete()
            return JsonResponse({'status': 'success', 'message': 'Trade deleted successfully.'})
        except Trade.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Trade not found.'}, status=404)

class DeleteView(View):
    def delete_trade(request, id):
        try:
            trade = Trade.objects.get(pk=id)
            trade.delete()
            return JsonResponse({'status': 'success', 'message': 'Trade deleted successfully.'})
        except Trade.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Trade not found.'}, status=404)
