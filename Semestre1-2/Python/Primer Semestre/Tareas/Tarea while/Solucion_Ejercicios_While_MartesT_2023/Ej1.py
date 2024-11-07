#Solucion tarea ciclo while
#Tipo prueba n°3

#Realizeu n programa para 3 personas, debe ingresar los datos de cada persona:
#Rut,Nombre,Seccion,Valor1,Valor2,Resultado
#En el titulo debe mostrar el numero de la persona ingresada
#Los valores de deben sumar

#limpiar pantalla
from os import system
system("cls")

#definir o declarar las variables

Rutt      = "";
Nombre    = "";
Seccion   = "";
Valor1    = 0 ;
Valror2   = 0 ;
Resultado = "";
Cont      = 0 ;

print("\n\n") #Asigna 2 lineas en blanco

cont=1
while(cont<=3):
    print("======================================")
    print           ("Ingreso de datos n°: ", Cont)
    Rutt=input      ("Ingrese Rut        : ")
    Nombre=input    ("Ingrese Nombre     : ")
    Seccion=input   ("Ingrese Seccion    : ")
    Valor1=int(input("Ingrese Valor 1    : "))
    Valor2=int(input("Ingrese Valor 2    : "))

    print("______________________________________")
    #Proceso a realizar
    Resultado=(Valor1+Valor2)

    print("\n . . . Muestra de datos . . . ")
    print("Su Rut es                    : ", Rutt);
    print("Su Nombre es                 : ", Nombre);
    print("Su Sección es                : ", Seccion);
    print("El Valor 1 es                : ", Valor1);
    print("El Valor 2 es                : ", Valor2);
    print("El Resultado de la suma es   : ", Resultado);
    print("La suma de ",Valor1 , "+" ,Valor2 , " = ", Resultado);
    Cont=Cont+1
    print("======================================\n")

print("\n\n . . . Saliendo del ciclo While . . . \n\n")
    