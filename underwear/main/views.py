from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def register(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
    form = RegisterForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/register.html', data)


def login(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
    form = LoginForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/login.html', data)


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
