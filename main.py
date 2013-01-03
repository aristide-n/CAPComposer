import logging, os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch

# Force Django to reload its settings.
from django.conf import settings

settings._target = None

# Log errors
def log_exception(*args, **kwds):
    logging.exception('Exception in request:')

signal = django.dispatch.Signal()

# Log errors.
signal.connect(log_exception, django.core.signals.got_request_exception)


# Unregister the rollback event handler.
django.dispatch.Signal.disconnect(django.core.signals.got_request_exception,
                                  django.db._rollback_on_exception)

application = django.core.handlers.wsgi.WSGIHandler()