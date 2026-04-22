# pede ao utilizador que digite o nome e guarda na variável 'nome'
nome = input("Nome: ")

# mostra o texto "Escolha:" no ecrã
print("Escolha:")

# mostra as opções disponíveis
print("1 - Java")
print("2 - Python")
print("3 - C++")

# pede ao utilizador que escolha uma opção e guarda como texto (string)
opcao = input("Opção: ")

# verifica se a opção escolhida é "1"
if opcao == "1":
    # se for, define o voto como "Java"
    voto = "Java"

# se não for "1", verifica se é "2"
elif opcao == "2":
    # se for, define o voto como "Python"
    voto = "Python"

# se não for "1" nem "2", verifica se é "3"
elif opcao == "3":
    # se for, define o voto como "C++"
    voto = "C++"

# se não for nenhuma das opções acima
else:
    # define voto como None (nenhum valor válido)
    voto = None

# verifica se o voto é inválido (ou seja, None)
if voto is None:
    # mostra mensagem de erro
    print("Voto inválido.")

# caso contrário (voto válido)
else:
    # imprime uma linha em branco (\n) e mostra o nome do utilizador
    print(f"\nUtilizador: {nome}")

    # mostra em qual linguagem o utilizador votou
    print(f"Voto registado em: {voto}")