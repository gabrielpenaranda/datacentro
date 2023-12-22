from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.decorators.http import require_http_methods

from django.core.paginator import InvalidPage
from django.http import Http404, HttpResponse
from django.utils.translation import gettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from http import cookies

from django.core.cache import cache

from .models import (
    TipoTercero, TipoPersona, Tercero, Persona, Sucursal
)
from .forms import (
    TipoTerceroForm, TipoPersonaForm, TerceroForm,
    PersonaForm, SucursalForm
)
from django.views.generic import (
    View, TemplateView, ListView,
    UpdateView, CreateView, DeleteView
)
from django.urls import reverse_lazy


# TIPO DE TERCERO
class TipoTerceroIndex(ListView):
    template_name = 'terceros/tipotercero/tipotercero_index.html'
    model = TipoTercero
    paginate_by = 7
    context_object_name = 'tipoterceros'


class TipoTerceroCreate(CreateView):
    model = TipoTercero
    template_name = 'terceros/tipotercero/tipotercero_create.html'
    form_class = TipoTerceroForm
    success_url = reverse_lazy('terceros:tipotercero-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Tercero|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Tercero'
        return context


class TipoTerceroEdit(UpdateView):
    model = TipoTercero
    template_name = 'terceros/tipotercero/tipotercero_create.html'
    form_class = TipoTerceroForm
    success_url = reverse_lazy('terceros:tipotercero-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Tercero|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Tercero'
        return context


def tipotercero_delete(request, id):
    tipotercero = TipoTercero.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Tercero',
            'titulo': 'Tipo de Tercero|Eliminar',
            'ruta': 'terceros:tipotercero-index',
            'objeto': tipotercero,
        }
        return render(request, 'terceros/tipotercero/tipotercero_delete.html', contexto)
    else:
        try:
            tipotercero.delete()
        except:
            mensaje = 'No puede eliminar Tipo de Tercero, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Tercero eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Tercero',
            'mensaje': mensaje,
            'titulo': 'Tipo de Tercero|Eliminar',
            'ruta': 'terceros:tipotercero-index',
            'objeto': tipotercero.descripcion,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TIPO DE PERSONA
class TipoPersonaIndex(ListView):
    template_name = 'terceros/tipopersona/tipopersona_index.html'
    model = TipoPersona
    paginate_by = 7
    context_object_name = 'tipopersonas'


class TipoPersonaCreate(CreateView):
    model = TipoPersona
    template_name = 'terceros/tipopersona/tipopersona_create.html'
    form_class = TipoPersonaForm
    success_url = reverse_lazy('terceros:tipopersona-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Persona|Agregar'
        context['titulo_pagina'] = 'Agregar Tipo de Persona'
        return context


class TipoPersonaEdit(UpdateView):
    model = TipoPersona
    template_name = 'terceros/tipopersona/tipopersona_create.html'
    form_class = TipoPersonaForm
    success_url = reverse_lazy('terceros:tipopersona-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tipo de Persona|Editar'
        context['titulo_pagina'] = 'Editar Tipo de Persona'
        return context


def tipopersona_delete(request, id):
    tipopersona = TipoPersona.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Persona',
            'titulo': 'Tipo de Persona|Eliminar',
            'ruta': 'terceros:tipopersona-index',
            'objeto': tipopersona,
        }
        return render(request, 'terceros/tipopersona/tipopersona_delete.html', contexto)
    else:
        try:
            tipopersona.delete()
        except:
            mensaje = 'No puede eliminar Tipo de Persona, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tipo de Persona eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tipo de Persona',
            'mensaje': mensaje,
            'titulo': 'Tipo de Persona|Eliminar',
            'ruta': 'terceros:tipopersona-index',
            'objeto': tipopersona.descripcion,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)


# TERCERO
@require_http_methods(["GET", "POST"])
def tercero_index(request):
    page_num = request.GET.get('page', 1)
    
    if request.method == 'GET':
        orderby = 'nombre'
        ascdesc = 'asc'
        resultado = Tercero.objects.todos_tercero(orderby, ascdesc)
        page_size = 5
        paginator = Paginator(resultado, page_size)
    elif request.method == 'POST':
        palabra_clave = request.GET.get("kword", '').lower()
        orderby = request.GET.get('orderby', '').lower()
        ascdesc = request.GET.get('ascdesc', '').lower()
        page_size = request.GET.get('page_size', '')
        
        # del resultado
                        
        if page_size == '':
            page_size = 10
        else:
            page_size = int(page_size)
            
        if (palabra_clave):
            resultado = Tercero.objects.buscar_tercero(palabra_clave, orderby, ascdesc)
        else:
            # terceros = Tercero.objects.all().select_related('ciudad').select_related('zona').order_by(order)
            resultado = Tercero.objects.todos_tercero(orderby, ascdesc)
        paginator = Paginator(resultado, page_size)
        
    
    print(resultado)
    
    try:
        terceros = paginator.page(page_num)
    except PageNotAnInteger:
        terceros = paginator.page(1)
    except EmptyPage:
        terceros = paginator.page(paginator.num_pages)
        
    return render(request, 'terceros/tercero/tercero_index.html', {'terceros': terceros})
    


class TerceroIndex(ListView):
    template_name = 'terceros/tercero/tercero_index.html'
    paginate_by = None
    context_object_name = 'terceros'

    def dispatch(self, request, *args, **kwargs):
        try:
            if (self.object_list):
                del self.object_list
        except:
            print('algo')
        return super().dispatch(request, *args, **kwargs)
    
   
    def get_queryset(self):       
        
        palabra_clave = self.request.GET.get("kword", '').lower()
        orderby = self.request.GET.get('orderby', '').lower()
        ascdesc = self.request.GET.get('ascdesc', '').lower()
        page_size = self.request.GET.get('page_size', '')
                        
        if page_size == '':
            page_size = 10
        else:
            page_size = int(page_size)

        # print(f'{palabra_clave}, {orderby}, {ascdesc}, {order}, {page_size}')
        self.paginate_by = page_size
        
        if (palabra_clave):
            terceros = Tercero.objects.buscar_tercero(palabra_clave, orderby, ascdesc)
        else:
            # terceros = Tercero.objects.all().select_related('ciudad').select_related('zona').order_by(order)
            terceros = Tercero.objects.todos_tercero(orderby, ascdesc)
         
        print(terceros)
        
        """
        terceros = self.paginate_queryset(terceros1, page_size)
        print('******************************************************')
        print(terceros)
        i = 0
        pag = []
        for p in terceros:
            print('+=========================================================+')
            pag.append(p)
            print(p)
            print(pag[i])
            i = i + 1
        """"
                       
        return terceros


class TerceroCreate(CreateView):
    model = Tercero
    template_name = 'terceros/tercero/tercero_create.html'
    form_class = TerceroForm
    success_url = reverse_lazy('terceros:tercero-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tercero|Agregar'
        context['titulo_pagina'] = 'Agregar Tercero'
        return context


class TerceroEdit(UpdateView):
    model = Tercero
    template_name = 'terceros/tercero/tercero_create.html'
    form_class = TerceroForm
    success_url = reverse_lazy('terceros:tercero-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tercero|Editar'
        context['titulo_pagina'] = 'Editar Tercero'
        return context


def tercero_delete(request, id):
    terceros = Tercero.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Tercero',
            'titulo': 'Tercero|Eliminar',
            'ruta': 'terceros:tercero-index',
            'objeto': terceros,
        }
        return render(request, 'terceros/tercero/tercero_delete.html', contexto)
    else:
        try:
            if terceros.tipo == 'CL':
                terceros.tipo = 'ER'
                terceros.save()
            else:
                terceros.delete()
        except:
            mensaje = 'No puede eliminar Tercero, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Tercero eliminado exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Tercero',
            'mensaje': mensaje,
            'titulo': 'Tercero|Eliminar',
            'ruta': 'terceros:tercero-index',
            'objeto': terceros.nombre,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)
    
    
# PERSONA
class PersonaIndex(ListView):
    template_name = 'terceros/persona/persona_index.html'
    # model = Persona
    paginate_by = 10
    context_object_name = 'personas'
    
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '').lower()
        orderby = self.request.GET.get('orderby', '').lower()
        ascdesc = self.request.GET.get('ascdesc', '').lower()
        # page_size = self.request.GET.get('page_size', '')
        
        if ascdesc == 'desc':
            order = '-' + orderby
        elif ascdesc == 'asc':
            order = orderby
        elif not ascdesc:
            order = 'nombre'
                
        """ if page_size == '':
            page_size = 10
        else:
            page_size = int(page_size) """

        # print(f'{palabra_clave}, {orderby}, {ascdesc}, {order}, {page_size}')

        # self.paginate_by = page_size
        
        if (palabra_clave):
            terceros = Tercero.objects.buscar_tercero(palabra_clave, orderby, ascdesc)
        else:
            # terceros = Tercero.objects.all().select_related('ciudad').select_related('zona').order_by(order)
            terceros = Tercero.objects.todos_tercero(orderby, ascdesc)
            
        return terceros


