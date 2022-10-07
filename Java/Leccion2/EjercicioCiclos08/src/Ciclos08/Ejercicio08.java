
package Ciclos08;

import javax.swing.JOptionPane;

public class Ejercicio08 {
    public static void main(String[] args) {
        int inicio = 1;
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (inicio <= numero) {
            JOptionPane.showMessageDialog(null, inicio);
            inicio ++;
        }
    }
}
