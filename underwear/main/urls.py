from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about123', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]
