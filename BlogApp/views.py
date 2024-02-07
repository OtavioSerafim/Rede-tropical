from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, CreateView
from .models import Post
from .forms import PostCreateForm

#Cria a função que recebe os dados do post e chama a página home.html dentro da pasta template utilizando dos dados dos Posts presentes no banco da dados
def home(request):
    #Estruturas necessárias para criar um Post pelo Home
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        #Se ele for válido, salva o post e recarrega a página
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, f'Postado!')
            return redirect('Blog-Home')
    else:
        form = PostCreateForm()

    context = {
        'posts': Post.objects.all(),
        'form': form
    }

    return render(request, 'BlogApp/home.html', context)


class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'conteudo']

#Cria a função para receber o request do usuário e chama a página about.html dentro da pasta template
def about(request):
    return render(request, 'BlogApp/about.html', {'title': 'About'})
