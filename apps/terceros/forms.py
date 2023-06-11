from django import forms
from .models import (
    TipoTercero, TipoPersona, Tercero, Persona, Sucursal
)


class TipoTerceroForm(forms.ModelForm):
    class Meta:
        model = TipoTercero
        fields = ["descripcion"]
        labels = {
            'descripcion': 'Tipo de tercero',
        }
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el tipo de tercero',
                    'id': 'descripcion'
                }
            )
        }


class TipoPersonaForm(forms.ModelForm):
    class Meta:
        model = TipoPersona
        fields = ["descripcion"]
        labels = {
            'descripcion': 'Tipo de persona',
        }
        widgets = {
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el tipo de persona',
                    'id': 'descripcion'
                }
            )
        }


class TerceroForm(forms.ModelForm):
    class Meta:
        model = Tercero
        fields = ["tipo_tercero", "nombre", "nombre_juridico", "direccion", "rif", "nit", "telefono", "email", 'web', "tipocapital", "ciudad", "zona", "descripcion_actividad", "tamano_empresa", "tipo_empresa", "vendedor"]
        labels = {
            'tipo_tercero': 'Tipo de tercero',
            'nombre': 'Nombre',
            'nombre_juridico': 'Nombre Jurídico',
            'direccion': 'Dirección',
            'rif': 'RIF',
            'nit': 'NIT',
            'telefono': 'Teléfono(s)',
            'email': 'Email',
            'web': 'Sitio web',
            'tipocapital': 'Tipo de capital',
            'ciudad': 'Ciudad',
            'zona': 'Zona',
            # 'actividad': 'Actividad',
            # 'ramo': 'Ramo',
            'descripcion_actividad': 'Descripción de la actividad',
            'tamano_empresa': 'Tamaño de la empresa',
            'tipo_empresa': 'Tipo de empresa',
        }
        widgets = {
            'tipo_tercero': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Agregue el tipo de  tercero',
                    'id': 'tipo_tercero'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre del tercero',
                    'id': 'nombre'
                }
            ),
            'nombre_juridico': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre jurídico del tercero',
                    'id': 'nombre_juridico'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la dirección del tercero',
                    'id': 'direccion'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s)',
                    'id': 'telefono'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el email',
                    'id': 'email'
                }
            ),
            'rif': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el RIF',
                    'id': 'rif'
                }
            ),
            'nit': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el NIT',
                    'value': '',
                    'id': 'nit'
                }
            ),
            'tipocapital': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese el tipo de capital',
                    'id': 'tipocapital'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese la ciudad',
                    'id': 'ciudad'
                }
            ),
            'zona': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese la zona',
                    'id': 'zona'
                }
            ),
            """ 'ramo': forms.Select(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Seleccione el ramo',
                    'id': 'ramo'
                }
            ), """
            'descripcion_actividad': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la descripción de la actividad',
                    'id': 'descripcion_actividad'
                }
            ),
            'tamano_empresa': forms.Select(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el tamaño de empresa',
                    'id': 'tamano_empresa'
                }
            ),
            'tipo_empresa': forms.Select(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la actividad',
                    'id': 'tipo_empresa'
                }
            ),
            'vendedor': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Ingrese el vendedor',
                    'id': 'vendedor'
                }
            ),
        }
        

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["nombre", "apellido", "cargo", "telefono_oficina", "telefono_celular", "tercero", "tipopersona"]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cargo': 'Cargo',
            'telefono_oficina': 'Teléfono Oficina',
            'telefono_celular': 'Teléfono Celular',
            'tercero': 'Tercero',
            'tipopersona': 'Tipo de Persona',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) nombre(s) de la persona',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) apellido(s) de la persona',
                    'id': 'apellido'
                }
            ),
            'cargo': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el cargo',
                    'id': 'cargo'
                }
            ),
            'telefono_oficina': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s) de oficina',
                    'id': 'telefono_oficina'
                }
            ),
            'telefono_celular': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el(los) teléfono(s) celular(es)',
                    'id': 'telefono_celular'
                }
            ),
            'tercero': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm',
                    'placeholder': 'Ingrese el tercero relacionado',
                    'id': 'tercero'
                }
            ),
            'tipopersona': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese el tipo de persona',
                    'id': 'tipopersona'
                }
            )
        }
        
        
class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = ["nombre", "direccion", "telefono", "ciudad", "tercero"]
        labels = {
            'nombre': 'Nombre de sucursal',
            'direccion': 'Dirección',
            'telefono': "Teléfono",
            'ciudad': "Ciudad",
            'tercero': "Tercero",
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese el nombre de la sucursal',
                    'id': 'nombre'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm mb-2',
                    'placeholder': 'Ingrese la dirección',
                    'id': 'direccion'
                }
            ),
            'ciudad': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese la ciudad',
                    'id': 'ciudad'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'placeholder': 'Ingrese el(los) teléfono(s)',
                    'id': 'telefono'
                }
            ),
            'tercero': forms.Select(
                attrs={
                    'class': 'form-select form-select-sm mb-2',
                    'placeholder': 'Ingrese el tercero',
                    'id': 'tercero'
                }
            )
        }
