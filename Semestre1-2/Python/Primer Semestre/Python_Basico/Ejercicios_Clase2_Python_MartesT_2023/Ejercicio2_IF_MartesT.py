#Ejerecicio N°2 Python
#   Instruccion IF
#   Ingreso de datos por telcado

#Realize un programa que controle las ventas de un supermercado
#para lo cual debe considerar los siguientes datos:
#Datos: Producto, Marca, Valor Unitario, Cantidad, Total, Dcto y Total Pagar

#Importante:
#Los datos que no calculen se debe ingresar por teclado
#Las ventas mayores a 100.000 tienen un descuento de 10%
#Las ventas mayores a 200.000 tienen un descuento de 20%

#Limpiar Pantalla
from os import system
system ("cls");

#Declaracion de Variables
Prod = "";
Marc = "";
ValU = 0;
Cant = 0;
Tot1 = 0;
Dcto = 0;
TotP = 0; 


#Calculo del Total sin Descuento
Tot1=(ValU*Cant);

#Calculo del 10% o el 20%
if(Tot1 >1 and Tot1 <100000):
    Dcto=0;
    TotP=(Tot1-Dcto);

if(Tot1>=100000 and Tot1 <200000):
    Dcto=(Tot1*100)/100;
    TotP=(Tot1-Dcto);

if(Tot1>=200000):
    Dcto=(Tot1*20)/100;
    TotP=(Tot1-Dcto);

#Ingreso de datos por teclado
print("");
print("");

print("=======================================");
print("........... Ingreso de Datos ..........");
print("=======================================");

Prod=input("Ingrese Producto.................");
Marc=input("Ingrese Marca ...................");
ValU=int(input("Ingrese el Valor Unitario.........."));   #int= le quita las comillas al N° Ingresado
Cant=int(input("Ingrese la Cantidad ..............."));   #int= le quita las comillas al N° Ingresado

print("=======================================");
print("........... Muestra de Datos ..........");
print("=======================================");


print("El Produto comrpado es................", Prod);
print("La Marca del producto es..............", Marc);
print("El Valor Unitario de producto es .....", ValU);
print("La cantidad de productos comprados es.", Cant);
print("El Total sin Dcto es de ..............", Tot1);
print("El descuento aplicado es .............", Dcto);
print("El Total Final a pagar es.............", TotP);