#app1/urls.py

from django.urls import path
from .views import *
urlpatterns = [
    path('hello1', hello1),
    path('hello2', hello2),
    path('get_product_detail/<id>', getProductDetail),
]