from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def addNew(request):
    return render(request,'addNew.html')

def login(request):
    return render(request,'login.html')