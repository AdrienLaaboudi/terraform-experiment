from rest_framework.permissions import BasePermission


class IsBuyer(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.buyer == request.user)


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.email.endswith('@mycompany.com'))
