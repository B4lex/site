from django.db import models


class Car(models.Model):

    title = models.CharField(max_length=30, db_index=True)
    link = models.TextField()
    image = models.TextField()
    usd_price = models.IntegerField()
    uah_price = models.IntegerField()
    description = models.TextField(max_length=500, blank=True)
    image_ref = models.CharField(max_length=20)
