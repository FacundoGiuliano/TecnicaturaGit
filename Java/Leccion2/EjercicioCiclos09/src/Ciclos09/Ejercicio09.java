
package Ciclos09;

import javax.swing.JOptionPane;

public class Ejercicio09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el dia: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
        int año = Integer.parseInt(JOptionPane.showInputDialog("Digite el año: "));
        if ((dia != 0) && (dia <= 30)) {
            if ((mes != 0) && (mes <= 12)) {
                if ((año != 0) && (año <= 2022)) {
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+dia+"/"+mes+"/"+año);
                }
                else {
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                }
            }
            else {
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
            }
        }
        else {
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, dia incorrecto");
        }
    }
}
