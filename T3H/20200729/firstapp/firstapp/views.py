#firstapp/views.py 
from django.shortcuts import HttpResponse, render

#127.0.0.1:8000
def index(request):
    return render(request, 'index.html')

#127.0.0.1:8000/hello?name=A&gender=M
def hello(request):
    name = request.GET.get('name', '')
    salutation = ''
    gender = request.GET.get('gender')
    if gender == 'M' : salutation = 'Mr'
    if gender == 'F' : salutation = 'Ms'
    context = {'name':name, 'salutation': salutation}
    return render(request, 'hello.html', context)