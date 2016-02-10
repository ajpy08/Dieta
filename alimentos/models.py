from __future__ import unicode_literals
from django.db import models
from tiposalimento.models import TipoAlimento

class Alimento(models.Model):
	nombre = models.CharField(max_length=255)
	porcion = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('id',)	

class Alimento_Tipo(models.Model):
	tipo = models.ForeignKey(TipoAlimento)
	alimento = models.ForeignKey(Alimento)

	class Meta:
		verbose_name = 'TiposAlimentos'
		verbose_name_plural = 'TiposAlimentos'

	def __str__(self):
		return '%s %s' % (self.tipo.tipo, self.alimento.nombre)