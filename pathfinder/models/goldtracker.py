from django.db import models

class GoldTracker(models.Model):
    level = models.IntegerField(unique=True)
    rewarded = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.level)