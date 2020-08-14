from django.shortcuts import render, redirect
from .models import *
from .forms import *
def index(request):
    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'index.html', context)

def createCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'category_form.html', context)

def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'category_form.html', context)

def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('/')
    
def listProduct(request): #127.0.0.1:8000/list_product
    productList = Product.objects.all()
    context = {'productList': productList}
    return render(request, 'product_list.html', context)

def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    context = {'form': form}
    return render(request, 'product_form.html', context)