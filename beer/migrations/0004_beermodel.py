# Generated by Django 3.2 on 2021-06-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0003_auto_20210607_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
                ('idade', models.PositiveIntegerField()),
                ('abv', models.FloatField()),
                ('ibu', models.IntegerField()),
                ('srm', models.FloatField()),
            ],
        ),
    ]
