"""
implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los
métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a
Definir dos objetos de la clase Alumno.

"""

class Alumno:
    
    def __init__(self):
        self.nombre= input("Nombre: ")
        self.nota = int(input("Nota: "))
        self.set_datos()
        self.set_estado()

    def set_datos(self):
        print(f"\nNombre:{self.nombre}  Nota: {self.nota}")

    def set_estado(self):
        if (self.nota) >= 4:
            print("\nSu estado es: REGULAR")
        
        else:
            print("\nSu estado es: LIBRE")


alumno1 = Alumno()
alumno2 = Alumno()