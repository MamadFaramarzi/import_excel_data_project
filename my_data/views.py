from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

import pandas as pd

from .models import Data
from .serializers import DataSerializers

@api_view(['POST'])
def show_data(request):
    if request.method == 'POST' and request.FILES.get('file'):
        excel_file = request.FILES['file']
        df = pd.read_excel('Excel_Data.xlsx')

        serializer = DataSerializers(data=df.to_dict(orient='records'), many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "No file found in request"}, status=status.HTTP_400_BAD_REQUEST)

































# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# import pandas as pd

# from .models import Data
# from .serializers import DataSerializers


# @api_view()
# def show_data(request,):

#     excel_file = request.FILES.get('Excel_Data.xlsx')
#     df = pd.read_excel(excel_file)

#     # my_data = Data.objects.all()
#     # serializer = DataSerializers(my_data, many=True)
#     serializer = DataSerializers(data=df.to_dict(orient='records'), many=True)


#     serializer.is_valid(raise_exception=True)
#     serializer.validated_data

#     return Response(serializer.data)



