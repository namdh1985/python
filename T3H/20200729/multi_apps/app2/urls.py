#app2/urls.py

from django.urls import path
from .views import *
urlpatterns = [
    #127.0.0.1:8000/app2/hello3
    path('hello3', hello3),
    #127.0.0.1:8000/app2/hello4
    path('hello4', hello4),
]