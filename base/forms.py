from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': _('Escribe tu nombre')}),
        min_length=3,
        max_length=100
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': _('Escribe tu email')}),
        min_length=3,
        max_length=100
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': _('Escribe tu mensaje')}),
        min_length=10,
        max_length=1000
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
