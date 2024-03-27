def buscaSeq(num,vetor):
    comparacoes = 0
    
    for n in range(len(vetor)):
        comparacoes += 1

        if vetor[n] == num:
            return "tamanho do vetor: " + str(len (vetor)), "índice: " + str(n), "comparações: " + str(comparacoes)
        
    return "tamanho do vetor: " + str(len (vetor)), "número não localizado", "comparações: " + str(comparacoes)

vetor1 = [14,21,5,45,12,3,86,98,46,53,24,2,1,15,90,47]
vetor2 = [1,2,3,5,12,14,15,21,24,45,46,47,53,86,90,98]

print(buscaSeq(5, vetor2))

#menos eficiente que o binário, mas funciona com o vetor não ordenado
