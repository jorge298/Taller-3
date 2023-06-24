"""
grupo de estudio:
archivo de prueba para crear, insertar, buscar y eliminar en listas enlazadas de acuerdo a
como estan definidas en listaEnlazada.py
20/06/23
"""

from listaEnlazada import ListaEnlazada as len

listaPrueba1 = None  # <---mala
listaPrueba2 = len()  # <---buena

#prueba de insersión y traer dato
#listaPrueba1 = len.insertar(listaPrueba1, 1)
listaprueba2 = len.insertar(listaPrueba2, 2)
listaprueba2 = len.insertar(listaPrueba2, 4)
dato = len.traerIndice(listaPrueba2, 1)
print(dato)
#funciona

#prueba de borrado
listaprueba2= len.borrar(4)
dato = len.traerIndice(listaPrueba2, 1)
print(dato)