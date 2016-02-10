from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.shortcuts import (
	render,
	get_object_or_404,
	redirect)
from .forms import AlimentoForm
from .models import Alimento

from django.views.generic import ListView
from django.views.generic.detail import DetailView

class ListaAlimentos(ListView):
	model = Alimento

class DetalleAlimento(DetailView):
	model = Alimento

def nuevo_alimento(request):
	if request.method == 'POST':
		form = AlimentoForm(request.POST, request.FILES)
		if form.is_valid():
			alimento = form.save()
			alimento.save()
			return HttpResponseRedirect('/')
	else:
		form = AlimentoForm()

	template = loader.get_template('nuevo_alimento.html')
	context = {
		'form': form
	}
	return HttpResponse(template.render(context, request))