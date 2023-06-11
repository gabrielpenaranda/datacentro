from django.contrib import admin
from django.urls import path, include
from .views import (
    TipoTerceroIndex, TipoTerceroCreate, TipoTerceroEdit, tipotercero_delete,
    TipoPersonaIndex, TipoPersonaCreate, TipoPersonaEdit, tipopersona_delete,
    TerceroIndex, TerceroCreate, TerceroEdit, tercero_delete,
    PersonaIndex, PersonaCreate, PersonaEdit, persona_delete,
    SucursalIndex, SucursalCreate, SucursalEdit, sucursal_delete,
)

app_name = "terceros"

urlpatterns = [
    path('tipotercero', TipoTerceroIndex.as_view(), name='tipotercero-index'),
    path('tipotercero/create', TipoTerceroCreate.as_view(),
         name='tipotercero-create'),
    path('tipotercero/edit/<int:pk>',
         TipoTerceroEdit.as_view(), name='tipotercero-edit'),
    path('tipotercero/delete/<int:id>',
         tipotercero_delete, name='tipotercero-delete'),
    #
    path('tipopersona', TipoPersonaIndex.as_view(), name='tipopersona-index'),
    path('tipopersona/create', TipoPersonaCreate.as_view(),
         name='tipopersona-create'),
    path('tipopersona/edit/<int:pk>',
         TipoPersonaEdit.as_view(), name='tipopersona-edit'),
    path('tipopersona/delete/<int:id>',
         tipopersona_delete, name='tipopersona-delete'),
    #
    path('tercero', TerceroIndex.as_view(), name='tercero-index'),
    path('tercero/create', TerceroCreate.as_view(),
         name='tercero-create'),
    path('tercero/edit/<int:pk>',
         TerceroEdit.as_view(), name='tercero-edit'),
    path('tercero/delete/<int:id>',
         tercero_delete, name='tercero-delete'),
    #
    path('persona', PersonaIndex.as_view(), name='persona-index'),
    path('persona/create', PersonaCreate.as_view(),
         name='persona-create'),
    path('persona/edit/<int:pk>',
         PersonaEdit.as_view(), name='persona-edit'),
    path('persona/delete/<int:id>',
         persona_delete, name='persona-delete'),
        #
    path('sucursal', SucursalIndex.as_view(), name='sucursal-index'),
    path('sucursal/create', SucursalCreate.as_view(),
         name='sucursal-create'),
    path('sucursal/edit/<int:pk>',
         SucursalEdit.as_view(), name='sucursal-edit'),
    path('sucursal/delete/<int:id>',
         sucursal_delete, name='sucursal-delete'),
]
