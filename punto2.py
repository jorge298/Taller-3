"""
Punto 2
26/06/23

En un museo se guarda la información del inventario de sus obras utilizando una lista simplemente
enlazadas en la que el campo dato es un objeto de la clase Obra. Una Obra en el inventario tiene dos
atributos nombre y cantidad.
>Desarrolle la operación agregarReplica(String nombre)
>Desarrolle la operación venderReplica(String nombre)
>Desarrolle la operación ListarReplicas()
"""

from obraEnlazada import ObraEnlazada as oben

def agregarReplica(lista, nombre):
    #verificar si la lista está vacía
    if oben.verificarListaVacia(lista)is not True:
        oben.insertar()

#def venderReplica(lista, nombre):

#def ListarReplicas(lista):