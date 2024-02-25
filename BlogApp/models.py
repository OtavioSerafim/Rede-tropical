from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#Modelo para salvar os Post na database
class Post(models.Model):
    titulo = models.CharField(max_length=64)
    conteudo = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs ={'pk':self.pk})


class Comentario(models.Model):
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField()
    data = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.conteudo
    