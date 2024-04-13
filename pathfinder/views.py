from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from datetime import datetime as dt

from .models import Loot, GoldTracker, Encounter, EncounterViewModel, SessionViewModel, Session

# Create your views here.
def loot(request, player_level=settings.PARTY_LEVEL):
    perms = Loot.objects.filter(rewarded_level=player_level, consumable=False)
    consumables = Loot.objects.filter(rewarded_level=player_level, consumable=True)
    gold = GoldTracker.objects.filter(level=player_level)
    template = loader.get_template("pathfinder/loot.html")
    context = {
        "level" : player_level,
        "perms" : perms,
        "consumables": consumables,
        "gold" : gold[0]
    }
    return HttpResponse(template.render(context, request))

def encounter(request, id):
    encounter = Encounter.objects.get(id=id)
    template = loader.get_template("pathfinder/encounter.html")
    viewModel = EncounterViewModel(encounter)
    context = {
        "model" : viewModel
    }

    return HttpResponse(template.render(context, request))

def session(request, id=None):
    if id is None:
        sessions = Session.objects.all()
        for sess in sessions:
            session = sess
            if sess.date >= dt.now().date():
                break
    else:
        session = Session.objects.get(id=id)
    template = loader.get_template("pathfinder/session.html")
    viewModel = SessionViewModel(session)
    context = {
        "model" : viewModel
    }

    return HttpResponse(template.render(context, request))