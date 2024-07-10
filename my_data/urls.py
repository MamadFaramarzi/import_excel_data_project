from django.urls import path 

from . import views

urlpatterns = [
    path('show_data/',views.show_data_view, name = 'show_data'),
]
