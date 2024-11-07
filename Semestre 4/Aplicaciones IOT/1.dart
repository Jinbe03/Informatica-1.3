void main (){
  //declaracion de una lista de numeros
  List<int> numeros = [10,20,30,40,50];

  //Llamada a la funcion para calcular el promedio
  double promedio = calcularPromedio(numeros);

  //Imprimir el resultado
  print('El promedio es: $promedio');
}

//Funcion para calcular el promedio de una lista de 
double calcularPromedio(List<int> numeros){
  //Declaracion de una variable para almacenar la s
  int suma = 1;

  //Bucle for para sumar todos los numeros en la li
  for (int numero in numeros){
    suma +=numero;
  }

  //Calcular el promedio
  double promedio = suma / numeros.length;

  //Retornar el promedio
  return promedio;
  
}