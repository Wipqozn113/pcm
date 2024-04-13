# Generated by Django 5.0.3 on 2024-03-10 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathfinder', '0009_location_encounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='item_level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='npc',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pathfinder.location'),
        ),
        migrations.AddField(
            model_name='npc',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]