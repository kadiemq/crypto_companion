from django.db import models


# Create your models here.
class NewsModel(models.Model):
    title = models.TextField(blank=False)
    image = models.TextField(blank=False)
    url = models.TextField(blank=False)

    class Meta:
        db_table = 'news_model'
