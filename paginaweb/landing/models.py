from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    fecha=models.DateTimeField(auto_now_add=True)
    publicado=models.BooleanField()

class Users(models.Model):
    user=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


