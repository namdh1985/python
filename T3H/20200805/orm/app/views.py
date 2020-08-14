from django.shortcuts import render, redirect
from .models import *
def index(request):
    productList = Product.objects.all()
    return render(request, 'index.html', {'productList': productList})

def createProduct(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        price = request.POST['price']
        category_id = request.POST['category_id']
        p = Product(category=Category(id=category_id),
                    code=code, name=name, price=price)
        p.save()
        return redirect('/')

    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'form.html', context)