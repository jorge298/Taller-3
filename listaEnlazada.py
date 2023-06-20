"""
grupo de estudio:
Estructura inicial de una lista enlazada
20/06/23
"""

from node import Node

class ListaEnlazada:
    def __init__(self):
        self.head = None
    
    def insertar(self, x):
        nodo = Node(x)
        actual = self.head

        if actual is None:
            self.head = nodo
        else:
            while actual.ptrNext is not None:
                actual = actual.ptrNext

            actual.ptrNext = nodo

    def traerIndice(self, i):
        cnt = 0
        actual = self.head
        while cnt < i and actual is not None:
            actual = actual.ptrNext
            cnt += 1
        
        if actual is None:
            raise OverflowError
        
        return actual.value
    
    def borrar(self, v):
        actual = self.head
        anterior = None

        while actual is not None and actual.value != v:
            anterior = actual
            actual = actual.ptrNext
        
        if actual is None:
            raise ReferenceError
        
        if anterior is None
            self.head = actual.ptrNext
        else:
            anterior.ptrNext = actual.ptrNext