
package caja;

public class Caja {
    int ancho;
    int alto;
    int profundidad;
    
    public Caja() {
        
    }
    
    public Caja(int ancho,int  alto,int profundidad) {
        this.alto = alto;
        this.ancho = ancho;
        this.profundidad = profundidad;
    }
    
    public int calcularVolumen() {
        return ancho * alto * profundidad;
    }
}
