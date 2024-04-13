# Generated by Django 5.0.3 on 2024-03-14 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pathfinder', '0018_location_type_alter_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pathfinder.location'),
        ),
    ]
