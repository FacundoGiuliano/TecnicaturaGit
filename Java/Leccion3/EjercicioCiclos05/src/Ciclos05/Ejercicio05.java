
package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, contador = 0;
        aleatorio = (int)(Math.random() * 100); //Numero aleatorio
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            if (numero < aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero MAYOR.");
            }
            else if (numero > aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero MENOR.");
            }
            else {
                JOptionPane.showMessageDialog(null, "USTED HA GANADO EL JUEGO");
            }
            contador ++;
        } while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "En: "+contador+" intentos!!!.");
    }
}
