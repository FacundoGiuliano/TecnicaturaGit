var nombre = "Jose ";
var apellido = "Montes"
var nombreCompleto = nombre+" "+apellido;
console.log(nombreCompleto);
var nombreCompleto2 = "Facundo"+" "+"Giuliano";
console.log(nombreCompleto2);
// Lee de izq a der. Se pueden usar parentesis
var juntos = nombre + (219 + 1);
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos)

nombre += apellido;
console.log(nombre);

// Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lopez"; // una constante no puede ser modificada
console.log(apellido2)

let x, y;

x = 17, y = 21; // Se pueden asignar varias variables en una sola linea

let z = x + y; // Se asigna el valor de una operacion
console.log(z);

let _1num = 31; // No utilizar numeros para el comienzo del nombre de la variable
let rompiendo = "rompe" // Tampoco nmbre de palabras reservadas

console.log(_1num)
console.log(rompiendo)







