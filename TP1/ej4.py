"""
Realizar una función, que reciba como parámetro una lista compuesta por números enteros y que nos
devuelva otra lista con el mismo contenido pero ordenada de mayor a menor.

"""
lista = [98,94,2,4,5,36,64,35,1,20,31,54,9,22]

def ordenar_lista(lista):
    lista.sort()
    print(f"La lista ordenada es igual a {lista}")


print(f"La lista sin ordenar es igual a {lista}")
ordenar_lista(lista)