# pyTUID
Allows authentication with TUID.

## Setup
* To set up install this python library (for example with pip).
* In your `settings.py`:
  * Add `pyTUID` to your `INSTALLED_APPS`.
  * Add `pyTUID.middleware.TUIDMiddleware` to your `MIDDLEWARE_CLASSES`.
  * Set at least `TUID_SERVER_URL` to your CAS server URL.
* Include `pyTUID.urls` in your `urls.py` at any path you like.
* Apply the migrations.
* That's it!

## Configuration
Currently the following settings are available:
* `TUID_SERVER_URL` the CAS server URL (default: `None`)
* `TUID_CREATE_USER` sets whether the logged in users should be saved to the database (default: `True`)
* `TUID_LOGIN_DEFAULT_NEXT` sets the default page after login when no `next` is present in `POST` or `GET` parameters (default: `"/"`)
* `TUID_LOGOUT_DEFAULT_NEXT` sets the default page after logout when no `next` is present in `POST` or `GET` parameters (default: `"/"`)
* `TUID_MAPPING` sets the mapping from SAML attributes to model fields (key is model field, value is SAML attribute) 
  The default is:
  ```python
  {'surname'    : 'surname',
   'given_name' : 'givenName',
   'email'      : 'mail',
   'groups'     : 'groupMembership'}
  ```
  Every key not provided in your config will be set to default.
  
## Usage
The easiest way to use this app is by using the [`@tuid_login_required`](https://github.com/d120/pyTUID/blob/3437bb3efefb9e9036f5400a298e21bc2051061c/pyTUID/decorators.py#L9) decorator on your view functions. This will check whether the user is logged in (via this app) or will otherwise redirect to the login page.
Currently the only other possibillity for interaction is using the [`TUIDUser`](https://github.com/d120/pyTUID/blob/3437bb3efefb9e9036f5400a298e21bc2051061c/pyTUID/models.py#L4) object, added to the request with the middleware.    
