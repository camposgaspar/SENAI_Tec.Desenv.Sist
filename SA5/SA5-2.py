class SA5():

    def __init__(self):
        self.stack = []
        self.choice = 0

    def getChoice(self): # Recebe o input do usuário e verifica se é valido.
        self.choice = int(input("Informe sua escolha: \n"))
        if self.choice not in range(0, self.nOptions):
            print("Por favor, selecione uma das opções apresentadas acima.")
            self.getChoice()

    def showOptions(self): # Apresenta as opções ao usuário e define o número de opções
        self.nOptions = 5 + 1
        print("\n"
              "Opção 1: Novo item\n"
              "Opção 2: Remover primeiro item\n"
              "Opção 3: Listar items\n"
              "Opção 4: Verificar se fila está vazia\n"
              "Opção 5: Limpar a fila\n")

    def newItem(self): # Adiciona novo item no topo da fila
        item = input("Qual item deseja adicionar à fila?\n")
        self.stack.append(item)
        print(f"Item {item} adicionado à fila na posição {self.stack.index(item)}.\n")

    def manyNewItem(self):  # Permite o cadastro de vários items, decidio pelo usuário
        try:
            howMany = int(input("Quantos items deseja cadastrar? "))
            print()
        except:
            howMany = 0
            print("O valor deve ser um número inteiro.\n")
            self.newItem()

        if howMany != 0:
            for i in range(0, howMany):
                self.newItem()
        else:
            return

    def removeLastItem(self): # Remove item do inicio da fila
        try:
            print(f"Item {self.stack.pop(0)} removido.\n") # Essa linha foi alterada para a Etapa 2
        except:
            print("A lista está vazia.")

    def listStack(self): # Lista os items
        print(f"Items na fila: ")
        for item in self.stack:
            print(item)

    def isStackEmpity(self): # Informa se a fila está vazia. Se não estiver, lista os items na fila
        if self.stack:
            print("Há itens na lista")
            self.listStack()
        else:
            print("Lista está vazia.")

    def clearStack(self): # Limpar a lista
        self.__init__()
        print("A fila foi limpa.")

    def run(self): # Abstração
        self.showOptions()
        self.getChoice()

        if self.choice == 1:
            self.manyNewItem()
        elif self.choice == 2:
            self.removeLastItem()
        elif self.choice == 3:
            self.listStack()
        elif self.choice == 4:
            self.isStackEmpity()
        elif self.choice == 5:
            self.clearStack()

        self.run()




if __name__ == "__main__":
    SA5 = SA5()

    SA5.run()