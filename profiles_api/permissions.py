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


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id # check if the object user id is similar to the current user's id

class CheckUpdateOwnStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id 
