from django.conf.urls import patterns, include, url
from .views import RegistrarPaquete, ReportarPaquete

urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarPaquete.as_view(), name='registrar_paquete'),
    url(r'^mostrar/$', 'apps.paquetes.views.ReportarPaquete', name='reportar_paquete'),
)