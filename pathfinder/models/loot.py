from django.db import models

class Loot(models.Model):
    name = models.CharField(max_length=100)
    aon_link = models.URLField(blank=True, null=True)
    item_level = models.IntegerField()
    rewarded_level = models.IntegerField()
    awarded = models.BooleanField()
    consumable = models.BooleanField()

    def __str__(self):
        return self.name
