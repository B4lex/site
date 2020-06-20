from django.db import models
from colorfield.fields import ColorField


class Car(models.Model):

    title = models.CharField(max_length=30, db_index=True)
    link = models.URLField()
    usd_price = models.IntegerField()
    uah_price = models.IntegerField()
    description = models.TextField(max_length=500, blank=True, null=True)
    image_ref = models.URLField()
    location = models.CharField(max_length=10, null = True)
    type = models.TextField(null=True)
    mileage = models.DecimalField(decimal_places=5, max_digits=10, null=True)
    engine = models.TextField(null=True)
    gearbox = models.TextField(null=True)
    transmission = models.TextField(null=True)
    color = models.CharField(max_length=10, null=True)
    color_val = ColorField(null=True)
    update_date = models.DateTimeField(auto_now=True)

    def update(self, source):
        for key, value in source.items():
            setattr(self, key, value)
            self.save()

    def __str__(self):
        return self.title