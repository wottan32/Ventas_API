from django.urls import path
from .api import ProductoAPI


urlpatterns = [
    path('product/', ProductoAPI.as_view(), name = 'producto_api'),
]