class PersonaCreate(CreateView):
    model = Persona
    template_name = 'terceros/persona/persona_create.html'
    form_class = PersonaForm
    success_url = reverse_lazy('terceros:persona-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Persona|Agregar'
        context['titulo_pagina'] = 'Agregar Persona'
        return context


class PersonaEdit(UpdateView):
    model = Persona
    template_name = 'terceros/persona/persona_create.html'
    form_class = PersonaForm
    success_url = reverse_lazy('terceros:persona-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Persona|Editar'
        context['titulo_pagina'] = 'Editar Persona'
        return context


def persona_delete(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Persona',
            'titulo': 'Persona|Eliminar',
            'ruta': 'terceros:persona-index',
            'objeto': persona,
        }
        return render(request, 'terceros/persona/persona_delete.html', contexto)
    else:
        try:
            persona.delete()
        except:
            mensaje = 'No puede eliminar Persona, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Persona eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Persona',
            'mensaje': mensaje,
            'titulo': 'Persona|Eliminar',
            'ruta': 'terceros:persona-index',
            'objeto': persona,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)
    
    
# SUCURSAL
class SucursalIndex(ListView):
    template_name = 'terceros/sucursal/sucursal_index.html'
    model = Sucursal
    paginate_by = 7
    context_object_name = 'sucursales'


class SucursalCreate(CreateView):
    model = Sucursal
    template_name = 'terceros/sucursal/sucursal_create.html'
    form_class = SucursalForm
    success_url = reverse_lazy('terceros:sucursal-index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Sucursal|Agregar'
        context['titulo_pagina'] = 'Agregar Sucursal'
        return context


class SucursalEdit(UpdateView):
    model = Sucursal
    template_name = 'terceros/sucursal/sucursal_create.html'
    form_class = SucursalForm
    success_url = reverse_lazy('terceros:sucursal-index')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Sucursal|Editar'
        context['titulo_pagina'] = 'Editar Sucursal'
        return context


def sucursal_delete(request, id):
    sucursal = Sucursal.objects.get(id=id)
    if request.method == 'GET':
        contexto = {
            'titulo_pagina': 'Eliminar Sucursal',
            'titulo': 'Sucursal|Eliminar',
            'ruta': 'terceros:sucursal-index',
            'objeto': sucursal,
        }
        return render(request, 'terceros/sucursal/sucursal_delete.html', contexto)
    else:
        try:
            sucursal.delete()
        except:
            mensaje = 'No puede eliminar Sucursal, tiene registros asociados'
            class_card = "card border-danger"
            class_title = "card-title text-white bg-danger"
        else:
            mensaje = 'Sucursal eliminada exitosamente'
            class_card = "card border-success"
            class_title = "card-title text-white bg-success"

        contexto = {
            'titulo_pagina': 'Eliminar Sucursal',
            'mensaje': mensaje,
            'titulo': 'Sucursal|Eliminar',
            'ruta': 'terceros:sucursal-index',
            'objeto': sucursal,
            'class_card': class_card,
            'class_title': class_title,
        }
        return render(request, 'layouts/mensaje.html', contexto)
