from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

#Cria a função que recebe os dados do post e chama a página home.html dentro da pasta template utilizando dos dados dos Posts presentes no banco da dados
"""def home(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'BlogApp/home.html', context)"""

#Cria uma classe com a mesma funcionalidade da função acima, melhorando em alguns quesitos como possibilidade de ordenação dos posts
class PostListView(ListView):
    model = Post
    template_name = 'BlogApp/home.html'
    context_object_name = 'posts'
    ordering = ['-data']
    
class PostDetailView(DetailView):
    model = Post



#Cria a função para receber o request do usuário e chama a página about.html dentro da pasta template
def about(request):
    return render(request, 'BlogApp/about.html', {'title': 'About'})
