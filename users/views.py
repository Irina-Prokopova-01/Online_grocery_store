from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Контроллер создания, просмотра, удаления, изменения пользователя."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Меняю логику контроллера для его правильной регистрации пользователя."""

        # Сохраняю пользователя и сразу делаю его активным
        user = serializer.save(is_active=True)
        # Хэширую пароль пользователя и сохраняю пользователя
        user.set_password(user.password)
        user.save()
