#Ejemplo N°3 de funciones 
#funciones basicas

#realice un programa en pyton utilizando funciones
#realice un programa menu que llame a otro menu

#limpiar pantalla
from os import system
system("cls")

#Inicializacion de variables 
Opc = 0 #Se inicializa la variable Opc que recibira las opciones del menu

print("\n\n")

def MenuPrincipal():
    while( Opc < 1 or Opc > 4 ):
        print("     Menu Operaciones Basicas    ")
        print("1.- Sumas Valores         ")
        print("2.- Restar Valores        ")
        print("3.- Multiplicar Valores   ")
        print("4.- Dividir Valores       ")
        print("5.- Autor                 ")
        Opc=int(input("Ingrese opcion (1-5) : "))
        print("");

# . . . Usted Continua . . .

