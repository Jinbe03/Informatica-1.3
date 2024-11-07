# Ejemplo 2 Funciones
#Funcion con retorno de valores o retorno de parametros

#Realice un programa que calcule el valor del pasaje de Santiago a Paris
#Datos a considerar: Rut, NombrePasajero, Destino, ValorPasaje, Cantidad de pasaje y Total

#Realice una funcion para calcular el total, esta funcion debe recibir 2 parametros
#los necesarios para calcular el Total


from os import system
system("cls")


#Definicion de variables
RutPa  = ""
NomPa  = ""
Dest   = ""
ValPa  = 0
CantPa = 0
Total  = 0

#Se crea la funcion CalculoTotal
def CalculoTotal (VP, CP):
    Total = (VP * CP) #Se calcula el total del viaje
    print("")
    print("                  Muestra de Datos                  ")
    print("=====================================================")
    print("El Rut del Pasajero es                :", RutPa)
    print("El Nombre del Pasajero es             :",NomPa)
    print("El Pasajero viaja a                   :",Dest)


    print("El Valor del pasaje es                :",VP);
    print("La cantidad del pasaje es             :",CP);
    print("")
    print("El total del viaje es                 :",Total);
    print("El total pagar del viaje es           :",VP * CP);
    print("=====================================================")

print("")
print("Ejemplo N°2 con retorno de valores o parametros")
print("")

print("                  Ingreso de Datos                  ")
print("=====================================================")
RutPa  =     input("Ingrese el Rut del Pasajero           : ")
NomPa  =     input("Ingrese el Nombre del Pasajero        : ")
Dest   =     input("Ingrese el Destino del Pasajero       : ")
ValPa  = int(input("Ingrese Valor del Pasaje              : "))
CantPa = int(input("Ingrese Cantidad de Pasajes           : "))

#Se llama a la funcion y se envian
CalculoTotal(ValPa,CantPa);
