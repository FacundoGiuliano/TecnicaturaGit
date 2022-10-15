
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        //variables locales, memoria stack
        int a = 10;
        int b = 7;
        miMetodo(); //Llamamos el nuevo metodo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atribuetos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        Persona persona = new Persona("Facundo", "Giuliano");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }
    
    // Modularidad creamos un nuevo metodo
    public static void miMetodo() {
        // int a = 10; //Una variable esta limitada
        System.out.println("Aquie hay otro metodo");
    }
}

// Creamos una nueva clase
class Persona {
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido) { //Constructor
        //super(); //Llamada al contructor de la clase padre Object
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir {
    public Imprimir() {
        super(); //El constructor de la clase padre para reservar memoria
    }
    
    public void imprimir(Persona persona) {
        System.out.println("Persona desde la clase Imprimir "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }
}






