from django.db import models
from django.db.models import Q


class TerceroManager(models.Manager):

    def buscar_tercero(self, kword):
               
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(tipo__icontains=kword)
        )

        return resultado