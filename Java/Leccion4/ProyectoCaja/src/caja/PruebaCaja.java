// Crear un proyecto se gun als especificaciones mostradas a continuacion.
// La formula es: volumen = ancho * alto * profundidad

package caja;


public class PruebaCaja {
    public static void main(String[] args) {
        // Variables locales
        int medidaAncho = 3;
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja();
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProf;
        int resultado = caja1.calcularVolumen(); // Llamamos al metrodo
        System.out.println("El volumen de caja 1 es: "+resultado); //Primer resultado
        
        Caja caja2 = new Caja(2, 4, 6); // Llamamos al contructor 2 con nuevos argumentos
        System.out.println("El volumen de la caja 2 es: " + caja2.calcularVolumen());
    }
}
