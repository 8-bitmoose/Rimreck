# Rimreck

Free, self-hostable reptile inventory and record-keeping app.

## Quickstart

Rimreck supports two local setup paths:

### Path A: `uv` (recommended)

Install `uv` on Ubuntu:

```bash
sudo snap install astral-uv --classic
```

If Snap warns about classic confinement, that is expected for this package.

Project setup:

```bash
cp .env.example .env
uv sync --all-extras
uv run rimreck
```

### Path B: plain `pip`

If you do not want to install `uv`, use:

```bash
python3 -m venv .venv
source .venv/bin/activate
cp .env.example .env
pip install --upgrade pip
pip install -e ".[dev]"
python manage.py migrate
python manage.py runserver
```

## Dependencies and `requirements.txt`

This project uses `pyproject.toml` as the dependency source of truth:

- `[project.dependencies]` for runtime packages
- `[project.optional-dependencies].dev` for lint/test/dev tools

A `requirements.txt` file is not required for this workflow.
If needed later, we can add exported lock files for deployment environments.

## Architecture

Single Django codebase with mode switching via `RIMRECK_MODE=personal|hosted`.

