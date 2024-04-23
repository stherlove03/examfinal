from django.db import models

# Create your models here.

class Livre(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    annee_publication = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self) :
        return self.titre
    
    
    class Meta:
        managed = False
        db_table = 'livre'