from os import system
system("cls")


class ingreso:
    NombrePelicula = ""
    Valor       = 0
    Cantidad    = 0
    Total       = 0
    Descuento   = 0
    TotalPagar  = 0

    def __init__(self):
        pass

    def IngresoDatos(self):
        print(" \n     INGRESO DE DATOS     ")
        self.NombrePelicula = input("Ingrese nombre pelicula       :")
        self.Valor = int(input("Ingrese valor de entrada      : "))
        self.Cantidad = int(input("Ingrese cantidad de entradas  :"))
        
class calculos:

    def __init__(self):
        pass

    def venta(self):

        self.Total= self.Valor * self.Cantidad

        if (self.Total < 99999):
            self.TotalPagar = self.Total - self.Descuento

        if (self.Total > 99999):
            self.Descuento = self.Total * 10/100
            self.TotalPagar = self.Total - self.Descuento   

        if (self.Total >= 200000):
            self.Descuento= self.Total * 20/100
            self.TotalPagar= self.Total - self.Descuento

class trabajador(ingreso,calculos):

    def __init__(self):
        pass

    def MuestraDatos(self):
        print(" \n\n       MUESTRA DE DATOS     ") 
        print(" Nombre de la pelicula  : ",self.NombrePelicula)
        print(" Valor de la entrada    : ",self.Valor)
        print(" Cantidad entradas      : ",self.Cantidad)
        print(" Total venta            : ",self.Total)
        print(" Descuento              : ",self.Descuento)
        print(" Total a Pagar          : ",self.TotalPagar)
        print("")

trabajdor1=trabajador()
trabajdor1.IngresoDatos()
trabajdor1.venta()
trabajdor1.MuestraDatos()        

trabajdor2=trabajador()
trabajdor2.IngresoDatos()
trabajdor2.venta()
trabajdor2.MuestraDatos()
