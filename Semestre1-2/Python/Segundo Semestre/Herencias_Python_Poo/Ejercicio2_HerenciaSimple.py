#          Ejercicio n°2 herencia
#               Herencia Simple

# Este es el ejercicio mas basico de herencia

#Realice un programa en python utilizado herencia simple
#El programa debe calcular el valor venta de articulos electronicos
#Atributos a considerar: RutCliente, Nombre, Producto, Cantidad, ValorProducto, Total, Dcto y TotalPagar

#Descuento = -Si total > 100.000 se aplica un 10% de dcto del total
#            -Si total > 300.000 se aplica un 20% de dcto del total
#            -Si total >= 400.000 y < 500.000 se aplica un 30% de dcto del total
#            -Si total > 800.000 se aplica un 40% de dcto del total

#El programa debe tener a lo menos 2 clases, una clase padre y la otra clase hija
#La clase padre debe tener a lo menos :
# 2 Variables publicas, 4 metodos o funciones (init, IngresoDatos, Calculos, MostrarDatos)


from os import system
system("cls")

class Tienda():

    a = 20
    b = 20