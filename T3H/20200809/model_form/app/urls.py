from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('create_category', createCategory, 
        name='create-category'),
    path('update_category/<pk>', updateCategory, name='update-category'),
    path('delete_category/<pk>', deleteCategory, name='delete-category'),
    path('list_product', listProduct, name='list-product'),
    path('create_product', createProduct, name='create-product'),
    
]