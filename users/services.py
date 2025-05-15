from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
       Менеджер для пользователей, который управляет созданием и сохранением
       экземпляров пользовательской модели.Предоставляет методы для
    создания обычных пользователей и суперпользователей."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Поле Email должно быть заполнено")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
