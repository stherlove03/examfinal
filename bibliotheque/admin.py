from django.contrib import admin
from .models import Livre
# Register your models here.
class affichagelivre(admin.ModelAdmin):
    list_display = ['code','titre','auteur','annee_publication', 'genre']

admin.site.register(Livre , affichagelivre)
