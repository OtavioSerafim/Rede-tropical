from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostCreateForm


#Cria a função que recebe os dados do post e chama a página home.html dentro da pasta template utilizando dos dados dos Posts presentes no banco da dados
def home(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, f'Postado!')
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostCreateForm()

    context = {
        'posts': Post.objects.all(),
        'form': form
    }

    return render(request, 'BlogApp/home.html', context)

#Cria a função para receber o request do usuário e chama a página about.html dentro da pasta template
def about(request):
    return render(request, 'BlogApp/about.html', {'title': 'About'})

#Gera a view de um post isolado
class PostDetailView(DetailView):
    model = Post


# class PostCreateView(CreateView):
#     model = Post
#     fields = ['titulo', 'conteudo']


#Cria a view de edição de Post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'conteudo']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
    
    
#Cria a view de exclusão de Post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False