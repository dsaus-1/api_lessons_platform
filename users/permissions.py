from rest_framework.permissions import BasePermission


class OwnerProfile(BasePermission):
    def has_permission(self, request, view):

        if view.action in ['update', 'destroy']:
            return request.user == view.get_object()
        return request.user.is_authenticated