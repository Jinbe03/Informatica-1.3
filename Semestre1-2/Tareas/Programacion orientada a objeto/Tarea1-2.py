from os import system
system("cls")


class Vendedor:
    
    Nombre       = ""
    Apellido     = ""
    Cargo        = ""
    Rut          = 0
    Edad         = 0
    Antiguedad   = ""
    Genero       = ""


    def __init__(self):
        pass

    def Ingresar_Datos(self):
        print                          ("\n=======================================")
        print                          ("          Ingresar Datos          ")
        self.Nombre         =     input("Ingrese el nombre del Vendedor          : ") 
        self.Apellido       =     input("Ingrese el codigo del Vendedor          : ")
        self.Cargo          = int(input("Ingrese el cargo del Vendedor           : ")) 
        self.Rut            = int(input("Ingrese RUT del Vendedor                : "))
        self.Edad           =     input("Ingrese la edad del Vendedor            : ")
        self.Antiguedad     =     input("Ingrese la antiguedad del Vendedor      : ")
        self.Genero         =     input("Ingrese el genero de Vendedor           : ")
        print                          ("\n=======================================")

    def Mostrar_Datos(self):
        print("\n=======================================")
        print("          Muestra de Datos          ")
        print("El Nombre del producto es : ", self.Nombre)  
        print("El codigo del producto es : ", self.Apellido)
        print("La forma de pago es       : ", self.Cargo)     
        print("La cantidad comprada es   : ", self.Rut)      
        print("La fecha de compra es     : ", self.Edad)         
        print("El metodo de pago es      : ", self.Antiguedad)    
        print("El Codigo de venta es     : ", self.Genero)    
        print("\n=======================================")

Vendedor1 = Vendedor()
Vendedor1.Ingresar_Datos()
Vendedor1.Mostrar_Datos() 