from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        price = request.POST['price']
        #TODO: Save to db
        context = {'code':code, 'name':name, 'price':price}
        return render(request, 'saved.html', context)
    return render(request, 'index.html')
