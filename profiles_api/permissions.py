from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to change their own profiles"""
    
    def has_object_permission(self,request,view,obj):
        """Check if users trying to change their own profiles"""
        if request.method in permissions.SAFE_METHODS: # If the request method is PUT then return True
            return True
        
        return obj.id == request.user.id # If request is PUT/PATCH etc then check if the obj.id is similar to the user.id


class CheckUpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.id
    