/*
Ejercicio 3: Leer numeros hasta que se introduzca un 0
Para cada uno indicar si es par o impar.
Primero con la clase Scanner
Luego con la clase JOptionPane
*/

package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println("El numero ingresado es PAR");
            }
            else {
                System.out.println("El numero ingresado es IMPAR");
            }
            System.out.println("Digite oto numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero 0 finaliza el programa.");
    }
}
