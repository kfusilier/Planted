# Generated by Django 4.0.3 on 2022-04-06 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_plant_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='updated_at',
        ),
    ]
