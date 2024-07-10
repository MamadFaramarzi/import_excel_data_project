from rest_framework import serializers
from .models import Data



class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['name','product','location','quantity','unit_price','total_price','date_time']




