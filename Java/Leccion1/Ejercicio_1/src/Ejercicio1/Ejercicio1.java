
//Ejercicio: Tienda de libros
//Mostrar: Ingrese los siguientes datos del libro
//Digite el nombre del libro
//Digite el ID del libro
//Digite el precio del libro
//Indicar si el envío es gratuito (True/False)
//Mostrar:
//	Nombre:
//	ID: 
//	Precio:
//	Envío Gratuito?:



package Ejercicio1;

import java.util.Scanner;


public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese los siguientes datos del libro: ");
        System.out.println("Digite el nombre del libro:");
        String nombre = entrada.nextLine();
        System.out.println("Digite el ID del libro:");
        int ID = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro: ");
        double precio = Double.parseDouble(entrada.nextLine());
        System.out.println("Indique si el envio es gratuito: ");
        boolean envio = Boolean.parseBoolean(entrada.nextLine());
        
        System.out.println("Nombre: " + nombre);
        System.out.println("ID = " + ID);
        System.out.println("Precio = " + precio);
        System.out.println("Envio = " + envio);
    }
}
