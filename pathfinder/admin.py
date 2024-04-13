from django.contrib import admin
from .models.npc import NPC
from .models.quest import  Quest
from .models.loot import Loot
from .models.goldtracker import GoldTracker
from .models.encounter import Encounter
from .models.location import Location
from .models.session import Session

# Register your models here.
admin.site.register(Quest)
admin.site.register(NPC)
admin.site.register(Loot)
admin.site.register(GoldTracker)
admin.site.register(Encounter)
admin.site.register(Location)
admin.site.register(Session)