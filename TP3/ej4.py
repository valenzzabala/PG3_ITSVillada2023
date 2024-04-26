"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo,
 capturar las excepciones ZeroDivisionError y ValueError.
"""

try:
    num1= int(input("Ingrese un numero: "))
    num2= int(input("Ingrese otro numero: "))
    print(f"La division es {num1/num2}")

except ZeroDivisionError:
    print("No es posible dividir por 0")

except ValueError:
    print("El tipo de dato ingresado no es numerico")


