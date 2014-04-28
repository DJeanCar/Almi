from django.db import models
from apps.lugares.models import Lugar

# Create your models here.

class Paquete(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	imagen = models.ImageField(upload_to='foto')
	precio = models.FloatField()
	lugar = models.ManyToManyField(Lugar)

	def __unicode__(self):
		return self.nombre
