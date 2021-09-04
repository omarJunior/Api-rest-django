from django.shortcuts import render

# Elementos necesarios para que el API REST funcione 
from rest_framework import viewsets 
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response

#Clase 'JugosSerializer'
from postres.serializers import PostresSerializer

#Modelo 'postres'
from postres.models import Postres

# Create your views here.
#Creo un ViewSet
class PostresViewSet(viewsets.ModelViewSet):    
    queryset = Postres.objects.all().order_by('id')
    serializer_class = PostresSerializer