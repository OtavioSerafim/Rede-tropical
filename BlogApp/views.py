from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
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
    
    #Cria a lista ordenada corretamente para ser usada pelo paginador    
    post_list = Post.objects.all().order_by('-data')
    #Pagina separando em grupos de 5 
    paginator = Paginator(post_list,5)
    #argumentos necessários para passar o obj de cada página
    page_number = request.GET.get('page')
    #Transforma cada página em um objeto que pode ser usado pelo código no html
    page_obj = paginator.get_page(page_number)


    context = {
        'form': form,
        'page_obj' : page_obj
    }

    return render(request, 'BlogApp/home.html', context)


#Cria a view dos posts de um usuário especifico usando uma classe List View
class UserPostListView(ListView):
    model = Post
    template_name = 'BlogApp/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    #Função para pegar corretamente o query com os posts do usuário selecionado e filtrar corretamente
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(autor=user).order_by('-data')

    #Função para passar informações de contexto necessárias para:
        #Conferir se o usuário é o mesmo da página para permitir fazer postagens por ela
        #Criar o formulário de postagem
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_user'] = get_object_or_404(User, username=self.kwargs.get('username'))
        context['form'] = PostCreateForm()
        return context
    
    #Função que permite que o formulário de postagem cumpra o requisito de POST
    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, f'Postado!')
            return redirect('post-detail', pk=post.pk)
        else:
            return self.get(request, *args, **kwargs)
    
    
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