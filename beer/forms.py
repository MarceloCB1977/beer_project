from django import forms
from django.forms import ModelForm
from .models import *


class BeerForm(ModelForm):
    # gen_choice = (('1', 'Masculino'), ('2', 'Feminino'), ('3', 'Outros...'))
    # abv_choice = (('2.5 - 4.5', 'Baixo Teor'), ('4.6 - 7.0', 'Medio Teor'), ('7.1 - 20', 'Alto Teor'))
    # srm_choice = (('0', 'Cerveja Clara'), ('1', 'Cerveja Escura'))
    # gender = forms.ChoiceField(choices=gen_choice)
    # idade = forms.IntegerField()
    # abv = forms.ChoiceField(choices=abv_choice)
    # srm = forms.ChoiceField(choices=srm_choice)

    class Meta():
        model = BeerModel
        fields = ('gender', 'idade', 'abv', 'srm')

        labels = {
            'gender':'Gender',
            'idade':'Age',
            'abv':'Alcohol content',
            'srm':'Beer colour',
        }

        widgets = {
            'gender':forms.Select(attrs={'class':'form-select'}),
            'idade':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Age'}),
            'abv':forms.Select(attrs={'class':'form-select'}),
            'srm':forms.Select(attrs={'class':'form-select'}),
        }
