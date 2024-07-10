from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=150)
    location = models.CharField(max_length=350)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField()
    total_price = models.DecimalField()
    date_time = models.DateTimeField()
