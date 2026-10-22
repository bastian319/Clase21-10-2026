from django import forms
from .models import Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado

        fields = [
            'nombre',
            'apellido',
            'sueldo',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'sueldo': 'Sueldo',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre',
            }),

            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),

            'sueldo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el sueldo',
                'step': '0.01',
                'min': '0',
            })
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if not nombre:
            raise forms.ValidationError(
                'El nombre es obligatorio.'
            )
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido'].strip()
        if not apellido:
            raise forms.ValidationError(
                'El apellido es obligatorio'
            )
        return apellido

    def clean_sueldo(self):
        sueldo = self.cleaned_data['sueldo']

        if sueldo < 0:
            raise forms.ValidationError(
                'El sueldo no puede ser negativo.'
            )
        return sueldo