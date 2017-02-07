from django.conf import settings

TUID_SERVER_URL     = getattr(settings, 'TUID_SERVER_URL', None)
TUID_CREATE_USER    = getattr(settings, 'TUID_CREATE_USER', True)
TUID_DEFAULT_NEXT   = getattr(settings, 'TUID_DEFAULT_NEXT', '/')
