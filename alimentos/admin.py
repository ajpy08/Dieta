from django.contrib import admin
from .models import Alimento, Alimento_Tipo

@admin.register(Alimento)
class AdminAlimento(admin.ModelAdmin):
    list_display = ('nombre', 'porcion',)
    list_filter = ('nombre',)

@admin.register(Alimento_Tipo)
class AdminAlimento_Tipo(admin.ModelAdmin):
	list_display = ('alimento', 'tipo',)
	list_filter = ('tipo',)
