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
        self.AA.execute("Select * From Alumnos VM")
        Busque = self.AA.fetcha11() #Devuelve todos los registros de la consulta y los almacena en la
        #Busque = self.AA.fetchone() #Devuelve solo un registro de consulta
    except Exception:
        print("")    
