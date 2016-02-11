from __future__ import unicode_literals
from django.db import models
from tiposalimento.models import TipoAlimento

class Alimento(models.Model):
	nombre = models.CharField(max_length=255)
	porcion = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)
	image = models.ImageField(blank=True)

	def __str__(self):
		return '%s %s %s %s' % (self.nombre, self.porcion, self.descripcion, self.image )

	class Meta:
		ordering = ('id',)	

class Alimento_Tipo(models.Model):
	alimento = models.ForeignKey(Alimento)
	tipo = models.ForeignKey(TipoAlimento)	

	class Meta:
		verbose_name = 'TiposAlimentos'
		verbose_name_plural = 'TiposAlimentos'

	def __str__(self):
		return '%s %s %s %s %s' % (self.alimento.nombre, self.porcion, self.descripcion, self.image, self.tipo.tipo )