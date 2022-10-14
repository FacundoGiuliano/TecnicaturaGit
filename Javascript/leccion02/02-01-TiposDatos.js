// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/

var nombre = 'Ariel'; //Tipo Str
console.log(typeof nombre);
numero = 7;
console.log(typeof numero)
nombre = 12.3;
console.log(typeof nombre);    

var numero = 3000; // Tipo Numérico
console.log(numero);

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2614567893"
}

console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion() {}
console.log(typeof miFuncion);

//Tipo de dato Syembol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato clase (en js es una funcion)
class Persona {
    constructor(nombre,apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x); 

x = undefined;
console.log(typeof x);

// null: significa ausencia de valor

var y = null; // null no es un tipo de dato pero su origen es object
console.log(typeof y);

// Tipo de dato array y Empty String
var autos = ["Citroen", "Audi", "BMW"];
console.log(autos);
console.log(typeof autos);

var z = "";
console.log(z);
console.log(typeof z);







