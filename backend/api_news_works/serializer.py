from rest_framework import serializers

from api_news_works.models import NewsModel


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'
