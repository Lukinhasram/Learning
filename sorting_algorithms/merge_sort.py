def mergeSort(lista, inicio = 0, fim = None):
    if fim == None:
        fim = len(lista)

    if fim - inicio > 1:

        meio = (inicio + fim)//2

        mergeSort(lista,inicio,meio)
        mergeSort(lista,meio,fim)
        
        merge(lista,inicio,meio,fim)

def merge(lista, inicio, meio, fim):

    esq = lista[inicio:meio]
    dir = lista[meio:fim]

    frente_esq, frente_dir = 0, 0

    for k in range(inicio,fim):

        if frente_esq >= len(esq):
            lista[k] = dir[frente_dir]
            frente_dir += 1
            
        elif frente_dir >= len(dir):
            lista[k] = esq[frente_esq]
            frente_esq += 1

        elif esq[frente_esq] < dir[frente_dir]:
            lista[k] = esq[frente_esq]
            frente_esq += 1

        else:
            lista[k] = dir[frente_dir]
            frente_dir += 1



lista = [2,6,5,2,1,3,4]
mergeSort(lista)
print(lista)