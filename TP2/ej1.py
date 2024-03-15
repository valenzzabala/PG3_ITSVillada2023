"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos
métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará
en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona.
"""


class Persona:

    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
    def saludar(self):
        print(f"Hola {self.nombre}, bienvenido.")


alumno1=Persona()
alumno1.saludar()


alumno2=Persona()
alumno2.saludar()