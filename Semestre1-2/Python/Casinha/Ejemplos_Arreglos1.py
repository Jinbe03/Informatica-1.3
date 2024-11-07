from os import system
system("cls")

#Arreglos

n = int(input(' Ingrese el numero de Arreglos    : '))
m = int(input(" Ingrese la cantidad de Arreglos  : "))

A = []
for i in range (0,n):
    A.append(i*m)

print(A)