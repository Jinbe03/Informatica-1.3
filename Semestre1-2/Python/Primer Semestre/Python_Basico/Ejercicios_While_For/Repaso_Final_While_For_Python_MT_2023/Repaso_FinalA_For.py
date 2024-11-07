#           Ejercicio Final
#       Ciclo Repetitivo For
#           if - else

#realize un programa en python utilizando ciclo For
#realize un prgorama para controlar el arriendo de vehiculos.
#el programa es solamete para 3 arriendos.
#Datos a considerar: Rut, Tipo Vehiculo(auto, camion, camioneta), valor arriendo dia, n° de dias a arrendar
#Total, Dcto, Total pagar.

#Dscto: Si total >= 100.000, se aplica 10% Dcto del total

#Limpiar pantalla
from os import system
system("cls")

#Variables
Rut    = ""
TipoV  = 0
Aviso  = ""
Valor  = 0
ValorD = 0
Total  = 0
Dcto   = 0
TotalP = 0
#Cont   = 0

Cont = 1
print("\n\n")
for x in range (1,4,1):
    print("=======================================")
    print("           Ingrese Datos N°",x,"           ")
    print("=======================================")
    Rut=input ("Ingrese Rut                          : ")
    TipoV=input("Ingrese tipo de Vehiculo             : ")
    Valor=int(input("Ingrese el valor diario del Arriendo : "))
    ValorD=int(input("Ingrese N° Dias de Arriendo          : "))

    #Calculo del Total
    Total = (Valor*ValorD)

    #Calculo del 10% Dcto.
    if(Total>=100000):
        Aviso = "Se ha Realizado un 10% de Descuento";
        Dcto  =( Total * 10)/100;
        TotalP=( Total - Dcto);
    else:
        Aviso  = "No Aplica Descuento";
        Dcto   = 0;
        TotalP = ( Total - Dcto);

    print("\n")
    print("======================================")
    print("          Muestra de Datos            ")
    print("======================================")
    print("El Rut del Cliente es                : ",Rut)
    print("El Tipo de Vehiculo elejido es       : ",TipoV)
    print("El Valor diario de arriendo es       : ",Valor)
    print("La cantidad de dias arrendados son   : ",ValorD)
    print("El total del arriendo es             : ",Total)
    print("Aplica o no a descuento              : ",Aviso)
    print("El descuento es de                   : ",Dcto)
    print("El total a pagar final es de         : ",TotalP)
    print("======================================")

    #Cont=Cont+1 #Incrementa el ciclo For

    print("\n Saliendo del ciclo For \n\n\n")