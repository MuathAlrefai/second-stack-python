# Generated by Django 2.2.4 on 2023-06-06 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TVShows_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='Title',
            new_name='title',
        ),
    ]
