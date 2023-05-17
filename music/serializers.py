from django.contrib.auth.models import User  
from rest_framework import serializers 
from music.models import Concert, Song, Part, File, Performance 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id', 'username']


class PartSerializer(serializers.ModelSerializer): 
    # songs = serializers.StringRelatedField(many=True) 

    class Meta: 
        ordering = ['name']
        model = Part 
        fields = ['id', 'name', 'songs']
        extra_kwargs = {'songs': {'required': False}}


class SongSerializer(serializers.ModelSerializer):
    # Causes 
    # concerts = serializers.StringRelatedField(many=True)
    # parts = serializers.StringRelatedField(many=True)
    parts = PartSerializer(many=True, read_only=True)

    class Meta: 
        ordering = ['title']
        model = Song 
        fields = ['id', 'title', 'concerts', 'parts']
        extra_kwargs = {'concerts': {'required': False},
                        'parts': {'required': False}}


class ConcertSerializer(serializers.ModelSerializer): 
    songs = SongSerializer(many=True, read_only=True)

    class Meta: 
        model = Concert 
        fields = ['id', 'title', 'season', 'songs']
        extra_kwargs = {'songs': {'required': False}}


class FileSerializer(serializers.ModelSerializer): 
    # song_name = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all())
    # part = serializers.StringRelatedField()

    class Meta: 
        ordering = ['song', 'part']
        model = File 
        fields = ['id', 'song', 'part', 'file_name', 'pdf', 'created_dt', 'modified_dt']

class PerformanceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Performance 
        fields = ['id', 'concert', 'performance_date']

