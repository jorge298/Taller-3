"""
Punto 1
20/06/23

Desarrolle la operación combinar(Lista L1, Lista L2) que recibe dos listas simplemente enlazadas,
cada una ordenada ascendentemente, y devuelve una lista L3 que tiene los elementos ordenados de ambas
listas. Las listas pueden tener elementos repetidos.

se implica que las listas están ordenadas ascendentemente para este ejercicio
"""

from listaEnlazada import ListaEnlazada as len

def combinar (L1, L2):
    # Verificar si alguna de las listas está vacía (caso triviial)
    if  len.verificarVacio(L1):
        return L2
    if len.verificarVacio(L2):
        return L1
    
    # Crear una lista enlazada vacía para almacenar la combinación
    nuevaLista = len()
    #actual = None

    # Recorrer ambas listas simultáneamente
    while len.verificarVacio(L1) is False and len.verificarVacio(L2) is False:
        if len.traerIndice(L1, 0) <= len.traerIndice(L2, 0):
            #Se agrega el nodo de L1 a L3 y se borra de L1
            len.insertar(nuevaLista, len.traerIndice(L1, 0))
            len.borrar(L1, len.traerIndice(L1, 0))
        else:
            #Se agrega el nodo de L2 a L3 y se borra de L2
            len.insertar(nuevaLista, len.traerIndice(L2, 0))
            len.borrar(L2, len.traerIndice(L2, 0))

    #Agregar los nodos restantes de L1 si L2 ya se vació
    while len.verificarVacio(L1) is False:
        len.insertar(nuevaLista, len.traerIndice(L1, 0))
        len.borrar(L1, len.traerIndice(L1, 0))
    
    #Agregar los nodos restantes de L2 si L1 ya se vació
    while len.verificarVacio(L2) is False:
        len.insertar(nuevaLista, len.traerIndice(L2, 0))
        len.borrar(L2, len.traerIndice(L2, 0))
    
    return nuevaLista

# Definir las listas

#Ejemplo 1:

# Lista 1: 1 -> 3 -> 5 -> 7
L1 = len()
len.insertar(L1, 1)
len.insertar(L1, 3)
len.insertar(L1, 5)
len.insertar(L1, 7)
len.insertar(L1, 9)
# Lista 2: 2 -> 4 -> 6 -> 8
L2 = len()
len.insertar(L2, 2)
len.insertar(L2, 4)
len.insertar(L2, 6)
len.insertar(L2, 8)
# Llamar a la función combinar y mostrar el resultado
L3 = combinar(L1, L2)
print("Ejemplo 1:")
len.recorrido(L3)

#Ejemplo 2:

# Lista 1: 1 -> 2 -> 2 -> 7 -> 15
L4 = len()
len.insertar(L4, 1)
len.insertar(L4, 2)
len.insertar(L4, 2)
len.insertar(L4, 7)
len.insertar(L4, 15)
# Lista 2: 0 -> 4 -> 7 -> 10 -> 20
L5 = len()
len.insertar(L5, 0)
len.insertar(L5, 4)
len.insertar(L5, 7)
len.insertar(L5, 10)
len.insertar(L5, 20)
# Llamar a la función combinar y mostrar el resultado
L6 = combinar(L4, L5)
print("Ejemplo 2:")
len.recorrido(L6)

#Ejemplo 3:

# Lista 1: None
L7 = len()
# Lista 2: 5 -> 10 -> 15 -> 20 -> 25
L8 = len()
len.insertar(L8, 5)
len.insertar(L8, 10)
len.insertar(L8, 15)
len.insertar(L8, 20)
len.insertar(L8, 25)
# Llamar a la función combinar y mostrar el resultado
L9 = combinar(L7, L8)
print("Ejemplo 3:")
len.recorrido(L9)