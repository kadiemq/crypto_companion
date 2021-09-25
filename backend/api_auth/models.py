from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import signing
from django.db import models


class EncryptedApiField(models.TextField):
    def __init__(self, *args, **kwargs):
        super(EncryptedApiField, self).__init__(*args, **kwargs)

    def get_db_prep_save(self, value, connection):
        value = super().get_db_prep_value(value, connection)
        if value is None:
            return value

        if len(value) == 0:
            return value

        return ((signing.dumps(str(value))).encode('utf-8')).decode('utf-8')

    def to_python(self, value):
        return value
        # if value is None:
        #     return value
        #
        # return signing.loads(value)

    def from_db_value(self, value, *args, **kwargs):
        if value is None:
            return value

        if len(value) == 0:
            return value
        return signing.loads(value)


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_subscribed', True)
        other_fields.setdefault('subscription_level', 1)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    subscription_level = models.IntegerField(default=0)
    binance_public_api = EncryptedApiField(blank=True)
    binance_secret_api = EncryptedApiField(blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
