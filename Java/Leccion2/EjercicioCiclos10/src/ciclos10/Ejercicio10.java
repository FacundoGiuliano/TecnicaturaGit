
package ciclos10;

import javax.swing.JOptionPane;

public class Ejercicio10 {
    public static void main(String[] args) {
        int total = 0;
        for(int i = 1; i <= 10; i ++) {
            int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            total += numero;
        }
        JOptionPane.showMessageDialog(null, "El resultado de la suma es: "+total);
    }
}
