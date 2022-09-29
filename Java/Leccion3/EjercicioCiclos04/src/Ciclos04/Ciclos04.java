/*
Pedir numeros hasta que se teclee uno negativo, y mostrar
cuantos numeros se han introducido.
*/
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int cantidad = 0;
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0) {
            cantidad ++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Se introdujo un numero negativo.");
        System.out.println("Se han introducido en total "+cantidad+" numeros positivos.");
    }
}
