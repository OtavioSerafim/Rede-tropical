from django.contrib import admin
from .models import Post, Comentario

#Registrando o modelo de Post para poder trabalhar com eles no painel ADMIN
admin.site.register(Post)

admin.site.register(Comentario)

