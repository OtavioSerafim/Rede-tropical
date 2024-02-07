from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
#Gera o formulário de criação de conta
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label = "Nome", max_length=30)
    last_name = forms.CharField(label = "Sobrenome", max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
#Gera o formulário de mudança de email e username
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']


# Gera o formulário de mudança de foto de perfil
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']
