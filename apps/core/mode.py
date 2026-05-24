from django.conf import settings


def current_mode() -> str:
    return getattr(settings, "RIMRECK_MODE", "personal").lower()


def is_personal() -> bool:
    return current_mode() == "personal"


def is_hosted() -> bool:
    return current_mode() == "hosted"
