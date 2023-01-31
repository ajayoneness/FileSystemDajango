from django.shortcuts import render,HttpResponse
from .models import fileDB

def fileHome(request):
    if request.method == "POST":
        des =request.POST['dec']
        file = request.FILES['file']
        obj = fileDB(description=des,document=file)
        obj.save()
        return HttpResponse("Successfully uploaded")
    return render(request,'home.html')

def display(request):
    obj = fileDB.objects.all()
    return render(request,'disp.html',{"obj":obj})