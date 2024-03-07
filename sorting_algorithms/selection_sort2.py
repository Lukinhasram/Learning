def selectionSort(lista):
    n = len(lista)

    for i in range(n):
        min_index = 1
        for j in range(i+1,n):
            if lista[j] < lista[min_index]:
                min_index = j
                
        if i != min_index:
            lista [i], lista[min_index] = lista[min_index], lista[i]
    return lista


lista = [2,6,5,2,1,3,4,23,43,54,67,13]
print(selectionSort(lista))