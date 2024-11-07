#Ejercicio N°2 Python

#Realize un programa que calcule el promedio de nota de los alumnos, para lo cual debe considerar los siguientes datos

#Datos: Rut, Nombre, Asignatura, Notas (3)
#Promedio, 80% prom, examen
#70% examen, Promedio final.

#Declaracion de Variables
Rutt = (""); #Se declara la variable Rutt que almacenara el Rut.
Nomm = (""); #Se declara la variable Nomm que almacenara el Nombre.
Asig = (""); #Se declara la variable Asig que almacenara la Asignatura.
Not1 = (""); #Se declara la variable Not1 que almacenara la Nota1.
Not2 = (""); #Se declara la variable Not2 que almacenara la Nota2.
Not3 = (""); #Se declara la variable Not3 que almacenara la Nota3.
Exam = (""); #Se declara la variable Exam que alacenara el Examen.
Exa1 = (""); #Se declara la variable Exa1 que alacenara el 20% del Examen.
Prom = (""); #Se declara la variable Prom que alamcenara el Promedio.
Pro8 = (""); #Se declara la variable Pro8 Que almacenara el Promedio 80%.
ProF = (""); #Se declara la variable ProF que almacenara el Promedio Final.

#Asignacion de las Variables
Rutt = "20843964-2";               #Se asigna el valor a la variable Rutt.
Nomm = "Bruno Rojas";              #Se asigna el valor a la variable Nomm.
Asig = "Intro. Pro.";              #Se asigna el valor a la variable Asig.
Not1 = 63;                         #Se asigna el valor a la variable Not1.
Not2 = 57;                         #Se asigna el valor a la variable Not2.
Not3 = 54;                         #Se asigna el valor a la variable Not3.
Exam = 70;                         #Se asigna el valor a la variable Exam.
Exa1 = (Exam*20)/100;              #Se asigna el valor a la variable Exa1.
Prom = (Not1+Not2+Not3)/3;         #Se asigna el valor a la variable Prom.
Pro8 = (Prom*80)/100;              #Se asigna el valor a la variable Pro8.
ProF = (Pro8+Exa1);                #Se Asigna el valor a la variable ProF.


print(""); #Se asigna una linea en blanco
print(""); #Se asigna una linea en blanco

print("...... Muestra de Datos ......"); 
print(" ============================= "); 
print("El Nombre del Alumno es ........:",Nomm); 
print("El Rut del Alumno es ...........:",Rutt); 
print("La Asignatura es ...............:",Asig); 
print("La Nota N1 es ..................:",Not1); 
print("La Nota N2 es ..................:",Not2);  
print("La Nota N3 es ..................:",Not3);
print("El Promedio es .................:",Prom);
print("El 80 del promedio es...........:",Pro8);
print("El Examen 1 es .................:",Exam);
print("El 70 del Examen es ............:",Exa1);
print("El Promedio final es............:",ProF);


print(""); #Se asigna una linea en blanco
print(""); #Se asigna una linea en blanco