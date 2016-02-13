from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.auth_login, name='authentication'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.ListaAlimentos.as_view(), name='home'),
    url(r'^alimento/(?P<pk>[0-9]+)/$',
        views.DetalleAlimento.as_view(), name='detalle'),
    url(r'^alimento/nuevo', views.nuevo_alimento, name='nuevo')
]
