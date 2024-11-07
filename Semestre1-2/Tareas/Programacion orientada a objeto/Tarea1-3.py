from os import system
system("cls")


class Producto:

    EstadoProducto   = ""
    NombreProducto   = ""
    Marca            = 0
    Precio           = 0
    TipoProducto     = 0
    CodigoProducto   = ""
    Stock            = 0


    def __init__(self):
        pass

    def Ingresar_Datos(self):
        print                          ("\n=======================================")
        print                          ("          Ingresar Datos          ")
        self.EstadoProducto =     input("Ingrese el estado del producto          : ") 
        self.NombreProducto =     input("Ingrese el nombre del producto          : ")
        self.Marca          =     input("Ingrese la marca del producto           : ")
        self.Precio         = int(input("Ingrese el precio del producto          : "))
        self.TipoProducto   =     input("Ingrese el tipo de producto             : ")
        self.CodigoProducto = int(input("Ingrese el codigo del producto          : "))
        self.Stock          = int(input("Ingrese el stock del producto           : "))
        print                          ("\n=======================================")

    def Mostrar_Datos(self):
        print("\n=======================================")
        print("          Muestra de Datos          ")
        print("El estado del producto es : ", self.EstadoProducto)  
        print("El nombre del producto es : ", self.NombreProducto)
        print("La marca del producto es  : ", self.Marca)
        print("El precio del producto es : ", self.Precio)      
        print("El Tipo del producto es   : ", self.TipoProducto)         
        print("El codigo del producto es : ", self.CodigoProducto)
        print("El stock del producto es  : ", self.Stock)
        print("\n=======================================")

Producto1 = Producto()
Producto1.Ingresar_Datos()
Producto1.Mostrar_Datos() 