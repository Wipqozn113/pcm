from django.db import models

class NPCModel(models.Model):
    name = models.CharField(max_length=100)