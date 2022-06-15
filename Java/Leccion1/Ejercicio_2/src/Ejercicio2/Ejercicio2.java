package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese cuantas horas trabaja semanalmente: ");
        int horas = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese cuanto es su salario por hora: ");
        float salarioHora = Float.parseFloat(entrada.nextLine());
        System.out.println("Horas: " + horas);
        System.out.println("Salario por hora: " + salarioHora);
        var salario = (horas * salarioHora) * 4;
        System.out.println("\nSalario semanal: USD" + salario);        
    }
}
