from django.forms import ModelForm
from .models import ProfessoresInteressados, Aulas
from django.forms import Form, ModelForm, TextInput, DateField, DateInput, ImageField, FileInput, CharField, IntegerField,Select, TimeInput
from django.utils.timezone import now


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