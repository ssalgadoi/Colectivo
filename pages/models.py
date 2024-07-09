from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel

class Page(TranslatableModel, BaseModel):
    translations = TranslatedFields(
        title=models.CharField(_("Título"), max_length=200),
        content=RichTextField(_("Contenido")),
    )
    order = models.SmallIntegerField(_("Orden"), default=0)
  

    class Meta:
        verbose_name = _("Página")
        verbose_name_plural = _("Páginas")
        ordering = ['order']
    
    def __str__(self):
        return self.title