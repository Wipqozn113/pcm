from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    LOCATION_TYPE = {
        "TWN" : "Town",
        "RGN" : "Region",
        "DNG" : "Dungeon",
        "OTH" : "Other"
    }
    type = models.CharField(max_length=3, choices=LOCATION_TYPE)
    description = models.TextField()
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    item_level = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
