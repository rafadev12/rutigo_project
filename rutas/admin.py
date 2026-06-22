from django.contrib import admin
from .models import Unidad, Ruta

@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'chofer', 'capacidad', 'estado')
    list_filter = ('estado',)
    search_fields = ('codigo', 'chofer')

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'origen', 'destino', 'hora_salida', 'precio_pasaje', 'unidad_asignada')
    list_filter = ('origen', 'destino', 'hora_salida')
    search_fields = ('nombre', 'origen', 'destino')