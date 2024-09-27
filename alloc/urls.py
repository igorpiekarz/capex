from django.contrib import admin
from django.urls import path
from alloc import views

urlpatterns=[
    path('',views.index,name='index'),
    
]