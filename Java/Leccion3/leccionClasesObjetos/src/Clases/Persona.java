
package Clases;

public class Persona {
    //Atributos de la clase (CARACTERISTICAS)
    public String nombre;
    public String apellido;
    
    //Metodos de la clase (ACCIONES)
    public void obtenerInformacion() { //Puede recibir argumentos
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
    }
}
