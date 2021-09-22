contatos = {}

def chavesContatos(contatos, nome):
  chaves = []
  for chave in contatos:
    if chave.startswith(nome):
      chaves.append(chave)
  return chaves

def novoContato(): 
  cont = int(input("Informe quantos contatos deseja adicionar: "))
  while cont > 0:  
    nome = input("Informe o nome:").strip()
    telefone = int(input("Informe o telefone: ")) 
    email = input("Informe o e-mail: ").strip() 
    twitter = input("Informe o Twitter: ").strip() 
    facebook = input("Informe o Facebook: ").strip() 
    contatos[nome] = {
      "nome" : nome, 
      "telefone" : telefone, 
      "email" : email, 
      "twitter" : twitter,
      "facebook" : facebook 
      } 
    print ("\nContato salvo com sucesso!")
    cont-=1
def buscarContato(nome, contatos): 
  tabela = []
  chaves = chavesContatos(contatos, nome)
  if len(chaves) > 0:
    for contato in contatos:
        
#      tabela.append([ 
#        contatos[chave]["nome"], contatos[chave]["telefone"], contatos[chave]["email"], contatos[chave]["twitter"], contatos[chave]["facebook"]
#      ])
#    print(tabulate.tabulate(tabela,headers=["Nome", "Telefone", "E-mail", "Twitter", "Facebook"], tablefmt="grid"))

  else:
    print("Não encontrado na Agenda!")

def listarContatos(contatos): 
  tabela = []
  if len(contatos) > 0:
    """
    for nome in contatos:
      tabela.append([ 
        contatos[nome]["nome"], contatos[nome]["telefone"], contatos[nome]["email"], contatos[nome]["twitter"], contatos[nome]["facebook"]
      ])
    print(tabulate.tabulate(tabela,headers=["Nome", "Telefone", "E-mail", "Twitter", "Facebook"], tablefmt="grid"))
    """
    print("Nome , Telefone , E-mail , Twitter , Facebook")
    for contato in contatos:
      print(contatos[contato]["nome"],",",contatos[contato]["telefone"],",",contatos[contato]["email"],",",contatos[contato]["twitter"],",",contatos[contato]["facebook"])
  else:
    print("Agenda vazia!")

def apagarContato(contatos, nome):
    if len(contatos) > 0:
      for chave in contatos:
        if chave == nome:
          contatos.pop(nome)
          print ("O contato {} removido com sucesso da agenda!".format(nome))
        else:
          print("Contato não localizado!")
    else:
      print("A agenda está vazia!")

def limparAgenda(contatos):
    if len(contatos) == 0:
      print("A agenda está vazia!")
    else:
      contatos.clear()
      print("Todos os contatos foram removidos!")

def atualizarContato(contatos,nome): 
  if len(contatos) > 0:
      for chave in contatos:
        if chave == nome:
          nomeAtualizado = input('Informe o novo nome: ').strip()
          telefoneAtualizado = int(input('Informe o novo telefone: '))
          emailAtualizado = input('Informe o novo e-mail: ').strip()
          twitterAtualizado = input('Informe o novo Twitter: ').strip()
          facebookAtualizado = input('Informe o novo Facebook: ').strip()
          contatos[nomeAtualizado] = contatos.pop(nome)
          contatos[nomeAtualizado] = {
            "nome" : nomeAtualizado, 
            "telefone" : telefoneAtualizado, 
            "email" : emailAtualizado, 
            "twitter" : twitterAtualizado,
            "facebook" : facebookAtualizado 
          } 
          print("Contato atualizado com sucesso!".format(nome))
          break
        else:
          print("Contato não localizado!")
  else:
    print("A agenda está vazia!")

# Programa Principal
print('-'*30)
print('AGENDA TELEFÔNICA') 
print('-'*30)

while True:
  print('-'*30) 
  print('MENU AGENDA') 
  print('1 - Novo contato;') 
  print('2 - Localizar contato;') 
  print('3 - Listar todos os contatos;') 
  print('4 - Apagar contato;') 
  print('5 - Limpar a agenda;') 
  print('6 - Atualizar contato;') 
  print('7 - Sair')
  while True:
    try:
      opcao = int(input('Entre com a opção desejada: '))
      opcao = int(opcao)
      break
    except ValueError:
      print('-'*30)
      print("Apenas números são aceitos! \nDigite um número!")
      print('-'*30) 
  print('-'*30)
  if opcao == 1:
    chaves = novoContato() 
  elif opcao == 2: 
    nome = input('Digite o nome para a pesquisa: ')
    buscarContato(nome, contatos)
  elif opcao == 3: 
    listarContatos(contatos)
  elif opcao == 4: 
    nome = input('Digite o nome para a pesquisa: ')
    apagarContato(contatos,nome)
  elif opcao == 5: 
    limparAgenda(contatos)
  elif opcao == 6: 
    nome = input('Digite o nome para a pesquisa: ')
    atualizarContato(contatos,nome) 
  elif opcao == 7: 
    print('Saindo da agenda!')
    print('-'*30) 
    break 
  else: 
    print('Digite a opção correta!') 
  print('-'*30)
