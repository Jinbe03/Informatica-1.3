#Realize un programa para 3 alumnos
#Datos del alumno: Rut, Nombre, Asignatura y promedio

from os import system
system("cls");

#Deficinion o declaracion de variables 
Rut        = ""
Nombre     = ""
Asignatura = ""
Promedio   = ""

print("\n\n")

for a in range(1,4,1):
    print("--- Ingreso de Datos ---")
    Rut=input       ("Ingrese Rut del Alumno      : ")
    Nombre=input    ("Ingrese Nombre del Alumno   : ")
    Asignatura=input("Ingrese Asignatura          : ")
    Promedio=input  ("Ingrese Promedio del Alumno : ")
    print("")
    print(". . . Muestra de Datos N°",a," . . .")
    print("============================")
    print("El Rut del Alumno es    : ", Rut)
    print("El Nombre del Alumno es : ", Nombre)
    print("La Asignatura es        : ", Asignatura)
    print("El Promedio es          : ", Promedio) 
    print("")

print("")
print(". . . Saliendo del Ciclo For . . .")
print("\n\n")