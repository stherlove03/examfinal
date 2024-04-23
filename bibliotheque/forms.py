from django import forms
from django.forms import ModelForm
from .models import Livre

class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields = ('titre','auteur','annee_publication', 'genre')
        labels = {
           'titre': '',
           'auteur': '',
           'annee_publication': '',
           'genre': '',
        }
       # Widgets nous permettra de styliser notre forme avec Bootstrap
        widgets={
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Auteur'}),
            'annee_publication': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Année de Publication'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}),
       }
