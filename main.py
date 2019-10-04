from CRUD_Postgres.livro import *

def menu():
    op = int(input('MENU\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   '1 - CADASTRO\n'
                   '2 - MOSTRAR \n'
                   '3 - ATUALIZAR\n'
                   '4 - DELETAR \n'
                   '5 - SAIR\n'
                   '=-=-=-=-=-=-=-=-=-=-=-=-\n'
                   'DIGITE A OPÇÃO DESEJADA: '))
    return op

l = Livro()

while True:
    op = menu()

    if op == 1:
        print('Cadastrar!')
        autor = input("Digite o autor: ")
        tipo = input("Digite o tipo: ")

        l.cadastrar(autor, tipo)

    elif op == 2:
        print('Mostrar!')
        find = input("Digite o nome do autor para buscar:")

        print(l.mostrar(find))

    elif op == 3:
        print('Editar')
        editar = input("Digite o nome do autor para editar: ")

        flag = l.existe(editar)
        if flag == 1:
            autor = input("Digite o nome do autor novo: ")
            tipo = input("Digite o tipo novo: ")
            l.editar(editar, autor, tipo)
        else:
            op = input("Autor não encontrado. Deseja cadastrar? S/N").strip().upper()[0]
            if op == 'S':
                print('Cadastrar!')
                autor = input("Digite o autor: ")
                tipo = input("Digite o tipo: ")
                l.cadastrar(autor, tipo)

    elif op == 4:
        print('Deletar')
        delete = input("Digite o autor para deletar: ")

        l.deletar(delete)

    elif op == 5:
        print("Finalizando...")
        break

    else:
        print(f'Opção inválida. Tente novamente!')
print("FIM!")
