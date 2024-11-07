# Funciones de operaciones matematicas basicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero"

# Menu Matematicas basicas
def menu_operaciones_basicas():
    while True:
        print("====================================================")
        print("     Operaciones Matematicas Basicas      ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Regresar al menu anterior")

        print("")
        opcion = int(input("Seleccione una opción: "))
        print("====================================================")
        

        if opcion == 5:
            break

        a = float(input("\nIngrese el primer valor:  "))

        if opcion == 2:
            b = float(input("\nIngrese el segundo valor: "))
            while b >= a:
                print("El segundo valor debe ser menor que el primero.")
                b = float(input("\nIngrese el segundo valor nuevamente: "))
        else:
            b = float(input("\nIngrese el segundo valor: "))

        if opcion == 1:
            resultado = suma(a, b)
            nombre_operacion = "Suma"

        elif opcion == 2:
            resultado = resta(a, b)
            nombre_operacion = "Resta"

        elif opcion == 3:
            resultado = multiplicacion(a, b)
            nombre_operacion = "Multiplicacion"

        elif opcion == 4:
            resultado = division(a, b)
            nombre_operacion = "Division"
        else:
            print("Opción inválida")
            continue

        print("====================================================")
        print("       Resultado       ")
        print("")
        print("Operacion:", nombre_operacion)
        print("")
        print("Valor 1:", a)
        print("Valor 2:", b)
        print("")
        print("Resultado:", resultado)
        print("====================================================")

# Resto del código permanece igual
# Submenu de calculo de sueldo
def calcular_sueldo_liquido(rut, s_base, aguinaldo):
    bono_porcentaje = 0.3
    afp_porcentaje  = 0.15
    gratificacion   = 70000 if s_base < 280000 else 40000

    bono_valor      = s_base * bono_porcentaje
    afp_valor       = (s_base + bono_valor + gratificacion) * afp_porcentaje
    anticipo        = float(input("Ingrese el Anticipo: "))
    s_liquido       = (s_base + bono_valor + aguinaldo + gratificacion) - (anticipo + afp_valor)


    print("==========================================================")
    print("       Calculo de Sueldo Liquido       ")
    print("Rut:                       ", rut)
    print("Sueldo Base:               ", s_base)
    print("Bono (%):                  ", bono_porcentaje * 100, "% | Valor:", bono_valor)
    print("Aguinaldo:                 ", aguinaldo)
    print("Gratificacion:             ", gratificacion)
    print("AFP (%):                   ", afp_porcentaje * 100, "% | Valor:", afp_valor)
    print("Anticipo:                  ", anticipo)
    print("Suldo Liquido:             ", s_liquido)
    print("==========================================================")


def menu_calculo_sueldo():
    print("==========================================================")
    print("         Submenu - Cálculo de Sueldo          ")
    print("\n\n")

    while True:
        print("Seleccione el tipo de ciclo:")
        print("\n")
        print("1. Calcular sueldo con ciclo while")
        print("2. Calcular sueldo con ciclo for")
        print("3. Volver al menú anterior")
        print("\n")
        print("==========================================================")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            trabajadores = 3
            while trabajadores > 0:
                print("      Calculo de Sueldo      ")
                print("Trabajadores restantes:", trabajadores)

                rut = input("Ingrese el Rut del trabajador: ")
                s_base = float(input("Ingrese el Sueldo Base: "))
                aguinaldo = float(input("Ingrese el Aguinaldo: "))

                calcular_sueldo_liquido(rut, s_base, aguinaldo)

                trabajadores -= 1

        elif opcion == 2:
            trabajadores = 3
            for i in range(trabajadores):
                print("      Calculo de Sueldo      ")
                print("Trabajadores restantes:", trabajadores - i)

                rut = input("Ingrese el Rut del trabajador: ")
                s_base = float(input("Ingrese el Sueldo Base: "))
                aguinaldo = float(input("Ingrese el Aguinaldo: "))

                calcular_sueldo_liquido(rut, s_base, aguinaldo)

        elif opcion == 3:
            return

        else:
            print("Opción inválida")



#Menu de datos del autor
def mostrar_datos_autor():
    print("================================================")
    print("         Autor del Programa         ")
    print("Nombre:     Bruno Rojas")
    print("Carrera:    Ingenieria en Informatica")
    print("Asignatura: Introduccion a la Programacion")
    print("Fecha:      20 de Junio de 2023")
    print("Profesor:   Cesar Arce")
    print("================================================")



# Menu principal
while True:
    print("=====================================")
    print("          Menu Principal          ")
    print("1. Operaciones Matematicas Basicas")
    print("2. Programa Calculo de Sueldo")
    print("3. Autor del Programa")
    print("4. Salir del Programa")
    print("=====================================")

    opcion = int(input("Seleccione una opcion: "))


    if opcion == 1:
        menu_operaciones_basicas()

    elif opcion == 2:
        menu_calculo_sueldo()

    elif opcion == 3:
        mostrar_datos_autor()

    elif opcion == 4:
        print("=======================")
        print(" Fin de la Prueba N°3")
        print("=======================")
        break
    
    else:
        print("Opcion invalida")
