"""
Realizar la carga de dos números enteros por teclado e imprimir su suma, luego preguntar si quiere seguir sumando valores.
Codificar un programas uno que capture la excepción de ingreso de datos no numérico.

"""
print("SUMAR NUMEROS ENTEROS")
numeros = []

try:
    num1= int(input("Ingrese un numero: "))
    numeros.append(num1)
    num2= int(input("Ingrese otro numero: "))
    numeros.append(num2)
    while True:
        opcion= input("¿Desea ingresar otro valor?(s/n)")
        if opcion == 's':
            num = int(input("Ingrese un numero: "))
            numeros.append(num)
            continue
        elif opcion =="n":
            print(f'La suma de los numeros {num1} y {num2} da como resultado: {sum(numeros)}')
            break
        else:
            print("Opcion no valida.")
            break
except ValueError:
    print("El tipo de dato ingresado no es un dato numerico")

