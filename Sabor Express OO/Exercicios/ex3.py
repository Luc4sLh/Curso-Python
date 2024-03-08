'''Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
   Instancie um restaurante e atribua valores aos seus atributos.'''

class Restaurate:
    def __init__(self, nome, categoria, ativo, delivery, pagamento) -> None:
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo 
        self.delivery = delivery
        self.pagamento = pagamento

    def __str__(self) -> str:
        return f'{self.nome} | {self.ativo} | {self.delivery} | {self.pagamento}'
    

restaurante_foms = Restaurate("Fom's", 'Lanchonete', True, True, ['Pix', 'Cartão', 'Dinheiro'])
print(restaurante_foms)