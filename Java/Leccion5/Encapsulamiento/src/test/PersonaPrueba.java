
package test;

//import dominio.*; importamos todas las clases del package
import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modififcar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        // persona1.nombre = "Juan Ignacio"; Ya no se puede utilizar
        // System.out.println("Nombre: "+persona1.nombre); Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        // Tarea: crear un nuevo objeto de tipo persona con sus valores iniciales, luego modificarlos y volver a imprimir
        Persona persona2 = new Persona("Homero", 80.000, true);
        System.out.println("\npersona2 con su nombre: "+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());
        
        persona2.setNombre("Bart");
        persona2.setSueldo(60.000);
        persona2.setEliminado(false);
        System.out.println("\npersona2 con su nombre modificado: "+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo modificado: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano modificado: "+persona2.isEliminado());
        
        System.out.println("persona1 = " + persona1); // Metodo toString
        
    }
}
