from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from parler.models import TranslatableModel, TranslatedFields
from base.models import BaseModel


class Post(TranslatableModel, BaseModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name="Título"),
        content=models.TextField(verbose_name="Contenido"),
    )
    
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog")
    url_link = models.URLField(verbose_name="Enlace", help_text="Enlace")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name="article_posts")
    

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['-published']

    def __str__(self):
        return self.title
