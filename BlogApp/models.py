from django.db import models
from django.utils import timezone

class Post(models.Model):
    Título = models.CharField(max_length=200)
    Contenido = models.TextField()
    Publicado = models.DateTimeField(blank=True, null=True)

    def Publicar(self):
        self.Publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.Título