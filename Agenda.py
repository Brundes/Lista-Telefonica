import time

# A lista "lista" foi criada como variável global para facilitar a utilização da mesma dentro de cada "def" diferente

lista = []

# A função "def contato_existente" serve para avaliar se o contato escrito já se escontra cadastrado dentro da lista

def contato_existente(email):
    if len(lista) > 0:
        for contato in lista:
            if contato["nome"] == email:
                return True
    return False

# A função "def cadastrar" vai receber a informações necessárias, que serão inseridas pelo usuário e adicionar no dicionário "contato",
#  logo em seguida coloca essas informações na lista criada dentro da "def agenda"

def cadastrar():
    while True:
        email = str(input("Insira o e-mail do contato a ser cadastrado: ")).lower()
        if not contato_existente(email):
            break
        else:
            print("Já existe um contato com esse endereço de e-mail, por favor escolha outro.")

 # "contato" é a agenda que receberá as informações do contato

    contato = {
        "nome": str(input("Insira o nome: ")).lower(),
        "numero": str(input("Insira o número: ")),
        "email": email,
        "twitter": str(input("Insira a conta Twitter (caso tenha): ")),
        "instagram": str(input("Insira a conta Instagram (caso tenha): "))
    }
    lista.append(contato)

    print("~"*45)
    print("Contato {} cadastrado com sucesso!".format(contato["nome"]))
    time.sleep(1)

# A "def cadastrar_mais" atua de maneira análoga à "cadastrar", agora com uma função while que registra a quantidade de vezes que o usuário
#  decidi cadastrar novos contatos

def cadastrar_mais():
    cad = int(input("Quantos contatos deseja cadastrar? "))
    registro = 0
    while (cad > 0):
        contato = {
        "nome": str(input("\nInsira o nome: ")).lower(),
        "numero": str(input("Insira o número: ")),
        "email": str(input("Insira o e-mail: ")).lower(),
        "twitter": str(input("Insira a conta Twitter (caso tenha): ")),
        "instagram": str(input("Insira a conta Instagram (caso tenha): "))
        }
        cad -= 1
        registro += 1
        lista.append(contato)
        print(f"\nRestam-se {cad} contatos a serem adicionados.")
    
    print(f"{registro} adicionados com sucesso")
    time.sleep(1)

# A "def alterar" pede para o usuário informar um e-mail válido para acessar todas as informações sobre um determinado contato, fazendo assim
#  com que se altere suas respectivas informações de acordo com a nova vontade do usuário

def alterar():
    if len(lista) > 0:
        email = str(input("Digite o e-mail do contato a ser alterado: "))
        if not contato_existente(email):
            for contato in lista:
                if contato["email"] == email:
                    print("\nNome: {}".format(contato["nome"]))
                    print("Numero: {}".format(contato["numero"]))
                    print("E-mail: {}".format(contato["email"]))
                    print("Twitter: {}".format(contato["twitter"]))
                    print("Instagram: {}".format(contato["instagram"]))

                    print("~"*45)
                    contato["nome"] = input("Insira o novo nome desejado: ").lower()
                    contato["numero"] = input("Digite o novo número desejado: ")
                    contato["email"] = input("Digito o novo e-mail desejado: ").lower()
                    contato["twitter"] = input("Insira a nova conta do Twitter: ")
                    contato["instagram"] = input("Insira a nova conta do Instagram: ")

                    print("Os dados do {} foram alterados com sucesso".format(contato["nome"]))
                    time.sleep(1)
                    break

        else:
            print("Contato não cadastrado, escolha um contato válido.")
    else:
        print("Não há contato cadastrado para ser alterado.")

# A "def procurar" checa se o e-mail recebido encontra-se registrada em algum contato, caso o contato exista no registro do programa, todas
#  as outras informações do respectivo contato será disposta no terminal

