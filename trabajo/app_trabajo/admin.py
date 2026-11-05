from django.contrib import admin
from .models import Reclamo


@admin.register(Reclamo)
class ReclamoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "tipo", "estacion", "fecha", "creado")
    list_filter = ("tipo", "estacion")
    search_fields = ("nombre", "email", "descripcion")