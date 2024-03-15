"""
Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista con los
nombres de los hijos.
Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de todos sus
hijos.
"""

class Familia:
    def __init__(self):
        self.padre = input("Padre: ")
        self.madre = input("Madre: ")
        self.hijos = ["Juan","Valentin","Juana"]

    def __str__(self):
        return f" Padre:{self.padre}, Madre:{self.madre}, Hijos:{self.hijos}"
    

print(Familia())