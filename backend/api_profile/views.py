from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api_binance_info.send_binance_account_microservice import send_binance_account_microservice_rabbitmq


class UpdateBinanceApis(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        data = request.data
        user = request.user
        user.binance_secret_api = data['binance_secret_api']
        user.binance_public_api = data['binance_public_api']

        user.save()
        return Response('Success')


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        response = Response()

        if len(user.binance_public_api) > 0 and len(user.binance_secret_api) > 0:
            send_binance_account_microservice_rabbitmq(user.id, user.binance_public_api, user.binance_secret_api)
            response.data = {'user': user.username, 'setup_api': 'true'}
        else:
            response.data = {'user': user.username, 'setup_api': 'false'}
            print('user didnt setup apis yet')

        return response
