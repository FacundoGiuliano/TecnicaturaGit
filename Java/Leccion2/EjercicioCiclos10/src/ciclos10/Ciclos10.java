// Pedir 10 numeros y escribir la suma total

package ciclos10;

import java.util.Scanner;


public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int contador = 0;
        int total = 0;
        
        for(int i = 1; i <= 10; i ++) {
            System.out.println("Digite un numero a sumar: ");
            int numero = Integer.parseInt(entrada.nextLine());
            total += numero;
        }
        System.out.println("El total de la suma de numeros igresados es: "+total);
        
        while (contador < 10) {
            System.out.println("Digite un numero a sumar: ");
            int numero = Integer.parseInt(entrada.nextLine());
            contador ++;
            total += numero;
        }
        System.out.println("El total de la suma de numeros igresados es: "+total);
    }
}
