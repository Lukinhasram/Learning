class Item():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None

class Lista():
    #inicializando a lista
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    #inserindo no inicio
    def inserir_inicio(self, item):
        #se a lista estiver vazia
        if self.inicio is None:
            #o item que está sendo inserido, passa a ser o inicio e o fim da lista
            self.inicio = item
            self.fim = item
            item.proximo = item
            item.anterior = item
        #se a lista não estiver vazia
        else:
            #o item que está no inicio da lista, passa a ser o próximo do item que está sendo inserido, e o anterior do item que está no inicio da lista, passa a ser o item que está sendo inserido
            item.proximo = self.inicio
            item.anterior = self.fim
            self.inicio.anterior = item
            self.fim.proximo = item
            self.inicio = item
    
    #inserindo no fim
    def inserir_fim(self, item):
        #se a lista estiver vazia
        if self.inicio is None:
            #o item que está sendo inserido, passa a ser o inicio e o fim da lista
            self.inicio = item
            self.fim = item
            item.proximo = item
            item.anterior = item
        #se a lista não estiver vazia
        else:
            #o item que está no fim da lista, passa a ser o próximo do item que está sendo inserido, e o anterior do item que está no fim da lista, passa a ser o item que está sendo inserido
            item.anterior = self.fim
            item.proximo = self.inicio
            self.fim.proximo = item
            self.inicio.anterior = item
            self.fim = item
    
    def inserir_vetor(self, vetor):
        #para cada item no vetor, insere no fim da lista
        for i in vetor:

            self.inserir_fim(Item(i[0], i[1]))

    #imprimindo a lista
    def imprimir(self):
        #se a lista estiver vazia, imprime "Lista vazia"
        if self.inicio is None:
            print("Lista vazia")
            return
        #ordem normal
        item_atual = self.inicio
        #enquanto o item atual não for o inicio, imprime o nome e a nota do item atual
        while True:
            print(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo
            if item_atual == self.inicio:
                break
        
    def imprimir_inverso(self):
        #ordem reversa
        item_atual = self.fim
        #enquanto o item atual não for o fim, imprime o nome e a nota do item atual
        while True:
            print(item_atual.nome, item_atual.nota)
            item_atual = item_atual.anterior
            if item_atual == self.fim:
                break
    
    #verificando se a lista está vazia
    def vazia(self):
        return self.inicio is None
    
    #buscando um elemento
    def buscar(self, nome):
        #se a lista estiver vazia, imprime "Lista vazia"
        if self.inicio is None:
            print("Lista vazia")
            return

        item_atual = self.inicio

        while True:
            #se o nome do item atual for igual ao nome que está sendo buscado, imprime o nome e a nota do item atual
            if item_atual.nome == nome:
                print("aluno(a): ", item_atual.nome, item_atual.nota)
                return
            item_atual = item_atual.proximo
            if item_atual == self.inicio:
                break
        #se o nome não for encontrado, imprime que não foi possível achar o aluno
        print("não foi possível achar o aluno(a) com o nome de: ", nome)
    
    #retirando um elemento
    def retirar(self, nome):
        #se a lista estiver vazia, imprime "Lista vazia"
        if self.inicio is None:
            print("Lista vazia")
            return

        item_atual = self.inicio

        while True:
            
            if item_atual.nome == nome:
                #se o item atual for o inicio, o item que está no fim da lista, passa a ser o próximo do item atual, e o próximo do item atual, passa a ser o inicio da lista
                if item_atual == self.inicio:
                    self.inicio = item_atual.proximo
                    self.fim.proximo = self.inicio
                    self.inicio.anterior = self.fim
                #senão, o próximo do item anterior ao item atual, passa a ser o próximo do item atual, e o anterior do item posterior ao item atual, passa a ser o anterior do item atual
                else:
                    item_atual.anterior.proximo = item_atual.proximo
                    item_atual.proximo.anterior = item_atual.anterior
                #o próximo do item atual passa a ser nulo, e o anterior do item atual passa a ser nulo
                item_atual.proximo = None
                item_atual.anterior = None
                return
            item_atual = item_atual.proximo
            #se o item atual for o inicio, para o loop
            if item_atual == self.inicio:
                break

        print("não foi possível achar o aluno(a) com o nome de: ", nome)
    
    #esvaziando a lista
    def esvaziar(self):
        self.inicio = None
        self.fim = None

    def vetor(self):
        vetor = []	
        #se a lista estiver vazia, retorna um vetor vazio
        if self.inicio is None:
            return vetor

        item_atual = self.inicio
        #enquanto o item atual não for o inicio, adiciona o nome e a nota do item atual ao vetor
        while True:
            vetor.append([item_atual.nome, item_atual.nota])
            
            item_atual = item_atual.proximo
            if item_atual == self.inicio:
                return vetor
    
    def num_nos(self):
        num_nos = 0
        #se a lista estiver vazia, retorna 0
        if self.inicio is None:
            return num_nos
        
        item_atual = self.inicio
        #enquanto o item atual não for o inicio, incrementa o número de nós e passa para o próximo item
        while True:
            num_nos += 1

            item_atual = item_atual.proximo
            if item_atual == self.inicio:
                return num_nos



#criando as listas
l1 = Lista()

l1.inserir_inicio(Item("huguinho","12"))
l1.inserir_inicio(Item("zezinho","23"))
l1.inserir_fim(Item("luisinho","21"))
l1.inserir_inicio(Item("patricia","190"))
l1.inserir_fim(Item("patinhas","100"))
l1.inserir_inicio(Item("donald","345"))

l2 = Lista()

#imprimindo as listas
l1.imprimir()
print("-"*35)
l1.imprimir_inverso()
print("-"*35)
l2.imprimir()
print("-"*35)

#buscando os elementos
l1.buscar("zezinho")
print("-"*35)

l1.buscar("patinhas")
print('-'*35)

#retirando elementos
l1.retirar("huguinho")

l1.imprimir()
print("-"*35)

print(l1.vetor())
print("-"*35)

#verificando se a lista está vazia
print(l1.vazia())
print(l2.vazia())

l1.esvaziar()

print(l1.vazia())
print("-"*35)

vetor = [["phineas", "10"], ["ferb", "9"], ["candace", "8"], ["perry", "7"], ["doofenshmirtz", "6"]]

l2.inserir_vetor(vetor)

l2.imprimir()
print("-"*35)

print(l2.num_nos())