from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from evento_app.models import *
from evento_app.serializers import *

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ArtigoViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

def manipularEvento(request):
    return HttpResponse("http://127.0.0.1:8000/eventos/")
