from django.contrib import admin
from jogadores.models import jogador, Time, Contrato


class Jogadores(admin.ModelAdmin):
    list_display=('nome','posicao','peDominante','nacionalidade')
    list_display_links=('nome','posicao')
    search_fields=('nome',)
    list_per_page = 20

admin.site.register(jogador,Jogadores)

class Times(admin.ModelAdmin):
    list_display=('nome_time','codigo_time','fundacao','titulos')
    list_display=('nome_time','codigo_time')
    search_fields=('codigo_time',)


admin.site.register(Time,Times)

class Contratos(admin.ModelAdmin):
    list_display=('Jogador','time')
    list_display_links=('Jogador',)

admin.site.register(Contrato,Contratos)