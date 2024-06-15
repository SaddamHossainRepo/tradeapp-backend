from django.urls import path
from .views import TradeListView, DeleteView
from . import views

urlpatterns = [
    path('trades/', TradeListView.as_view(), name='trade-list'),
    path('trades/add/', TradeListView.add_trade , name='trade-add'),
    path('delete_trade/<int:id>/',  TradeListView.delete_trade , name='trade-delete'),
]
