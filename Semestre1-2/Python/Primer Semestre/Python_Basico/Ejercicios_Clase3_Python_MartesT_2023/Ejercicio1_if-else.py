#    ejercicio N°1
#     if-else
#      (Si - De lo contrario)

#Realize un programa en python que calcule las ventas de ropa de una tienda
#Datos a considerar:
#     Rut Cliente, Nombre Cliente, Producto, Valor Producto, Cantidad, Total, Dcto, Total Pagar.
#Datos: Los datos se deben ingresar por teclado

#Limpiar Pantalla
from os import system
system ("cls");

#Definir las variables del programa

RutC = "";
NomC = "";
Prod = "";
ValP = 0;
Cant = 0;
Total= 0;
Dcto = 0;
TotP = 0;
ContMA= 0;
ContME= 0;

print("");  #Asigna una linea en blanco
print("");  #Asigna una linea en blanco

print(" .............. Inreso de Datos .............. ");
print(" ============================================= ");
RutC=input("Ingrese rut del cliente.................: ");
NomC=input("Ingrese Nombre del cliente..............: ");
Prod=input("Ingrese Producto a Comprar..............: ");
ValP=int(input("Ingrese Valor del producto..............: "));
Cant=int(input("Ingrese cantidad de productos a comprar.: "));

#Calculo del Total
Total=(ValP*Cant);

#Calculo del Descuento
if (Total>=100000):
    ContMA=ContMA+1
    Dcto=(Total*10)/100;
    TotP=(Total-Dcto);
else:
    ContME=ContME+1
    Dcto=0;
    TotP=(Total-Dcto);

print("");  #Asigna una linea en blanco
print("");  #Asigna una linea en blanco

print(" .............. Muestra de Datos .............. ");
print(" ============================================== ");
print("El Rut del cliente es.........................: ", RutC);
print("El Nombre del Cliente es .....................: ", NomC);
print("El Producto comprado fue .....................: ", Prod);
print("El Valor Unitario del producto es ............: ", ValP);
print("La Cantidad de Productos comprados fue .......: ", Cant);
print("El total de la compra fue ....................: ", Total);
print("El Descuento aplicado fue ....................: ", Dcto);
print("El Total a Pagar es ..........................: ", TotP);

print("");  #Asigna una linea en blanco
print("");  #Asigna una linea en blanco