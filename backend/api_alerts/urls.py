from django.urls import path

from api_alerts.views import CreateListAlertView, DeleteAlert

urlpatterns = [
    path('', CreateListAlertView.as_view()),
    path('delete/<int:pk>/', DeleteAlert.as_view())
]
