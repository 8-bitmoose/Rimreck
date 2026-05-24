from django.contrib.auth import login
from django.contrib.auth import get_user_model
from apps.core.mode import is_personal


class PersonalModeAutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if is_personal() and not request.user.is_authenticated:
            user_model = get_user_model()
            user, _ = user_model.objects.get_or_create(
                username="local",
                defaults={"is_staff": True, "is_superuser": True, "email": "local@rimreck.local"},
            )
            login(request, user)
        return self.get_response(request)
