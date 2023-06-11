from django.contrib import admin
from django.db.models import fields
from .models import Ciudad, Estado, Actividad, Sector, Ramo, Region, Zona, TipoCapital, Vendedor, Pais, TamanoEmpresa, TipoEmpresa


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre']


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'pais')


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'estado']
    list_display = ('nombre', 'estado', 'pais')
    fields = ('nombre', 'estado')
    # list_display_links = ['nombre']
    list_editable = ['estado']
    list_filter = ['estado']
    ordering = ['nombre', 'estado']
    save_on_top = True
    save_as = True
    list_per_page = 10



admin.site.register(Actividad)
admin.site.register(Ramo)
admin.site.register(Sector)
admin.site.register(Region)
admin.site.register(Zona)
admin.site.register(TamanoEmpresa)
admin.site.register(TipoEmpresa)
admin.site.register(TipoCapital)
admin.site.register(Vendedor)