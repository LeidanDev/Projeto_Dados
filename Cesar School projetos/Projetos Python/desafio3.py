# Lista para armazenar os registros de estudantes
estudantes = []

# Função para adicionar um novo registro de estudante
def adicionar_estudante():
    nome = input("Digite o nome do estudante: ")
    id_estudante = input("Digite o ID do estudante: ")
    notas = input("Digite as notas separadas por espaço: ").split()
    notas = [float(nota) for nota in notas]
    estudantes.append({"nome": nome, "id": id_estudante, "notas": notas})

# Função para exibir todos os registros de estudantes
def exibir_estudantes():
    for estudante in estudantes:
        print(f"Nome: {estudante['nome']}, ID: {estudante['id']}, Notas: {estudante['notas']}")

# Função para procurar um estudante pelo ID
def procurar_por_id():
    id_procurado = input("Digite o ID do estudante que deseja procurar: ")
    encontrado = False
    for estudante in estudantes:
        if estudante['id'] == id_procurado:
            print(f"Nome: {estudante['nome']}, ID: {estudante['id']}, Notas: {estudante['notas']}")
            encontrado = True
            break
    if not encontrado:
        print("ID não encontrado.")

# Função para calcular e exibir a média de notas de todos os estudantes
def calcular_media():
    todas_as_notas = []
    for estudante in estudantes:
        todas_as_notas.extend(estudante['notas'])
    media = sum(todas_as_notas) / len(todas_as_notas)
    print(f"A média de notas de todos os estudantes é: {media}")

# Função para salvar os registros de estudantes em um arquivo de texto
def salvar_arquivo():
    with open('registros_estudantes.txt', 'w') as arquivo:
        for estudante in estudantes:
            linha = f"{estudante['nome']},{estudante['id']},{','.join(map(str, estudante['notas']))}\n"
            arquivo.write(linha)

# Função para carregar os registros de estudantes de um arquivo de texto
def carregar_arquivo():
    with open('registros_estudantes.txt', 'r') as arquivo:
        for linha in arquivo:
            nome, id_estudante, notas_str = linha.strip().split(',')
            notas = [float(nota) for nota in notas_str.split(',')]
            estudantes.append({"nome": nome, "id": id_estudante, "notas": notas})



while True:
    print("-")
    print(" | Sistema de Gerencimento de Registros de Estudante |")
    print("-")
    print(
        "1. Adicionar Registro de Estudante \n2. Exibir Registos de Estudantes \n3. Procurar por um Estudante \n4. Calcular Média das Notas \n5. Salvar Registros em Arquivo \n6. Carregar Registros de Arquivo \n7. Sair ")
    print("...")

    escolha = input("Digite sua escolha (1-7): ")



    # Exemplo de uso das funções

    match escolha:
        case "1":
            adicionar_estudante()
        case "2":
            exibir_estudantes()
        case "3":
            procurar_por_id()
        case "4":
            calcular_media()
        case "5":
            salvar_arquivo()
        case "6":
            carregar_arquivo()
        case "7":
            print("Até logo!")
            break
        case _:
            print("Escolha inválida. Por favor, tente novamente.")





