from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

import pandas as pd
from .serializers import DataSerializers
from . models import Data



class DisplayData(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializers

    def post(self, request, *args, **kwargs):
        df = pd.read_excel('./Excel_Data.xlsx',header =None, names=['date_time','location','name','product','quantity','unit_price','total_price'])

        data_list = []
        for index, row in df.iterrows():
            data_dict = {
                'date_time': row['date_time'],  
                'location': row['location'],  
                'name': row['name'], 
                'product': row['product'], 
                'quantity': row['quantity'], 
                'unit_price': row['unit_price'], 
                'total_price': row['total_price'], 
            }

            data_list.append(data_dict)

        print(f'data frame: {df}')
        serializer = self.get_serializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        



# @api_view(['GET', 'POST'])
# def show_data(request):

#     if request.method == "GET":
#         data_queryset = Data.objects.all()
#         serializer = DataSerializers(data_queryset,context={'request':request},many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     elif request.method == 'POST':
#         print('hello')
#         # excel_file_path = './Excel_Data.xlsx' 
#         df = pd.read_excel('./Excel_Data.xlsx' )
#         print(f'data frame: {df}')

#         serializer = DataSerializers(data=df.to_dict(orient='records'), many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response({"error": "No file found in request"}, status=status.HTTP_400_BAD_REQUEST)






















