from django.db import models

class Data(models.Model):
    date_time = models.DateField()
    location = models.CharField(max_length=350)
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name
