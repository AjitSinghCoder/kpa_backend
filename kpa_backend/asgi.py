"""
ASGI config for kpa_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from dotenv import load_dotenv
from django.core.asgi import get_asgi_application

# Load environment variables
load_dotenv()

# Get environment from .env file
django_env = os.getenv('DJANGO_ENV', 'prod')

# Set settings module based on environment
if django_env == 'prod':
    settings_module = 'kpa_backend.settings.prod'
else:
    settings_module = 'kpa_backend.settings.dev'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
