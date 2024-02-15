from django.urls import path
from . import views
from .views import PostDetailView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    #Define a URL padrão do site como o diretório Home do arquivo views
    path('', views.home, name='Blog-Home'),
    
    #Define a URL para página de posts de um usuário especifico
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    #Cria caminhos para páginas individuais de cada post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    #Cria o caminho para a página de criar Posts
    #path('post/new/', PostCreateView.as_view(), name='post-create'), 
    
    #Cria o caminho para a página de atualização de Posts
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    #Cria o caminho para a página de excluir Post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    
    #Define o URL da página about do arquivo views
    path('about/', views.about, name= 'Blog-About'), 
]