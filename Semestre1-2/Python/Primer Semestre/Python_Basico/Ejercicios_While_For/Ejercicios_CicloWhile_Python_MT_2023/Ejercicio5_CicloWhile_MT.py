#           Ejercicios N°5
#            Ciclo While

#Realize un pgroama utilizando ciclo whine que entregue la siguiente informacion
#El programa debe realizar los procesos del 20 al 5
#Imprima el valor del proceso
#Imprima el valor del contador while
#Imprima la cantidad de proceso que realizo el programa 

# Limpiar Pantalla
from os import system
system("cls")

#Deficion de variables
Cont    = 20;  
proceso = 1;
ContL   = 0;

print("");
print("Entrando al ciclo While");
print("");
print("Proesos del 20 al 5");
print("");

while(Cont >= 5):
    print("Contador N°{}: {}".format(proceso, Cont))
    Cont    = Cont    -1
    proceso = proceso +1
    ContL   = ContL   +1

print("");
print("Las lineas ejecutadas en total son: ", ContL);
print("");
print("Saliendo del ciclo While");
print("");