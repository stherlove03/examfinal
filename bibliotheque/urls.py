from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
   # Pour la page d'Accueil
   path('', views.home, name='home'),
   path('liste_livre/', views.listelivre, name='liste-livre'),
]