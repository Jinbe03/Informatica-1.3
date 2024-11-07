#   CONEXION N°1 CON BD
#     PYTHON - ORACLE

# Lo primero es indicarle al programa a que BD se conectara el 
# programa, y para eso debe importar la libreria de conexion,
# en este caso se conectara a Oracle, por lo tanto debe importar
# la libreria cx_Oracle

import cx_Oracle
#import mysql


from os import system
system("cls")

class ConexionOra():

    RRut = ""
    NNom = ""
    FFon = ""
    DDir = ""
    CCiu = ""

    # se crea la conexion a la BD en el constructor
    def __init__(self):
        self.ConexionBDVM = cx_Oracle.connect(
            user="system",
            password="123456",
            dsn="localhost/xe"  # dsn = Data Source Name ( Nombre de la fuente de los datos )
            # dsn="localhost:1521/xe"  # 1521 = Este es el puerto que oracle que trae por defecto
        )
        

        #Se crea el cursor para seleccionar la tabla de la BD y realiazar la consultas de datos
        self.AA = self.ConexionBDVM.cursor()
        print("\n====================-m pip install --upgrade pip==========================================")
        print(" . . . . . . Conexion Establecida de la BD . . . . . . ")
        print("==============================================================")

    def InsertarRegistros(self):
        print("\n==============================================================")
        print(" . . . . . . Grabado de Registros en la BD . . . . . . ")
        print("==============================================================")

        try:
            RRut = input("Ingrese Rut       : ")
            NNom = input("Ingrese Nombre    : ")
            FFon = int(input("Ingrese Fono      : "))
            DDir = input("Ingrese Direccion : ")
            CCiu = input("Ingrese Ciudad    : ")

            print("")
            print(" . . . . . . Listado de Sueldo sin BD . . . . . .")
            print("==============================================================")
            print("El rut del trabajador : ", RRut)
            print("El nombre del Trabajador es : ", NNom)
            print(" ... Usted arregla este listado .... ")
            print("")
            system("pause")

            #===================== GRABADO DE DATOS ===========================

            self.AA.execute('''Insert into AlumnosVM(Rut,Nombre,Fono,Direccion,Ciudad) Values ('{}','{}','{}','{}','{}')'''.format(RRut,NNom,FFon,DDir,CCiu))
            self.ConexionBDMM.commit();
            print("\n==============================================================")
            print(" . . . . . . Registro Insertado . . . . . . ")
            print("==============================================================\n")
        except Exception:
            print("\n==============================================================")
            print(" . . . . . . Error Al Grabar . . . . . . ")
            print("==============================================================\n")

    def EliminarTodosLosRegistros(self):
        try:
            self.AA.exceute("Delete From AlumnosVM")
            self.ConexionBDVM.commit()
            print(" .... Todos los Registros se han Eliminado ....!!!")
        except Exception:
            print("\n==============================================================")
            print(" . . . . . . Todos los Registros se han Eliminado . . . . . . ")
            print("==============================================================\n")

    def ActualizarRegistros (self):
        try:
            self.RRut = input ("Ingrese el rut del registro a modificar : ")
            self.AA.execute("Update AlumnosVM Set Nombre = 'AAA', Fono = 7777777 where Rut = '"+self.RRut+"'")
            self.ConexionBDVM.commit()
            print (" ... El Registro de ha modificado...!!!")
            print("\n\n")
        except Exception:
            print("Error al modificar el registro")

    def Listado1(self):
        try:
            self.AA.execute("Select * From AlumnosVM")
            Busque = self.AA.fetchall()  #Devuelve todos los registros de la consulta y los almacena en la variable Busque
            #Busque = self.AA.fechone()  #Devuelve solo un registro de la consulta , solo el primer registro
            print(" ")
            print(" Los datso de los alumnos son :",Busque)
            print("")
        except Exception:
            print(" =================================== ")
            print(" . . . Error en la consulta . . .")
            print(" ====================================")
    
    def Listado2(self):
        try:
            #Cursor ejecuta la consola que almacena AA
            self.AA.execute("Select * From AlumnosVM")
            #self,cursor.execute("Select * From AlumnosVM")
            Busque = self.AA.fetchall()  
            print("")
            print("\n ========================== LISTADO N°2 DESDE LA BASE DE DATOS ==========================")
            print("")
            print(" El rut del Alumno es .......:",Busque[0])
            print(" El nombre del Alumno es ....:",Busque[1])
            print(" El fono del Alumno es ......:",Busque[2])
            print(" La Direccion del Alumno es .:",Busque[3])
            print(" La ciudad del Alumno es ....:",Busque[4])
        except Exception:
            print("\n==============================================")
            print(" . . . . . . Error en la consulta . . . . . .")
            print("================================================")

    def Listado3(self):
        try:
            #Cursor ejecuta la consola que almacena AA
            self.AA.execute("Select * From AlumnosVM")
            #self,cursor.execute("Select * From AlumnosVM")
            Busque = self.AA.fetchall()
            print("")
            for x in Busque :
                print(" El rut del Alumno es .......:",x[0])
                print(" El nombre del Alumno es ....:",x[1])
                print(" El fono del Alumno es ......:",x[2])
                print(" La direccion del Alumno es .:",x[3])
                print(" La ciudad del Alumno es ....:",x[4])
                print("")
        except Exception:
                print("=================================================")
                print(" . . . . . . Error en la consulta 3 . . . . . . ")
                print("=================================================")

# ========================== Creacion de objetos =================================

# Se crea el objeto Conn1 e instancia a ConexionBD
Conn1=ConexionOra()
Conn1.Listado1()
Conn1.Listado2()
Conn1.Listado3()    
Conn1.InsertarRegistro()
Conn1. EliminarTodosLosRegistros()
Conn1.ActualizarRegistros()
