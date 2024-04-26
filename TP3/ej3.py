"""
Almacenar en una tupla los nombres de meses del año. 
Solicitar el ingreso del número de mes y mostrar seguidamente el nombre de dicho mes. 
Capturar la excepción IndexError.

"""

meses = ('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')

a = int(input("Ingrese el numero de mes: "))
indice = a-1
try:
    print(f"El mes es {meses[indice]}")
except IndexError:
    print("Ese no es un numero de mes.")
