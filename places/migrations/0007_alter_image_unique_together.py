# Generated by Django 4.0.10 on 2023-12-23 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_remove_place_place_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='image',
            unique_together={('id', 'order')},
        ),
    ]
