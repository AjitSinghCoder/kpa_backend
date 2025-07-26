#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Run administrative tasks."""
    # Get environment from .env file
    django_env = os.getenv('DJANGO_ENV', 'dev')

    # Set settings module based on environment
    if django_env == 'prod':
        settings_module = 'kpa_backend.settings.prod'
    else:
        settings_module = 'kpa_backend.settings.dev'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
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
