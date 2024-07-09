from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from parler.models import TranslatableModel, TranslatedFields
from base.models import BaseModel



class Post(TranslatableModel, BaseModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name="Título"),
        content=models.TextField(verbose_name="Contenido")
    )
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name="image_posts")



    class Meta:
        verbose_name = "imagen"
        verbose_name_plural = "imagenes"
        ordering = ['-published']

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='imagenes')
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)

    class Meta:
        verbose_name = "Imagen de post"
        verbose_name_plural = "Imágenes de post"