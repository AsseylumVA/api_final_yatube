from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверка разрешений на редактирование"""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class FollowPermissions(permissions.BasePermission):
    """Разрешения на доступ к Follows"""

    def has_permission(self, request, view):
        return request.method == 'GET' or request.method == 'POST'
