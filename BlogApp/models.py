from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Modelo para salvar os Post na database
class Post(models.Model):
    titulo = models.CharField(max_length=64)
    conteudo = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.titulo

class Teste(models.Model):
    nome = models.CharField(max_length=64)