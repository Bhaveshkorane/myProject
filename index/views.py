from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages, auth
from .models import empdata,Profile
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


# def signup(request):
#     if request.method == 'POST':
#         username=request.POST['uname']
#         first_name=request.POST['fname']
#         last_name=request.POST['lname']
#         email=request.POST['email']
#         age=request.POST['age']
#         gender=request.POST['gender']
#         location=request.POST['location']
#         pass1=request.POST['pass1']
#         pass2=request.POST['pass2']

#         if pass1 == pass2:
#             if User.objects.filter(email = email).exists():
#                 messages.info(request,"the email already exist")
#                 return redirect('signup/')
#             if User.objects.filter(username = username).exists():
#                 messages.info(request,"user name already exist")
#                 return redirect('signup/')
#             else:
#                 User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,age=age,gender=gender,location=location,password=pass1)
#                 User.save()

#                 user_model=User.objects.get(username=username)
#                 new_profile=profile.objects.create(user=user_model,id_user=user_model.id)
#                 new_profile.save()
#                 return redirect('login/')
#         else:
#             messages.info(request,"Enter correct password")
#             return redirect('signup/')
#     else:
#         return render(request, 'registration.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

def signup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        location = request.POST['location']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "The email already exists")
                return redirect('signup/')
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('signup/')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=pass1)
                user.save()

                profile = Profile(user=user, age=age, gender=gender, location=location)
                profile.save()

                return redirect('login/')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('signup/')
    else:
        return render(request, 'registration.html')


def login(request):
    return render(request,'login.html')

