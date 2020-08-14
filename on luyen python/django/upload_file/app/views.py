from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage()  # khởi tạo đối tượng
def index(request):
    if request.method == 'POST':
        file = request.FILES.get('img')
        if file and file.name != '':
            saved_path = fs.save('static/'+file.name, file)
            return redirect('/' + saved_path)
    return render(request, 'index.html')


