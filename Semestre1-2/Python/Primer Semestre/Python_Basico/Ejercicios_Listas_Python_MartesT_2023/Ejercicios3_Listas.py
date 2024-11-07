#           EJERCICIO N°3 LISTAS

#Ejemplo de lista con datos ya ingresados predefinidamente

from os import system
system("cls")

print(" _____________________________________________")
print("|                                             |")
print("|            EJEMPLO N°3 DE LISTAS            |")
print("|_____________________________________________|")

#se crea la lista con datos alfanumericos
NombresVarios =['JPerez','MSoto','RPino','CToro'] #4 nombres = 4 elementos

#Se crea una lista con daatos Alfanumericos
Asignaturas = ['Asig1','Asig2','Asig3']

#Se crea la lista con datos numericos
Promedios = [44,55,35,65]

print("")
print("===========================================================================================")
print("")
print("            Muestra de datos de las Listas            ")
print("Muestra toda la lista alfanumerica : ",NombresVarios)
print("Muestra de la Lista Alfanumerica   : ",Asignaturas)
print("Muestra de la lista Numerica       : ",Promedios)
print("")
print("===========================================================================================")
print("")
print("            Muestra de datos de una lista por su indice            ")
print("Muestra el primer  elemento de la lista o indice = 0   : ",NombresVarios[0])
print("Muestra el segundo elemento de la lista o indice = 1   : ",NombresVarios[1])
print("Muestra el tercer  elemento de la lista o indice = 2   : ",NombresVarios[2])
print("Muestra el cuarto  elemento de la lista o indice = 3   : ",NombresVarios[3])
print("")
print("===========================================================================================")
print("")
print("            Muestra de datos de una lista por su indice            ")
print("Muestra el primer  elemento de la lista o indice = 0   : ",Promedios[0])
print("Muestra el segundo elemento de la lista o indice = 1   : ",Promedios[1])
print("Muestra el tercer  elemento de la lista o indice = 2   : ",Promedios[2])
print("Muestra el cuarto  elemento de la lista o indice = 3   : ",Promedios[3])
print("")
print("===========================================================================================")
print("")
print("            Muestra de datos de una lista por su indice            ")
print("El Alumno 1 es :",NombresVarios[0], "y su promedio es :",Promedios[0])
print("El Alumno 2 es :",NombresVarios[1], " y su promedio es :",Promedios[1])
print("El Alumno 3 es :",NombresVarios[2], " y su promedio es :",Promedios[2])
print("El Alumno 4 es :",NombresVarios[3], " y su promedio es :",Promedios[3])
print("")
print("===========================================================================================")