from django.conf.urls import patterns, include, url
from .views import contactanos, inicio


urlpatterns = patterns('',
    url(r'^$', 'apps.inicio.views.inicio', name="index"),
    url(r'^contactanos/$', contactanos.as_view()),
    #url(r'^$', 'django.contrib.auth.views.login', {'template_name':'inicio/index.html'}, name='login'),
    #url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
