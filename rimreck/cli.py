import os
import subprocess
from pathlib import Path


def _ensure_writable_dir(path: Path) -> Path:
    try:
        path.mkdir(parents=True, exist_ok=True)
        return path
    except OSError:
        fallback = Path.cwd() / ".rimreck"
        fallback.mkdir(parents=True, exist_ok=True)
        return fallback


def main() -> None:
    home = _ensure_writable_dir(Path(os.getenv("RIMRECK_PERSONAL_HOME", "~/.rimreck")).expanduser())
    (home / "media").mkdir(parents=True, exist_ok=True)

    os.environ.setdefault("RIMRECK_MODE", "personal")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.personal")

    subprocess.run(["python", "manage.py", "migrate"], check=True)
    subprocess.run(["python", "manage.py", "runserver", "127.0.0.1:8000"], check=True)
