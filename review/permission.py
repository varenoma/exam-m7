from rest_framework import permissions


class IsVerifiedReviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.reviewer_verified
