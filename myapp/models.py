from django.db import models

# Create your models here.

from django.db import models

class PC(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Composant(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE, related_name='composants')
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} ({self.type})"
