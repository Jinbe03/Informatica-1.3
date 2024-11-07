#            EJERCICIO N°2 LISTAS

#Ejemplo de lista vacia, sin datos
#Realice un ejercicio donde el usuario ingrese valores por teclado,
#y cada uno de estos valores se almacene en una lista vacia.
#El usuario puede ingresar los valores que quiera, hasta que ingrese 
#el valor cero "0"

from os import system
system ("cls")

#Inicializacion de variables
Valor  = 0 #Se inicializa la variable "Valor"

print("\nEjemplos de la lista 2\n")

Lista1 = []
#Ingreso de valores por teclado del usuario 
Valor = int(input("Ingrese un valor cualquiera : "))

#El while se ejectua mientras el usuario ingrese un valor distinto a cero "0"
while (Valor !=0):
    Lista1.append(Valor)
    Valor=int(input("Continue ingresando valores : "))

print("")
print("estoy fuera del ciclo while y la lista")
print("")

print("La lista se lleno con los siguientes valores : ",Lista1)
print("La cantidad de datos que tiene la lista es   : ",len(Lista1))
print("")