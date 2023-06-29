/*
 * 
 */
package punto_3;

/**
 *
 * @author jesus ayala
 * Cristian David Florez Lopez- 1974001
 */
public class Pruebas {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        PilaConColas pila = new PilaConColas();
        PilaConColas pila2 = new PilaConColas();
        PilaConColas pila3 = new PilaConColas();

        // Ejemplo para probar la operación "estaVaciaPilaConColas()"
        System.out.println("¿La pila está vacía? " + pila.estaVaciaPilaConColas());  // Salida esperada: true

        // Ejemplo para probar la operación "pushPilaConColas(Object o)"
        pila.pushPilaConColas("Elemento 1");
        pila.pushPilaConColas("Elemento 2");
        pila.pushPilaConColas("Elemento 3");

       
        // Ejemplo para probar la operación "popPilaConColas()"
        System.out.println("Elemento eliminado: " + pila.popPilaConColas());  // Salida esperada: Elemento 3

        // Ejemplo para probar la operación "consultarTopePilaConColas()"
        System.out.println("Tope de la pila: " + pila.consultarTopePilaConColas());  // Salida esperada: Elemento 2

        // Ejemplo para probar la operación "mostrarPilaConColas()"
        System.out.println("Elementos de la pila:");
        pila.mostrarPilaConColas();
        // Salida esperada:
        // Elemento 1


        pila3.pushPilaConColas(1);
        pila3.pushPilaConColas(2);
        pila3.pushPilaConColas(3);
        pila3.pushPilaConColas(4);
        pila3.pushPilaConColas(5);

        System.out.println("Elementos de la pila3:");
        pila3.mostrarPilaConColas();
         // Ejemplo para probar la operación "estaVaciaPilaConColas()"
        System.out.println("¿La pila 3 está vacía? " + pila3.estaVaciaPilaConColas());  // Salida esperada: false




        // Ejemplo adicional para probar la operación "estaVaciaPilaConColas()" después de eliminar todos los elementos
        System.out.println("¿La pila está vacía? " + pila.estaVaciaPilaConColas());  // Salida esperada: false
        System.out.println("¿La pila2 está vacía? " + pila2.estaVaciaPilaConColas());  // Salida esperada: true
    }
    
    }
    

