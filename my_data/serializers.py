from rest_framework import serializers
from .models import Data


class DataSerializers(serializers.Serializer):
        file = serializers.FileField()

    # class Meta:
    #     model = Data
        # fields = ['name', 'product', 'location', 'quantity', 'unit_price', 'total_price', 'date']
        # date = serializers.DateField(format="%Y-%m-%d")
