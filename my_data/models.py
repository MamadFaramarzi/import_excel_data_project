from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=150)
    location = models.CharField(max_length=350)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.name
