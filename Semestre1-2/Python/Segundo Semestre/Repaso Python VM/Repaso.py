#                Demo 1 Repaso
#        Repaso Ejercicio Final Arreglos

#Si utiliza numPy debe importar la libreria
#C:\>pip install numpy

#Realice un programa utilizando arreglos
#( listas=[], Diccionaroos={} y tuplas=() )

#El programa debe realizar lo siguiente:
#realice un prgorama que calcule el promedio de notas
#el programa es para 3 alumnos
#datos a considerar:
#Rut, nombre, asignatura, nota1, nota2, nota3, promedio, situacion, y promedio final
#nota 1 = 25%
#nota 2 = 35%
#nota 3 = 40%
#sitacuin : promedio : 10 - 39 = reprobado
#           promedio : 40 - 49 = Aprobado
#           promedio : 50 - 70 = Eximido
#promedio final: es el promedio de los 3 alumnos

from os import system
system("cls")



alumnos = {
    "alumno1": ["12345678-9", "Juan Pérez", "Matemáticas", 4.5, 5.0, 6.0],
    "alumno2": ["98765432-1", "María González", "Lenguaje", 5.0, 4.0, 6.5],
    "alumno3": ["56789012-3", "Pedro Sánchez", "Historia", 6.0, 6.5, 7.0]
}

for alumno, datos in alumnos.items():
    rut = datos[0]
    nombre = datos[1]
    asignatura = datos[2]
    nota1 = datos[3]
    nota2 = datos[4]
    nota3 = datos[5]
    
    promedio = (nota1 * 0.25) + (nota2 * 0.35) + (nota3 * 0.4)
    
    if promedio < 40:
        situacion = "Reprobado"
    elif promedio < 50:
        situacion = "Aprobado"
    else:
        situacion = "Eximido"
    
    datos.append(promedio)
    datos.append(situacion)

promedio_final = sum(datos[6] for datos in alumnos.values()) / len(alumnos)

print("Promedio final:", promedio_final)
