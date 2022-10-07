/*
Pedir el dia mes y año de una fecha e indicar si la fecha es correcta, suponiendo que todos los meses tienen 30 dias
*/

package Ciclos09;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);
       var correcta = false;
       while (correcta == false) {
            System.out.println("Digite el dia: ");
            int dia = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite el mes: ");
            int mes = Integer.parseInt(entrada.nextLine());
            System.out.println("Digite el año: ");
            int año = Integer.parseInt(entrada.nextLine());
        if ((dia > 0 && dia <= 30) && (mes > 0 && mes <= 12) && (año > 0 && año <= 2022)){
            System.out.println("La fecha ingresada es CORRECTA.");
            correcta = true;
        }
        else {
            System.out.println("La fecha ingresada es INCORRECTA.");
            System.out.println("Intentelo nuevamente: ");
            correcta = false;
            }
        }
    }
}
