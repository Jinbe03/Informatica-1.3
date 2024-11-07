from os import system
system("cls")

import json;

#Se crea una funcion que recibe 1 parametro de retorno

print("\n=============================================================")
print("                   Ejemplo 1 conexion JSON                ")
print("=============================================================\n")



def LLamarArchivoJson(RutaArchivo):
    open (RutaArchivo);                 # open = se utiliza para abrir y leer archivos json

    #with open (RutaArchivo) as RR: 
 a
    with open (RutaArchivo) as RR:      #Con la variable RR se podria trabajar dentro del archivo json
        DatosArchivos = json.load(RR)
        print("DatosArchivos");
        
        # for xx in DatosArchivos:
        #   print(xx.get())

if __name__ == '__main__':

    #Se crea una variable para llamr al archivo "json"
    #AA = 'ArchivoJson.json';         #El archivo json esta en la misma ruta del archivo python.

    AA = 'ArchivoJson.json';          #Se coloca la ruta donde esta el archivo json, en este caso dentro de de la carpeta datos
    AA = 'Datos/ArchivoJSON.json';    #Se colocla la ruta donde esta el archivo json, en este caso dentro de la carpta
    LLamarArchivoJson(AA);   