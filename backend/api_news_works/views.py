import redis
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from api_news_works.models import NewsModel
from api_news_works.save_news_to_redis import save_news_to_redis
from api_news_works.serializer import NewsSerializer


class ListNewsApi(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsSerializer

    def get_queryset(self):
        r = redis.Redis(host='', port=6379, db=0)
        redis_data = r.get('news_list')

        if redis_data is None:
            print('no redis data')
            queryset = NewsModel.objects.all()
            save_news_to_redis(queryset, r)
            return queryset

        redis_data = redis_data.decode()
        redis_data = eval(redis_data)
        return redis_data
