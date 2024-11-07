import cx_Oracle

from os import system
system("cls");

class ConexionOra():

    def __init__(self):

        self.conexionBDMT = cx_Oracle.connect(
            user = "system",
            password = "123456",
            dsn = "localhost:1521/xe"
        );

        self.cursorBDMT = self.conexionBDMT.cursor();
        print("\n_____________________________________________");
        print("\n________    /Conexion Establecida\     ______");
        print("\n_____________________________________________");
        system("pause");
        system("cls");
    
        
    def calcular_sueldo(self):
        system("cls");
        self.Rut       = input      ("Ingrese el Rut .......: ");
        self.Nombre    = input      ("Ingrese el Nombre ....: ");
        self.SBase     = float(input("Ingrese el Sueldo Base: "));
        self.Bono      = (self.SBase * 20) / 100  # Calculo del 20% del SBase;
        self.Aguinaldo = 60000 if self.SBase < 180000 else (40000 if self.SBase <= 300000 else 20000);
        self.Afp       = float(input("Dto Afp ..............: "))
        self.Anticipo  = float(input("Ingrese el Anticipo ..: "));
        self.SLiquido  = (self.SBase + self.Bono + self.Aguinaldo) - (self.Anticipo + self.Afp);

        system("cls");
        print("\n _____________ Listado Datos Alumno _____________\n");
        print(" Rut       :",self.Rut);
        print(" Nombre    :",self.Nombre);
        print(" SBase     :",self.SBase);
        print(" Bono      :",self.Bono);
        print(" Aguinaldo :",self.Aguinaldo);
        print(" Afp       :",self.Afp);
        print(" Anticipo  :",self.Anticipo);
        print(" SLiquido  :",self.SLiquido);

        system("pause");
        
        self.cursorBDMT.execute('''Insert Into Sueldos values ('{}','{}',{}, {}, {}, {}, {}, {})'''.format(self.Rut,self.Nombre,self.SBase,self.Bono,self.Aguinaldo, self.Afp, self.Anticipo, self.SLiquido))
        self.conexionBDMT.commit();
        system("cls");
        print("\n __________ Sueldo Calculado e Ingresado ________\n");
        system("pause");
        system("cls");
        
    def listar_datos(self):
        try:
            self.cursorBDMT.execute("Select * from Sueldos");
            busca = self.cursorBDMT.fetchall();
            for x in busca:
                print("\n\n ____________ Listado BD ________________\n");
                print(" El Rut es          :",x[0]);
                print(" El Nombre es       :",x[1]);
                print(" El SBase es        :",x[2]);
                print(" El Bono es         :",x[3]);
                print(" El Aguinaldo es    :",x[4]);
                print(" El DTO del Afp es  :",x[5]);
                print(" El SLiquido es     :",x[6]);
                system("pause")
        
        except Exception:
            print(" \n ____ /Error en la consulta Realizada\ ___\n");

     
        self.Rut = input("\nIngrese el Rut del registro a eliminar: ");
        self.cursorBDMT.execute("DELETE FROM Sueldos WHERE Rut = :Rut", {'Rut': self.Rut})
        self.conexionBDMT.commit();
        print("Registro eliminado");

    def menu_principal(self):
        while True:
            system("cls");
            print("\nMENU PRINCIPAL");
            print("1. Programa Calculo de Sueldo");
            print("2. Autor del Programa");
            print("3. Salir del Programa");

            opcion = input("Seleccione una opción (1/2/3): ");

            if opcion == "1":
                self.calcular_sueldo();
                self.listar_datos();
            elif opcion == "2":
                system("cls");
                print("Autor del Programa:");
                print("Nombre: Elliot Fuentealba");
                print("Jornada: Diurna");
                print("Sección: 162-D");
                print("Fecha: 12-12-2023");
                print("Profesor: Cesar Arce");
                system("pause");
                system("cls");
            elif opcion == "3":
                system("cls");
                confirmacion = input("\n¿Está seguro de salir? (Si/No): ");
                if confirmacion.lower() == "si":
                    print("\nSaliendo del programa...");
                    break
                elif confirmacion.lower() == "no":
                    print("\nRegresando al Programa...");
                    system("pause");
                    system("cls");
                else:
                    system("cls");
                    print("\nOpción no válida. Regresando al Programa...");
                    system("pause");
                    system("cls");
            else:
                system("cls");
                print("Opción no válida. Intente de nuevo.");
                system("pause");
                system("cls");

Conn1 = ConexionOra();
Conn1.menu_principal();