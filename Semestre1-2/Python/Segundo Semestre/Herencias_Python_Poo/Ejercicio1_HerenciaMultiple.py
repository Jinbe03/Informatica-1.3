#               Ejercicio N°1 Herencia Multiple

#Este es el ejercico mas basico de herencia multiple

from os import system
system("cls")

class Carreras():
    NumM = 0 #Atributo Publico
    Carr = ""
    Rutt = ""
    Nomm = ""

    def __init__ (self):
        pass;


    def DatosMatricula(self):
        print("\n\n    Ingreso de Datos de Matricula    ")
        self.NumM = input("Ingrese N° de Matricula        : ")
        self.Carr = input("Ingrese nombre de la Carrera   : ")
        self.Rutt = input("Ingrese Rut del Alumno         : ")
        self.Nomm = input("Ingrese Nombre del Alumno      : ")

# ========================== ESTA ES OTRA CLASE ==========================

class PagoMatricula():
    pago = 1850000
    def __init__(self):
        pass

    def DatosAlumnos(self):
        print("\n\n     Forma de pago Matricula     ")
        print("============================================")
        self.FPago = input ("Ingrese forma de pago : ")

    def ListarDatos(self):
        print("")
        print("\n Listado de datos de la matricula ")
        print("============================================")
        print("El numero de matricula del alumno es  : ", self.NumM)
        print("El nombre de la Carrera es            : ", self.Carr)
        print("El ruut del almuno es                 : ", self.Rutt)
        print("El nombre del alumno matriculado es   : ", self.Nomm)
        print("El valor a pagar de la carrera fue    : ", self.Pago)
        print("La forma de pago de la matricula es   : ", self.FPago)
        print("============================================")
        print("")

# ========================== ESTA ES OTRA CLASE ==========================

class Matriculas(Carreras,PagoMatricula):
    pass

#     SE CREA EL OBJETO 1 DE ENFERMERIA
# Se instancia o copia la clase ENFERMERIA, pero hereda el constructor, los atributos y el metodo de
# CrearAsignatura de la clase padre

Matricula1= Matriculas()
Matricula1.DatosMatricula()
Matricula1.DatosAlumnos()
Matricula1.ListarDatos()
print("")
print("==== ESTOY DE REGRESO EN LA CLASE MATRICULAS ====")
print("")