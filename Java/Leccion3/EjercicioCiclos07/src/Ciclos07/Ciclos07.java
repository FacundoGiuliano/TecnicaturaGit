/*
Pedir numeros hasta que se introduzca uno negativo y calcular la media.
*/

package Ciclos07;

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, cantidad = 0, suma = 0;
        float promedio = 0;
        do {
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if (numero < 0) {
                break;
            }
            else if (numero == 0) {
                System.out.println("Error, no se puede dividir entre 0");
            }
            cantidad ++;
            suma += numero;
        } while (numero >= 0);
        promedio = (float)suma/cantidad;
        System.out.println("La media de los numeros introducidos es : "+promedio);
    }
}
