from django.shortcuts import render, HttpResponse
from django.contrib import messages, auth
from .models import empdata,profile
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def addData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        salary = request.POST.get('salary')
        print(name, age, salary, email, department, phone)

        data = empdata(name=name, age=age, email=email, phone=phone, department=department, salary=salary)
        data.save()
        return render(request, 'addNew.html')

def addNew(request):
    return render(request, 'addNew.html')

def viewDetails(request):
    mydata = empdata.objects.filter(name='bhavesh ').values()
    return render(request, 'view.html', context={'data': mydata})


def signup(request):
    if request.method == 'POST':
        username=request.POST['uname']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        location=request.POST['location']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']




    return render(request, 'registration.html')

def login(request):
    return render(request,'login.html')

