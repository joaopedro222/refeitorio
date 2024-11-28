from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    FIRST_NAME_CHOICES =[
        ('Aluno', 'Aluno')
        ('Servidor', 'Servidor')
        ('Chefe', 'Chefe')
    ]
    class meta:
        model = User
        fields =['username','email', 'last_name', 'first_name']

    username = forms.CharField(label='Matricula:')
    email = forms.EmailField(label='E-mail:')
    last_name = forms.CharField(label='Nome Completo:')
    first_name = forms.ChoiceFiel(
        label ='Status:',
        choices=FIRST_NAME_CHOICES,
        widgets=forms.Select(attrs={'class':'custom-select'}),
        initial='Aluno'

    )