from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Songs, Singer
from .serializers import SongSerializer, SingerSerializer
from .permissions import IsSingerOrReadOnly

class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    permission_classes = [IsSingerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['singer__name']
    search_fields = ['title']
    ordering_fields = ['title', 'duration_minutes', 'duration_seconds', 'singer__name']
    ordering = ['title']  # default ordering

    def get_queryset(self):
        # If user is authenticated, show only their songs
        if self.request.user.is_authenticated:
            return Songs.objects.filter(singer__user=self.request.user)
        # Otherwise show all songs
        return Songs.objects.all()

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
