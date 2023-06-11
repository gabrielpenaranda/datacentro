from django import forms
from .models import (
    Ciudad, Estado, Pais, Sector, Ramo, Actividad,
    TipoEmpresa, TamanoEmpresa, TipoCapital,
    Vendedor, Region, Zona
    )


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ["nombre", "estado"]
        labels = {
            'nombre': 'Nombre de la ciudad',
            'estado': 'Estado',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la ciudad',
                    'id': 'nombre'
                }
            ),
            'estado': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione el estado',
                    'id': 'estado',
                }
            )
        }


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["nombre", "pais"]
        labels = {
            'nombre': 'Nombre del estado',
            'pais':  'País',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre del estado',
                    'id': 'nombre'
                }
            ),
            'pais': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione país',
                    'id': 'nombre'
                }
            )
        }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ["nombre"]
        labels = {
            'nombre': 'Nombre del país',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el nombre del país',
                    'id': 'nombre'
                }
            )
        }


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ["nombre", "descripcion"]
        labels = {
            'nombre': 'Nombre del sector',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre del sector',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            )
        }

class RamoForm(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ["nombre", "descripcion", "sector"]
        labels = {
            'nombre': 'Nombre del ramo',
            'descripcion': 'Descripción',
            'sector':  'Sector',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el nombre del ramo',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            ),
            'sector': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione sector',
                    'id': 'sector'
                }
            )
        }


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ["nombre", "descripcion", "ramo"]
        labels = {
            'nombre': 'Nombre de la actividad',
            'descripcion': 'Descripción',
            'ramo':  'Ramo',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la actividad',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            ),
            'ramo': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione sector',
                    'id': 'ramo'
                }
            )
        }


class TipoEmpresaForm(forms.ModelForm):
    class Meta:
        model = TipoEmpresa
        fields = ["nombre", "descripcion"]
        labels = {
            'nombre': 'Tipo de empresa',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tipo de empresa',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            )
        }


class TamanoEmpresaForm(forms.ModelForm):
    class Meta:
        model = TamanoEmpresa
        fields = ["nombre", "descripcion"]
        labels = {
            'nombre': 'Tamaño de empresa',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tamaño de empresa',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            )
        }


class TipoCapitalForm(forms.ModelForm):
    class Meta:
        model = TipoCapital
        fields = ["nombre", "descripcion"]
        labels = {
            'nombre': 'Tipo de capital',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tipo de capital',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            )
        }


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = [
            "nombre",
            "apellido",
            "cedula",
            "rif",
            "direccion",
            "ciudad",
            "telefono",
            "email",
         ]
        labels = {
            "nombre": "Nombre",
            "apellido": "Apellido",
            "cedula": "Cédula",
            "rif": "RIF",
            "direccion": "Dirección",
            "ciudad": "Ciudad",
            "telefono": "Teléfono(s)",
            "email": "E-mail",
         }
        widgets = {
            "nombre": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre',
                    'id': 'nombre'
                }
            ),
            "apellido": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el apellido',
                    'id': 'apellido'
                }
            ),
            "cedula": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la cédula',
                    'id': 'cedula'
                }
            ),
            "rif": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el RIF',
                    'id': 'rif'
                }
            ),
            "direccion": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la dirección',
                    'id': 'direccion'
                }
            ),
            "ciudad": forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese la ciudad',
                    'id': 'ciudad'
                }
            ),
            "telefono": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s)',
                    'id': 'telefono'
                }
            ),
            "email": forms.EmailInput(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el e-mail',
                    'id': 'email'
                }
            )
         }


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["nombre", "descripcion"]
        labels = {
            'nombre': 'Nombre de la region',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la region',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            )
        }


class ZonaForm(forms.ModelForm):
    class Meta:
        model = Zona
        fields = ["nombre", "descripcion", "region"]
        labels = {
            'nombre': 'Nombre de la zona',
            'descripcion': 'Descripción',
            'region':  'Región',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la zona',
                    'id': 'nombre'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Agregue una descripción',
                    'id': 'descripcion',
                }
            ),
            'region': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione region',
                    'id': 'region'
                }
            )
        }
