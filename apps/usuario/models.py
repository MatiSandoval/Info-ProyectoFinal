from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Usuario(AbstractBaseUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuario/default.png')
    
    def get_absolute_url(self):
        return reverse('index')