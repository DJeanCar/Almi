from django.db import models

# Create your models here.

class Lugar(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	imagen = models.ImageField(upload_to = 'foto')

	def __unicode__(self):
		return self.nombre