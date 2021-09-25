from django.contrib.postgres.fields import ArrayField
from django.db import models


class Alerts(models.Model):
    type = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    order_type = models.CharField(max_length=255)
    time_in_force = models.CharField(max_length=255)
    trigger = models.FloatField()
    price = models.FloatField()
    quantity = models.FloatField()
    direction = models.CharField(max_length=255)
    notify = ArrayField(models.CharField(max_length=50))
    action = models.CharField(max_length=255)
    user_id = models.IntegerField()
    user_email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'alerts_model'


