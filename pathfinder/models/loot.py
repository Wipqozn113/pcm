from django.db import models

class Loot(models.Model):
    name = models.CharField(max_length=100)
    item_level = models.IntegerField()
    rewarded_level = models.IntegerField()
    awarded = models.BooleanField()
    consumable = models.BooleanField()
