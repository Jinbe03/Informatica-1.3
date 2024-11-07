#Ejercicio 3
#Validar resta de n°
#Este ejemplo se realiza con ciclo repetitivo For

#Realice un programa que permita ingresar 2 valores por teclado
#Estos valores se deben restar
#Valide la resta que el valor1>= al valor2 para poder restarlos

from os import system
system("cls")

Val1      = 0
Val2      = 0
Resultado = 0

print("\n\n")
print("============================================")
print(" . . . Validacion al restar 2 valores . . . ")
print("")
Val1=int(input("Ingrese Valor 1   : "))
Val2=int(input("Ingrese Valor 2   : "))
print("============================================")
while(Val1 <= Val2 ):
    print("")
    print("_______________________________________________________________")
    print("Error, El Valor 1 debe ser >= Valor2 para poder restarlos: ", Val1)
    print("")
    Val2=int(input("Ingrese el Valor 2 nuevamente :"))
    print("_______________________________________________________________")
    print("")

Resultado=(Val1 - Val2)


print("=======================================")
print(". . . Muestra de Datos . . .")
print("El Valor 1 ingreaado es        : ", Val1)
print("El Valor 2 ingresado es        : ", Val2)
print("El Resusltado de", Val1, "-" , Val2," es    : ", Resultado,)
print("=======================================")
print("\n\n")