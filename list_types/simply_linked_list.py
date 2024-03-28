class Item():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        self.proximo = None

class Lista():
    def __init__(self):
        self.inicio = None
    
    def inserir_inicio(self, item):
        item.proximo = self.inicio
        self.inicio = item
    
    def inserir_fim(self, item):
        item_atual = self.inicio

        while item_atual.proximo != None:
            item_atual = item_atual.proximo

        item_atual.proximo = item
    
    def imprimir(self):
        item_atual = self.inicio

        while item_atual != None:
            print(item_atual.nome, item_atual.nota)
            item_atual = item_atual.proximo
        
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
                
                return

            else:
                item_atual = item_atual.proximo

        print("não foi possível achar o aluno(a) com o nome de: ",nome)
    
    def retirar(self, nome):
        item_atual = self.inicio
        item_anterior = item_atual

        while item_atual != None:
            

            if item_atual.nome == nome and item_atual == self.inicio:
                self.inicio = item_atual.proximo
                item_atual.proximo = None
                item_anterior = None

                return

            elif item_atual.nome == nome:
                item_anterior.proximo = item_atual.proximo
                item_atual.proximo = None

                return

            else:
                item_anterior = item_atual
                item_atual = item_atual.proximo

        print("não foi possível achar o aluno(a) com o nome de: ",nome)
        
    def esvaziar(self):
        self.inicio = None



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

#verificando se a lista está vazia
print(l1.vazia())
print(l2.vazia())

l1.esvaziar()

print(l1.vazia())
