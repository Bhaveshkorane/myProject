from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import empdata

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

