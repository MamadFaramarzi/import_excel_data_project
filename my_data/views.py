from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

import pandas as pd
from .serializers import DataSerializers
from .models import Data


class ImportApiView(APIView):
    serializer_class = DataSerializers
    parser_classes = [MultiPartParser,FormParser]
    # queryset = Data.objects.all()

    def post(self, request):
        try :
            data = request.FILES
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response({
                    'status':False,
                    'massage': 'Provide a valid file'
                },status=status.HTTP_400_BAD_REQUEST)

            exel_file = data.get('file')
            df = pd.read_excel(exel_file,sheet_name=0)

            data_list = []
            for index, row in df.iterrows():
                date = row['date']
                location = row['location']
                name = row['name']
                product = row['product']
                quantity = row['quantity']
                unit_price = row['unit_price']
                total_price = row['total_price']
                data = Data.objects.all()
                if data.exist():
                    continue
                date = Data(
                    date=date,
                    location=location,
                    name=name,
                    product=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    total_price=total_price,
                )
                data_list.append(data)
            Data.objects.bulk_create(data_list)
            return Response({
                'status': True,
                'massage': 'data imported successfully'
            }, status=status.HTTP_201_CREATED)

        except Exception as e :
            return Response({
                'status': False,
                'massage':'not complete import'
            }, status=status.HTTP_400_BAD_REQUEST)


        # df = pd.read_excel('./Excel_Data.xlsx', header=None,
        #                    names=['date', 'location', 'name', 'product', 'quantity', 'unit_price', 'total_price'])
        #
        # data_list = []
        # for index, row in df.iterrows():
        #     data_dict = {
        #         'date': row['date'],
        #         'location': row['location'],
        #         'name': row['name'],
        #         'product': row['product'],
        #         'quantity': row['quantity'],
        #         'unit_price': row['unit_price'],
        #         'total_price': row['total_price'],
        #     }
        #     # df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce').dt.strftime('%Y-%m-%d')
        #
        #     data_list.append(data_dict)
        #
        # print(f'data frame: {df}')
        # serializer = self.get_serializer(data=data_list, many=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        #
        #
















# class DisplayData(generics.ListCreateAPIView):
#     queryset = Data.objects.all()
#     serializer_class = DataSerializers
#
#     def post(self, request, *args, **kwargs):
#         df = pd.read_excel('./Excel_Data.xlsx', header=None,
#                            names=['date', 'location', 'name', 'product', 'quantity', 'unit_price', 'total_price'])
#
#         data_list = []
#         for index, row in df.iterrows():
#             data_dict = {
#                 'date': row['date'],
#                 'location': row['location'],
#                 'name': row['name'],
#                 'product': row['product'],
#                 'quantity': row['quantity'],
#                 'unit_price': row['unit_price'],
#                 'total_price': row['total_price'],
#             }
#             # df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce').dt.strftime('%Y-%m-%d')
#
#             data_list.append(data_dict)
#
#         print(f'data frame: {df}')
#         serializer = self.get_serializer(data=data_list, many=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)




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
