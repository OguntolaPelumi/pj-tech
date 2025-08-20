# """
# WSGI config for myweb project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application
# from whitenoise import WhiteNoise


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myweb.settings")

# application = get_wsgi_application()
# application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'), prefix='static/')


# application = get_wsgi_application()



import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Define BASE_DIR (same as in settings.py)
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')

application = get_wsgi_application()

# Point WhiteNoise to the same STATIC_ROOT directory
application = WhiteNoise(
    application,
    root=os.path.join(BASE_DIR, 'staticfiles'),
    prefix='static/'
)
