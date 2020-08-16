from django.shortcuts import render
from .models import *

def index(request):
    keyword = request.GET.get('keyword', '')
    productList = Product.objects.all()
    context = {
        'keyword': keyword
        'productList': productList
    }
    return render(request, 'index.html', context)
