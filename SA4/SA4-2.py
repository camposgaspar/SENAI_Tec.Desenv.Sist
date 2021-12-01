class SA():

    def __init__(self):
        self.userCount = 0
        self.userDict = {}
        self.users = []

    def getChoice(self):  # Recebe o input do usuário e verifica se é valido.
        self.choice = int(input("Informe sua escolha: \n"))
        if self.choice not in range(0, self.nOptions):
            print("Por favor, selecione uma das opções apresentadas acima.")
            self.getChoice()

    def options(self):  # Apresenta as opções ao usuário e define o número de opções
        self.nOptions = 5 + 1
        print("Opção 1: Cadastro\n"
              "Opção 2: Usuários cadastrados\n"
              "Opção 3: Sair\n"
              "Opção 4: Localizar Usuário\n"
              "Opção 5: Remover Usuário\n")

    def signUp(self):  # Permite o cadastro de usuários
        name = input("Informe o nome: ")
        age = int(input("Informe a idade: "))

        self.userDict[name] = self.userCount
        self.users.append([name, age])
        self.userCount += 1
        print(f"Usuário {name} cadastrado\n")

    def manySignUp(self):  # Permite o cadastro de vários usuários, decidio pelo usuário
        try:
            howMany = int(input("Quantos usuários deseja cadastrar? "))
            print()
        except:
            howMany = 0
            print("O valor deve ser um número inteiro.\n")
            self.manySignUp()

        if howMany != 0:
            for i in range(0, howMany):
                self.signUp()
        else:
            return

    def listAllUsers(self):  # Lista todos os usuários
        for name, age in self.users:
            print(f"Usuário nº: {self.userDict[name]}\n"
                  f"Nome: {name}\n"
                  f"Idade: {age}\n")

    def findUser(self):  # Procura um usuário com base no nome e retorna as informações
        try:
            userName = input("Nome do usuário: ")
            userNum = self.userDict[userName]

            print(f"Usuário nº: {userNum}")
            print(f"Nome: {userName}")
            print(f"Idade: {self.users[userNum][1]}\n")

        except Exception as e:  # Caso o usuário não esteja cadastrado
            # print(e)
            print(f"Usuário {userName} não localizado")
            return -1

    def removeUser(self):  # Procura um usuário com base no nome e remove o usuário
        try:
            userName = input("Nome do usuário para remoção: ")
            userNum = self.userDict[userName]

            self.users.pop(userNum)
            del self.userDict[userName]

        except:
            print(f"Usuário {userName} não localizado")

    def run(self):  # Abstração
        self.options()
        self.getChoice()

        if self.choice == 1:
            self.manySignUp()
        elif self.choice == 2:
            self.listAllUsers()
        elif self.choice == 4:
            self.findUser()
        elif self.choice == 5:
            self.removeUser()

        if self.choice == 3:
            __name__ == ""
        else:
            self.run()


if __name__ == "__main__":
    SA = SA()

    SA.run()
