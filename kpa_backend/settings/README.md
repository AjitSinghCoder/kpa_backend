# Django Settings Configuration

This directory contains the Django settings files split into different environments.

## Files Structure

- `base.py` - Common settings shared across all environments
- `dev.py` - Development-specific settings
- `prod.py` - Production-specific settings

## Usage

### Development
The project is configured to use development settings by default:
```bash
python manage.py runserver
```

### Production
For production deployment, set the environment variable:
```bash
export DJANGO_SETTINGS_MODULE=kpa_backend.settings.prod
```

Or use it directly with commands:
```bash
python manage.py migrate --settings=kpa_backend.settings.prod
python manage.py collectstatic --settings=kpa_backend.settings.prod
```

### Custom Environment
You can create additional settings files (e.g., `staging.py`) that inherit from base:
```python
from .base import *

# Staging-specific settings here
DEBUG = False
ALLOWED_HOSTS = ['staging.kpa.suvidhaen.com']
```

## Environment Variables

Make sure to set the following environment variables in your `.env` file:

### Required for all environments:
- `SECRET_KEY`
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`

## Security Notes

- Never commit `.env` files to version control
- Use strong, unique secret keys for each environment
- Enable SSL/HTTPS in production
- Configure proper firewall rules for production databases
