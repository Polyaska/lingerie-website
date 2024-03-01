from django.forms import ModelForm, TextInput, EmailInput, NumberInput, PasswordInput

from .models import Register, Login


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['mail', 'telephone', 'age', 'username', 'password', 'password2']

        widgets = {
            "mail": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "telephone": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату рождения'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ник'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'
            }),
        }


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ник'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }
