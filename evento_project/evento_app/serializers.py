from rest_framework import routers, serializers, viewsets
from evento_app.models import *

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ArtigoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'

class AvaliacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
