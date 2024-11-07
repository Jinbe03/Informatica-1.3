# Se importa la librería para trabajar con archivos json
import json;

# Se Limpia pantalla
from os import system;
system("cls");

print("\n=========================================================");
print(" . . . . .  EJEMPLO Nº1 CONSUMO  API EXTERNA  . . . . . . !!! ");
print("===========================================================\n"); 

# Se crea una función que recibe 1 parametro de  retorno  
def LLamarArchivoJson(RutaArchivo):
    open (RutaArchivo );  # open = Se utiliza para abrir y leer un archivos json

    # with = se utiliza por que no se sabe el tamaño del archivo a abrir
    with open (RutaArchivo ) as  RR: # Con la variable RR se podra trabajar dentro del archivo json
      DatosArchivos = json.load(RR);
      print(DatosArchivos);

      # for xx in DatosArchivos:
      #    print( xx.get());

if __name__ == '__main__':
   # Se crea un variable para llamar al archivo "json"
   # AA = 'ArchivoJson.json'; # El archovo json esta en la misma ruta del archivo Python.
   AA = 'Datos/ArchivoJason.json'; # Se coloca la ruta donde esta el archivo json, en este caso dentro de la carpeta Datos.
   LLamarArchivoJson(AA);

print("\n\n=========================================================");
print(" . . . . .  EJEMPLO Nº2 CONSUMO  API EXTERNA  . . . . . . !!! ");
print("===========================================================\n"); 

# Se crea una función que recibe 1 parametro de  retorno  
def LLamarArchivoJson(RutaArchivo):
    open (RutaArchivo );  # open = Se utiliza para abrir y leer un archivos json

    # with = se utiliza por que no se sabe el tamaño del archivo a abrir
    with open (RutaArchivo ) as  RR: # Con la variable RR se podra trabajar dentro del archivo json
      DatosArchivos = json.load(RR);
      print(DatosArchivos);
      print("");

      for xx in DatosArchivos:
         print(xx);

if __name__ == '__main__':
   # Se crea un variable para llamar ala rchivo "json"
   # AA = 'ArchivoJson.json'; # El archovo json esta en la misma ruta del archivo Python.
   AA = 'Datos/ArchivoJason.json'; # Se coloca la ruta donde esta el archivo json, en este caso dentro de la carpeta Datos.
   LLamarArchivoJson(AA);

print("\n\n");