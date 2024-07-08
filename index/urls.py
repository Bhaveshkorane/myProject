from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('addData/', views.addData, name='addData_url'),
    path('view/', views.viewDetails, name='view_url'),
    path('addNew/', views.addNew, name='addNew_url'),
    path('signup/',views.signup,name='signup_url'),
    path('login/',views.login,name='login_url')
]
