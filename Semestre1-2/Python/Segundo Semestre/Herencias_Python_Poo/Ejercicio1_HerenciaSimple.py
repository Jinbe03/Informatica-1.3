#          Ejercico N°1 Herencia
#               HerenciaSimple

#     Este es eñ ejercicio mas basico de herencia

from os import system
system ("cls")

#Clase Padre llama Carreras

class Carreras():

    NumLab = 99 #Atributo Publico

    #contructor que recibe 4 argumentos; asig, prof, NHrs, TipoA
    def __init__(self,Asig,Profe,NHrs,TipoA):
        self.Asignatura = Asig
        self.Profesor   = Profe
        self.NHrs       = NHrs
        self.TipoAsig   = TipoA

    def MostrarDatos(self):
        print("============================================================")
        print("\n               Muestra de Datos               ")
        print("La asignatura creada es                 : ", self.Asignatura)
        print("El Profesor que dicta la asignatura es  : ", self.Profesor)
        print("El numero de horas de la asignatura es  : ", self.NHrs)
        print("El tipo de asignatura es                : ",self.TipoAsig)
        print("La clase se dicta en el laboratorio n°  : ", self.NumLab)
        print("============================================================")
        print("")


#========================= ESTA ES OTRA CLASE =========================

#Clase hija o sub-clase llamada enfermeria
#esta clase no tiene constructor, atributos, etc, todo lo hereda de la clase padre

class Enfermeria(Carreras):
    pass


#========================= SE CREA OBJETO 1 DE ENFERMERIA =========================
# Se instancia o copia la clase enfermeria, pero hereda el constructor, los atributos
# y el metodo crea asignatura de la clase padre

Carrera1 = Enfermeria ("Farmacologia","JuanPerez",72,"Practica")
Carrera1.MostrarDatos()


#========================= SE CREA OBJETO 2 DE ENFERMERIA =========================
# Se instancia o copia la clase Enfermeria, pero hereda el constructor, los atributos
# y el metodo CrearAsignatura de la clase padre

Carrera2 = Enfermeria("Anatomia","Alumnos",99,"Teorica")
Carrera2.NumLab=777
Carrera2.MostrarDatos()        