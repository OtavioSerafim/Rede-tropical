from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


#Cria um perfil toda vez que uma conta é criada.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
#Salva o perfil criado.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()