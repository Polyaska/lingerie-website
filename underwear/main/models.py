from django.db import models


class Register(models.Model):
    mail = models.CharField('Введите почту', max_length=150)
    telephone = models.IntegerField('Введите номер телефона')
    age = models.IntegerField('Введите дату рождения')
    username = models.CharField('Придумайте ник', max_length=50)
    password = models.CharField('Введите пароль', max_length=50)
    password2 = models.CharField('Повторите пароль', max_length=50)


class Login(models.Model):
    username = models.CharField('Введите свой ник', max_length=50)
    password = models.CharField('Введите пароль', max_length=50)


class Product(models.Model):
    photo = models.ImageField('фото')
    name = models.CharField('название', max_length=150)
    description = models.CharField('описание', max_length=250)
    price = models.IntegerField('цена')
    size = models.CharField('размер', max_length=15)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


