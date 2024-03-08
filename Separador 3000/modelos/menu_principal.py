from modelos.cliente import Cliente

class Menu:
    def __init__(self, titulo, lista_opcoes=None) -> None:
        self.titulo = titulo
        self.opcoes = lista_opcoes

    def titulo_do_menu(self, texto=''):
        linha = '='*(len(texto)+25)
        
        titulo = f'''\
{linha}
{texto.center(len(linha))}
{linha}
'''
        return print(titulo,end='')
    
    def opcoes_do_menu(self,nome_opcoes):
        for i,opcoes in enumerate(nome_opcoes,start=1):
            exibir = f'{i}. {opcoes}'
            print(exibir)
        self.escolher_opcao()

    def exibir_menu(self):
        self.titulo_do_menu(self.titulo)
        self.opcoes_do_menu(self.opcoes)

    def escolher_opcao(self):
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        match opcao_escolhida:
            case 1:
                Cliente.cadastrar_cliente()
            case 2: 
                self.separar_corte()



