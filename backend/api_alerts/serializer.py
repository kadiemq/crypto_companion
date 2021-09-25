from rest_framework import serializers

from api_alerts.models import Alerts


class AlertSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField()
    user_email = serializers.ReadOnlyField()

    class Meta:
        model = Alerts
        fields = '__all__'
        widgets = {'__all__': 'required'}
