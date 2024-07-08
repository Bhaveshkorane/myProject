from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('addData/', views.addData, name='addData_url'),
    path('view/', views.viewDetails, name='view_url'),
    path('addNew/', views.addNew, name='addNew_url'),
]
