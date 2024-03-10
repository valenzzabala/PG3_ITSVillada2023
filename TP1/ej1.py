lista = [20,10,39,58,46,34,6,8,5,3,1]

def buscar_en_lista(lista,elemento):
    indice = lista.index(elemento)
    print(f"El numero {elemento} se encuentra en el indice: {indice}")

print(f"La lista es: {lista}")

while True:
    elemento = int(input("Ingrese el elemento que desea saber el indice: "))
    if elemento in lista:
        buscar_en_lista(lista,elemento)
        break
            
    else:
        print("El elemento no se encuentra en la lista.")
        break