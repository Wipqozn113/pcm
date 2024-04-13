from django.db import models
from .location import Location

class Encounter(models.Model):
    name = models.CharField(max_length=100)
    DIFFICULTY_CHOICES = {
        "T": "Trivial",
        "L": "Low",
        "M": "Moderate",
        "S": "Severe",
        "E": "Extreme"
    }
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    monster_1 = models.CharField(null=True, blank=True)
    monster_1_URL = models.URLField(null=True, blank=True)
    monster_2 = models.CharField(null=True, blank=True)
    monster_2_URL = models.URLField(null=True, blank=True)
    monster_3 = models.CharField(null=True, blank=True)
    monster_3_URL = models.URLField(null=True, blank=True)
    monster_4 = models.CharField(null=True, blank=True)
    monster_4_URL = models.URLField(null=True, blank=True)
    monster_5 = models.CharField(null=True, blank=True)
    monster_5_URL = models.URLField(null=True, blank=True)
    monster_6 = models.CharField(null=True, blank=True)
    monster_6_URL = models.URLField(null=True, blank=True)
    monster_7 = models.CharField(null=True, blank=True)
    monster_7_URL = models.URLField(null=True, blank=True)
    monster_8 = models.CharField(null=True, blank=True)
    monster_8_URL = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class MonsterViewModel:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class EncounterViewModel:
    def __init__(self, encounter):
        self.id = encounter.id
        self.name = encounter.name
        self.difficulty = encounter.difficulty
        self.location = encounter.location
        self.monsters = self.__populateMonsters__(encounter)

    def __populateMonsters__(self, encounter):
        monsters = []

        if encounter.monster_1 is not None and encounter.monster_1_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_1, encounter.monster_1_URL))

        if encounter.monster_2 is not None and encounter.monster_2_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_2, encounter.monster_2_URL))

        if encounter.monster_3 is not None and encounter.monster_3_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_3, encounter.monster_3_URL))

        if encounter.monster_4 is not None and encounter.monster_4_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_4, encounter.monster_4_URL))

        if encounter.monster_5 is not None and encounter.monster_5_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_5, encounter.monster_5_URL))

        if encounter.monster_6 is not None and encounter.monster_6_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_6, encounter.monster_6_URL))

        if encounter.monster_7 is not None and encounter.monster_7_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_7, encounter.monster_7_URL))

        if encounter.monster_8 is not None and encounter.monster_8_URL is not None:
            monsters.append(MonsterViewModel(encounter.monster_8, encounter.monster_8_URL))

        return monsters
    
    @property
    def Difficulty(self):
        return Encounter.DIFFICULTY_CHOICES[self.difficulty]
