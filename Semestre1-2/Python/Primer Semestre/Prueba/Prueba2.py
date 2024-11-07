# Limpiar Pantalla
from os import system
system("cls")

# Definición o declaración de variables
Rut = 0
Producto = ""
Fecha = 0
Valor = 0
Cantidad = 0
Total = 0
Dcto = 0
TotalP = 0
MetodoP = ""

print(". . . . . Método de Pago . . . . .")
print("==========================================")
Rut = input("Ingrese Rut del Cliente . . . . . . . . . . . . . .: ")
Producto = input("Ingrese Producto . . . . . . . . . . . . . . . . .: ")
Fecha = input("Ingrese Fecha de compra . . . . . . . . . . . . . : ")
Valor = float(input("Ingrese Valor de la compra . . . . . . . . . . . .: "))
Cantidad = int(input("Ingrese la cantidad de productos . . . . . . . . .: "))
print("")

# Calcular Total
Total = Valor * Cantidad

# Determinar forma de pago
print("==========================================")
print("Seleccione la forma de pago:")
print("1. Efectivo")
print("2. Tarjeta")
print("3. Cheque")

opcion = int(input("Ingrese el número de opción: "))
print("==========================================")

if opcion == 1:
    TotalP = Total * 0.9  # Aplicar descuento del 10%

    if TotalP > 100000:
        TotalP = TotalP * 0.95  # Aplicar descuento adicional del 5%

    if TotalP > 500000:
        TotalP = TotalP * 0.9  # Aplicar descuento adicional del 10%

    if TotalP > 800000:
        TotalP = TotalP * 0.85  # Aplicar descuento adicional del 15%

elif opcion == 2:
    print("==========================================")
    print("Seleccione el tipo de tarjeta:")
    print("1. Banco")
    print("2. Tienda")
    print("3. Supermercado")
    tarjeta = int(input("Ingrese el número de opción: "))
    print("==========================================")

    if tarjeta == 1:
        TotalP = Total * 0.95  # Aplicar descuento del 5%

        if TotalP >= 100000 and TotalP <= 200000:
            TotalP = TotalP * 0.9  # Aplicar descuento adicional del 10%

        elif TotalP > 200000 and TotalP <= 400000:
            TotalP = TotalP * 0.85  # Aplicar descuento adicional del 15%

        elif TotalP > 400000:
            TotalP = TotalP * 0.8  # Aplicar descuento adicional del 20%

    elif tarjeta == 2:
        TotalP = Total  # No se aplica descuento inicial

        if TotalP > 200000:
            TotalP = TotalP * 0.9  # Aplicar descuento del 10%

        if TotalP > 400000:
            TotalP = TotalP * 0.85  # Aplicar descuento adicional del 15%

    elif tarjeta == 3:
        TotalP = Total * 1.1  # Aplicar interés del 10%
        print("==========================================")
        cuotas = int(input("Ingrese la cantidad de cuotas: "))
        print("==========================================")
        if (cuotas >= 5 and cuotas <= 10):
            TotalP = TotalP * 1.1  # Aplicar interés adicional del 10%

        elif (cuotas >= 11 and cuotas <= 36):
            TotalP = TotalP * 1.2  # Aplicar interés adicional del 20%

        elif (cuotas > 36):
            TotalP = TotalP * 1.5  # Aplicar interés adicional del 50%


    else:
        print("==========================================")
        print("Opcion invalida.")
        print("==========================================")


elif opcion == 3:
    print("==========================================")
    print("Seleccione el banco del cheque:");
    print("1. Banco Chile");
    print("2. Banco Estado");
    print("3. Banco BCI");
    cheque = int(input("Ingrese el número de opción: "))
    print("==========================================")

    if cheque == 1:
        TotalP = Total * 1.05  # Aplicar interés del 5%


    elif cheque == 2:
        TotalP = Total * 1.05  # Aplicar interés del 5%


    elif cheque == 3:
        TotalP = Total * 1.05  # Aplicar interés del 5%


    else:
        print("Opción inválida.")

    print("Se le ha aplicado un 5% de Interes");


# Imprimir resultado
print("Total de la compra:", Total)
print("Total a pagar:", TotalP)
