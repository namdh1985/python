from django.shortcuts import render, HttpResponse

#127.0.0.1:8000/app1/hello1
def hello1(request):
    return render(request, 'hello1.html')

#127.0.0.1:8000/app1/get_product_detail/<id>
#path variable
def getProductDetail(request, id):
    product = {
        'id': id,
        'name': f'Product {id}',
        'code': f'P_{id}'
    }
    context = {'product': product}
    return render(request, 'product_detail.html', context)

#127.0.0.1:8000/app1/hello2
def hello2(request):
    return render(request, 'hello2.html')
