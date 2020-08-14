from django.shortcuts import render

productList = [
    {'code': 'IPX', 'name': 'Iphone X', 'price': 17.5},
    {'code': 'IP8', 'name': 'Iphone 8', 'price': 12.5},
    {'code': 'IP7', 'name': 'Iphone 7', 'price': 8.5},
]

def index(request):
    context = {'productList' : productList}
    return render(request, 'index.html', context)
