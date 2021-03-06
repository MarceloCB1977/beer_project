# Generated by Django 3.2 on 2021-06-07 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=200)),
                ('style_key', models.CharField(max_length=20)),
                ('style_number', models.PositiveIntegerField()),
                ('ABV_min', models.PositiveIntegerField()),
                ('ABV_max', models.PositiveIntegerField()),
                ('IBU_min', models.PositiveIntegerField()),
                ('IBU_max', models.PositiveIntegerField()),
                ('SRM_min', models.PositiveIntegerField()),
                ('SRM_max', models.PositiveIntegerField()),
                ('style_groups', models.CharField(max_length=20)),
                ('style_key_family', models.CharField(max_length=100)),
                ('recommend', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
