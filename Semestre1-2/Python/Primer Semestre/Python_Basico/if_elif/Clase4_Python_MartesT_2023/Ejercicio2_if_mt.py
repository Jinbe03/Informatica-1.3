#Ejercicio N°2 if
#Practica de la estrucutra del control if

#Realice un programa utilizando if, que busque y diga que color es el seleccionado por el usuario

#como se realiza una pregunta en python
#if = se utiliza para realizar una pregunta en un programa

#Limpiar Pantalla
from os import system
system ("cls");

#Declara o definir las variables
Color = "";

print("");
print("");
print(" . . . . . . . . . . Seleccione un Color . . . . . . . . . . ");
print("=============================================================");

Color = input("Ingrese el color . . . . :")

if(Color=="Rojo" or Color=="ROJO" or Color=="rojo"):
    print("Ud. ha seleccionado Rojo y tambien ingreso el Color: ", Color);
    print("=============================================================");
    print("");

if(Color=="Verde" or Color=="VERDE" or Color=="verde"):
    print("Ud. ha seleccionado Verde y tamien ingreso el Color: ",Color)
    print("============================================================")
    print("");

if(Color=="Azul" or Color=="AZUL" or Color=="azul"):
    print("Ud. ha seleccionado Azul y tambien ingreso el Color: ", Color)
    print("=============================================================")
    print("");


else:
    print("")
    print("===============================================")
    print(" . . . No esta el color que usted buscar . . . ")
    print("===============================================")
    print("")
