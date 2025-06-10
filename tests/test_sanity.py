import os
import pytest


django = pytest.importorskip("django")


def test_django_setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tooncam.settings")
    django.setup()
