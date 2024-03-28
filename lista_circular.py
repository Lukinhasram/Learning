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

        item.anterior = self.fim

    def imprimir(self):
        item_atual = self.inicio

        while item_atual != self.fim:

            print(item_atual.nome, item_atual.nota,)
            print("-"*35)

            item_atual = item_atual.proximo

        print(item_atual.nome, item_atual.nota)

        
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
        item_anterior = item_atual

        while item_atual.proximo != self.fim:

            if item_atual.proximo.nome == nome:
                
                item_anterior = item_atual
                item_atual = item_atual.proximo

                break

            else:
                item_atual = item_atual.proximo
        
        if item_atual.proximo.nome == nome:
                
            item_anterior = item_atual
            item_atual = item_atual.proximo


        item_anterior.proximo = item_atual.proximo
        item_atual.proximo = None

    def esvaziar(self):
        self.inicio = None




l1 = Lista()

l1.inserir_inicio(Item("huguinho","12"))
l1.inserir_inicio(Item("zezinho","23"))
l1.inserir_inicio(Item("luisinho","21"))
l1.inserir_inicio(Item("pato donald","45"))
l1.inserir_inicio(Item("patricia","190"))
l1.inserir_inicio(Item("donald","345"))


l1.imprimir()
