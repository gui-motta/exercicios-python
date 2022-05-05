def menu():
        print("1 - Cadastrar alguém no final da agenda")
        print("2 - Mostrar os nomes da agenda")
        print("3 - Cadastrar alguém no início da agenda")
        print("4 - Remover um nome da agenda")
        print("5 - Substituir um nome na agenda")
        print("6 - Mostrar o total de cadastrados na agenda")
        print("7 - Colocar a agenda em ordem alfabética")
        print("8 - Sair do programa")
        op = int(input("Digite a opção desejada: "))
        while op < 1 or op > 8:
            print("Valor inválido!")
            op = int(input("Digite a opção desejada: "))
        return op


def cadastrar_final(agenda):
    nome = input("Digite o nome a ser cadastrado: ")
    agenda.append(nome)



def mostrar_contatos(agenda):
    print(agenda)


def cadastrar_inicio(agenda):
    nome = input("Digite o nome a ser cadastrado no início da agenda: ")
    agenda.insert(0, nome)


def remove_nome(agenda):
    nome = input("Digite o nome para remover da agenda: ")
    for i in range(len(agenda)):
        if agenda[i] == nome:
            del agenda[i]
            break


def substitui_nome(agenda):
    nome1 = input("Digite o nome a ser substituido: ")
    nome2 = input("Digite o nome substituto: ")
    for i in range(len(agenda)):
        if agenda[i] == nome1:
            agenda[i] = nome2
            break


def total_cadastros(agenda):
    print("O total de cadastrados é: ", len(agenda))


def ordem_alfabetica(agenda):
    agenda.sort()
    print(agenda)


def main():
    agenda = []
    while True:
        op = menu()
        if op == 8:
            break
        if op == 1:
            cadastrar_final(agenda)
        elif op == 2:
            mostrar_contatos(agenda)
        elif op == 3:
            cadastrar_inicio(agenda)
        elif op == 4:
            remove_nome(agenda)
        elif op == 5:
            substitui_nome(agenda)
        elif op == 6:
            total_cadastros(agenda)
        elif op == 7:
            ordem_alfabetica(agenda)

main()
