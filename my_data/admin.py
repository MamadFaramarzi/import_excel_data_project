from django.contrib import admin
from .models import Data

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['date','location','name','product','quantity', 'unit_price', 'total_price',]
    list_per_page = 10
    list_editable = ['unit_price']
    search_fields = ['name']
    actions = ['date']