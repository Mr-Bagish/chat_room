from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/', views.room, name='room'),
    path('room_validate', views.room_validate, name='room_validate'),
    path('send', views.send, name='send'),
]