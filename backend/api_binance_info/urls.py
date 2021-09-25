from django.urls import path

from api_binance_info.views import BinanceInfoApi

urlpatterns = [
    path('', BinanceInfoApi.as_view())
]
