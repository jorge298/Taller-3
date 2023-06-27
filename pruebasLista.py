"""
grupo de estudio:
archivo de prueba para crear, insertar, buscar y eliminar en listas enlazadas de acuerdo a
como estan definidas en listaEnlazada.py
20/06/23
"""

from listaEnlazada import ListaEnlazada as len

listaPrueba1 = None  # <---mala
listaPrueba2 = len()  # <---buena

#prueba de inserción y traer dato
listaprueba2 = len.insertar(listaPrueba2, 2)
listaprueba2 = len.insertar(listaPrueba2, 4)
dato1 = len.traerIndice(listaPrueba2, 0)
print(dato1)
#funciona

#prueba de borrado
#len.borrar(listaPrueba2, 4)
dato2 = len.traerIndice(listaPrueba2, 0)
print(dato2)

#prueba de lista vacía
listaPrueba3 = len()
listaPrueba4 = len()
len.insertar(listaPrueba4, 7)
print(len.verificarVacio(listaPrueba3))
print(len.verificarVacio(listaPrueba4))