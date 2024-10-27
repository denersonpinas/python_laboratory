import os

restaurantes = [{ 'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False }, { 'nome': 'Pizzaria Suprema', 'categoria': 'Italiana', 'ativo': True }, { 'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False }]

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
    3. Ativar restaurante
    4. Sair
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
                alternar_estado_restaurante()
            case 4:
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
    categoria_do_restaurante = input('Digite a categoria do restaurante {nome_do_restaurante}: ')

    restaurantes.append({'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False})
    print('Restaurante cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    exibir_sub_menu('Listando os restaurantes')
    titulo = f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}'
    linha = ('-' * len(titulo))
    print(f'{titulo}')
    print(f'{linha}')
    for restaurante in restaurantes:
        print(f'{restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'Ativado' if restaurante['ativo'] else 'Desativado'}')
    
    voltar_menu_principal()

def alternar_estado_restaurante():
    exibir_sub_menu('Alterarando estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_do_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado!')
            
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