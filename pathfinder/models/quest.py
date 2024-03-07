from django.db import models

class Quest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rewards = models.TextField(blank=True)
    
    def __str__(self):
        return self.name