from django.shortcuts import render
from .models import Livre
# Create your views here.

def home(request):
    return render(request, 'livre/home.html')

def listelivre(request):
   livre = Livre.objects.all()
   return render(request, 'livre/liste_livre.html', {'livre': livre})

def afficher_un_livre(request, code):
    livre = Livre.objects.get(pk=code)
    return render(request, 'employe/afficher_un_livre.html', {'livre': livre})
