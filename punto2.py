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
    error = False
    try:
        oben.insertarObra(lista, nombre)
    except ReferenceError:
        error = True
    if error:
        print("Error al agregar la obra '" + nombre +"'.")
    else:
        print("La obra '" + nombre +"' ha sido agregada en el inventario.")

def venderReplica(lista, nombre):
    error = False
    try:
        oben.sustraerObra(lista, nombre)
    except FileNotFoundError:
        error = True
    if error:
        print("Error, la obra '" + nombre +"' no se encuentra disponible en el inventario.")
    else:
        print("Se ha vendido una replica de la obra '" + nombre + "'.")

def listarReplicas(lista):
    try:
        oben.verificarListaVacia(lista)
    except True:
        print("El inventarío se encuentra vacio.")
        
    oben.mostrarObras(lista)

#ejemplos y pruebas

#ejemplo 1:
inv1 = oben()
agregarReplica(inv1, "Mona Lisa")
agregarReplica(inv1, "Mona Lisa")
agregarReplica(inv1, "El grito")
agregarReplica(inv1, "Mona Lisa")
listarReplicas(inv1)
venderReplica(inv1, "Mona Lisa")
listarReplicas(inv1)
print("______________________________________________")

#ejemplo 2
inv2 = oben()
agregarReplica(inv2, "El hijo del hombre")
agregarReplica(inv2, "La gran ola de Kanagawa")
agregarReplica(inv2, "El hijo del hombre")
venderReplica(inv2, "La gran ola de Kanagawa")
venderReplica(inv2, "La gran ola de Kanagawa")
listarReplicas(inv2)
print("______________________________________________")

#ejemplo 3
inv3 = oben()
listarReplicas(inv3)
agregarReplica(inv3, "Gótico estadounidense")
agregarReplica(inv3, "La dama del armiño")
agregarReplica(inv3, "La última cena")
agregarReplica(inv3, "La persistencia de la memoria")
agregarReplica(inv3, "La dama del armiño")
agregarReplica(inv3, "La persistencia de la memoria")
venderReplica(inv3, "La joven de la perla")
listarReplicas(inv3)