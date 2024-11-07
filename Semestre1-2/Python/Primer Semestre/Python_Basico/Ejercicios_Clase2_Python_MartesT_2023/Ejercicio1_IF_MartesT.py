#Ejercicio N°1 Pyton
#Intruccion IF

#Realize un prgorama en Python
#que calcule el promedio de notas de los alumnos de Introduccion a la Programacion, para lo cual debe
#considerar los siguientes datos
#Datos:
#Rut, Nombre, Asignatura, Nota1, Nota2, Nota3, Promedio y Situacion del Alumno
#Situacion (Reprobado, Aprobado y Eximido)
#Mostrar todos los datos de forma perfecta

#Definicion de variables
Rutt = ""; #Se declara la variable Rutt
Nomm = ""; #Se declara la variable Nomm
Asig = ""; #Se declara la variable Asig
Not1 = 0;  #Se declara la variable Not1
Not2 = 0;  #Se delcara la variable Not2
Not3 = 0;  #Se declara la variable Not3
Prom = 0;  #Se declara la variable Prom
Sitt = ""; #Se declara la  variable Sitt
ContR = 0; #Se declara la variable ContR
ContA = 0; #Se declara la variable ContA
ContE = 0; #Se declara la variable ContE


#Asignacion de datos a las variables

Rutt = "20843964-2";                     #Se declara la variable Rutt
Nomm = "Bruno Exequiel Rojas Maldonado"; #Se declara la variable Nomm
Asig = "Introduccion a la programacion"; #Se declara la variable Asig
Not1 = 22;                               #Se declara la variable Not1
Not2 = 33;                               #Se delcara la variable Not2
Not3 = 44;                               #Se declara la variable Not3
Prom = 33;                               #Se declara la variable Prom

#Calculo del Promedio
Prom = (Not1+Not2+Not3)/3;

#Validacion de la situacion (Reprovado, Aprovado y Eximido);
if(Prom>= 10 and Prom <40):
    ContR = ContR + 1;
    Sitt = "Reprovado";

if(Prom>= 40 and Prom <50):
    ContA = ContA + 1;
    Sitt = "Aprovado";

if(Prom>= 50 and Prom <71):
    ContE = ContE + 1;
    Sitt = "Eximido";

print(""); #Se asigna una linea en blanco
print(""); #Se asigna una linea en blanco

print("........... Muestra de datos ............");
print("=========================================");
print("El Rut del Alumno es ..............", Rutt);
print("El Nombre del Almuno es ...........", Nomm);
print("La Asignatura evaluada es..........", Asig);
print("La Nota1 del Alumno es ............", Not1);
print("La Nota2 del Almuno es ............", Not2);
print("La Nota3 del Alumno es ............", Not3);
print("El Promedio del Alunmno es ........", Prom);
print("La Situacion final del Almuno es...", Sitt);

print(""); #Se asigna una linea en blanco
print(""); #Se asigna una linea en blanco