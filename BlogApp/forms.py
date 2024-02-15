from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    titulo = forms.CharField(label='Título')
    conteudo = forms.CharField(widget=forms.Textarea(attrs={'rows': 8}), label='Conteúdo')
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']