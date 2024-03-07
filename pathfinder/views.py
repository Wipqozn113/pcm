from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Loot

# Create your views here.
def loot(request, player_level):
    loot_list = Loot.objects.filter(rewarded_level=player_level)
    template = loader.get_template("pathfinder/loot.html")
    context = {
        "loot_list" : loot_list
    }
    return HttpResponse(template.render(context, request))