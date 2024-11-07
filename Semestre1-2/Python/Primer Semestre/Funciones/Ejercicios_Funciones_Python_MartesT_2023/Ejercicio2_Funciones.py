#Ejemplo 2 de Funciones
#Realiceu n progama en python utilizando funciones
#El programa debe calcular el valor de una factura
#Datos a considerar: Producto, Cantidado, ValorProducto y Total
#Utilize a lo menos 2 funciones


#limpiar pantalla
from os import system
system("cls")

#Variables
Prod   = ""
Cantt  = 0
ValorP = 0
Total  = 0

print("\n\n")
print("===========================================")
print("       Ingreso de datos de la factura       ")
print("===========================================")

#Funcion IngresoDatos
def IngresoDatos():
    global Prod
    global Cantt
    global ValorP
    Prod = input("Ingrese Producto de la factura : ")
    Cantt=int(input("Ingrese cantidad del producto  : "))
    ValorP=int(input("Ingrese Valor de cada producto : "))

#Funcion que muestra los datos
def MuestraDeDatos():
    print("")
    print("=====================================")
    print("     Muestra de datos en funcion     ")
    print("=====================================")
    print("El Producto de la factura es : ", Prod)
    print("La Cantidad del producto es  : ", Cantt)
    print("El valor del produto es      : ", ValorP)
    print("El total de la factura es    : ", Total)
    print("=====================================")
    
#Inicio del programa
IngresoDatos(); #Se llama a la funcion ingresodatos

Total = (Cantt * ValorP )

MuestraDeDatos(); #Se llama a la funcion MuestraDeDatos

print("");
print("    Ahora estoy fuera de las funciones   ");
print("\n\n")