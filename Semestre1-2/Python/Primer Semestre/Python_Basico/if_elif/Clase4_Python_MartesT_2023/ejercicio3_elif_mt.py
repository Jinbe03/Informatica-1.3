#Ejercicio 1 if - else

#la instruccion if else evalua 2 opciones V y F
#Lo primero que realiza esta instruccion es evaluar
#la opcion verdadera del if, y esta opcion no se cumple, recien pasa a ejecutar el else

#realice un programa en python que determine si la persona es mayor de edad
#datos a considerar: Rut, Nombre, Edad
#Dato: de los 21 años hacia arriba es mayor de edad

from os import system;
system("cls");

#declaracion de variables
Rut           = 0;
Nombre        = "";
Edad          = "";
EdadIngresada = ";"

print("")
print("")
print(" . . . Determina si la persona es mayor de edad . . . ");
print("======================================================");
print("")

#Ingreso de datos
Rut=input("Ingrese Rut de la persona. . . . . . : " );
Nombre=input("Ingrese Nombre de la persona . . . . : " );
Edad=int(input("Ingrese la edad . . . . . . . . . . : " ));

#Pregunta si EDAD es mayor a 21 años

if(Edad>=21):
    EdadIngresada ="Es Mayor de edad";

else:
    EdadIngresada="Es Menor de edad, es muy chico . . .";

print("")
print(" . . . Muestra de Datos . . . ");
print("==============================");
print("El Rut de la persona es es :  ",Rut);
print("El nombre de la persona es :  ",Nombre);
print("La edad de la persona es   :  ",Edad);
print("Y usted es                 :  ",EdadIngresada)
print("==============================");
print("")
