"""
ASGI config for mimsoft_co project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mimsoft_co.settings')

application = get_asgi_application()

