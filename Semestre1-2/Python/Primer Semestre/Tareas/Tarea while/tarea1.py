# Limpiar Pantalla
from os import system
system("cls")

#Deficion de variables
Cont    = 0;  
proceso = 1;
ContL   = 0;
Suma    = 0;

print("");
print("=======================")
print("Entrando al ciclo While");
print("");
print("Proesos del 1 al 50");
print("");

while(Cont <= 50):
    print("Contador N°{}: {}".format(proceso, Cont))
    Cont    = Cont    +5
    proceso = proceso +1
    ContL   = ContL   +1

print("");
print("Las lineas ejecutadas en total son: ", ContL);
print("");
print("Saliendo del ciclo While");
print("=======================")
print("");