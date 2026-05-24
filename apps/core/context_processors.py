from apps.core.mode import current_mode


def rimreck_mode(_request):
    return {"rimreck_mode": current_mode()}
