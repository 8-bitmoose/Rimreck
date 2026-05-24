import os


def test_mode_env_defaults():
    assert os.getenv("RIMRECK_MODE", "personal") in {"personal", "hosted"}
