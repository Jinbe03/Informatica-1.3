from django.contrib import admin
from .models import *

# Register your models here.
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','apellido','edad','direccion','telefono','tipo']
    search_fields = ['rut']
    list_per_page = 5

admin.site.register(TipoEmpleado)
admin.site.register(Empleado,EmpleadosAdmin)