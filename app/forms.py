from django import forms
from .models import Servidor
import os
from django.forms import ValidationError
from django.core.validators import MinValueValidator

from django.forms.widgets import ClearableFileInput


class ValidForm(forms.Form):
    nome  = forms.CharField(max_length = 100) 
    cpf   = forms.CharField(max_length = 11) 
    imagem=forms.ImageField(widget=ClearableFileInput)
    print(cpf)
    def clean_cpf(self):
        _cpf = self.cleaned_data['cpf']
        print(_cpf)
        a = validar_cpf(_cpf)
        
        if a == True:
            if not Servidor.objects.filter(cpf = _cpf):
                return _cpf
            else: 
                raise ValidationError("O cpf inserido é inválido ou já existe!")
    
class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ('nome','cpf', 'imagem')
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'max_length': 255,
                'placeholder': 'aaaaa'
            }),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }
        error_messages = {
                'nome' :{
                    'required': 'Campo obrigatório'
                },
            }
        


def validar_cpf(numbers):
        #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]
    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False
    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True
