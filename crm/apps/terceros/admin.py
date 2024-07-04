from django.contrib import admin
from .models import TipoPersona, TipoTercero, Tercero, Persona, Sucursal


@admin.register(Tercero)
class TerceroAdmin(admin.ModelAdmin):
    fields = ('nombre', 'nombre_juridico',
        ('rif', 'nit', 'tipocapital'),
        ('telefono', 'email', 'web'),
        ('ciudad', 'zona'),
        'descripcion_actividad',
        ('tamano_empresa', 'tipo_empresa'),
        ('tipo_tercero', 'vendedor')
    )
    ordering = ['nombre', 'nombre_juridico']
    list_display = ['nombre', 'nombre_juridico', 'rif', 'tipo_tercero', 'ciudad']
    list_filter = ['tipo_tercero', 'ciudad', 'zona']
    search_fields = ['nombre', 'rif']
    list_per_page = 10




admin.site.register(TipoPersona)
admin.site.register(TipoTercero)
admin.site.register(Persona)
admin.site.register(Sucursal)
