#NAME: LEE KEI KAR
#STUDENT ID: 23100598


"""
WSGI config for DRIS_Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRIS_Project.settings')

application = get_wsgi_application()
