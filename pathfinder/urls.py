from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/loot/5/
    path("loot/<int:player_level>/", views.loot, name="loot")
]