from django.db import models

# Create your models here.


class ProfessoresInteressados(models.Model):
    nome = models.TextField(max_length = 200)
    sobrenome = models.TextField(max_length = 200)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    senha = models.TextField(max_length=100, null=True, blank=True)
    endereco = models.TextField(max_length= 200, null=True, blank=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    cidade =  models.CharField(max_length=40, blank=True, null=True)
    estado =  models.CharField(max_length=40, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    foto = models.ImageField(upload_to='professores', blank=True, null=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.PROTECT)

class Professor(models.Model):
    nome = models.TextField(max_length = 200)
    sobrenome = models.TextField(max_length = 200)
    cep = models.CharField(max_length=9, blank=True, null=True)
    foto = models.FileField(upload_to='media/', blank=True, null=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.PROTECT)

class Disciplina(models.Model):
    nome = models.TextField()
    def __str__(self):
        return self.nome
    def professores(self):
        return ProfessoresInteressados.objects.filter(disciplina = self)

class Aulas(models.Model):
    titulo = models.TextField(max_length= 200)
    nome = models.TextField(max_length = 100)


    
