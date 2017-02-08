from functools import wraps

from django.utils.decorators import available_attrs
from django.core.urlresolvers import reverse
from django.utils.http import urlquote_plus
from django.http import HttpResponseRedirect


def tuid_login_required():
    """
    Decorator for views tht checks that the user has logged in with TUID,
    redirects to the log-in page otherwise
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if request.TUIDUser:
                return view_func(request, *args, **kwargs)
            login_url = reverse('tuid-login')
            current_url = request.get_full_path()
            return HttpResponseRedirect(login_url + '?next=' +
                    urlquote_plus(current_url))
        return _wrapped_view
    return decorator
