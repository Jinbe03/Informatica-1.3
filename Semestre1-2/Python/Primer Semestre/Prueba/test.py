#         Evaluación  N°4   
#                  Introducción a Programación
#                           PROGRAMACION  EN  PYTHON


from os import system
system ("cls")


#Sub Menu 1
def calculo_sueldo():
    ruts = []
    matriz_datos = []
    sueldos_liquidos = []

    for i in range(3):
        print("===============================================================")
        print(f"\nTrabajador {i + 1}\n")
        rut = input("Ingrese el Rut del trabajador: ")
        ruts.append(rut)

        sbase = float(input("Ingrese el sueldo base del trabajador: "))
        bono = sbase * 0.3
        aguinaldo = float(input("Ingrese el aguinaldo del trabajador: "))

        gratificacion = 0
        if sbase <= 280000:
            gratificacion = 70000
        elif sbase >= 450000:
            gratificacion = 20000

        afp = 0.1 * (sbase + bono)
        anticipo = float(input("Ingrese el anticipo del trabajador: "))
        print("===============================================================")

        sliquido = (sbase + bono + aguinaldo + gratificacion) - (anticipo + afp)

        datos = [sbase, bono, aguinaldo, gratificacion, afp, anticipo, sliquido]
        matriz_datos.append(datos)
        sueldos_liquidos.append(sliquido)

    print("Resultados ")

    for i, (rut, datos) in enumerate(zip(ruts, matriz_datos), start=1):
        print("===============================================================")
        print("")
        print(f"Trabajador {i}")
        print("")
        print("Rut:", rut)
        print("Sueldo Base     : ", datos[0])
        print("Bono            : ", datos[1])
        print("Aguinaldo       : ", datos[2])
        print("Gratificacion   : ", datos[3])
        print("AFP             : ", datos[4])
        print("Anticipo        : ", datos[5])
        print("Sueldo Líquido  : ", datos[6])
        print("")
        print("===============================================================")

#Sub Menu 2
def calcular_venta(nombre, valor, cantidad):
    total = valor * cantidad

    descuento = 0
    if total >= 200000:
        descuento = total * 0.2
    elif total >= 99999:
        descuento = total * 0.1

    total_pagar = total - descuento

    return total, descuento, total_pagar


def programa_ventas():
    productos = []
    totales = []
    descuentos = []
    totalpagar = []

    for _ in range(3):
        print("======================================================================")
        print("")
        nombre = input("Ingrese el nombre del producto: ")
        valor = float(input("Ingrese el valor del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        print("")
        print("======================================================================")
        total, descuento, total_pagar = calcular_venta(nombre, valor, cantidad)

        productos.append(nombre)
        totales.append(total)
        descuentos.append(descuento)
        totalpagar.append(total_pagar)

        print("======================================================================")
        print("")
        print("Producto       : ", nombre)
        print("Valor          : ", valor)
        print("Cantidad       : ", cantidad)
        print("Total          : ", total)
        print("Descuento      : ", descuento)
        print("Total a Pagar  : ", total_pagar)
        print("")
        print("======================================================================")

#Sub Menu 3
def datos_autor():
    print("================================================")
    print("")
    print("         Autor del Programa         ")
    print("Nombre:     Bruno Rojas")
    print("Asignatura: Introduccion a la Programacion")
    print("Jornada:    Martes Tarde")
    print("Fecha:      18 de Julio de 2023")
    print("Profesor:   Cesar Arce")
    print("")
    print("================================================")

#Salida del Menu ((Sub Menu 4))
def salir():
    print("=======================")
    print(" Fin del Programa ")
    print("=======================")
    exit()

#Menu Principal
while True:
    print("=============================================================")
    print("")
    print("Bienvenido al Menú Principal")
    print("")
    print("1. Programa Calculo de Sueldo con Arreglos.")
    print("2. Programa Ventas de Productos Tecnologicos con Arreglos")
    print("3. Autor del Programa")
    print("4. Fin del menu")
    print("")
    print("=============================================================")

    opcion = input("Selecciona una opcion (1-4): ")

    if opcion == "1":
        calculo_sueldo()
    elif opcion == "2":
        programa_ventas()
    elif opcion == "3":
        datos_autor()
    elif opcion == "4":
        salir()
    else:
        print("Opcion inválida. Por favor, selecciona una opcion valida.")
