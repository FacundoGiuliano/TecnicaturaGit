/*
Pedir un numero N, y mostrar todos los numeros del 1 al N.
*/

package Ciclos08;

import java.util.Scanner;


public class Ciclos08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int inicio = 1;
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        while (inicio <= numero) {
            System.out.println(inicio);
            inicio ++;
        }
    }
}
