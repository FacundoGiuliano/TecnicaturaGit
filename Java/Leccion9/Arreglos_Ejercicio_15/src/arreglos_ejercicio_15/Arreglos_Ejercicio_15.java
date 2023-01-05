/*
Ejercicio 15: Leer 10 enteros ordenados crecientemente. Leer N y buscarlo en la tabla.
Se debe mostrar la posicion en que se encuentra. Si no esta, indicarlo con un mensaje.
 */
package arreglos_ejercicio_15;

import java.util.Scanner;

public class Arreglos_Ejercicio_15 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int serie1[] = new int[10];
        int numero;
        boolean creciente = true;
        
        System.out.println("Llenado de tabla N 1: ");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.print((i)+". Digite un numero: ");
                serie1[i] = entrada.nextInt();
            }
            
            // Comprobamos si esta ordenado de forma creciente
            for (int i = 0; i < 9; i++) {
                if(serie1[i] < serie1[i+1]) { //creciente 1,2,3
                    creciente = true;
                }
                if(serie1[i] > serie1[i+1]) {
                    creciente = false;
                    break;
                }
            }
            
            if (creciente == false) {
                System.out.println("\nEl arreglo no esta ordenado en forma creciente, vuelva a digitar\n");
            }
        }while(creciente == false);
        
        int posicion;
        System.out.print("Digite un numero a buscar: ");
        numero = entrada.nextInt();
        boolean bandera = false;
                
        for (int j = 0; j < 10; j++) {
            if(numero == serie1[j]) {
                bandera = true;
                posicion = j;
                System.out.println("La posicion del numero es: "+posicion);   
            }
        }
        if(bandera == false) {
            System.out.println("No se encontro el numero.");
        }
    }
}
