from django.urls import path
from .views import *

# LAS URLS SIRVEN PARA LLAMAR A LAS PAGINAS

urlpatterns = [
    path('', index, name="index"), # PAGINA DE INICIO
    path('contacto/', contacto, name="contacto"),
    path('quienessomos/', quienessomos , name="quienessomos"),
    path('empleados/', empleados , name="empleados"),
    path('addempleado/', addEmpleado , name="addEmpleado"),
    path('updateempleado/<id>/', updateempleado , name="updateempleado"),
    path('deleteempleado/<id>/', deleteempleado , name="deleteempleado"),
]