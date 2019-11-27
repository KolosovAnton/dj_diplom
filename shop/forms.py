from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Review


class ReviewForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '1', 'cols': '25'}),
        label='Имя')
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '5', 'cols': '25'}),
        label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')


class RegisterForm(UserCreationForm):
    username = forms.EmailField(
        label='Email:',
        widget=forms.TextInput
    )
    password1 = forms.CharField(
        label='Придумайте пароль:',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтвердите пароль:',
        widget=forms.PasswordInput
    )


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email:',
        widget=forms.TextInput
    )
    password = forms.CharField(
        label='Пароль:',
        widget=forms.PasswordInput
    )
