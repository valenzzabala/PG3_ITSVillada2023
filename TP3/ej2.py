"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo, capturar la excepción ZeroDivisionError.
"""


num1= int(input("Ingrese un numero: "))
num2= int(input("Ingrese otro numero: "))

try:
    divison=num1/num2
    print(f"La division entre {num1 }y {num2} es igual a {divison}")
except ZeroDivisionError:
    print("No puedes dividir por 0")
