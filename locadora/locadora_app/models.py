from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()

class Filme(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    preco = models.FloatField()

class Aluguel(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
