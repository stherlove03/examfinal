from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
   # Pour la page d'Accueil
   path('', views.home, name='home'),
   path('liste_livre/', views.listelivre, name='liste-livre'),
   path('ajouter_livre/', views.ajouter_livre, name='ajouter-livre'),
   path('afficher_un_livre/<str:code>/', views.afficher_un_livre, name='un-livre'),
   path('modifier_livre/<str:code>/', views.modifier_livre, name='modifier-livre'),
]