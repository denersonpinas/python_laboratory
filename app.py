import os
from modelos import Restaurante

def exibir_name():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_menu():
    print("""
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Sair
    """)

def escolher_opcao():
    try:
        option = int(input('Escolha uma opção: '))

        match option:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                finalizar_app()
            case _:
                opcao_invalida()
    except:  # noqa: E722
        opcao_invalida()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal!')
    main()

def exibir_sub_menu(texto):
    ''' Exibe um sub menu personalizado
    :param  - texto with describend sub menu
    :return - None
    '''

    reset()
    exibir_name()

    linha = '*' + ('=' * len(texto)) + '*'
    print(f'\n{linha}')
    print(f'{texto}')
    print(f'{linha}\n')

def cadastrar_novo_restaurante():
    exibir_sub_menu('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    Restaurante(nome_do_restaurante, categoria_do_restaurante)
    print('Restaurante cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_sub_menu('Listando os restaurantes')
    Restaurante.listar_restaurantes()    
    voltar_menu_principal()
            
def finalizar_app():
    exibir_sub_menu('Finalizar programa!')

def opcao_invalida():
    exibir_sub_menu('Opção inválida!')
    voltar_menu_principal()

def reset():
    os.system('clear')

def main():
    reset()
    exibir_name()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()