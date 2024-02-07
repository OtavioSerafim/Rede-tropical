from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    #Define a URL padrão do site como o diretório Home do arquivo views
    path('', PostListView.as_view(), name='Blog-Home'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #Define o URL da página about do arquivo views
    path('about/', views.about, name= 'Blog-About'), 
]