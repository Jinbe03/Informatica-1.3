from os import system
system("cls")


class Venta():
    NombreC = ""
    Produc  = ""
    Cant    = 0
    ValoU   = 0


    def __init__(self):
        pass;
    
    def MostrarDatos(self):
        print("")
        print("\n          Listado De Datos          ")
        print("El nombre del Cliente es ", self.NombreC)
        print("El producto Comprado es  ", self.Produc)
        print("La cantidad comprada fue ", self.Cant)
        print("El valor del producto es ", self.ValoU)

    def IngresoDatos(self):
        print("\n\n      Ingreso de Datos     \n\n")
        print("====================================")
        self.Produc = input("Ingrese Producto        : ")
        self.Cant   = input("Ingrese la cantidad     : ")
        self.ValoU  = input("Ingrese Valor Unitario  : ")

#================== Se rean los objetos, se inregan y se muestran los datos ==================

from os import system
system ("cls")

Objeto1VM = Venta ();
Objeto1VM.IngresoDatos()
Objeto1VM.MostrarDato()

Objeto2VM = Venta ()
Objeto2VM.IngresoDatos()
Objeto2VM.MostrarDatos()
