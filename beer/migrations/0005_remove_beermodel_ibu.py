# Generated by Django 3.2 on 2021-06-21 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0004_beermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beermodel',
            name='ibu',
        ),
    ]