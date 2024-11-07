#if-else
# (si - de lo contrario)

#Realize un programa en python que determine si la persona es hombre o mujer
#Si es hombre debe ingresar: Nombre, Cargo, Antiguedad y Sueldo
#Si es mujer debe ingresar: Nombre, Estado Civil, Edad y Numero de hijos

#Limpiar Pantalla
from os import system
system ("cls");

#Definir variables del programa

Persona    ="";
Nombre     ="";
Cargo      ="";
TipoPersona="";
Antiguedad =0;
Sueldo     =0;
ContH     =0;

EstadoCivil ="";
Edad        = 0; 
NumeroHijos = 0;
ContM      = 0;

print(""); #Se asigna una linea en blanco
print(""); #Se asigna una linea en blanco,

persona =input(" ... Ingrese el Generro de la persona ... ");
print("") #Se asigna una linea en blanco

#Pregunta si la persona es hombre o mujer.
if(Persona=="Mujer" or Persona =="mujer" or Persona=="MUJER"):
    ContM=ContM+1;
    TipoPersona="Mujer";
    print(""); #Se asigna una linea en blanco
    print(" ........ Ingreso de Datos de la mujer ........");
    print("===============================================");
    print=(input("Nombre de la Persona.......................: ", Nombre));
    print=(input("Ingrese el Estado Civil....................:", EstadoCivil));
    print=(input("Ingrese Edad...............................: ", Edad));
    print=(input("Ingrese Numero de Hijos....................: ", NumeroHijos));

    print(""); #Se asigna una linea en blanco

    print(" ........ Muestra de Datos de la mujer ........");
    print("===============================================");
    print("La Cantidad de Mujeres es .....................: ", ContM);
    print("El Genero de la persona es ....................: ", TipoPersona);
    print("El Nombre de la Mujer es ......................: ",Nombre);
    print("El Estado Civil de la Mujer es ................: ", EstadoCivil);
    print("La Edad de la Mujer es ........................: ", Edad);
    print("El Numero de Hijos que tiene es ...............: ",NumeroHijos);

print("") #Se asigna una linea en blanco

if (Persona == "HOMBRE" or Persona == "hombre" or Persona == "Hombre"):
    ContH+ContH+1;
    TipoPersona="Hombre";

    print(""); #Se asigna una linea en blanco
    print(" ........ Ingreso de Datos del Hombre ........ ");
    print("===============================================");
    print=(input("Nombre de la Persona.......................: ", Nombre));
    print=(input("Ingrese el Cargo .......................: ", Cargo));
    print=(input("Ingrese la Antiguedad...................: ", Antiguedad));
    print=(input("Ingrese el Sueldo.......................: ", Sueldo));

print(""); #Se asigna una linea en blanco

print(" ........ Muestra de Datos de la mujer ........");
print("===============================================");
print("La Cantidad de Hombres es ....................: ", ContH);
print("El genero de la persona es ...................: ", TipoPersona);
print("El Nombre del Hombre es ......................: ", Nombre);
print("El Cargo del Hombre es .......................: ", Cargo);
print("La Antiguedad trabajando es ..................: ", Antiguedad);
print("El Sueldo del Hombre es ......................: ", Sueldo);