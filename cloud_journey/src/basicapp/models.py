from django.db import models

# Create your models here.
#cloud_journey/src/pets/models.py
class Pets(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()