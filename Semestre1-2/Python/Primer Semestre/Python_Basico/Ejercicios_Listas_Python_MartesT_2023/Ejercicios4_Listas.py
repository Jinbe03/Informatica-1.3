#          EJERCICIO N°4 LISTAS

#Ejercicio que pregunta cuantos datos desea que tenga la lista

from os import system 
system ("cls")

#Inicializacion de variables
Numm = 0; #Se inicializa la variable "Numm"
Ciu  = ""


print("")
print("         Ejemplo N°4 de Listas         ")
print("")

#Se crea una lista vacia llamada ciudades
Ciudades=[]

Numm = int(input("Cuantos elementos desea que tenga la lista?  : "))
print("")


for i in range (Numm):
    Ciu=input("Ingrese Ciudad : ")
    Ciudades.append(Ciu); #append = agrega un espacio en blanco al final de la lista

print("")
print("Las ciudades que se ingresaron a la lista son : ", Ciudades)
print("")