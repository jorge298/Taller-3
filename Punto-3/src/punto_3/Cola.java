
package punto_3;

/**
 *
 * @author jesus ayala
 * Cristian David Florez Lopez- 1974001
 */
public class Cola {
    private Nodo frente;
    private Nodo fin;
    private int tamaño;

    private class Nodo {
        Object dato;
        Nodo siguiente;

        public Nodo(Object dato) {
            this.dato = dato;
            this.siguiente = null;
        }
    }

    public Cola() {
        frente = null;
        fin = null;
        tamaño = 0;
    }

    public boolean estaVacia() {
        return tamaño == 0;
    }

    public void agregar(Object elemento) {
        Nodo nuevoNodo = new Nodo(elemento);
        if (estaVacia()) {
            frente = nuevoNodo;
            fin = nuevoNodo;
        } else {
            fin.siguiente = nuevoNodo;
            fin = nuevoNodo;
        }
        tamaño++;
    }

    public Object eliminar() {
        if (estaVacia()) {
            throw new IllegalStateException("La cola está vacía");
        }
        Object elemento = frente.dato;
        frente = frente.siguiente;
        tamaño--;
        if (estaVacia()) {
            fin = null;
        }
        return elemento;
    }

    public Object consultarPrimero() {
        if (estaVacia()) {
            throw new IllegalStateException("La cola está vacía");
        }
        return frente.dato;
    }

    public int tamaño() {
        return tamaño;
    }
}

