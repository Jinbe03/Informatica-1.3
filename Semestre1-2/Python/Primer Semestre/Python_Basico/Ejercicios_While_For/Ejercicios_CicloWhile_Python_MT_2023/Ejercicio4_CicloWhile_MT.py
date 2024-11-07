#           Ejemplo n°4
#            Realize un programa utilizando ciclo While

#El programa debe realizar los procesos del 10 al 25
#Imprima el valor del contador en cada proceso
#Imprima la cantidad de procesos que realizo el programa
#Imprima el total de proceso acumulados en el programa

# Limpiar Pantalla
from os import system
system("cls")

#Deficion de variables
Cont    = 10;  #dependiendo del numero es donde empezara el contador
proceso = 1;
ContL   = 0;

print("");
print("Entrando al ciclo While");
print("");
print("Proesos del 10 al 25");
print("");

while(Cont <= 25):
    print("Contador N°{}: {}".format(proceso, Cont))
    Cont    = Cont    +1
    proceso = proceso +1
    ContL   = ContL   +1

print("");
print("Las lineas ejecutadas en total son: ", ContL);
print("");
print("Saliendo del ciclo While");
print("");