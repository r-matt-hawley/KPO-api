from django.shortcuts import render
from music.serializers import UserSerializer, ConcertSerializer, SongSerializer, PartSerializer, FileSerializer, PerformanceSerializer
from rest_framework import  permissions, renderers, viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User
from music.models import Concert, Song, Part, File, Performance

# from music.permissions import IsOwnerReadOnly 


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Concert 


class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concert.objects.all() 
    serializer_class = ConcertSerializer

# Song

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all() 
    serializer_class = SongSerializer
    
# Part

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all() 
    serializer_class = PartSerializer

# File

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all() 
    serializer_class = FileSerializer

# Performance

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all() 
    serializer_class = PerformanceSerializer


