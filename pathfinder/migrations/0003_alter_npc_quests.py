# Generated by Django 5.0.3 on 2024-03-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathfinder', '0002_npc_quest_delete_npcmodel_npc_quests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='quests',
            field=models.ManyToManyField(blank=True, to='pathfinder.quest'),
        ),
    ]