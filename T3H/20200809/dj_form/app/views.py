from django.shortcuts import render
from .forms import *
def index(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            context = {'form': form.cleaned_data}
            return render(request, 'confirm.html', context)

    context = {'form': form}
    return render(request, 'index.html', context)
