#       Ejercicio N°3
#Realize un programa utilizando ciclo While que imprima los numeros del 50 al 80 de 2 en 2


# Limpiar Pantalla
from os import system
system("cls")

#Deficion de variables
Cont = 50;  #dependiendo del numero es donde empezara el contador

print("");
print("Entrando al ciclo While");
print("");

while(Cont <= 80):
    print("El valor del contador es: ", Cont)
    Cont = Cont + 2;

print("");
print("Saliendo del ciclo While");
print("")