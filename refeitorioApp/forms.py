from refeitorioApp.models import Aluno, Evento
from django import forms

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        #fields =['nome_aluno', 'matricula_aluno', 'foto_aluno']
        fields ='__all__'