from rest_framework.generics import CreateAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from api_alerts.models import Alerts
from api_alerts.permissions import OnlyOwner
from api_alerts.serializer import AlertSerializer


class CreateListAlertView(ListCreateAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Alerts.objects.all()

        queryset = queryset.filter(user_id=user.id)
        return queryset

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id, user_email=self.request.user.email)


class DeleteAlert(DestroyAPIView):
    queryset = Alerts.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated, OnlyOwner]
