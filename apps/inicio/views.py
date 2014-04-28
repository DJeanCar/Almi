# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import ListView, TemplateView
from apps.lugares.models import Lugar
from apps.paquetes.models import Paquete
from django.template import RequestContext

#class index(ListView):
#	template_name = 'inicio/index.html'
#	model = Lugar
#	context_object_name = 'lugares'	

def inicio(request):
	lugares = Lugar.objects.all()[:3]
	paquetes = Paquete.objects.all()[:3]
	return render_to_response('inicio/index.html', {'paquetes':paquetes, 'lugares':lugares}, context_instance=RequestContext(request))

class contactanos(TemplateView):
	template_name = 'inicio/contactanos.html'

