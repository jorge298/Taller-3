"""
Grupo de trabajo:
Punto 1
20/06/23
"""
from listaEnlazada import ListaEnlazada as len
#from nodo import Nodo

def combinar (L1, L2):
    # Verificar si alguna de las listas está vacía (caso triviial)
    if  len.verificarVacio(L1):
        return L2
    if len.verificarVacio(L2):
        return L1
    
    # Crear una lista enlazada vacía para almacenar la combinación
    L3 = None
    actual = None

    # Recorrer ambas listas simultáneamente
    while len.verificarVacio(L1) and len.verificarVacio(L2):
        if len.traerIndice(L1) <= len.traerIndice(L2):
            #Se agrega el nodo de L1 a L3 y se borra de L1
            len.insertar(L3, len.traerIndice(L1))
            len.borrar(L1, len.traerIndice(L1))
        else:
            #Se agrega el nodo de L2 a L3 y se borra de L2
            len.insertar(L3, len.traerIndice(L2))
            len.borrar(L2, len.traerIndice(L2))

    #Agregar los nodos restantes de L1 si L2 ya se vació
    while len.verificarVacio(L1):
        len.insertar(L3, len.traerIndice(L1))
        len.borrar(L1, len.traerIndice(L1))
    
    #Agregar los nodos restantes de L2 si L1 ya se vació
    while len.verificarVacio(L2):
        len.insertar(L3, len.traerIndice(L2))
        len.borrar(L2, len.traerIndice(L2))
    
    return L3

# Definir las listas
# Lista 1: 1 -> 3 -> 5 -> 7

L1 = len(None)
len.insertar(L1, 1)
len.insertar(L1, 3)
len.insertar(L1, 5)
len.insertar(L1, 7)
len.insertar(L1, 9)


# Lista 2: 2 -> 4 -> 6 -> 8
L2 = len(None)
len.insertar(L2, 2)
len.insertar(L2, 4)
len.insertar(L2, 6)
len.insertar(L2, 8)


# Llamar a la función combinar
L3 = combinar(L1, L2)

#mostrar el primer indice de L3
print(len.traerIndice(L3,1))

# Imprimir la lista combinada
"""
while not(len.verificarVacio(L3)):
    print(len.traerIndice(L3), end=" -> ")
    len.borrar(L3,len.traerIndice(L3))
print("None")
"""