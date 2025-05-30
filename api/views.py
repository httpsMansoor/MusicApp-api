from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Songs, Singer
from .serializers import SongSerializer, SingerSerializer
from .permissions import IsSingerOrReadOnly

class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsSingerOrReadOnly]

    def perform_create(self, serializer):
        # Get the singer associated with the current user
        singer = Singer.objects.get(user=self.request.user)
        serializer.save(singer=singer)

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            # Allow anyone to create a singer (register)
            return [AllowAny()]
        # Require authentication for other actions
        return [IsAuthenticated()]
