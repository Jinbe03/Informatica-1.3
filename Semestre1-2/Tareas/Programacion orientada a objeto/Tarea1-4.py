from os import system
system("cls")


class Venta:

    NombreProducto   = ""
    NombreProducto   = 0
    FormaPago        = ""
    Cantidad         = 0
    Fecha            = 0
    MetodoPago       = ""
    CodigoVenta      = 0

    def __init__(self):
        pass

    def Ingresar_Datos(self):
        print                          ("\n=======================================")
        print                          ("          Ingresar Datos          ")
        self.NombreProducto = input    ("Ingrese el nombre del producto         : ") 
        self.CodigoProducto = int(input("Ingrese el codigo del producto         : "))
        self.FormaPago      = input    ("Ingrese la forma de pagar              : ") 
        self.Cantidad       = int(input("Ingrese la cantidad de compra          : "))
        self.Fecha          = int(input("Ingrese la fecha de compra             : "))
        self.MetodoPago     = input    ("Ingrese el metodo de pago              : ") 
        self.CodigoVenta    = int(input("Ingrese el codigo de venta             : "))
        print                          ("=======================================")

    def Mostrar_Datos(self):
        print("\n=======================================")
        print("          Muestra de Datos          ")
        print("El Nombre del producto es : ", self.NombreProducto)
        print("El codigo del producto es : ", self.CodigoProducto)
        print("La forma de pago es       : ", self.FormaPago)     
        print("La cantidad comprada es   : ", self.Cantidad)      
        print("La fecha de compra es     : ", self.Fecha)         
        print("El metodo de pago es      : ", self.MetodoPago)    
        print("El Codigo de venta es     : ", self.CodigoVenta)    
        print("\n=======================================")

Venta1 = Venta()
Venta1.Ingresar_Datos()
Venta1.Mostrar_Datos() 