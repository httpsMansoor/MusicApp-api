from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Songs, Singer
from .serializers import SongSerializer, SingerSerializer
from .permissions import IsSingerOrReadOnly
from .throttles import SongCreateRateThrottle, SongListRateThrottle, SingerCreateRateThrottle

class SongViewSet(viewsets.ModelViewSet):
    serializer_class = SongSerializer
    permission_classes = [IsSingerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'singer__name']
    throttle_classes = [SongCreateRateThrottle, SongListRateThrottle]

    def get_queryset(self):
        queryset = Songs.objects.all()
        search_query = self.request.query_params.get('search', None)
        
        if search_query:
            # Case-insensitive partial matching for both title and singer name
            queryset = queryset.filter(
                title__icontains=search_query
            ) | queryset.filter(
                singer__name__icontains=search_query
            )
        
        # If user is authenticated, show only their songs
        if self.request.user.is_authenticated:
            queryset = queryset.filter(singer__user=self.request.user)
            
        return queryset.distinct()  # Use distinct to avoid duplicates

    def perform_create(self, serializer):
        # Get the singer associated with the current user
        singer = Singer.objects.get(user=self.request.user)
        serializer.save(singer=singer)

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    throttle_classes = [SingerCreateRateThrottle]
    
    def get_permissions(self):
        if self.action == 'create':
            # Allow anyone to create a singer (register)
            return [AllowAny()]
        # Require authentication for other actions
        return [IsAuthenticated()]
