from rest_framework import serializers
from .models import Songs, Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = '__all__'
