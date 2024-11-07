from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name="login"),
    path('register/', register, name="register"),
    path('index/', index, name="index"),
    path('contacto/', contacto, name="contacto"),
]