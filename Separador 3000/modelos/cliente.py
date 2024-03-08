from modelos.sub_menu import SubMenu

cliente_submnenu = SubMenu('Cadastrar cliente')
class Cliente():
    lista_cliente = []
    def cadastrar_cliente():
        print(cliente_submnenu.titulo_do_menu(), end='')
        nome_cliente = str(input('Digite o nome do cliente: '))
        numero_cliente = str(input(f'Digite o numero do {nome_cliente}: '))
        informacoes_cliente = [nome_cliente,numero_cliente]

        




        
