# Generated by Django 4.1.5 on 2023-07-16 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passanger'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passanger',
            old_name='flight',
            new_name='flights',
        ),
    ]
