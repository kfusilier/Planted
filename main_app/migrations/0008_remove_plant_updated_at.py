# Generated by Django 4.0.3 on 2022-04-06 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_plant_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='updated_at',
        ),
    ]