from django.db import models
from .quest import Quest
from .location import Location

class NPC(models.Model):
    name = models.CharField(max_length=100)
    quests = models.ManyToManyField(Quest, blank=True)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name