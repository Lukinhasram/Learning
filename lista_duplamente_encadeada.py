class Item():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        self.proximo = None
        self.anterior = None

class Lista():
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def inserir_inicio(self, item):
        item.proximo = self.inicio
        self.inicio = item
        if item.proximo != None:
            item.proximo.anterior = item

        if self.fim == None:
            self.fim = item
            item.proximo = self.inicio

    
    def inserir_fim(self, item):
        item_atual = self.inicio

        while item_atual.proximo != None:
            item_atual = item_atual.proximo

        item_atual.proximo = item
        item.anterior = item_atual

        self.fim = item

        #print(item.anterior.nome, item.anterior.nota, "anterior", item_atual.proximo.nome, item_atual.proximo.nota, "atual")
        #print("-"*35)

    def imprimir(self):
        item_atual = self.inicio
        
        while item_atual != None:
            print(item_atual.nome, item_atual.nota,)
            item_atual = item_atual.proximo
        
        print("-"*35)

        item_atual = self.fim

        while item_atual != None:
            print(item_atual.nome, item_atual.nota,)
            item_atual = item_atual.anterior
        
    def vazia(self):
        if self.inicio == None:
            return True
        else:
            return False
        
    def buscar(self, nome):
        item_atual = self.inicio

        while item_atual != None:

            if item_atual.nome == nome:
                
                print("aluno(a): ",item_atual.nome, item_atual.nota)
                break

            else:
                item_atual = item_atual.proximo
    
    def retirar(self, nome):
        item_atual = self.inicio

        while item_atual.proximo != None:

            if item_atual.nome == nome:
                item_atual = item_atual.proximo

                break
        
        if item_atual.anterior.anterior != None:
            item_atual.anterior = item_atual.anterior.anterior
            item_atual.anterior.proximo = item_atual
        elif item_atual.anterior != None:
            item_atual.anterior = None
            self.inicio = item_atual
        
        if item_atual.proximo != None:
            item_atual.proximo = item_atual.proximo.proximo
            item_atual.proximo.anterior = item_atual
        elif item_atual.proximo == None:
            item_atual.proximo = None
            self.fim = item_atual  

    def esvaziar(self):
        self.inicio = None




l1 = Lista()

l1.inserir_inicio(Item("huguinho","12"))
l1.inserir_inicio(Item("zezinho","23"))
l1.inserir_fim(Item("luisinho","21"))
l1.inserir_fim(Item("pato donald","45"))
l1.inserir_inicio(Item("patricia","190"))
l1.inserir_inicio(Item("donald","345"))

l1.imprimir()

l1.retirar("luisinho")
print("-"*35)

l1.imprimir()


