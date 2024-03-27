def buscaBinR(num,vetor,inicio,final): #tem que por o inicio e o final, pois o meio é calculado a partir deles
    
    if inicio <= final: #se o inicio for maior que o final, o vetor não foi encontrado *
        
        meio = (inicio + final)//2 

        if vetor[meio] == num: #se o meio for igual ao numero, retorna o meio
                return meio
        
        else:

            if vetor[meio] > num: #se o meio for maior que o numero, chama a função com o final sendo o meio-1
                    return buscaBinR(num,vetor,inicio,meio-1)

            elif vetor[meio] < num: #se o meio for menor que o numero, chama a função com o inicio sendo o meio+1
                    return buscaBinR(num,vetor,meio+1,final)

        print(num,inicio,final,meio)

    return "Não encontrado" #se o inicio for maior que o final, o vetor não foi encontrado *
    

vetor1 = [14,21,5,45,12,3,86,98,46,53,24,2,1,15,90,47]
vetor2 = [1,2,3,5,12,14,15,21,24,45,46,47,53,86,90,98]
vetor1ord = vetor1.sort()

print(buscaBinR(14,vetor1,0,15))
print(buscaBinR(46,vetor1,0,15))
print(buscaBinR(90,vetor1,0,15))
print(buscaBinR(50,vetor1,0,15))
#não funcionou para o vetor1, pois ele não está ordenado

print(buscaBinR(14,vetor1ord,0,15))
print(buscaBinR(46,vetor1ord,0,15))
print(buscaBinR(90,vetor1ord,0,15))
print(buscaBinR(50,vetor1ord,0,15))
#funcionou para o vetor1ord, pois ele está ordenado

print(buscaBinR(14,vetor2,0,15))
print(buscaBinR(46,vetor2,0,15))
print(buscaBinR(90,vetor2,0,15))
print(buscaBinR(50,vetor2,0,15))
#funcionou para o vetor2, pois ele está ordenado


"""
A função buscaBinR recebe o número a ser buscado, o vetor ordenado, o índice de início e o índice final do intervalo de busca. 
Ela utiliza a recursão para dividir o intervalo pela metade a cada chamada, até encontrar o número desejado ou determinar que ele não está presente. 
O retorno da função é o índice do número no vetor, se encontrado, ou a string "Não encontrado" caso contrário 

A busca binária só é eficiente em vetores ordenados. 
Se o vetor não estiver ordenado, será necessário primeiro ordená-lo, como foi feito para as chamadas das funções para o vetor1, 
o que pode ter uma complexidade de tempo maior.
"""
