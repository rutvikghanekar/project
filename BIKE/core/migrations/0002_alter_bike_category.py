# Generated by Django 5.0.2 on 2024-03-07 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='category',
            field=models.CharField(choices=[('SPORT_BIKE', 'sport_bike'), ('ELECTRIC_BIKE', 'electric_bike'), ('ELECTRIC_SCOTY', 'electric_bike')], max_length=20),
        ),
    ]
