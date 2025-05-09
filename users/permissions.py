from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    """
    Разрешает доступ только активным пользователям для всех методов,
    кроме просмотра, который доступен любому пользователю.
    """
    def has_permission(self, request, view):
        """Разрешаем доступ всем пользователям для GET запросов"""
        if request.method == 'GET':
            return True
        return request.user and request.user.is_active

