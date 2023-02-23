from django.db import models

class jogador(models.Model):
    nome = models.CharField(max_length=30)
    posicao = models.CharField(max_length=30)
    peDominante = models.CharField(max_length=30)
    nacionalidade = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Time(models.Model):
    nome_time = models.CharField(max_length=30)
    codigo_time = models.CharField(max_length=10)
    fundacao = models.DateField()
    titulos = models.CharField(max_length=30)


    def __str__(self):
        return self.nome_time


class Contrato(models.Model):
    Jogador = models.ForeignKey(jogador, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
