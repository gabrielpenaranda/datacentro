from django.contrib import admin
from django.urls import path, include
from .views import (
    CiudadIndex, CiudadCreate, CiudadEdit, ciudad_delete,
    EstadoIndex, EstadoCreate, EstadoEdit, estado_delete,
    PaisIndex, PaisCreate, PaisEdit, pais_delete,
    SectorIndex, SectorCreate, SectorEdit, sector_delete,
    RamoIndex, RamoCreate, RamoEdit, ramo_delete,
    ActividadIndex, ActividadCreate, ActividadEdit, actividad_delete,
    TipoEmpresaIndex, TipoEmpresaCreate, TipoEmpresaEdit, tipoempresa_delete,
    TamanoEmpresaIndex, TamanoEmpresaCreate, TamanoEmpresaEdit, tamanoempresa_delete,
    TipoCapitalIndex, TipoCapitalCreate, TipoCapitalEdit, tipocapital_delete,VendedorIndex, VendedorCreate, VendedorEdit, vendedor_delete,
    RegionIndex, RegionCreate, RegionEdit, region_delete,
    ZonaIndex, ZonaCreate, ZonaEdit, zona_delete,
)


app_name = 'base'

urlpatterns = [
    path('ciudad', CiudadIndex.as_view(), name='ciudad-index'),
    path('ciudad/create', CiudadCreate.as_view(), name='ciudad-create'),
    path('ciudad/edit/<int:pk>', CiudadEdit.as_view(), name='ciudad-edit'),
    path('ciudad/delete/<int:id>', ciudad_delete, name='ciudad-delete'),
    #
    path('estado', EstadoIndex.as_view(), name='estado-index'),
    path('estado/create', EstadoCreate.as_view(), name='estado-create'),
    path('estado/edit/<int:pk>', EstadoEdit.as_view(), name='estado-edit'),
    path('estado/delete/<int:id>', estado_delete, name='estado-delete'),
    #
    path('pais', PaisIndex.as_view(), name='pais-index'),
    path('pais/create', PaisCreate.as_view(), name='pais-create'),
    path('pais/edit/<int:pk>', PaisEdit.as_view(), name='pais-edit'),
    path('pais/delete/<int:id>', pais_delete, name='pais-delete'),
    #
    path('sector', SectorIndex.as_view(), name='sector-index'),
    path('sector/create', SectorCreate.as_view(), name='sector-create'),
    path('sector/edit/<int:pk>', SectorEdit.as_view(), name='sector-edit'),
    path('sector/delete/<int:id>', sector_delete, name='sector-delete'),
    #
    path('ramo', RamoIndex.as_view(), name='ramo-index'),
    path('ramo/create', RamoCreate.as_view(), name='ramo-create'),
    path('ramo/edit/<int:pk>', RamoEdit.as_view(), name='ramo-edit'),
    path('ramo/delete/<int:id>', ramo_delete, name='ramo-delete'),
    #
    path('actividad', ActividadIndex.as_view(), name='actividad-index'),
    path('actividad/create', ActividadCreate.as_view(), name='actividad-create'),
    path('actividad/edit/<int:pk>', ActividadEdit.as_view(), name='actividad-edit'),
    path('actividad/delete/<int:id>', actividad_delete, name='actividad-delete'),
    #
    path('tipo_empresa', TipoEmpresaIndex.as_view(), name='tipoempresa-index'),
    path('tipo_empresa/create', TipoEmpresaCreate.as_view(), name='tipoempresa-create'),
    path('tipo_empresa/edit/<int:pk>', TipoEmpresaEdit.as_view(), name='tipoempresa-edit'),
    path('tipo_empresa/delete/<int:id>', tipoempresa_delete, name='tipoempresa-delete'),
    #
    path('tamano_empresa', TamanoEmpresaIndex.as_view(), name='tamanoempresa-index'),
    path('tamano_empresa/create', TamanoEmpresaCreate.as_view(), name='tamanoempresa-create'),
    path('tamano_empresa/edit/<int:pk>', TamanoEmpresaEdit.as_view(), name='tamanoempresa-edit'),
    path('tamano_empresa/delete/<int:id>', tamanoempresa_delete, name='tamanoempresa-delete'),
    #
    path('tipo_capital', TipoCapitalIndex.as_view(), name='tipocapital-index'),
    path('tipo_capital/create', TipoCapitalCreate.as_view(), name='tipocapital-create'),
    path('tipo_capital/edit/<int:pk>', TipoCapitalEdit.as_view(), name='tipocapital-edit'),
    path('tipo_capital/delete/<int:id>', tipocapital_delete, name='tipocapital-delete'),
    #
    path('vendedor', VendedorIndex.as_view(), name='vendedor-index'),
    path('vendedor/create', VendedorCreate.as_view(), name='vendedor-create'),
    path('vendedor/edit/<int:pk>', VendedorEdit.as_view(), name='vendedor-edit'),
    path('vendedor/delete/<int:id>', vendedor_delete, name='vendedor-delete'),
    #
    path('region', RegionIndex.as_view(), name='region-index'),
    path('region/create', RegionCreate.as_view(), name='region-create'),
    path('region/edit/<int:pk>', RegionEdit.as_view(), name='region-edit'),
    path('region/delete/<int:id>', region_delete, name='region-delete'),
    #
    path('zona', ZonaIndex.as_view(), name='zona-index'),
    path('zona/create', ZonaCreate.as_view(), name='zona-create'),
    path('zona/edit/<int:pk>', ZonaEdit.as_view(), name='zona-edit'),
    path('zona/delete/<int:id>', zona_delete, name='zona-delete'),
]
