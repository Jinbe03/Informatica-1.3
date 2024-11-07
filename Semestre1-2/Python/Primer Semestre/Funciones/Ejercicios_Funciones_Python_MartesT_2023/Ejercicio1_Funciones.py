#Ejemplo 1 de Funciones
#Ejemplo de funcion basicas y simples o sin retorno o sin parametros

#Realice un programa menu en python validando el menu en ciclo while y utilizando funciones
#en la muestra de datos 
#la funcion se realiza una sola vez y se puede ejecutar las veces que sean necesarias

#Realiza un programa con 5 opciones
#el menu debe mostrar las 4 operaciones basica mas el autor
#debe ingresar dos datos por teclado para las operaciones
#Valide el menu con cilo while
#muestr los datos en una funcion simple


#limpiar pantalla
from os import system
system("cls")

#Variables
Opc       = 0 #Se inicializa la variable Opc que recibira las opciones del menu
Val1      = 0 
Val2      = 0
Result    = 0
Operacion = 0

print("");
print("        Ejemplo N°1 de Funciones        ");
print("");

while( Opc < 1 or Opc > 5):
    print("           Menu Principal           ");
    print("==================================");
    print("    1.- Sumar Valores             ");
    print("    2.- Restar Valores            ");
    print("    3.-Multiplicar Valores        ");
    print("    4.-Dividir Valores            ");
    print("    5.-Autor del Programa         ");
    print("");
    Opc=int(input("   Ingrese Opción (1-5) : "));
    print("");


#Se crea la funcion MostrarDatos
def MostrarDatos():
    print("")
    print("                Muestra de Datos                ")
    print("================================================")
    print("La operacion seleccionada es    : ",Operacion)
    print("El Valor 1 ingresado fue        : ",Val1 )
    print("El Valor 2 ingresado fue        : ",Val2 )
    print("El Resultado de la operacion es : ",Result)
    print("================================================")
    print("");

if(Opc==1):
    Operacion = ("Sumar")
    Val1=int(input("Ingrese Valor 1 : "));
    Val2=int(input("Ingrese Valor 2 : "));
    Result = (Val1+Val2)
    print("==================================");
    MostrarDatos();#Se llama a la funcion MostarDatos

if(Opc==2):
    Operacion = ("Restar")
    while( Val1 < Val2 ):
        print("")
        print("    Error, el valor 1 debe ser >= Valor2 para poder restarlos : ", Val1)
        print("")
        Val2=int(input("Ingrese el valor 2 nuevamente : "))
        print("")
    Val1=int(input("Ingrese Valor 1 : "));
    Val2=int(input("Ingrese Valor 2 : "));
    Result = ( Val1 - Val2 )
    print("==================================");
    MostrarDatos();#Se llama a la funcion MostarDatos

if(Opc==3):
    Operacion = ("Multiplicar")
    Val1=int(input("Ingrese Valor 1 : "));
    Val2=int(input("Ingrese Valor 2 : "));
    Result = ( Val1 * Val2 )
    print("==================================");
    MostrarDatos();#Se llama a la funcion MostarDatos


if(Opc==4):
    Operacion = ("Dividir")
    Val1=int(input("Ingrese Valor 1 : "));
    Val2=int(input("Ingrese Valor 2 : "));
    Result = ( Val1 / Val2 )
    print("==================================");
    MostrarDatos();#Se llama a la funcion MostarDatos

if(Opc==5):
    Operacion = ("Autor")
    Autor  = "Alumnos MartesT"
    Asig   = "Introd. a la programacion"
    Secc   = "MNartes Tarde"
    Prof   = "Juan Perez"   
    print("                Muestra de Datos                ")
    print("================================================")
    print("El Nombre del autor es           : ", Autor)
    print("La Asignatura es                 : ", Asig)
    print("La seccion es                    : ", Secc)
    print("El profesor es                   : ", Prof)
    print("================================================")
    print("");
