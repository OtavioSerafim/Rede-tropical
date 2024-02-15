from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
#Import necessário para utilizar o aplicativo BlogApp
from django.urls import path, include
#Importando as views do app users para não precisar criar um url pro registro
from users import views as user_views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #Criando o Caminho para a página de Registro
    path('register/', user_views.register, name = 'register'),
    
    #Criando o Caminho para a página de Perfil
    path('profile/', user_views.profile, name = 'profile'),
    
    #Criando o Caminho para a página de Login
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
    
    #Criando o Caminho para a página de Resposta de Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    
    #Criando o caminho para a página de Reset de senha
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
         name = 'password_reset'),
    
    #Criando o caminho para a página de resposta de Reset de Senha
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name = 'password_reset_done'),
    
    #Cria o caminho com o token para a troca da senha do usuário (link que recebe no email)
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name = 'password_reset_confirm'),
    
    #Cria o caminho para a página de confirmação de troca de senha
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name = 'password_reset_complete'),
    
    
    #Definindo o caminho padrão do home para o aplicativo BlogApp
    path('', include('BlogApp.urls'))
    
    

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)