#Repaso N°1 Instruccion 

#Ejercicio "Operaciones Matematicas Basicas simples"
#Ingrese 2 valores por teclado
#Luego el usuario determina que operacion desea realizar
#Si es una Suma, Resta, Multiplicacion o Division

#Limpiar Pantalla
from os import system
system ("cls");

#Definicion o declaracion de variables 
Val1 = 0;
Val2 = 0;
Respuesta  = 0;
Resultado  = 0;
Nombre     = "Bruno"
Asignatura = "Introduccion a la Programacion"
Seccion    = "Martes Tarde"
Profesor   = "Spiderman"



print("");
print(" .... Operaciones matematicas basicas ... ");
print("==========================================");

Val1 = int(input("Ingrese Valor 1 : "));                   #int es para hacer una operacion matematica 
Val2 = int(input("Ingrese Valor 2 : "));                   #input es para escribir despues de ejecutar 

#Menu de Opciones
print("");
print(" . . . Menu de Opciones . . . ");
print("==============================");
print(" 1.- Sumar Valores            ");
print(" 2.- Resta de Valores         ");
print(" 3.- Multiplicar Valores      ");
print(" 4.- Dividir Valores          ");
print(" 5.- Autor del Programa       ");

Respuesta=int(input("Ingrese opcion 1-5: "));

#Evaluar la respuesta ingresada por el usuario 

if(Respuesta == 1):
    Resultado =(Val1+Val2);
    print("");
    print(" . . . . Muesta de Datos . . . . . ");
    print("La Operacion fue Suma . . . . . . .");
    print("El Valor 1 ingresado fue . . . . . ", Val1);
    print("El Valor 2 ingresado fue . . . . . ", Val2);
    print("La suma de los 2 valores fue . . . ", Resultado);
    print("");


if(Respuesta == 2):
    Resultado =(Val1-Val2);
    print("");
    print(" . . . . Muesta de Datos . . . . . ");
    print("La Operacion fue Resta . . . . . . ");
    print("El Valor 1 ingresado fue . . . . . ", Val1);
    print("El Valor 2 ingresado fue . . . . . ", Val2);
    print("La suma de los 2 valores fue . . . ", Resultado);
    print("");

if(Respuesta == 3):
    Resultado =(Val1*Val2);
    print("");
    print(" . . . . Muesta de Datos . . . . . ");
    print("La operacion fue Multiplicacion . .")
    print("El Valor 1 ingresado fue . . . . . ", Val1);
    print("El Valor 2 ingresado fue . . . . . ", Val2);
    print("La suma de los 2 valores fue . . . ", Resultado);
    print("");

if(Respuesta == 4):
    Resultado =(Val1/Val2);
    print("");
    print(" . . . . Muesta de Datos . . . . . ");
    print("La Opercion fue Division . . . . . ");
    print("El Valor 1 ingresado fue . . . . . ", Val1);
    print("El Valor 2 ingresado fue . . . . . ", Val2);
    print("La suma de los 2 valores fue . . . ", Resultado);
    print("");

if(Respuesta == 5):
    print("")
    print("")
    print("=================================")
    print(" . . .Autor del programa . . . ")
    print(" Nombre     : . . . . . ", Nombre)
    print(" Asignatura : . . . ", Asignatura)
    print(" Seccion    : . . . . . ", Seccion)
    print(" Profesor   : . . . . .", Profesor)
    print("=================================")
    print("")
    print("")

