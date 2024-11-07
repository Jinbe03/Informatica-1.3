#           Ejercicio n°2
#             Ciclo While

#Realice un programa utilizando ciclo while que imprima por pantalla los numeros del 4 al 15
#debe utilizar un contador.

# Limpiar Pantalla
from os import system
system("cls")

#Deficion de variables
Cont = 5;  #dependiendo del numero es donde empezara el contador

print("");
print("Entrando al ciclo While");
print("");

while(Cont <= 15):
    print("El valor del contador es: ", Cont)
    Cont = Cont + 1;

print("");
print("Saliendo del ciclo While");
print("")