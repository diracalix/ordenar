def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


entrada_usuario = input("Ingresa una lista de números separados por comas: ")
numeros = [int(num) for num in entrada_usuario.split(",")]

ordenamiento_burbuja(numeros)
print("Lista ordenada:", numeros)
