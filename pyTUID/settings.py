from django.conf import settings

TUID_SERVER_URL     = getattr(settings, 'TUID_SERVER_URL', None)
TUID_CREATE_USER    = getattr(settings, 'TUID_CREATE_USER', True)
TUID_DEFAULT_NEXT   = getattr(settings, 'TUID_DEFAULT_NEXT', '/')

__tuid_mapping_default = {  'surname'       : 'surname',
                            'given_name'    : 'givenName',
                            'email'         : 'mail',
                            'groups'        : 'groupMembership'}

TUID_MAPPING        = getattr(settings, 'TUID_MAPPING', {})

for key in __tuid_mapping_default:
    if key not in TUID_MAPPING:
        TUID_MAPPING[key] =__tuid_mapping_default[key]
