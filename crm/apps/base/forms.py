from django import forms
from .models import (
    Ciudad, Estado, Pais, Sector, Ramo, Actividad,
    TipoEmpresa, TamanoEmpresa, TipoCapital,
    Vendedor, Region, Zona
    )


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ["ciudad", "estado"]
        labels = {
            'ciudad': 'Nombre de la ciudad',
            'estado': 'Estado',
        }
        widgets = {
            'ciudad': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la ciudad',
                    'id': 'ciudad'
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
        fields = ["estado", "pais"]
        labels = {
            'estado': 'Nombre del estado',
            'pais':  'País',
        }
        widgets = {
            'estado': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre del estado',
                    'id': 'estado'
                }
            ),
            'pais': forms.Select(
                attrs = {
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Seleccione país',
                    'id': 'pais'
                }
            )
        }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ["pais"]
        labels = {
            'pais': 'Nombre del país',
        }
        widgets = {
            'pais': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el nombre del país',
                    'id': 'pais'
                }
            )
        }


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ["sector", "descripcion"]
        labels = {
            'sector': 'Nombre del sector',
            'descripcion': 'Descripción',
        }
        widgets = {
            'sector': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre del sector',
                    'id': 'sector'
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
        fields = ["ramo", "descripcion", "sector"]
        labels = {
            'ramo': 'Nombre del ramo',
            'descripcion': 'Descripción',
            'sector':  'Sector',
        }
        widgets = {
            'ramo': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el nombre del ramo',
                    'id': 'ramo'
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
        fields = ["actividad", "descripcion", "ramo"]
        labels = {
            'actividad': 'Nombre de la actividad',
            'descripcion': 'Descripción',
            'ramo':  'Ramo',
        }
        widgets = {
            'actividad': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la actividad',
                    'id': 'actividad'
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
        fields = ["tipo_empresa", "descripcion"]
        labels = {
            'nombre': 'Tipo de empresa',
            'descripcion': 'Descripción',
        }
        widgets = {
            'tipo_empresa': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tipo de empresa',
                    'id': 'tipo_empresa'
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
        fields = ["tamano_empresa", "descripcion"]
        labels = {
            'tamano_empresa': 'Tamaño de empresa',
            'descripcion': 'Descripción',
        }
        widgets = {
            'tamano_empresa': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tamaño de empresa',
                    'id': 'tamano_empresa'
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
        fields = ["tipo_capital", "descripcion"]
        labels = {
            'tipo_capital': 'Tipo de capital',
            'descripcion': 'Descripción',
        }
        widgets = {
            'tipo_capital': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tipo de capital',
                    'id': 'tipo_capital'
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
            "numero_fiscal",
            "direccion",
            "ciudad",
            "telefono",
            "email",
         ]
        labels = {
            "nombre": "Nombre",
            "apellido": "Apellido",
            "cedula": "Cédula",
            "numero_fiscal": "Identificador Fiscal",
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
            "numero_fiscal": forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el Identificador Fiscal',
                    'id': 'numero_fiscal'
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
        fields = ["region", "descripcion"]
        labels = {
            'region': 'Nombre de la region',
            'descripcion': 'Descripción',
        }
        widgets = {
            'region': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la region',
                    'id': 'region'
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
        fields = ["zona", "descripcion", "region"]
        labels = {
            'zona': 'Nombre de la zona',
            'descripcion': 'Descripción',
            'region':  'Región',
        }
        widgets = {
            'zona': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la zona',
                    'id': 'zona'
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
