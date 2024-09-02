def menu():
    print("\nMenu:")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Visualizar todos os alunos")
    print("0 - Sair")

def adicionar_aluno(alunos):
    nome = input("Digite o nome do Aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    if matricula in alunos:
        print("Aluno Registrado.")
    else:
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso!")

def remover_aluno(alunos):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno Removido!")
    else:
        print("Número de matrícula não encontrado.")

def visualizar_alunos(alunos):
    if alunos:
        print("\nLista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Matricula: {matricula}, Nome: {nome}")
    else:
        print(f"Nenhum aluno registrado nessa {matricula}.")

def main():
    alunos = {}
    while True:
        menu()
        escolha = input("Escolha uma opção (0-3): ")
        
        if escolha == '1':
            adicionar_aluno(alunos)
        elif escolha == '2':
            remover_aluno(alunos)
        elif escolha == '3':
            visualizar_alunos(alunos)
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor escolher um número de 0 à 3.")

if __name__ == "__main__":
    main()