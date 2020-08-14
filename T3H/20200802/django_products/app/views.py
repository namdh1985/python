from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()
productList = []

def index(request):
    return render(request, 'index.html', {'productList': productList})

def createProduct(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        price = request.POST['price']
        file = request.FILES.get('img')
        if file and file.name != '':
            saved_path = fs.save('static/'+ file.name, file)
            img_path = '/' + saved_path
        else:
            img_path = None

        productList.append({'code': code, 'name': name, 'price': price, 'img_path': img_path})
        #print(productList)
        return redirect('/')
    return render(request, 'form.html')
