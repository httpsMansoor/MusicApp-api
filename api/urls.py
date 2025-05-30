from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import SongViewSet, SingerViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'singers', SingerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] 