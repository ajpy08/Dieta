from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .forms import AlimentoForm
from .models import Alimento


class ListaAlimentos(ListView):
    model = Alimento


class DetalleAlimento(DetailView):
    model = Alimento


@login_required()
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


def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(first_name=first_name,
                                            last_name=last_name,
                                            username=username,
                                            password=password,
                                            email=email)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    context = {}
    return render(request, 'login/login.html', context)
