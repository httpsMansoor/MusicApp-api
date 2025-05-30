from rest_framework import permissions

class IsSingerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow singers to edit their own songs.
    """
    def has_permission(self, request, view):
        # Allow read permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the singer of the song
        return obj.singer and obj.singer.user == request.user 