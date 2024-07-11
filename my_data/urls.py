from django.urls import path 

from . import views

urlpatterns = [
    path('display_data/',views.DisplayData.as_view(), name = 'show_data'),
]
