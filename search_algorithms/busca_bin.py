def buscaBin(num,vetor):

    encontrado = False
    inicio = 0
    final = len(vetor)-1
    meio = round((final-inicio)/2)
    comparacoes = 0

    while not encontrado and meio < len(vetor):
        
        comparacoes += 1
        
        if vetor[meio] == num:
                encontrado = True

        if vetor[meio] > num:
                final = meio
                meio = round((final+inicio)/2)

        elif vetor[meio] < num:
                inicio = meio
                meio = round((final+inicio)/2)+1

    if encontrado:
          return "tamanho do vetor: " + str(len(vetor)), "índice: " + str(meio), "comparações: " + str(comparacoes)
    else:
          return "tamanho do vetor: " + str(len(vetor)), "número não encontrado", "comparações: " + str(comparacoes)


vetor2 = [1,2,3,5,12,14,15,21,24,45,46,47,53,86,90,93]

print(buscaBin(1,vetor2))

#muito mais eficiente que o sequencial, porém só funciona com o vetor ordenado