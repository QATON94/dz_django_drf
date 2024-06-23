from django.utils.deprecation import MiddlewareMixin

from users.models import User


class OnlineNowMiddleware(MiddlewareMixin):
    """Обновляет базу данных пользователей всякий раз,
    когда прошедший проверку подлинности пользователь отправляет HTTP-запрос."""

    @staticmethod
    def process_request(request):
        user = request.user
        if not user.is_authenticated:
            return

        User.update_user_activity(user)
