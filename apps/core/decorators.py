from functools import wraps
from django.http import HttpResponseForbidden
from apps.core.mode import current_mode


def mode_required(*allowed_modes: str):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if current_mode() not in allowed_modes:
                return HttpResponseForbidden("Mode not allowed")
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator
