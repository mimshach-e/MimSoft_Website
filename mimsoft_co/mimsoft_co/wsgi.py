"""
WSGI config for mimsoft_co project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mimsoft_co.settings')

application = get_wsgi_application()

