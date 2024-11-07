#       Ejercicio N°2
#        Clases Basicas

#Desarrollo paso a paso de una clase basica en POO
# La clase que se desarrollara es la de a PPT revisada en clases de POO

#Se deben crear 3 funciones en la clase 

#Limpiar pantalla

from os import system
system ("cls");

Rutt  = "";
Nomm  = "";
SBase = "";
Bono  = 0 ;
SLiqu = 0 ;


class Alumno():

    def __init__(self):
        pass;
    
    def Ingreso():

        global Rutt
        global Nomm
        global SBase
        global Bono
        global SLiqu

        print("               Ingreso de Datos               ")
        Rutt  = input("Ingrese Rut de Usuario: ")
        Nomm  = input("Ingrese Nombre del Usuario: ")
        SBase = int(input("Ingrese Sueldo Base del Usuario: "))
        Bono  = int(input("Ingrese Bono del Usuario: "))
        SLiqu = SBase + Bono



    def Grabar():
        Eddad=777
        print("")
        print("          Grabado de Datos          ")
        print("La edad de Grabado es : ", Eddad)
        print("")

    def Listar():
        print("");
        print("          Listado de Datos          ")
        print("El Rut del usuario es nuevo creado es         : ", Rutt);
        print("El Nombre del Usuario nuevo creado es         : ", Nomm);
        print("El Sueldo Base del Usuario nuevo creado es    : ", SBase);
        print("El Bono del Usuario nuevo creado es           : ", Bono);
        print("El Suelo Liquido del Usuario nuevo creado es  : ", SLiqu);
        print("");


    Ingreso();
    Listar (); #se llama a la funcion listar
    Grabar ();

    print("");
    print("     Estoy fuera de la Funcion     ");
    print("\n\n\n")