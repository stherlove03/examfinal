from django.shortcuts import render
from .models import Livre
from django.views.decorators.csrf import csrf_protect
from .forms import LivreForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'livre/home.html')

def listelivre(request):
   livre = Livre.objects.all()
   return render(request, 'livre/liste_livre.html', {'livre': livre})

@csrf_protect

def ajouter_livre(request):
   submitted = False
   if request.method == 'POST':
       form = LivreForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/ajouter_livre?submitted=True')
   else:
       form = LivreForm()
       if 'submitted' in request.GET:
           submitted = True
   return render(request, 'livre/ajouter_un_livre.html', {'form':form, 'submitted':submitted})

def afficher_un_livre(request, code):
    livre = Livre.objects.get(pk=code)
    return render(request, 'employe/afficher_un_livre.html', {'livre': livre})

def modifier_livre(request, code):
    livre= Livre.objects.get(pk=code)
    form = LivreForm(request.POST or None, instance=livre)
    if form.is_valid():
        form.save()
        return redirect('liste-livre')
    return render(request, 'livre/modifier_livre.html', {'livre': livre, 'form': form})
