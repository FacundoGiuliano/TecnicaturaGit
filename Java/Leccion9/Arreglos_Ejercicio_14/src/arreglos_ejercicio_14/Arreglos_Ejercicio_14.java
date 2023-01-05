/*
Ejercicio 14: Leer dos series de 10 enteros, que estaran ordenados crecientemente.
Copiar (fusionar) las dos tablas en una tercera, de forma que sigan ordenados.
 */
package arreglos_ejercicio_14;

import java.util.Scanner;

public class Arreglos_Ejercicio_14 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int serie1[] = new int[10];
        int serie2[] = new int[10];
        int serie3[] = new int[20];
        boolean creciente = true;
        
        System.out.println("Llenado de tabla N 1: ");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.print((i+1)+" .Digite un numero: ");
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
        
        System.out.println("Llenado de tabla N° 2: ");
        do{
            for (int i = 0; i < 10; i++) {
                System.out.print((i+1)+" .Digite un numero: ");
                serie2[i] = entrada.nextInt();
            }
            
            // Comprobamos si esta ordenado de forma creciente
            for (int i = 0; i < 9; i++) {
                if(serie2[i] < serie2[i+1]) { //creciente 1,2,3
                    creciente = true;
                }
                if(serie2[i] > serie2[i+1]) {
                    creciente = false;
                    break;
                }
            }
            
            if (creciente == false) {
                System.out.println("\nEl arreglo no esta ordenado en forma creciente, vuelva a digitar\n");
            }
        }while(creciente == false);
        
        int i = 0, j = 0, k = 0;
        
        while(i < 10 && j < 10) {
            if(serie1[i] < serie2[j]) {
                serie3[k] = serie1[i];
                i++;
            }
            else {
                serie3[k] = serie2[j];
                j++;
            }
            k++;
        }
        
        if(i==10) {
            while(j < 10) {
                serie3[k] = serie2[j];
                j++;
                k++;
            }
        }
        else{
            while(i < 10) {
                serie3[k] = serie1[i];
                i++;
                k++;
            }
        }
        
        System.out.println("\nEl arreglo completo es: ");
        for(k = 0; k < 20 ;k++) {
            System.out.print(serie3[k]+" - ");
        }
        System.out.println();
    }
}
