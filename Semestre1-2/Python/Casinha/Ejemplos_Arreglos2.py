#Arreglos 2

#Ejemplo
#[1,5,8,9,30,9,13]
#Imprimir en pantalla los numeros impares a 3

A = [1,5,8,9,30,9,13]
B = []
for i in range (A):
    if i > 3 and i % 2 == 0:
        B.append(i)
