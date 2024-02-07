from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#inicia o processo de criação de perfil
class Profile(models.Model):
    
    #Cria o modelo um pra um do Perfil do usuário
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    #Cria a dependência necessária para ter uma foto de perfil
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    
    #função para redimensionar a imagem salva em uma menor 300x300
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        