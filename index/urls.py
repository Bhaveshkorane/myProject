from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index_url'),
    path('login/',views.login,name='login_url'),
    path('addNew/',views.addNew,name='addNew_url')
]