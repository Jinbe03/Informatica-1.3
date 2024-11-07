from django.contrib import admin
from .models import *

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','apellido','edad','telefono','direccion','tipo']
    search_fields = ['rut','nombre']
    list_per_page = 2

admin.site.register(TipoEmpleado)
admin.site.register(Empleado, EmpleadoAdmin)