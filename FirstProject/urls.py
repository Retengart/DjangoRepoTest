# from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('home/', views.home),
    path('about', views.about),
    path('items/<int:id>', views.item_page),
    path('items/', views.item_list),
]
