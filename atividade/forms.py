# forms.py
from django import forms
from .models import Hospedagem

class HospedagemForm(forms.ModelForm):
    class Meta:
        model = Hospedagem
        fields = ['cliente', 'quarto', 'data_entrada', 'data_saida', 'valor']


 

   
