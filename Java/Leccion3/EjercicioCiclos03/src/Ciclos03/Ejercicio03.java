
package Ciclos03;

import javax.swing.JOptionPane;


public class Ejercicio03 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El numero ingresado es PAR");
            }
            else {
                JOptionPane.showMessageDialog(null, "El numero ingresado es PAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero 0 finaliza el programa.");
    }
}
