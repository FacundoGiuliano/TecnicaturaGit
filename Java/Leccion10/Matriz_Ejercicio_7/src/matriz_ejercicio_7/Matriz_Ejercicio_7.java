/*
Ejercicio 7: Crear una matriz "marco" de tamaño 5x5: todos sus elementos deben ser 0 salvo los de los borden que deben ser 1. Mostrarla
 */
package matriz_ejercicio_7;

public class Matriz_Ejercicio_7 {
    public static void main(String[] args) {
        int matriz[][] = new int[5][5];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if(i == 0 || i == 4 || j == 0 || j == 4) {
                    matriz[i][j] = 1;
                }
            }
        }
        
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("");
        }
    }
}
