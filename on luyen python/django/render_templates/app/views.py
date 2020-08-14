from django.shortcuts import render

#productList = [
    #{'code': 'IPX', 'name': 'Iphone X', 'price': 17.5},
    #{'code': 'IP8', 'name': 'Iphone 8', 'price': 11.5},
    #{'code': 'IP7', 'name': 'Iphone 7', 'price': 8.5},
#]

def index(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        price = request.POST['price']
        return render(request, 'saved.html', {'code':code,'name':name,'price':price})
    return render(request, 'index.html')
