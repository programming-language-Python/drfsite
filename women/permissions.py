from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    # has_permission - позволяет достраивать права доступа на уровне всего запроса от клиента
    # has_object_permission - позволяет достраивать права доступа на уровне отдельного объекта (данных, записи БД)
    def has_permission(self, request, view):
        # проверка безопасности запроса
        if request.method in permissions.SAFE_METHODS:
            # предоставили всем права
            return True

        # доступ для админа
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
