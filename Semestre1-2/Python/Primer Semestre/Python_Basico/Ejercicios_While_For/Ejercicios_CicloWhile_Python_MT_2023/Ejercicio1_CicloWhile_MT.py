#           Ejercicio n°1
#             Ciclo While

#Realice un programa utilizando ciclo que se repita 5 veces, debe utilizar un contador.

# Limpiar Pantalla
from os import system
system("cls")

#Deficion de variables
Cont = 1;
print("");
print("Ejemplo basico ciclo while");
print("");

while(Cont <= 5):
    print("El valor del contador es: ", Cont)
    Cont = Cont + 1; #Incrementa el contador de1 en 1 

print("");
print("Ahora estoy fuera del ciclo while");
print("")