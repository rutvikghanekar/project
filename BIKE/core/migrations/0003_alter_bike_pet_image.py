# Generated by Django 5.0.2 on 2024-03-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_bike_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='pet_image',
            field=models.ImageField(upload_to='bike_images'),
        ),
    ]
