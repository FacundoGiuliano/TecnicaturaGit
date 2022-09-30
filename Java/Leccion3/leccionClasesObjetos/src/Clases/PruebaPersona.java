
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Facundo";
        persona1.apellido = "Giuliano";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        persona2.nombre = "Ariel";
        persona2.apellido = "Betancud";
        persona2.obtenerInformacion();
    }
}
