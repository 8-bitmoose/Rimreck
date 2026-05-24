from pathlib import Path
from config.settings.base import *  # noqa: F403,F401


def _ensure_writable_dir(path: Path) -> Path:
    try:
        path.mkdir(parents=True, exist_ok=True)
        return path
    except OSError:
        fallback = BASE_DIR / ".rimreck"  # noqa: F405
        fallback.mkdir(parents=True, exist_ok=True)
        return fallback


personal_home = _ensure_writable_dir(
    Path(env("RIMRECK_PERSONAL_HOME", default="~/.rimreck")).expanduser()  # noqa: F405
)

personal_db = Path(
    env("RIMRECK_PERSONAL_DB", default=str(personal_home / "db.sqlite3"))  # noqa: F405
).expanduser()
personal_db.parent.mkdir(parents=True, exist_ok=True)

media_dir = Path(
    env("RIMRECK_PERSONAL_MEDIA", default=str(personal_home / "media"))  # noqa: F405
).expanduser()
media_dir.mkdir(parents=True, exist_ok=True)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": personal_db,
    }
}

MEDIA_ROOT = media_dir
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
