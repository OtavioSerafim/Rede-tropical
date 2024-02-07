from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']

    def save(self, commit=True):
        post = super().save(commit=False)
        # Faça qualquer manipulação adicional nos dados do post aqui, se necessário
        if commit:
            post.save()
        return post
