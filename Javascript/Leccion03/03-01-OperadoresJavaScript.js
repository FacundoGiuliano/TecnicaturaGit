// Ejercicio para encontrar numeros pares e impares

let parImpar = 10;
if(parImpar % 2 == 0) {
    console.log("Es un numero PAR");
}
else {
    console.log("Es un numero IMPAR");
}

// Ejercicio: es mayor de edad

let edad = 14, adulto = 18;
if( edad >= adulto ) {
    console.log("Es MAYOR de edad")
}
else {
    console.log("Es MENOR de edad")
}

// Ejercicio dentro de un rango

let dentroRango = 5; // Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if (dentroRango >= valMin && dentroRango <= valMax) {
    console.log("Esta dentro del rango");
}
else {
    console.log("Esta fuera del rango");
}

// Ejercicio si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = false;
if (vacaciones || diaDescanso) {
    console.log("El padre puede asistir al juego de su hijo"); 
}
else {
    console.log("El padre no puede asistir al juego de su hijo");
}

// Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2);
let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un numero PAR" : "Es un numero IMPAR";
console.log(resultado2)

// Convertir String a Number
let miNumero = "10";
console.log(typeof miNumero);
let edad2 = Number(miNumero); //funcion para convertir
console.log(typeof edad2);
// Funcion isNan
if(isNaN(edad2)) { // No es un numero , devuelve un booleano
    console.log("La variable no contiene solo numeros")
}
else {
    if(edad2 >= 18) {
        console.log("Puede votar");
    }
    else {
    console.log("No puede votar");
    }
}

let resultado3 = edad2 >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado3);





