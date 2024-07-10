from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import pandas as pd

from .models import Data
from .serializers import DataSerializers


@api_view()
def show_data_view(request,):
    # my_data = Data.objects.all()
    # serializer = DataSerializers(my_data, many=True)
    serializer = DataSerializers(data=df.to_dict(orient='records'), many=True)

    excel_file = request.FILES.get('Excel_Data')
    df = pd.read_excel(excel_file)

    serializer.is_valid(raise_exception=True)
    serializer.validated_data

    return Response(serializer.data)