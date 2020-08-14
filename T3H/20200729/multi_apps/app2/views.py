from django.shortcuts import render, HttpResponse

def hello3(request):
    return render(request, 'hello3.html')

def hello4(request):
    return render(request, 'hello4.html')
