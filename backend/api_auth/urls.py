from django.urls import path

from api_auth.views import LoginAPI, RegisterAPI, LogoutAPI

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('logout/', LogoutAPI.as_view())
]
