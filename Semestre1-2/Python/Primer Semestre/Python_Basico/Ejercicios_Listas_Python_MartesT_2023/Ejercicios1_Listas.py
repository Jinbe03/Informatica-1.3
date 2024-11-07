#       Ejercicios N°1 Listas

#Ejemplo de lista vacia, sin datos
#Realice un ejercicio donde el usuario ingrese 5 valores por teclado
#y cada uno de estos valores se almacene en una lista vacia

from os import system
system ("cls")

#Inicializacion de variables
i    = 0;    #Se inicializa la variable "i" del ciclo while
Numm = 0;    #Se inicializa la variable "Numm"


print("");
print("            Ejemplo de Listas            ");
print("");


#Se crea la lista vacia llamda Lista1
Lista1 = []

i=1;

while (i <=5):
    #Ingreso de valores por teclado del usuario
    Numm=int(input("Ingrese un valor cualquiera: "))

    #Se llena la lista con los valores ingresados por el usuario
    Lista1.append(Numm); #append = agrega un elemento al final de la lista
    print("")
    i +=1

print("")
print("estoy fuera de while y de la lista")
print("")

print("La lista se lleno con los siguientes Valores : ",Lista1)
print("La cantidad de datos que tiene la lista es   : ",len(Lista1))
print("")