from django.contrib import admin
from .models import Emisora


@admin.register(Emisora)
class EmisoraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cadena', 'ciudad', 'via', 'orden')
    list_filter = ('cadena', 'ciudad', 'via')
    search_fields = ('titulo', 'cadena', 'ciudad')
    ordering = ('orden', 'id')
