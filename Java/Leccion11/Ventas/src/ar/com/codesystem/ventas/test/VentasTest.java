
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Remera", 5500.00);
        Producto producto4 = new Producto("Medias", 500.00);
        Producto producto5 = new Producto("Corbata", 3000.00);
        Producto producto6 = new Producto("Zapatos", 20000.00);
        Producto producto7 = new Producto("Camisa", 9500.00);
        Producto producto8 = new Producto("Calzoncillo", 2000.00);
        Producto producto9 = new Producto("Saco", 12500.00);
        Producto producto10 = new Producto("Reloj", 35000.00);
        
        Orden orden1 = new Orden();
        // Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto10);
        orden2.mostrarOrden();
    }
}
