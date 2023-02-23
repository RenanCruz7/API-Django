from rest_framework import viewsets, generics
from jogadores.models import jogador, Time, Contrato
from jogadores.serializer import JogadorSerializer, TimeSerializer, ContratoSerializer

class JogadoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os jogadores"""
    queryset = jogador.objects.all()
    serializer_class = JogadorSerializer

class TimesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os times"""
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

