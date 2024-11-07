#       CONEXION  Nº1  CON  BD 
#         PYTHON -  ORACLE


#  Lo primero es indicarle al programa a que BD se conectara el
#  programa, y para eso debe importa la librería de conexión,
#  en este caso se conectara a Oracle, por lo tanto debe importar
#  la libreria cx_Oracle.


import  cx_Oracle;
#import  mysql;

#Se limpia la pantalla
from os import system;
system("cls");

class ConexionOra():    

    #Se crea la conexión a la BD en el constructo
    def __init__(self):
               
        self.ConexionBDVM=cx_Oracle.connect(
            user="system",
            password="654321",
            dsn="localhost/xe"        #dsn = Data Source Name ( Nombre de la funte de los datos )
            #dsn="localhost:1521/xe"  #1521 = Este es el puerto que oracle  que trae por defecto.           
        );

         # Se crea el cursor para seleccionaR la tabla de la BD y realizar la consultas de datos
        self.AA = self.ConexionBDVM.cursor();
        print("\n=========================================================");
        print(" . . . . . . Conexión Establecida a la BD  . . . . . . !!! ");
        print("===========================================================\n"); 

    def Listado1(self):         
        try:        
            self.AA.execute("Select * From  AlumnosMT");  
            Busque = self.AA.fetchall(); # Devuelve todos los registros de la consulta y los almacena en la variable Busque
            #Busque = self.AA.fetchone();  # Devuelve solo un  registros de la consulta , solo el primer registro
            print(" " );
            print(" Los datos de los Alumnos son  :\n",Busque );
            print(" " );
        except Exception:
            print("\n==============================================");
            print("....... Error  en la Consulta  Realizado ....... ");
            print("==============================================\n");

    def Listado2(self):        
        try:
            # Cursor ejecuta la consulta que  almacena RR
            self.AA.execute("Select * From  AlumnosLN");
            #self.cursor.execute("Select * From  AlumnosLN");  
            Busque = self.AA.fetchall(); # Devuelve todos los registros de la consulta y los almacena en la variable Busque
            print(" " );
            print("\n       ========================= LISTADO  Nº2 DESDE LA  BASE DE DATOS =====================");
            print("");   
            print(" El Rut del Alumno  es  ........ :",Busque[0]);
            print(" El Nombre del Alumno  es ...... :",Busque[1]); 
            print(" El Fono del Alumno  es ........ :",Busque[2]);
            print(" La Dirección del Alumno  es ... :",Busque[3]);
            print(" La Ciudad del Alumno  es  : ....:",Busque[4]);                        
            print(" " ); 
        except Exception:
            print("\n==============================================");
            print("....... Error  en la Consulta  Realizado ....... ");
            print("==============================================\n");

    def Listado3(self):        
        try:
            # Cursor ejecuta la consulta que  almacena el cursor llamado AA
            self.AA.execute("Select * From  AlumnosLN");
            #self.cursor.execute("Select * From  AlumnosLN");  
            Busque = self.AA.fetchall(); # Devuelve todos los registros de la consulta y los almacena en la variable Busque
            print(" " );
            print("\n       ========================= LISTADO  Nº3 DESDE LA  BASE DE DATOS =====================");
            print("");   

            for x in Busque :
                print(" El Rut del Alumno  es  ........ :",Busque[0]);
                print(" El Nombre del Alumno  es ...... :",Busque[1]); 
                print(" El Fono del Alumno  es ........ :",Busque[2]);
                print(" La Dirección del Alumno  es ... :",Busque[3]);
                print(" La Ciudad del Alumno  es  : ....:",Busque[4]);                        
                print(" " ); 
        except Exception:
                print("\n==============================================");
                print("....... Error  en la Consulta 3  Realizado ....... ");
                print("==============================================\n");


# ===================== CREACION DE OBJETOS ===================== #

# Se crea el objetos  Conn1  e instancia a ConexionBD
Conn1 = ConexionOra(); # El objeto Conn1 llama a la clase Conexión, y esta lanza el constructor y crea la conexión
Conn1.Listado1();
Conn1.Listado2();
Conn1.Listado3(); 






