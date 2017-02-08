from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

import cas

from . import settings
from .models import TUIDUser
from .util import update_user


def _get_service_url(request):
    return 'https://' + request.get_host() + request.get_full_path()


def login(request):
    """
    Either logs a user in by verifying it's ticket, if no ticket is present the
    user is redirected to the CAS login.
    """

    casClient = cas.CASClient(
            version = 'CAS_2_SAML_1_0',

            service_url = _get_service_url(request),
            server_url  = settings.TUID_SERVER_URL,
    )

    ticket = request.GET.get('ticket')

    if not ticket:  #No ticket present redirect to CAS login
        return HttpResponseRedirect(casClient.get_login_url())
    
    #Ticket is present verify it.
    user, attr, _ = casClient.verify_ticket(ticket)

    #Ticket seems to be valid save user and attributes in session
    if user:
        request.session['TUID_uid'] = user
        request.session['TUID_attrs'] = attr

        if settings.TUID_CREATE_USER:
            tuid_user , created = TUIDUser.objects.get_or_create(uid = user)
            update_user(tuid_user, user, attr)
            tuid_user.save()

        next_page = request.POST.get('next', request.GET.get('next',
            settings.TUID_LOGIN_DEFAULT_NEXT))
        return HttpResponseRedirect(next_page)

    else:
        raise PermissionDenied('Login failed.')


def logout(request, next_page=None):
    request.session['TUID_uid'] = None
    request.session['TUID_attrs'] = None

    next_page = request.POST.get('next', request.GET.get('next',
        settings.TUID_LOGOUT_DEFAULT_NEXT))
    return HttpResponseRedirect(next_page)
