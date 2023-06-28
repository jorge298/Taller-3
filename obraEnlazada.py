"""
Estructura inicial para las funciones tipo obra del punto 2
27/06/23
"""

from obra import Obra

class ObraEnlazada:
    def __init__(self):
        self.head = None
    
    def buscarObra(self, nombre):
        actual = self.head
        while actual.nombre != nombre and actual is not None:
            actual = actual.siguiente

        if actual is None:
            raise FileNotFoundError
        else:
            return [actual.nombre, actual.cantidad]

    def insertarObra(self, nombre):
        obraNueva = Obra(nombre, 1)
        actual = self.head

        if actual is None:
            self.head = obraNueva
        else:
            while actual.siguiente is not None and actual.nombre != nombre:
                actual = actual.siguiente
            
            if actual.nombre == nombre:
                actual.cantidad += 1
            else:
                actual.siguiente = obraNueva

    def sustraerObra(self, nombre):
        actual = self.head
        anterior = None

        while actual is not None and actual.nombre != nombre:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            raise FileNotFoundError
        
        if actual.nombre == nombre and actual.cantidad > 1:
            actual.cantidad -= 1

        if actual.nombre == nombre and actual.cantidad <= 1:
            if anterior is None:
                self.head = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
    
    def mostrarObras(self):
        actual = self.head
        print("Nombre de la obra | cantidad de replicas")
        while actual is not None:
            print(actual.nombre + " | " + str(actual.cantidad))
            actual = actual.siguiente
    
    def verificarListaVacia(self):
        if self.head is None:
            return True
        else:
            return False