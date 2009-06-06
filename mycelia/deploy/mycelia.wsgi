# myproject.wsgi is configured to live in projects/myproject/deploy.

import os
import sys

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr

from os.path import abspath, dirname, join
from site import addsitedir

sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from django.conf import settings
os.environ["DJANGO_SETTINGS_MODULE"] = "mycelia.settings"

sys.path.insert(0, join(settings.PINAX_ROOT, "apps"))
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))
print sys.path
#from django.core.handlers.wsgi import WSGIHandler
#application = WSGIHandler()

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    if environ.get("HTTP_X_FORWARDED_PROTOCOL") == "https" or environ.get("HTTP_X_FORWARDED_SSL") == "on":
        environ["wsgi.url_scheme"] = "https"
#       environ['wsgi.url_scheme'] = environ.get('HTTP_X_URL_SCHEME', 'http')
    return _application(environ, start_response)
                                                  
