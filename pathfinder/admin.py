from django.contrib import admin
from .models.npc import NPC
from .models.quest import  Quest
from .models.loot import Loot

# Register your models here.
admin.site.register(Quest)
admin.site.register(NPC)
admin.site.register(Loot)
