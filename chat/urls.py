from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/', views.room, name='room'),
    path('create_room', views.create_room, name='create_room'),
    path('join_room', views.join_room, name='join_room'),
    # path('room_validate', views.room_validate, name='room_validate'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]