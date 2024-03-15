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
            return redirect('home')
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


def women(request):
    context = {
        'title': 'женщинам',
        'goods': [
            {
                'image': 'main/img/1RB1908001-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Бюстгальтер-Балконет Paris Fancy Bride',
                'price': 50,
            },
            {
                'image': 'main/img/1RI1915270W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Слегка Уплотненный Бюстгальтер-Балконет Wien Glitter Garden Lace',
                'price': 500,
            },
            {
                'image': 'main/img/1SB1906269W-M.jpg',
                'name': 'Нижнее белье',
                'description': 'Бразильяно Soft Mint Cammeo',
                'price': 500,
            },
            {
                'image': 'main/img/1TS1906269W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Бюстгальтер-Треугольник Lisbon Soft Mint Cammeo',
                'price': 500,
            },
            {
                'image': 'main/img/1SP1903258W-M.jpg',
                'name': 'Нижнее белье',
                'description': 'Стринги Pearl Pink Lace',
                'price': 500,
            },
            {
                'image': 'main/img/1TS060257W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Бюстгальтер-Треугольник Lisbon из Переработанного Кружева Без Уплотнения',
                'price': 500,
            },
            {
                'image': 'main/img/1RB1905A019-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Бюстгальтер-Балконет Paris Midnight Lace',
                'price': 500,
            },
            {
                'image': 'main/img/1RT1915270W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Уплотненный Бюстгальтер Бра-Топ Пуш-Ап Glitter Garden Lace',
                'price': 500,
            },
            {
                'image': 'main/img/1TI1905265W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Бюстгальтер-Треугольник Havana Midnight Lace с Легким Уплотнением',
                'price': 500,
            },
        ]
    }
    return render(request, 'main/women.html', context)


def men(request):
    context = {
        'title': 'мужчинам',
        'goods_men': [
            {
                'image': 'main/img/2SB550A429W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Хлопковые Боксеры с Контрастными Строчками и Логотипами',
                'price': 50,
            },
            {
                'image': 'main/img/2SB15D019-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Боксеры из эластичного хлопка с закрытой резинкой',
                'price': 500,
            },
            {
                'image': 'main/img/2SB15D001-M.jpg',
                'name': 'Нижнее белье',
                'description': 'Хлопковые Боксеры с Контрастной Окантовкой и Логотипом',
                'price': 500,
            },
            {
                'image': 'main/img/2SB550T425W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Хлопковые Боксеры с Принтом, Контрастной Окантовкой и Логотипами',
                'price': 500,
            },
            {
                'image': 'main/img/2SB550A430W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Хлопковые Боксеры с Контрастными Строчками и Логотипами',
                'price': 500,
            },
            {
                'image': 'main/img/2SB5506001-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Боксеры из эластичного хлопка с закрытой резинкой',
                'price': 500,
            },
            {
                'image': 'main/img/2SB550T424W-M.jpg',
                'name': 'Нижнее белье',
                'description': 'Хлопковые Боксеры с Контрастной Окантовкой и Логотипом',
                'price': 500,
            },
            {
                'image': 'main/img/2SB550A427W-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Боксеры из эластичного хлопка с закрытой резинкой',
                'price': 500,
            },
            {
                'image': 'main/img/2SN550660V-FI.jpg',
                'name': 'Нижнее белье',
                'description': 'Хлопковые Слипы с Контрастной Окантовкой и Логотипом',
                'price': 500,
            },
        ]
    }
    return render(request, 'main/men.html', context)
