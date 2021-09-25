from django.urls import path

from api_news_works.views import ListNewsApi

urlpatterns = [
    path('', ListNewsApi.as_view())
]
