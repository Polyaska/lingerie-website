from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('women123', views.women, name='women'),
    path('men123', views.men, name='men'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]
