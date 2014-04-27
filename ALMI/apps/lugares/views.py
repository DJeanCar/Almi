# Create your views here.
from django.views.generic import CreateView, ListView, TemplateView
from .models import Lugar
from django.core.urlresolvers import reverse_lazy 

class RegistrarLugar(CreateView):
	template_name = 'lugares/lugar.html'
	model = Lugar
	success_url = reverse_lazy('reportar_lugar')

class ReportarLugar(ListView):
	template_name = 'lugares/reportar_lugares.html'
	model = Lugar
	context_object_name = 'lugares'

from django.core import serializers
from django.http import HttpResponse

class BusquedaAjax(TemplateView):

	def get(self, request, *args, **kwargs):
		nombre_lugar = request.GET['valor']
		lugares = Lugar.objects.filter(nombre = nombre_lugar)
		data = serializers.serialize('json', lugares, fields={'nombre','descripcion','imagen'})
		return HttpResponse(data, mimetype='application/json')