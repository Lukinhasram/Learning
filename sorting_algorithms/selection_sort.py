def selectionSort(lista):
    compcount = 0
    for i in range(len(lista)):
        num_atual = i
        menor = num_atual

        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
            compcount += 1

        lista[menor] , lista[num_atual] = lista[num_atual], lista[menor]

    return lista, compcount



lista = [2,6,5,2,1,3,4,23,43,54,67,13]
print(selectionSort(lista))
