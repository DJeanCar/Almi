from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'turefull.views.home', name='home'),
    # url(r'^turefull/', include('turefull.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('apps.inicio.urls')),
    url(r'^paquete/', include('apps.paquetes.urls')),
    url(r'^lugar/', include('apps.lugares.urls')),
)
