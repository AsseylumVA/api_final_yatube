from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверка разрешений на редактирование"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class FollowPermissions(permissions.BasePermission):
    """Разрешения на доступ к Follows"""

    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        return False
