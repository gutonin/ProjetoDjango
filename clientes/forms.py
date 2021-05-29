from django.forms import ModelForm, fields

from .models import Pessoa


class FormPessoa(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'sobrenome', 'idade', 'salario', 'bio', 'foto']