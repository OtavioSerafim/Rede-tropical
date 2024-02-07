from django.contrib import admin
from .models import Post

#Registrando o modelo de Post para poder trabalhar com eles no painel ADMIN
admin.site.register(Post)


