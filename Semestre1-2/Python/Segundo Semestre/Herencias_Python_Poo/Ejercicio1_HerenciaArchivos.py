from os import system
system ("cls")

#llamo al archivo metFuncion e improto la clase metodos
from Ejercicio1_HerenciaArchivos import Metodos

#Creo la clase principal
class pricipal():
    Mett = Metodos

    def __init__(self):
        pass

    def CorrerPrograma(self):
        self.Mett.IngresarDatos()
        self.Mett.ListarDatos()

#Creo los objetos