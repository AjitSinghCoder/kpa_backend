"""
WSGI config for kpa_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

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

application = get_wsgi_application()
