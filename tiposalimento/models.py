from __future__ import unicode_literals

from django.db import models

class TipoAlimento(models.Model):
	tipo = models.CharField(max_length=255)

	def __str__(self):
		return self.tipo

	class Meta:
		ordering = ('tipo',)
