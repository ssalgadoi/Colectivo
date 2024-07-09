from django.db import models
from django.utils.translation import gettext_lazy as _

class Link(models.Model):
    key = models.SlugField(verbose_name=_("Nombre clave"), max_length=100, unique=True)
    name = models.CharField(max_length=100, verbose_name=_("Red Social"))
    url = models.URLField(verbose_name=_("Enlace"), max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Fecha de edición"))

    class Meta:
        verbose_name = _("enlace")
        verbose_name_plural = _("enlaces")
        ordering = ['name']

    def __str__(self):
        return self.name