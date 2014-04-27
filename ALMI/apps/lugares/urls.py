from django.conf.urls import patterns, include, url
from .views import RegistrarLugar, ReportarLugar, BusquedaAjax

urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarLugar.as_view(), name='registrar_lugar'),
    url(r'^mostrar/$', ReportarLugar.as_view(), name='reportar_lugar'),
    url(r'^busqueda_ajax/$', BusquedaAjax.as_view()),
)