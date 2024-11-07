from os import system
system("cls")

class Cliente:
    def __init__(self):
        self.Nombre    = ""
        self.Apellido  = ""
        self.Telefono  = 0
        self.Rut       = 0
        self.Direccion = ""
        self.Mail      = ""
        self.Genero    = ""

    def Ingresar_Datos(self):
        print("\n=======================================")
        print("          Ingresar Datos          ")
        self.Nombre    =     input("Ingrese el nombre del Cliente          : ") 
        self.Apellido  =     input("Ingrese el apellido del Cliente        : ") 
        self.Telefono  = int(input("Ingrese el telefono del Cliente        : "))
        self.Rut       = int(input("Ingrese RUT del Cliente                : "))
        self.Direccion =     input("Ingrese la direccion del Cliente       : ") 
        self.Mail      =     input("Ingrese el mail del Cliente            : ") 
        self.Genero    =     input("Ingrese el genero del Cliente          : ") 
        print("=======================================")

    def Mostrar_Datos(self):
        print("\n=======================================")
        print("          Muestra de Datos          ")
        print("El Nombre del cliente es   : ", self.Nombre)       
        print("El apellido del cliente es : ", self.Apellido)     
        print("El telefono del cliente es : ", self.Telefono)     
        print("El RUT del cliente es      : ", self.Rut)          
        print("La direccion del cliente es: ", self.Direccion)    
        print("El mail del cliente es     : ", self.Mail)         
        print("El genero del cliente es   : ", self.Genero)       
        print("\n=======================================")

Cliente1 = Cliente()
Cliente1.Ingresar_Datos()
Cliente1.Mostrar_Datos()
