from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from parler.models import TranslatableModel, TranslatedFields
from base.models import BaseModel
from django.contrib.auth.models import User




class Post(TranslatableModel, BaseModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, verbose_name="Título"),
        description = models.CharField(max_length=200, verbose_name="Descripción", null=True, blank=True),
        content = models.TextField(verbose_name="Contenido"),
        data = models.CharField(max_length=200, verbose_name="Datos")
    )
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen",  upload_to="blog")
    video = EmbedVideoField(verbose_name="Enlace del video", help_text="Enlace")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, related_name="valle_posts")


    class Meta:
        verbose_name = "Valle"
        verbose_name_plural = "Valles"
        ordering = ['-published']

    def __str__(self):
        return self.safe_translation_getter('title', default='')
