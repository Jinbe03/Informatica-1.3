#Ejercicio n°3 IF
#Como se realiza una pregunta en python

#Realice un programa en python que pregunte la edad de una persona y que en base a la edad, determine si la persona
#es Niño, Adolecente, Juvenil, Adulto, Adutlo Myor

#Limpiar Pantalla
from os import system
system ("cls");

print("");
print("");
print("==============================================")
print(" . . . . . . Introduzca su edad . . . . . . : ");
print("==============================================")

EEdad=int(input("Ingrese edad de la persona: "));

if(EEdad>= 1 and EEdad<12):
    print("Ud. es un Niño y tiene: ",EEdad," Años")
    print("==============================================")
    print("");

elif(EEdad>=12 and EEdad <18):
    print("Ud. es un adolecente y tiene:" ,EEdad,"Años")
    print("==============================================")
    print("");

elif(EEdad>=18 and EEdad<21):
    print("Ud. es Juvenil y tiene;",EEdad," Años")
    print("==============================================")
    print("");

elif(EEdad>=21 and EEdad <65):
    print("Ud. es un Adulto y tiene:",EEdad," Años")
    print("==============================================")
    print("");

elif(EEdad>=65 and EEdad < 105):
    print("Ud. es un Adulto Mayor y tiene: ",EEdad," Años")
    print("==============================================")
    print("");

else:
    print("")
    print("===============================================")
    print(" . . . La edad de la persona no es valida . . .")
    print("==============================================")
    print("")