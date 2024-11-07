#Ejercicio 1 ciclo for
#Ciclo repetitivo for ( for = para)

#Realice un programa que repita 5 procesos cualquiera y que muetre el numero de procesos a realizar

#limpiar pantalla
from os import system
system("cls")


print("")
print(" . . . Ejemplo Repetir con ciclo FOR 1 . . . ")
print("=============================================")
print("");

#ejemplo n°1 con tres argumentos, inicia en 1, se repite 5 veces el proceso de 1 en 1
for i in range(1, 6 ,1):
    print(i, end=", ")#print: 1, 2, 3, 4, 5,
    #print(i);

print("\n\n")
print("=============================================")
print("\n")

#Ejemplo n°2 con dos argunmentos, inicia en 1, repite 3 veces el proceso, y por defecto
for i in range (1, 4):
    print(i, end=", ")
    #print(i)

print("\n\n")
print("=============================================")
print("\n")
#Ejemplo N°3 con argumento, Inicia en 0, repite 7 veces el proceso y por defecto va 1 en 1.
for i in range(7):
    print(i, end=", ")
    #print(i)

print("\n\n")
print("=============================================")
print("\n")

