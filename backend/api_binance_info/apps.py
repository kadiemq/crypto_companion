from django.apps import AppConfig
import os

from api_binance_info.secret_key import get_secret


class ApiBinanceInfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_binance_info'

    def ready(self):
        os.environ['encryption_key'] = get_secret()
