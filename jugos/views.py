from django.shortcuts import render

# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

#Clase 'JugosSerializer'
from jugos.serializers import JugosSerializer

#Modelo 'jugos'
from jugos.models import Jugos

# Create your views here.
#Creo un ViewSet
class JugosViewSet(viewsets.ModelViewSet):    
    queryset = Jugos.objects.all().order_by('id')
    serializer_class = JugosSerializer