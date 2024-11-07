#trabajo (?)

from os import system
system("cls")

class Viaje:
        
    Rut           = ""
    Origen        = ""
    Destino       = ""
    ValorP        = 0
    NPasajes      = 0
    FormaPago     = ""
    Dcto          = 0
    Interes       = 0
    TotalPagar    = 0
    
    def __init__(self):
        pass

    def ingresar_datos(self):
        print("================================================================")
        self.Rut      =       input("Ingrese el Rut del pasajero        : ")
        self.Origen   =       input("Ingrese el origen del viaje        : ")
        self.Destino  =       input("Ingrese el destino del viaje       : ")
        self.ValorP   = float(input("Ingrese el valor del pasaje        : "))
        self.NPasajes = int  (input("Ingrese el número de pasajes       : "))
        print("-----------------------------------------------------------------")
        print("\nSeleccione la forma de pago      : ")
        print("1. Contado")
        print("2. Tarjeta Banco")
        print("3. Tarjeta Tienda")
        print("-----------------------------------------------------------------")

        while True:
            try:
                self.FormaPago = int(input("Ingrese el número correspondiente al método de pago: "))
                print("================================================================")
                if 1 <= self.FormaPago <= 3:
                    break
                else:
                    print("Opción no válida. Ingrese 1, 2 o 3.")
            except ValueError:
                print("Opción no válida. Ingrese 1, 2 o 3.")

    def venta_pasajes(self):
        if self.FormaPago == 1:              #Contado
            self.Dcto = 0.20 * self.ValorP

        elif self.FormaPago == 2:            #Tarjeta Banco
            self.Dcto = 0.10 * self.ValorP

        elif self.FormaPago == 3:           #Tarjeta Tienda
            self.Interes = 0.10 * self.ValorP

        self.TotalPagar  = (self.ValorP * self.NPasajes) - self.Dcto + self.Interes


    def mostrar_datos(self):
        print("================================================================")
        print("---------- Datos del Viaje ----------")
        print("Rut del Pasajero  : ",self.Rut)
        print("Origen            : ",self.Origen)
        print("Destino           : ",self.Destino)
        print("Valor del Pasaje  : ",self.ValorP)
        print("Número de Pasajes : ",self.NPasajes)
        print("Forma de Pago     : ",self.FormaPago)
        print("Descuento         : ",self.Dcto)
        print("Interes           : ",self.Interes)
        print("Total a Pagar     : ",self.TotalPagar)
        print("================================================================")

viaje = Viaje()
viaje.ingresar_datos()
viaje.venta_pasajes()
viaje.mostrar_datos()
