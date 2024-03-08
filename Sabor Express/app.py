import os

restaurantes = [{'nome':"Fom's", 'categoria':'lanchonete', 'ativo':False},
                {'nome':"Acesso livre", 'categoria':'restaurante', 'ativo':True},
                {'nome':"Sushiya", 'categoria':'japonesa', 'ativo':True}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    '''Função responsavel por exibir as opções do menu principal'''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def listar_restaurantes():
    ''''Função responsavel por listar os restaurantes ja cadastrados na aplicação'''

    os.system('cls')
    exibir_subtitulo('Listando Restaurantes!')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()

def escolher_opcao():
    '''Função responsavel por validar a entrada do usuário e encaminhar a aplicação para a opção escolhida'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizazndo_app()

    except:
        opcao_invalida()

def alternar_estado_restaurante():
    '''Função responsavel por alternar o status do restaurante para Ativo ou Desativado'''

    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes: 
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O {nome_restaurante} não foi encontrado')




    voltar_ao_menu()

def cadastrar_novo_restaurante():
    '''Função responsável por cadastrar novos restaurantes na aplicação'''

    exibir_subtitulo('Cadastrar novos restaurantes.')
    novo_restaurante = input('Digite o nome do novo restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {novo_restaurante}: ')
    print(f'O restaurante {novo_restaurante} foi cadastrado com sucesso!')
    dados_do_restaurante = {'nome' : novo_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    '''Função responsavel por personalizar e exibir o subtitulo de cada função do aplicativo'''
    os.system('cls')
    linha = '=' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu():
    input('\nDigite uma tecla pra volta ao menu principal: ')
    main()

def finalizazndo_app():
    exibir_subtitulo('Encerrando programa')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
