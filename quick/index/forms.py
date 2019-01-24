from django.forms import ModelForm
from .models import ProfessoresInteressados, Aulas
from django.forms import Form, ModelForm, TextInput, DateField, DateInput, ImageField, FileInput, CharField, IntegerField,Select, TimeInput
from django.utils.timezone import now
from django import forms
from django.contrib.auth.models import User

# Formulário de Cadastro de Usuário
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets ={
            'username': forms.TextInput(attrs={'max_length': 100}),
            'password': forms.PasswordInput(attrs={'max_length': 100}),
            'email': forms.EmailInput(attrs={'max_length': 100}),
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class InteresseForm(ModelForm):
    class Meta:
        model = ProfessoresInteressados
        fields = ['nome', 'foto', 'disciplina']
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder':'Primeiro Nome'}),
            'foto': FileInput(attrs={'class':'input'}),
            'disciplina': Select(attrs={'class': 'form-control', 'placeholder':'Disciplina'})
        }
    

class ProfessorForm(ModelForm):
    class Meta:
        model = ProfessoresInteressados
        fields = ['nome', 'foto','disciplina']
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder':'Primeiro Nome'}),
            'foto': FileInput(attrs={'class':'input'}),
            'disciplina': TextInput(attrs={'class': 'form-control', 'placeholder':'Disciplina'})
        }
    

class PedidoForm(ModelForm):
    class Meta:
        model = ProfessoresInteressados
        fields = ['foto']
        widgets = {
            'foto': FileInput(attrs={'class':'input'})
        }


class AulaForm(ModelForm):
    class Meta:
        model = Aulas
        fields = ['dia','horario','duracao','disciplina','conteudo']
        widgets = {
            'dia' : TextInput(attrs={'class': 'form-control', 'placeholder':'Dia da aula'}),
            'horario': TimeInput(attrs={'class':'form-control', 'placeholder':'Horario da aula'}),
            'duracao': TimeInput(attrs={'class':'form-control', 'placeholder':'Duração da aula'}),
            'disciplina' : TextInput(attrs={'class': 'form-control', 'placeholder':'Disciplina ministrada na aula'}),
            'conteudo' : TextInput(attrs={'class': 'form-control', 'placeholder':'Conteudo da aula'})
        }