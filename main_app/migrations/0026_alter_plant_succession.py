# Generated by Django 4.0.3 on 2022-04-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_alter_plant_seed_depth_alter_plant_succession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='succession',
            field=models.CharField(choices=[('Not Applicable', 'N/A'), ('Re-seed every 7 days', 'every 7 days'), ('Re-seed every 14 days', 'every 14 days'), ('Re-seed every 21 days', 'every 21 days'), ('Re-seed every 30 days', 'every 30 days')], max_length=50),
        ),
    ]