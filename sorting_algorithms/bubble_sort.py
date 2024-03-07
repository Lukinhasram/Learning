def bubbleSort(lista):
    tam_ord = len(lista) -1
    ordenado = False

    while not ordenado:

        ordenado = True

        for i in range(tam_ord):

            if lista[i] > lista[i+1]:
                ordenado = False
                lista[i+1], lista[i] = lista[i], lista[i+1]

    return lista




lista = [2,6,5,2,1,3,4,23,43,54,66,13]
print(bubbleSort(lista))
