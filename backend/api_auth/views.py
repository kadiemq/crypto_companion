import datetime

import jwt
from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api_auth.permission import IsNotAuthenticated
from api_auth.serializers import LoginSerializer, RegistrationSerializer
from api_binance_info.send_binance_account_microservice import send_binance_account_microservice_rabbitmq
from config import settings


class LoginAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.data)
        if user:

            # login(request, user)

            csrf.get_token(request)
            response = Response()
            token = jwt.encode({
                'username': user.username,
                'iat': datetime.datetime.utcnow(),
                'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=31)
            }, settings.SECRET_KEY)

            response.set_cookie(
                key='auth_token',
                value=token,
                expires=datetime.datetime.utcnow() + datetime.timedelta(days=30),
                secure=False,
                httponly=True,
                samesite='Lax'
            )

            if len(user.binance_public_api) > 0 and len(user.binance_secret_api) > 0:
                send_binance_account_microservice_rabbitmq(user.id, user.binance_public_api, user.binance_secret_api)
                response.data = {'user': user.username, 'token': token, 'setup_api': 'true'}
            else:
                response.data = {'user': user.username, 'token': token, 'setup_api': 'false'}
                print('user didnt setup apis yet')

            return response
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterAPI(APIView):
    permission_classes = [IsNotAuthenticated]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Account Successfully Created')


class LogoutAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        response = Response()
        for cookie in request.COOKIES:
            response.delete_cookie(cookie)

        response.data = {'Logged out'}
        return response
