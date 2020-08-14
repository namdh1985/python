from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

def index(request):
    return render(request, 'index.html')

def hello(request): #127.0.0.1:8000/hello
    data = {'message': 'hello'}
    return HttpResponse(json.dumps(data), content_type='application/json')

productList = [
    {'code': 'IPX', 'name': 'IPhone X', 'price': 17.5},
    {'code': 'IP8', 'name': 'IPhone 8', 'price': 11.5},
    {'code': 'IP7', 'name': 'IPhone 7', 'price': 8.5},
]

def searchProduct(request): #127.0.0.1:8000/search_product?keyword=IP
    keyword = request.GET.get('keyword', '')
    result = [p for p in productList if keyword in p['code']
                                    or keyword in p['name']]
    return HttpResponse(json.dumps(result), content_type=('application/json'))

