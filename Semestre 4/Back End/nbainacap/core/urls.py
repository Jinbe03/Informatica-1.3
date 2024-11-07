from django.urls import path
from .views import *

# VIEW -> URL -> RENDERIZA

urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('quienessomos/', quienessomos, name="quienessomos"),
]