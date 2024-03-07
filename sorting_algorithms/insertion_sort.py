def inserionSort(lista):
    compcount = 0
    tam_ord = range(1, len(lista))
    for i in tam_ord:
        num_atual = lista[i]

        while lista[i-1] > num_atual and i>0:
            compcount += 1
            lista[i-1], lista[i] = lista[i], lista[i-1]
            i = i-1
    return lista, compcount


lista = [2,6,5,2,1,3,4]
print(inserionSort(lista))
