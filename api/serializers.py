from rest_framework import serializers
from .models import Songs, Singer

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender']

class SongSerializer(serializers.ModelSerializer):
    singer_name = serializers.CharField(source='singer.name', read_only=True)
    singer = serializers.PrimaryKeyRelatedField(queryset=Singer.objects.all(), write_only=True)
    
    class Meta:
        model = Songs
        fields = ['id', 'title', 'duration_minutes', 'duration_seconds', 'singer', 'singer_name']
