from django.urls import path 

from . import views

urlpatterns = [
    path('import/',views.ImportApiView.as_view(), name='import_view'),
    path('export/',views.ExportApiView.as_view(), name="Export_view"),
]
