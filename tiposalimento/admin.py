from django.contrib import admin
from .models import TipoAlimento


@admin.register(TipoAlimento)
class AdminTipoAlimento(admin.ModelAdmin):
    list_display = ('id', 'tipo',)
    list_filter = ('tipo',)
