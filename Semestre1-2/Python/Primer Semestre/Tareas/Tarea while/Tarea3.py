# Limpiar Pantalla
from os import system
system("cls")

#Deficion de variables
Cont    = 70;  
proceso = 1;
ContL   = 0;
Suma    = 0;

print("");
print("=======================");
print("Entrando al ciclo While");
print("");
print("Proesos del 70 al 1");
print("");

while(Cont >= 0):
    Suma+=Cont
    print("Contador N°{}: {}, Suma: {}".format(proceso, Cont, Suma))
    Cont    = Cont    -1
    proceso = proceso +1
    ContL   = ContL   +1

print("");
print("Las lineas ejecutadas en total son: ", ContL);
print("");
print("Saliendo del ciclo While");
print("=======================");
print("");