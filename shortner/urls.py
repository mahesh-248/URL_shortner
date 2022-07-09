from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go') #here in <str:pk>, pk is declared as string which stores encoded shortened URL helps to access the original link through databse 
]