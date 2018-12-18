from django.forms import ModelForm
from .models import ProfessoresInteressados, Aulas
from django.forms import Form, ModelForm, TextInput, DateField, DateInput, ImageField, FileInput, CharField, IntegerField,Select



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
        fields = ['titulo']
        widgets = {
            'titulo' : TextInput(attrs={'class': 'form-control', 'placeholder':'titulo da aula'}),
        }