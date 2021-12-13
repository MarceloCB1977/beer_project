from django.db import models

# Create your models here.
class BeerData(models.Model):
    style_name = models.CharField(max_length=200)
    ABV_min = models.FloatField()
    ABV_max = models.FloatField()
    IBU_min = models.FloatField()
    IBU_max = models.FloatField()
    SRM_min = models.IntegerField()
    SRM_max = models.IntegerField()
    style_key_family = models.CharField(max_length=200)
    recommend = models.CharField(max_length=200)
    image = models.ImageField()
    food_pair = models.TextField(max_length=1000, blank=True)
    desc = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.style_name


gen_choice = [('1', 'Male'), ('2', 'Female'), ('3', 'Others...')]
abv_choice = [('2.5 - 4.5', 'Low Alcohol'), ('4.6 - 7.0', 'Medium Alcohol'), ('7.1 - 20', 'High Alcohol')]
srm_choice = [('0', 'Light Colour'), ('1', 'Dark Colour')]


class BeerModel(models.Model):
    gender = models.CharField(max_length=50, choices=gen_choice, default='1')
    idade = models.PositiveIntegerField()
    abv = models.FloatField(choices=abv_choice, default='2.5 - 4.5')
    srm = models.FloatField(choices=srm_choice, default='0')

    def __str__(self):
        return self.gender + ' ' + self.idade
