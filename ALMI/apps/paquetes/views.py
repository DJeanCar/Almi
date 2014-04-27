# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import CreateView, ListView
from .models import Paquete, Lugar
from django.core.urlresolvers import reverse_lazy 
from django.template import RequestContext

class RegistrarPaquete(CreateView):
	template_name = 'paquetes/paquete.html'
	model = Paquete
	success_url = reverse_lazy('reportar_paquete')

#class ReportarPaquete(ListView):
#	template_name = 'paquetes/reportar_paquetes.html'
#	model = Paquete
#	context_object_name = 'paquetes'

def ReportarPaquete(request):
	lugares = Lugar.objects.all()
	paquetes = Paquete.objects.all()
	return render_to_response('paquetes/reportar_paquetes.html', {'paquetes':paquetes, 'lugares':lugares}, context_instance=RequestContext(request))
