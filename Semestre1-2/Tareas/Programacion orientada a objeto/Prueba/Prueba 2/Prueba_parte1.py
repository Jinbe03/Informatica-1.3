class SuperCAR:

    def IngresarDatos(self):
        print("==================================================")
        print("     Ingreso de Datos     ")
        self.Rut = int(input("Ingrese rut del cliente: "))
        self.NombreCliente = input("Ingrese Nombre del Cliente: ")
        self.ApellidoCliente = input("Ingrese Apellido del Cliente: ")
        self.TipoVehiculo = input("Ingrese el Tipo de vehiculo a comprar: ")
        self.ValorVehiculo = int(input("Ingrese el Valor del vehiculo: "))
        self.Cantidad = int(input("Ingrese la Cantidad de vehiculos a comprar: "))
        self.Total = self.ValorVehiculo * self.Cantidad
        print("==================================================\n")

    def Calculos(self):
        print("==================================================")
        print("Seleccione la forma de pago : ")
        print("1. Contado")
        print("2. Tarjeta")
        print("3. Cheque")

        opcion = int(input("Ingrese el numero de opcion: "))
        print("==========================================")

        if opcion == 1:
            self.TotalPagar = self.Total * 0.8  # se aplica un 20% de descuento

        elif opcion == 2:
            print("==========================================")
            print("Seleccione el tipo de tarjeta:")
            print("1. Banco")
            OpcionTarjeta = int(input("Ingrese el numero de la opcion: "))
            if OpcionTarjeta == 1:
                self.TotalPagar = self.Total * 0.9  # Aplicar descuento del 10%

        elif opcion == 3:
            print("==========================================")
            print("Seleccione el banco del cheque:")
            print("1. Cheque al Dia")
            print("2. Cheque a Fecha")
            OpcionCheque = int(input("Ingrese el numero de la opcion: "))
            if OpcionCheque == 1:
                self.TotalPagar = self.Total  # se aplica 0% de descuento
            elif OpcionCheque == 2:
                self.TotalPagar = self.Total * 1.10  # Aplicar interes del 10%

    def TotalFinalPagar(self):
        print("==================================================")
        print("     Detalle de la Compra     ")
        print("Rut del Cliente:", self.Rut)
        print("Nombre del Cliente:", self.NombreCliente)
        print("Apellido del Cliente:", self.ApellidoCliente)
        print("Tipo de Vehiculo:", self.TipoVehiculo)
        print("Valor del Vehiculo:", self.ValorVehiculo)
        print("Cantidad de Vehiculos:", self.Cantidad)
        print("Total a Pagar:", self.TotalPagar)
        print("==================================================\n")



supercar1 = SuperCAR()
supercar1.IngresarDatos()
supercar1.Calculos()
supercar1.TotalFinalPagar()