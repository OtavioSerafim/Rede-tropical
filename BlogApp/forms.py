from django import forms
from .models import Post, Comentario

class PostCreateForm(forms.ModelForm):
    titulo = forms.CharField(label='Título')
    conteudo = forms.CharField(widget=forms.Textarea(attrs={'rows': 8}), label='Conteúdo')
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        

class CommentCreateForm(forms.ModelForm):
    conteudo = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Digite seu comentário aqui...' }),label='Comentário')
    

    class Meta:
        model = Comentario
        fields = ['conteudo']