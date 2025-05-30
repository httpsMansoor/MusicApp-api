from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Songs, Singer

class SingerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'username', 'password']

    def create(self, validated_data):
        # Extract user data
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        # Create singer with user
        singer = Singer.objects.create(
            user=user,
            **validated_data
        )
        
        return singer

class SongSerializer(serializers.ModelSerializer):
    singer_name = serializers.CharField(source='singer.name', read_only=True)
    
    class Meta:
        model = Songs
        fields = ['id', 'title', 'duration_minutes', 'duration_seconds', 'singer_name']
