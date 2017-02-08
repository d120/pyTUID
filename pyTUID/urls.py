from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='tuid-login'),
    url(r'^logout/$', views.logout, name='tuid-logout'),
]

