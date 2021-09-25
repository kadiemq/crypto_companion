from django.urls import path

from api_profile.views import Profile, UpdateBinanceApis

urlpatterns = [
    path('', Profile.as_view()),
    path('update_binance_apis', UpdateBinanceApis.as_view())
]
