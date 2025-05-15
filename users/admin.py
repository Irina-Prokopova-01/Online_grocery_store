from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админ. интерфейс для модели User.
    Этот класс определяет, какие поля будут отображаться в списке пользователей
    в административной панели Django.
    """

    list_display = ("id", "first_name", "last_name", "email")
