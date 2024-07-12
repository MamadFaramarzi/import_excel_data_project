from django.db import models
from datetime import datetime


class Data(models.Model):
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=350, blank=True)
    name = models.CharField(max_length=255, blank=True)
    product = models.CharField(max_length=150, blank=True)
    quantity = models.IntegerField(blank=True, null=True, default=None)
    unit_price = models.BigIntegerField(blank=True, null=True)
    total_price = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
