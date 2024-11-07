# Ejemplo 3 funciones
#Funcion con retorno de valores o retorno de parametros

from os import system 
system ("cls");

print("");
print("    Ejemplo 1 Funciones con retorno de parametros    ");
print("");

#Definicion de Valores
#Num1 y Num2 son los argumento o parametros de la funcion

def Valores(a, b, r ):
    Result = (a + b + r)
    print("La suma es :  ", Result);
    print("La suma es :  ", a + b + r);

def Valores2( x,a ):
    Result = ( x * a);
    print("El VBalor de la Variable X es ", x);
    print("El VBalor de la Variable A es ", a);
    print("");
    print("La Multiplicacion es :  ", Result);
    print("La Multiplicacion es :  ", (x * a));

#Llamo a la funcion y le mando los valores o argumentos
#a la funcion a las variables A, B, R respectivamente

Valores(10,20,55); #Se llama funcion Valores y se le envian 3 valores

print("")
print("====================")