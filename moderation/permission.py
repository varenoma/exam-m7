from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsModerPermission(permissions.BasePermission):
    message = "Siz moderator emassiz"

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.moder_verified:
                return True
            raise PermissionDenied(detail=self.message)
        return False
