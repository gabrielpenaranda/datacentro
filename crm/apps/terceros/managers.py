from django.db import models
from django.db.models import Q


class TerceroManager(models.Manager):

    def buscar_tercero(self, kword, orderby, ascdesc):

        if ascdesc == 'desc':
            order = '-' + orderby
        elif ascdesc == 'asc':
            order = orderby

        resultado = self.filter(
                Q(nombre__icontains=kword) | 
                Q(tipo__icontains=kword) | 
                Q(ciudad__ciudad__icontains=kword) | 
                Q(zona__zona__icontains=kword) |
                Q(zona__region__region__icontains=kword) |
                Q(ciudad__estado__estado__icontains=kword) |
                Q(ciudad__estado__pais__pais__icontains=kword)
            ).order_by(order).select_related('ciudad').select_related('zona')
        
        return resultado
    
    
    def todos_tercero(self, orderby, ascdesc):
        
        if ascdesc == 'desc':
            order = '-' + orderby
        elif ascdesc == 'asc':
            order = orderby
        elif not ascdesc:
            order = 'nombre'

        resultado = self.all().select_related('ciudad').select_related('zona').order_by(order)
        
        return resultado
