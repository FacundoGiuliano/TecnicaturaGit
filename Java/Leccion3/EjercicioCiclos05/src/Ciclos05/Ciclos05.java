/*
Juego para divinar un nomero. Generar un numero aleatorio entre 0-100, y luego
ir pidiendo numeros indicando "es mayor" o "es menor" segun sea mayor o mneor
con respecto a N. El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos.
*/
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        var numAleatorio = (int)(Math.random() * 100); //Numero aleatorio
        System.out.println("El numero aleatorio es: "+numAleatorio);
        var contador = 0;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != numAleatorio) {
            if (numero > numAleatorio) {
                contador ++;
                System.out.println("El numero a adivinar es MENOR que el numero ingresado.");
                System.out.println("Digite otro numero: ");
                numero = Integer.parseInt(entrada.nextLine());
            }
            else {
                contador ++;
                System.out.println("El numero a adivinar es MAYOR que el numero ingresado.");
                System.out.println("Digite un numero: ");
                numero = Integer.parseInt(entrada.nextLine());
            }
        }
        System.out.println("USTED HA GANADO EL JUEGO!!!!!!");
        System.out.println("Numero de intentos fallidos: "+contador);
    }
}
