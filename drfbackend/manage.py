#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from drfbackend.settings.common import set_django_settings
from pathlib import Path
from os.path import join
from dotenv import load_dotenv
dotenv_path = join(Path(__file__).parent.parent, '.env')
load_dotenv(dotenv_path)

def main():
    """Run administrative tasks."""
    set_django_settings()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
