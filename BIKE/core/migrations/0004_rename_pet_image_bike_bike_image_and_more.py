# Generated by Django 5.0.2 on 2024-03-07 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_bike_pet_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='pet_image',
            new_name='bike_image',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pet',
            new_name='bike',
        ),
    ]
