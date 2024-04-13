from django.db import models
from .location import Location
from .npc import NPC
from .encounter import Encounter, EncounterViewModel

class Session(models.Model):
    date = models.DateField(unique=True)
    overview = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    npcs = models.ManyToManyField(NPC, blank=True)
    encounters = models.ManyToManyField(Encounter, blank=True)

    def __str__(self):
        return str(self.date)
    
class SessionViewModel:
    def __init__(self, session):
        self.date = session.date
        self.overview = session.overview
        self.notes = session.notes
        self.locations = session.locations
        self.npcs = session.npcs
        self.encounters = self.__create_encounters__(session.encounters)

    def __create_encounters__(self, encounters):
        encs = []

        for encounter in encounters.all():
            encs.append(EncounterViewModel(encounter))
        
        return encs

    

    