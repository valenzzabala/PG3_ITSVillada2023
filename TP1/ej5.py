"""
Escribir una función que reciba como parámetro una palabra, y devuelva True si esa palabra es un
palíndromo y False si no lo es.
Ejemplo:
esCapicua("neuquen") === True
esCapicua("jovenes") === False


"""


def capicua(palabra):
    if palabra[::-1]== palabra:
        print("La palabra es capicua")

    else:
        print("La palabra no es capicua")

palabra= input("Ingrese una palabra para determinar si es capicua:")

capicua(palabra)