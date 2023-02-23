from rest_framework import serializers
from jogadores.models import jogador,Time,Contrato #trazendo os modelos

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = jogador
        fields = ['nome','posicao','peDominante','nacionalidade']

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields ='__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        exclude = []