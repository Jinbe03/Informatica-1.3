from django import forms
from django.forms import ModelForm
from .models import *

# TEMPLATE PARA PODER USARLO EN LOS HTML
class EmpleadoForm(ModelForm):

    rut = forms.CharField(min_length=2 ,max_length=40)
    edad = forms.IntegerField(min_value=18)

    class Meta:
        model = Empleado
        fields = ['rut', 'nombre', 'apellido', 'edad', 'direccion', 'telefono', 'tipo', 'nacimiento','foto']

        widgets = {
            'nacimiento' : forms.SelectDateWidget(years=range(1940, 2007))
        }