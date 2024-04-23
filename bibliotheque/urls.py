from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
   # Pour la page d'Accueil
   path('', views.home, name='home'),
   path('liste_livre/', views.listelivre, name='liste-livre'),
    path('afficher_un_livre/<str:code>/', views.afficher_un_livre, name='un-livre'),
]