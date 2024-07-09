from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
  # Importar el modelo User

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        abstract = True
        
    def __str__(self):
        return str(self.author)  # Devolver una representación en cadena del autor

class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name=_("Ingresa tu nombre"))
    email = models.EmailField(max_length=20, verbose_name=_("Escribe tu email"))
    message = models.TextField(max_length=100, verbose_name=_("Escribe tu mensaje"))
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-created']

    def __str__(self):
        return self.name
