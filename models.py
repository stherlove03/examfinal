# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



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

     