let nombre = prompt("Ingrese su nombre: ");
let apellido = prompt("Ingrese su apellido: ");
alert("Hola " + nombre + " " + apellido);

document.write("<h2> Hola " + nombre + " " + apellido + "</h2>");

let numero1 = parseInt(prompt("Ingrese Número 1:"));
let numero2 = parseInt(prompt("Ingrese Número 2:"));

if (numero1 > numero2) {
    alert(numero1 + " es mayor que " + numero2);
} else if (numero1 == numero2) {
    alert(numero1 + " es igual a " + numero2);
} else {
    alert(numero1 + " es menor que " + numero2);
}


// Imprimir en un alert la suma y resta de numero1 y numero2
alert("Suma = " + (numero1 + numero2) + "\nResta = " + (numero1 - numero2));



// Calcular el factorial de numero1 utilizando un ciclo while
factorial = 1;
i = 1;
while (i <= numero1) {
    factorial *= i;
    i+=1;
}
alert("El factorial de " + numero1 + " es " + factorial);



// Calcular la suma de los primeros numero2 números naturales usando un ciclo for
suma = 0;
for (i = 1; i <= numero2; i++){
    suma +=1;}
alert("la suma de los primeros "+numero2+" numeros naturales es "+suma)



//funciones
alert("Suma = " + sumar(numero1,numero2))

function sumar(n1, n2){
    resultado = n1+n2;
    return resultado;
}

Semana = ["Lunes","Martes","Jueves","Viernes","Sabado","Domingo"]
for(i = 1; i < Semana.length; i++){
    document.write("<br>Dia "+ ( i+1 )+ ": " + Semana[i])
}

n = parseInt(prompt("Ingrese numero del dia: "));
if (n == 1){
    document.write("<h1> Dia " + n + ": "+ semana[n-1] +"</h1>")
} else if (n == 2){
    document.write("<h1> Dia " + n + ": "+ semana[n-1] +"</h1>")
} else if (n == 3){
    document.write("<h1> Dia " + n + ": "+ semana[n-1] +"</h1>")
} else if (n == 4){
    document.write("<h1> Dia " + n + ": "+ semana[n-1] +"</h1>")
} else if (n == 5){
    document.write("<h1> Dia " + n + ": "+ semana[n-1] +"</h1>")
} else if (n == 6){
    document.write("<h1> Dia " + n + ": "+ semana[n-1] +"</h1>")
}else if (n == 7){
    document.write("<h1> Dia " + n + ": "+ semana[n-1] +"</h1>")
}

