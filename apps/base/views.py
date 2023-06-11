from django.shortcuts import render, redirect
from .models import (
    Pais, Estado, Ciudad, Sector, Ramo, Actividad,
    TipoEmpresa, TamanoEmpresa, TipoCapital,
    Vendedor, Region, Zona
)
from .forms import (
    CiudadForm, EstadoForm, PaisForm,
    SectorForm, RamoForm, ActividadForm,
    TipoEmpresaForm, TamanoEmpresaForm, TipoCapitalForm,
    VendedorForm, RegionForm, ZonaForm
)
from django.views.generic import (
    View, TemplateView, ListView,
    UpdateView, CreateView, DeleteView
)
from django.urls import reverse_lazy


# CIUDAD
class CiudadIndex(ListView):
    template_name = 'base/ciudad/ciudad_index.html'
    model = Ciudad
    paginate_by = 7
    context_object_name = 'ciudades'


class CiudadCreate(CreateView):
    model = Ciudad
    template_name = 'base/ciudad/ciudad_create.html'
    form_class = CiudadForm
    success_url = reverse_lazy('base:ciudad-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ciudad|Agregar'
        context['titulo_pagina'] = 'Agregar Ciudad'
        return context


class CiudadEdit(UpdateView):
    model = Ciudad
    template_name = 'base/ciudad/ciudad_create.html'
    form_class = CiudadForm
    success_url = reverse_lazy('base:ciudad-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ciudad|Editar'
        context['titulo_pagina'] = 'Editar Ciudad'
        return context


def ciudad_delete(request, id):
    ciudad = Ciudad.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Ciudad',
            'titulo': 'Ciudad|Eliminar',
            'ruta': 'base:ciudad-index',
            'objeto': ciudad,
        }
        return render(request, 'base/ciudad/ciudad_delete.html', contexto)
    else:
        try:
            ciudad.delete()
        except:
            mensaje = 'No puede eliminar Ciudad, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Ciudad eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Ciudad',
            'mensaje': mensaje,
            'titulo': 'Ciudad|Eliminar',
            'ruta': 'base:ciudad-index',
            'objeto': ciudad.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# ESTADO
class EstadoIndex(ListView):
    template_name = 'base/estado/estado_index.html'
    model = Estado
    paginate_by = 7
    context_object_name = 'estados'


class EstadoCreate(CreateView):
    model = Estado
    template_name = 'base/estado/estado_create.html'
    form_class = EstadoForm
    success_url = reverse_lazy('base:estado-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Estado|Agregar'
        context['titulo_pagina'] = 'Agregar Estado'
        return context


class EstadoEdit(UpdateView):
    model = Estado
    template_name = 'base/estado/estado_create.html'
    form_class = EstadoForm
    success_url = reverse_lazy('base:estado-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Estado|Editar'
        context['titulo_pagina'] = 'Editar Estado'
        return context


def estado_delete(request, id):
    estado = Estado.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Estado',
            'titulo': 'Estado|Eliminar',
            'ruta': 'base:estado-index',
            'objeto': estado,
        }
        return render(request, 'base/estado/estado_delete.html', contexto)
    else:
        try:
            estado.delete()
        except:
            mensaje = 'No puede eliminar Estado, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Estado eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Estado',
            'mensaje': mensaje,
            'titulo': 'Estado|Eliminar',
            'ruta': 'base:estado-index',
            'objeto': estado.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# PAIS
class PaisIndex(ListView):
    template_name = 'base/pais/pais_index.html'
    model = Pais
    paginate_by = 7
    context_object_name = 'paises'


class PaisCreate(CreateView):
    model = Pais
    template_name = 'base/pais/pais_create.html'
    form_class = PaisForm
    success_url = reverse_lazy('base:pais-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'País|Agregar'
        context['titulo_pagina'] = 'Agregar País'
        return context


class PaisEdit(UpdateView):
    model = Pais
    template_name = 'base/pais/pais_create.html'
    form_class = PaisForm
    success_url = reverse_lazy('base:pais-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'País|Editar'
        context['titulo_pagina'] = 'Editar País'
        return context


def pais_delete(request, id):
    pais = Pais.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar País',
            'titulo': 'País|Eliminar',
            'ruta': 'base:pais-index',
            'objeto': pais,
        }
        return render(request, 'base/pais/pais_delete.html', contexto)
    else:
        try:
            pais.delete()
        except:
            mensaje = 'No puede eliminar País, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'País eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar País',
            'mensaje': mensaje,
            'titulo': 'País|Eliminar',
            'ruta': 'base:pais-index',
            'objeto': pais.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# SECTOR
class SectorIndex(ListView):
    template_name = 'base/sector/sector_index.html'
    model = Sector
    paginate_by = 7
    context_object_name = 'sectores'


class SectorCreate(CreateView):
    model = Sector
    template_name = 'base/sector/sector_create.html'
    form_class = SectorForm
    success_url = reverse_lazy('base:sector-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Sector|Agregar'
        context['titulo_pagina'] = 'Agregar Sector'
        return context


class SectorEdit(UpdateView):
    model = Sector
    template_name = 'base/sector/sector_create.html'
    form_class = SectorForm
    success_url = reverse_lazy('base:sector-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Sector|Editar'
        context['titulo_pagina'] = 'Editar Sector'
        return context


def sector_delete(request, id):
    sector = Sector.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Sector',
            'titulo': 'Sector|Eliminar',
            'ruta': 'base:sector-index',
            'objeto': sector,
        }
        return render(request, 'base/sector/sector_delete.html', contexto)
    else:
        try:
            sector.delete()
        except:
            mensaje = 'No puede eliminar Sector, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Sector eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Sector',
            'mensaje': mensaje,
            'titulo': 'Sector|Eliminar',
            'ruta': 'base:sector-index',
            'objeto': sector,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)

# RAMO


class RamoIndex(ListView):
    template_name = 'base/ramo/ramo_index.html'
    model = Ramo
    paginate_by = 7
    context_object_name = 'ramos'


class RamoCreate(CreateView):
    model = Ramo
    template_name = 'base/ramo/ramo_create.html'
    form_class = RamoForm
    success_url = reverse_lazy('base:ramo-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ramo|Agregar'
        context['titulo_pagina'] = 'Agregar Ramo'
        return context


class RamoEdit(UpdateView):
    model = Ramo
    template_name = 'base/ramo/ramo_create.html'
    form_class = RamoForm
    success_url = reverse_lazy('base:ramo-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Ramo|Editar'
        context['titulo_pagina'] = 'Editar Ramo'
        return context


def ramo_delete(request, id):
    ramo = Ramo.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Ramo',
            'titulo': 'Ramo|Eliminar',
            'ruta': 'base:ramo-index',
            'objeto': ramo,
        }
        return render(request, 'base/ramo/ramo_delete.html', contexto)
    else:
        try:
            ramo.delete()
        except:
            mensaje = 'No puede eliminar Ramo, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Ramo eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Ramo',
            'mensaje': mensaje,
            'titulo': 'Ramo|Eliminar',
            'ruta': 'base:ramo-index',
            'objeto': ramo,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)

# ACTIVIDAD


class ActividadIndex(ListView):
    template_name = 'base/actividad/actividad_index.html'
    model = Actividad
    paginate_by = 7
    context_object_name = 'actividades'


class ActividadCreate(CreateView):
    model = Actividad
    template_name = 'base/actividad/actividad_create.html'
    form_class = ActividadForm
    success_url = reverse_lazy('base:actividad-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Actividad|Agregar'
        context['titulo_pagina'] = 'Agregar Actividad'
        return context


class ActividadEdit(UpdateView):
    model = Actividad
    template_name = 'base/actividad/actividad_create.html'
    form_class = ActividadForm
    success_url = reverse_lazy('base:actividad-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Actividad|Editar'
        context['titulo_pagina'] = 'Editar Actividad'
        return context


def actividad_delete(request, id):
    actividad = Actividad.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Actividad',
            'titulo': 'Actividad|Eliminar',
            'ruta': 'base:actividad-index',
            'objeto': actividad,
        }
        return render(request, 'base/actividad/actividad_delete.html', contexto)
    else:
        try:
            actividad.delete()
        except:
            mensaje = 'No puede eliminar Actividad, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Actividad eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Actividad',
            'mensaje': mensaje,
            'titulo': 'Actividad|Eliminar',
            'ruta': 'base:actividad-index',
            'objeto': actividad.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TIPO EMPRESA
class TipoEmpresaIndex(ListView):
    template_name = 'base/tipoempresa/tipoempresa_index.html'
    model = TipoEmpresa
    paginate_by = 7
    context_object_name = 'tipoempresas'


class TipoEmpresaCreate(CreateView):
    model = TipoEmpresa
    template_name = 'base/tipoempresa/tipoempresa_create.html'
    form_class = TipoEmpresaForm
    success_url = reverse_lazy('base:tipoempresa-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Empresa|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Empresa'
        return context


class TipoEmpresaEdit(UpdateView):
    model = TipoEmpresa
    template_name = 'base/tipoempresa/tipoempresa_create.html'
    form_class = TipoEmpresaForm
    success_url = reverse_lazy('base:tipoempresa-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Empresa|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Empresa'
        return context


def tipoempresa_delete(request, id):
    tipoempresa = TipoEmpresa.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Empresa',
            'titulo': 'Tipo de Empresa|Eliminar',
            'ruta': 'base:tipoempresa-index',
            'objeto': tipoempresa,
        }
        return render(request, 'base/tipoempresa/tipoempresa_delete.html', contexto)
    else:
        try:
            tipoempresa.delete()
        except:
            mensaje = 'No puede eliminar Tipo de Empresa, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Empresa eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Empresa',
            'mensaje': mensaje,
            'titulo': 'Tipo de Empresa|Eliminar',
            'ruta': 'base:tipoempresa-index',
            'objeto': tipoempresa.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TAMAÑO EMPRESA
class TamanoEmpresaIndex(ListView):
    template_name = 'base/tamanoempresa/tamanoempresa_index.html'
    model = TamanoEmpresa
    paginate_by = 7
    context_object_name = 'tamanoempresas'


class TamanoEmpresaCreate(CreateView):
    model = TamanoEmpresa
    template_name = 'base/tamanoempresa/tamanoempresa_create.html'
    form_class = TamanoEmpresaForm
    success_url = reverse_lazy('base:tamanoempresa-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tamaño de Empresa|Agregar'
        context['titulo_pagina'] = 'Agregar Tamaño de Empresa'
        return context


class TamanoEmpresaEdit(UpdateView):
    model = TamanoEmpresa
    template_name = 'base/tamanoempresa/tamanoempresa_create.html'
    form_class = TamanoEmpresaForm
    success_url = reverse_lazy('base:tamanoempresa-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tamaño de Empresa|Editar'
        context['titulo_pagina'] = 'Editar Tamaño de Empresa'
        return context


def tamanoempresa_delete(request, id):
    tamanoempresa = TamanoEmpresa.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tamaño de Empresa',
            'titulo': 'Tamaño de Empresa|Eliminar',
            'ruta': 'base:tamanoempresa-index',
            'objeto': tamanoempresa,
        }
        return render(request, 'base/tamanoempresa/tamanoempresa_delete.html', contexto)
    else:
        try:
            tamanoempresa.delete()
        except:
            mensaje = 'No puede eliminar Tamaño de Empresa, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tamaño de Empresa eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tamaño de Empresa',
            'mensaje': mensaje,
            'titulo': 'Tamaño de Empresa|Eliminar',
            'ruta': 'base:tamanoempresa-index',
            'objeto': tamanoempresa.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TIPO CAPITAL
class TipoCapitalIndex(ListView):
    template_name = 'base/tipocapital/tipocapital_index.html'
    model = TipoCapital
    paginate_by = 7
    context_object_name = 'tipocapitales'


class TipoCapitalCreate(CreateView):
    model = TipoCapital
    template_name = 'base/tipocapital/tipocapital_create.html'
    form_class = TipoCapitalForm
    success_url = reverse_lazy('base:tipocapital-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Capital|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Capital'
        return context


class TipoCapitalEdit(UpdateView):
    model = TipoCapital
    template_name = 'base/tipocapital/tipocapital_create.html'
    form_class = TipoCapitalForm
    success_url = reverse_lazy('base:tipocapital-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Capital|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Capital'
        return context


def tipocapital_delete(request, id):
    tipocapital = TipoCapital.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Capital',
            'titulo': 'Tipo de Capital|Eliminar',
            'ruta': 'base:tipocapital-index',
            'objeto': tipocapital,
        }
        return render(request, 'base/tipocapital/tipocapital_delete.html', contexto)
    else:
        try:
            tipocapital.delete()
        except:
            mensaje = 'No puede eliminar Tipo de Capital, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Capital eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Capital',
            'mensaje': mensaje,
            'titulo': 'Tipo de Capital|Eliminar',
            'ruta': 'base:tipocapital-index',
            'objeto': tipocapital.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# VENDEDOR
class VendedorIndex(ListView):
    template_name = 'base/vendedor/vendedor_index.html'
    model = Vendedor
    paginate_by = 7
    context_object_name = 'vendedores'


class VendedorCreate(CreateView):
    model = Vendedor
    template_name = 'base/vendedor/vendedor_create.html'
    form_class = VendedorForm
    success_url = reverse_lazy('base:vendedor-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Vendedor|Agregar'
        context['titulo_pagina'] = 'Agregar Vendedor'
        return context


class VendedorEdit(UpdateView):
    model = Vendedor
    template_name = 'base/vendedor/vendedor_create.html'
    form_class = VendedorForm
    success_url = reverse_lazy('base:vendedor-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Vendedor|Editar'
        context['titulo_pagina'] = 'Editar Vendedor'
        return context


def vendedor_delete(request, id):
    vendedor = Vendedor.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Vendedor',
            'titulo': 'Vendedor|Eliminar',
            'ruta': 'base:vendedor-index',
            'objeto': vendedor,
        }
        return render(request, 'base/vendedor/vendedor_delete.html', contexto)
    else:
        try:
            vendedor.delete()
        except:
            mensaje = 'No puede eliminar Vendedor, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Vendedor eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Vendedor',
            'mensaje': mensaje,
            'titulo': 'Vendedor|Eliminar',
            'ruta': 'base:vendedor-index',
            'objeto': vendedor.nombre + " " + vendedor.apellido,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# REGION
class RegionIndex(ListView):
    template_name = 'base/region/region_index.html'
    model = Region
    paginate_by = 7
    context_object_name = 'regiones'


class RegionCreate(CreateView):
    model = Region
    template_name = 'base/region/region_create.html'
    form_class = RegionForm
    success_url = reverse_lazy('base:region-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Región|Agregar'
        context['titulo_pagina'] = 'Agregar Región'
        return context


class RegionEdit(UpdateView):
    model = Region
    template_name = 'base/region/region_create.html'
    form_class = RegionForm
    success_url = reverse_lazy('base:region-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Región|Editar'
        context['titulo_pagina'] = 'Editar Región'
        return context


def region_delete(request, id):
    region = Region.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Región',
            'titulo': 'Región|Eliminar',
            'ruta': 'base:region-index',
            'objeto': region,
        }
        return render(request, 'base/region/region_delete.html', contexto)
    else:
        try:
            region.delete()
        except:
            mensaje = 'No puede eliminar Región, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Región eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Región',
            'mensaje': mensaje,
            'titulo': 'Región|Eliminar',
            'ruta': 'base:region-index',
            'objeto': region.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# ZONA
class ZonaIndex(ListView):
    template_name = 'base/zona/zona_index.html'
    model = Zona
    paginate_by = 7
    context_object_name = 'zonas'


class ZonaCreate(CreateView):
    model = Zona
    template_name = 'base/zona/zona_create.html'
    form_class = ZonaForm
    success_url = reverse_lazy('base:zona-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Zona|Agregar'
        context['titulo_pagina'] = 'Agregar Zona'
        return context


class ZonaEdit(UpdateView):
    model = Zona
    template_name = 'base/zona/zona_create.html'
    form_class = ZonaForm
    success_url = reverse_lazy('base:zona-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Zona|Editar'
        context['titulo_pagina'] = 'Editar Zona'
        return context


def zona_delete(request, id):
    zona = Zona.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Zona',
            'titulo': 'Zona|Eliminar',
            'ruta': 'base:zona-index',
            'objeto': zona,
        }
        return render(request, 'base/zona/zona_delete.html', contexto)
    else:
        try:
            zona.delete()
        except:
            mensaje = 'No puede eliminar Zona, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Zona eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Zona',
            'mensaje': mensaje,
            'titulo': 'Zona|Eliminar',
            'ruta': 'base:zona-index',
            'objeto': zona.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)
