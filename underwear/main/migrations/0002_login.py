# Generated by Django 4.2.9 on 2024-03-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Введите свой ник')),
                ('password', models.CharField(max_length=50, verbose_name='Введите пароль')),
            ],
        ),
    ]
