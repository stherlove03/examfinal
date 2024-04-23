from django.shortcuts import render
from .models import Livre
# Create your views here.

def home(request):
    return render(request, 'livre/home.html')

def listelivre(request):
   livre = Livre.objects.all()
   return render(request, 'livre/liste_livre.html', {'livre': livre})
