//Crear una matriz de tamaño 7x7 y rellenarla de forma que su diagonal principal sean 1 y el resto 0.

package matriz_ejercicio_4;

public class Matriz_Ejercicio_4 {
    public static void main(String[] args) {
        
        int matriz[][] = new int[7][7];
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                if (i==j) {
                    matriz[i][j] = 1;
                }
                else {
                    matriz[i][j] = 0;
                }
            }
        }
        System.out.println("Matriz: ");
        System.out.println();
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
