"""
Escribir una función que reciba como parámetro una frase y devuelva la cantidad de vocales que ésta tiene
"""

def vocales(frase):
    vocales = ["a","e","i","o","u"]
    contador = 0
    for elem in frase:
        if elem in vocales:
           contador+=1
    print(f"La cantidad de vocales en la frase: {contador}")


frase= input("Ingrese una frase: ")
frase.lower()
vocales(frase)