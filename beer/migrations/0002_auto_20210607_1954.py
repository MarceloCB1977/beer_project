# Generated by Django 3.2 on 2021-06-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beerdata',
            name='ABV_max',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='beerdata',
            name='ABV_min',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='beerdata',
            name='IBU_max',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='beerdata',
            name='IBU_min',
            field=models.FloatField(),
        ),
    ]
