# Generated by Django 5.0.3 on 2024-03-12 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathfinder', '0015_remove_encounter_monsters_remove_encounter_mts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encounter',
            old_name='monster1url',
            new_name='monster1_URL',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='monster2url',
            new_name='monster2_URL',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='monster3url',
            new_name='monster3_URL',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='monster4url',
            new_name='monster4_URL',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='monster5url',
            new_name='monster5_URL',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='monster6url',
            new_name='monster6_URL',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='monster7url',
            new_name='monster7_URL',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='monster8url',
            new_name='monster8_URL',
        ),
    ]