def procurar():
    if len(lista) > 0:
        email = str(input("Qual o e-mail do contato que você quer procurar: "))
        print("~"*45)
        if not contato_existente(email):
            for contato in lista:
                if contato["email"] == email:
                    print("Nome: {}".format(contato["nome"]))
                    print("Número: {}".format(contato["numero"]))
                    print("E-mail: {}".format(contato["email"]))
                    print("Twitter: {}".format(contato["twitter"]))
                    print("Instagram: {}".format(contato["instagram"]))
                    time.sleep(1)
                    break
        else:
            print("Contato não existente na agenda.")
    else:
        print("Não existe nenhum contato na agenda para procurar.")

# "def excluir" procura dentro da agenda onde está inserida a informação para poder excluir as informações do contato

def excluir():
    if len(lista) > 0:
        email = str(input("Qual o e-mail do contato que deseja excluir: "))
        if not contato_existente(email):
            for i, contato in enumerate(lista):
                if contato["email"] == email:
                    print("Nome: {}".format(contato["nome"]))
                    print("Numero: {}".format(contato["numero"]))
                    print("E-mail: {}".format(contato["email"]))
                    print("Twitter: {}".format(contato["twitter"]))
                    print("Instagram: {}".format(contato["instagram"]))

                    print("~"*45)
                    verificacao = str(input("Confirma a exclusão do contato? SIM ou NAO: ")).upper()
                    if verificacao == "SIM":
                        del lista[i]
                        print("\nContato excluido com sucesso!!")

                    else:
                        print("\nContato não excluido.")
                    break

        else:
            print("Contato não cadastrado, escolha um contato válido!")

    else:
        print("Não há contato para ser deletado.")

# "def listar" dispôe todas informações sobre todos os contatos que estão cadastrados na agenda

def listar():
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            #print("Nro\tNome\tE-mail\tTwitter\tInstagram")
            print("CONTATO {}".format(i+1))
            #print(f"Nome: {i}")
            print("Nome: {}".format(contato["nome"]))
            print("Numero: {}".format(contato["numero"]))
            print("E-mail: {}".format(contato["email"]))
            print("Twitter: {}".format(contato["twitter"]))
            print("Instagram: {}\n".format(contato["instagram"]))

        print("\nTem {} contatos cadastrados na agenda".format(len(lista)))

    else:
        print("\nNão existe nenhum contato dentro agenda para listar")

# "def agenda" é onde fica o menu principal do programa, o usuário escolherá entre as opções para poder interagir com a agenda

def agenda():
 #Função para criar o visual da agenda que o usuário verá quais opções estão disponíveis para escolher

    while True:
        print("~"*45)
        print("\t~~~~MENU AGENDA~~~~")
        print("")
        print("1 - Cadastrar novo contato")
        print("2 - Cadastrar mais de um novo contato")
        print("3 - Alterar informações de contato na agenda")
        print("4 - Procurar contato na agenda")
        print("5 - Excluir contato da agenda")
        print("6 - Listar todos os contatos da agenda")
        print("7 - Sair da agenda")
        print("~"*45)

 # A partir desse ponto, o programa receberá do usuário um número referente a uma das alternativas (de 1 a 6)
 #  disponibilizadas no "menu"

        while True:
            try:
                opcao = int(input("Selecione uma das opções: "))
                print("~"*45)
                time.sleep(1)
                break

 #Caso o usuário insira alguma alternativa fora do esperado, seria comum apresentar uma tela de erro, porém com o "Except ValueError",
 # o programa exibirá uma frase programada pedindo para inserir uma alternativa válida.

            except ValueError:
                print("Por favor, escolha uma alterativa válida!")

        if opcao == 1:
            cadastrar()

        elif opcao == 2:
            cadastrar_mais()

        elif opcao == 3:
            alterar()

        elif opcao == 4:
            procurar()

        elif opcao == 5:
            excluir()

        elif opcao == 6:
            listar()

        elif opcao == 7:
            print("\nObrigado por utilizar nossa agenda, volte sempre!!\n")
            break

agenda()