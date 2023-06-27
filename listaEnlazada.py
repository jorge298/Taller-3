"""
grupo de estudio:
Estructura inicial de una lista enlazada
20/06/23
"""

from nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.head = None
    
    def insertar(self, x):
        nodo = Nodo(x)
        actual = self.head # <--error de nonetype

        if actual is None: #anteriormente era: if actual is None
            self.head = nodo
        else:
            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nodo

    def traerIndice(self, i):
        cnt = 0
        actual = self.head
        while cnt < i and actual is not None:
            actual = actual.siguiente
            cnt += 1
        
        if actual is None:
            raise OverflowError
        
        return actual.dato
    
    def borrar(self, v):
        actual = self.head
        anterior = None

        while actual is not None and actual.dato != v:
            anterior = actual
            actual = actual.siguiente
        
        if actual is None:
            raise ReferenceError
        
        if anterior is None:
            self.head = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
    
    def verificarVacio(self):
        if self.head is None:
            return True
        else:
            return False
        
    def recorrido(self):
        aux = self.head
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente