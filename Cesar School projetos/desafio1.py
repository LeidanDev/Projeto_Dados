# Lista para armazenar os registros de estudantes
estudantes = []

while True:
    print("-")
    print(" | Sistema de Gerencimento de Registros de Estudante |")
    print("-")
    print("1. Adicionar Registro de Estudante \n2. Exibir Registos de Estudantes \n3. Procurar por um Estudante \n4. Calcular Média das Notas \n5. Salvar Registros em Arquivo \n6. Carregar Registros de Arquivo \n7. Sair ") 
    print("...")
    
    selecao = input("Digite sua escolha (1-7): ")

# Bloco que registra as informações dos alunos

    if selecao == "1":
        nome = input("Digite o nome do estudante: ")
        id_estudante = input("Digite o ID do estudante: ")
        notas = input("Digite as notas separadas por espaço: ").split()
        notas = [float(nota) for nota in notas]
        estudantes.append({"nome": nome, "id": id_estudante, "notas": notas})
        print("Registro adicionado com sucesso!")
    
# Bloco que exibe os registros

    elif selecao == "2":
        for estudante in estudantes:
            print(f"Nome: {estudante['nome']}, ID: {estudante['id']}, Notas: {estudante['notas']}")
            
#Bloco que busca aluno pelo ID

    elif selecao == "3":
        id_procurado = input("Digite o ID do estudante que deseja procurar: ")
        encontrado = False
        for estudante in estudantes:
            if estudante['id'] == id_procurado:
                print(f"Nome: {estudante['nome']}, ID: {estudante['id']}, Notas: {estudante['notas']}")
                encontrado = True
                break
            if not encontrado:
                print("ID não encontrado.")  

# Bloco que calcula a média de nota dos alunos

    elif selecao == "4":
            todas_as_notas = []
            for estudante in estudantes:
                todas_as_notas.extend(estudante['notas'])
                media = sum(todas_as_notas) / len(todas_as_notas)
                print(f"A média de notas de todos os estudantes é: {media}")   

# Bloco que salva as informações em arquivo .txt

    elif selecao == "5":
            with open('registros_estudantes.txt', 'w') as arquivo:
             for estudante in estudantes:
                linha = f"{estudante['nome']},{estudante['id']},{','.join(map(str, estudante['notas']))}\n"
                arquivo.write(linha)

# Bloco que lê arquivos .txt 

    elif selecao == "6":
            arquivo = open('registros_estudantes.txt', 'r') 
            linhas = arquivo.readlines()
            for linha in linhas:    
                print(linha)

# Bloco que encerra o programa

    elif selecao == "7": 
        break
        