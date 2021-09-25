from rest_framework.exceptions import MethodNotAllowed, APIException
from rest_framework.permissions import BasePermission


class IsNotAuthenticated(BasePermission):
    """
    Allows access only to non authenticated users.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            raise APIException(detail='User is already logged in cant create a new account', code=405)
        return bool(not request.user.is_authenticated)
