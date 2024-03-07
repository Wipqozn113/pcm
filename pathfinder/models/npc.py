from django.db import models
from .quest import Quest

class NPC(models.Model):
    name = models.CharField(max_length=100)
    quests = models.ManyToManyField(Quest, blank=True)

    def __str__(self):
        return self.name