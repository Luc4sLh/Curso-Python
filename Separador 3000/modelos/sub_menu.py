# from modelos.menu_principal import Menu
class SubMenu:
    def __init__(self, titulo):
        self._titulo = titulo
        
    def titulo_do_menu(self):
        linha = '='*(len(self._titulo)+25)
        
        titulo = f'''\
{linha}
{self._titulo.center(len(linha))}
{linha}
'''
        return titulo
    
    def voltar_menu_principal():
        input('Digite uma tecla para voltar ao menu principal: ')
        # Menu.exibir_menu()
