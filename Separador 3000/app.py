from modelos.menu_principal import Menu

titulo = 'Separador 3000'
opcoes = ['Cadastrar Cliente', 'Separar corte']
menu = Menu(titulo, opcoes)

def main():
    menu.exibir_menu()

if __name__ == '__main__':
    main()
