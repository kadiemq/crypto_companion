from django.core import serializers
import json

from api_news_works.serializer import NewsSerializer


def save_news_to_redis(queryset, r):
    data = NewsSerializer(queryset, many=True)
    json_data = json.dumps(data.data)
    r.set('news_list', str(json_data), ex=60)
