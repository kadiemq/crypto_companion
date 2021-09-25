import jwt
from api_auth.models import NewUser
from rest_framework.authentication import BaseAuthentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions

from config import settings


def get_authorization_header(request):
    raw_token = request.COOKIES.get('auth_token', ) or None
    auth = request.META.get('HTTP_AUTHORIZATION', )
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class JWTAuthentication(BaseAuthentication):
    keyword = 'auth_token'

    def authenticate(self, request):
        raw_token = request.COOKIES.get('auth_token', ) or None
        if raw_token is None:
            return None

        return self.authenticate_credentials(raw_token)

    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, settings.SECRET_KEY, algorithms="HS256")
            user = NewUser.objects.get(username=payload['username'])
        except (jwt.DecodeError, NewUser.DoesNotExist):
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        return (user, payload)

    def authenticate_header(self, request):
        return self.keyword
