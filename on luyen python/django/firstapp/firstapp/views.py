#firstapp\views.py
from django.shortcuts import HttpResponse, render

def index(request):
    return render(request, 'index.html')

def hello(request): #127.0.0.1:8000/hello?name=A&gender=M
    name = request.GET.get('name', '')
    salutation = ''
    gender = request.GET.get('gender', '')
    if gender == 'M': salutation = 'Mr'
    if gender == 'F': salutation = 'Ms'
    return render(request, 'hello.html', {'name':name, 'salutation':salutation})