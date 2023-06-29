/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package punto_3;

/**
 *
 * @author jesus ayala
 * Cristian David Florez Lopez- 1974001
 */
public class PilaConColas {
    
     private Cola colaPila;     

    public PilaConColas() {
         colaPila = new Cola();
    }
    
    public boolean estaVaciaPilaConColas() {
        return colaPila.estaVacia();
    }
    
    public void pushPilaConColas(Object o) {
        colaPila.agregar(o);
    }

    public Object popPilaConColas() {
        if (estaVaciaPilaConColas()) {
            throw new IllegalStateException("La pila está vacía");
        }
        int tamaño = colaPila.tamaño();
        for (int i = 1; i < tamaño; i++) {
            colaPila.agregar(colaPila.eliminar());
        }
        return colaPila.eliminar();
    }

    public Object consultarTopePilaConColas() {
        if (estaVaciaPilaConColas()) {
            throw new IllegalStateException("La pila está vacía");
        }
        int tamaño = colaPila.tamaño();
        for (int i = 1; i < tamaño; i++) {
            colaPila.agregar(colaPila.eliminar());
        }
        Object tope = colaPila.consultarPrimero();
        colaPila.agregar(colaPila.eliminar());
        return tope;
    }

    public void mostrarPilaConColas() {
        if (estaVaciaPilaConColas()) {
            System.out.println("La pila está vacía");
        } else {
            int tamaño = colaPila.tamaño();
            for (int i = 0; i < tamaño; i++) {
                Object elemento = colaPila.eliminar();
                colaPila.agregar(elemento);
                System.out.println(elemento);
            }
        }
    }    
}
