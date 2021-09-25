from rest_framework import serializers


class BinanceApisSerializer(serializers.Serializer):
    public_api = serializers.CharField(required=True)
    secret_api = serializers.CharField(required=True)
