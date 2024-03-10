"""
Cuando en un número la diferencia entre cada par de dígitos consecutivos es uno, se lo llama número "step"
(como el 123234, el 9876787654, etc.).
Escribir una función, que reciba como parámetro un número y devuelva True si es un número step o False si
no lo es.
"""

def numero_step(numero):
   for i in range(len(numero) - 1):
        if abs(int(numero[i]) - int(numero[i+1])) != 1:
            return False
        return True


num= input("Ingrese un numero: ")
print(numero_step(num))


