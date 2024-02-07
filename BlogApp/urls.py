from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView

urlpatterns = [
    #Define a URL padrão do site como o diretório Home do arquivo views
    path('', views.home, name='Blog-Home'),
    
    #Cria caminhos para páginas individuais de cada post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    #Cria o caminho para a página de criar Posts
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    
    #Define o URL da página about do arquivo views
    path('about/', views.about, name= 'Blog-About'), 
]