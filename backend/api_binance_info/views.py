import time

import redis
from rest_framework.exceptions import APIException

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api_binance_info.send_binance_account_microservice import send_binance_account_microservice_rabbitmq


class BinanceInfoApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        r = redis.Redis(host='', port=6379, db=0)

        user = request.user
        response = Response()

        if not len(user.binance_public_api) > 0 or not len(user.binance_secret_api) > 0:
            raise APIException(detail='Api keys are not configured for this account', code=400)

        redis_data = r.get(f'{user.id}_coin_list')

        if redis_data is None:
            send_binance_account_microservice_rabbitmq(user.id, user.binance_public_api, user.binance_secret_api)
            # response.data = {'No data in redis'}
            time.sleep(15)

            redis_data = r.get(f'{user.id}_coin_list')
            redis_data = eval(redis_data)
            response.data = {'estimated_net_worth': redis_data['net_worth'], 'coin_list': redis_data['coin_list']}
            return response

        redis_data = eval(redis_data)

        response.data = {'estimated_net_worth': redis_data['net_worth'], 'coin_list': redis_data['coin_list']}
        return response
