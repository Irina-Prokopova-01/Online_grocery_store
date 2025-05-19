from rest_framework.permissions import BasePermission, AllowAny


class IsActiveUser(BasePermission):
    """
    Разрешает доступ только активным пользователям для всех методов,
    кроме просмотра, который доступен любому пользователю.
    """

    def has_permission(self, request, view):
        """Разрешаем доступ всем пользователям для GET запросов"""
        if request.method == "GET":
            return True
        return request.user and request.user.is_active


class IsAdmin(BasePermission):
    """
    Разрешаем доступ к 'POST', 'PUT', 'PATCH', 'DELETE' только администратору,
    просмотр доступен любому пользователю.
    """

    def has_permission(self, request, view):
        """Разрешаем доступ к 'POST', 'PUT', 'PATCH', 'DELETE' только администратору"""

        # Проверяем метод запроса
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            # Только администраторы могут изменять/удалять
            return request.user and request.user.is_staff

        # Все могут просматривать
        return True  # Для методов GET и других разрешаем доступ всем
